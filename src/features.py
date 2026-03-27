import logging
import warnings

import networkx as nx
import numpy as np
from scipy.stats import skew, mode

logger = logging.getLogger(__name__)


def features(tree) -> np.ndarray:
    """Compute the 56-dimensional GoC fingerprint for a single function graph.

    Layout:
      [0:48]  node-level statistics  (6 metrics × 8 summary stats)
      [48:56] graph-level properties (network_size, edges, triangles, …)
    """
    weighted_degree = tree.degree(weight="weight")
    try:
        eigenvector_centrality = nx.eigenvector_centrality(tree, weight="weight", max_iter=1000)
    except nx.PowerIterationFailedConvergence:
        logger.debug("eigenvector_centrality failed to converge; defaulting to 0.0 for all nodes")
        eigenvector_centrality = {node: 0.0 for node in tree.nodes()}
    page_rank = nx.pagerank(tree, weight="weight")
    local_clustering = nx.clustering(tree.to_undirected())
    two_hop = twoHop(tree)
    neighbour_clustering = neighbourClustering(tree, local_clustering)

    G_undirected = tree.to_undirected()

    network_size = tree.number_of_nodes()
    total_edges = tree.number_of_edges()

    triangles_per_node = nx.triangles(G_undirected)
    # networkx counts each triangle once per vertex, so the raw sum is 3×
    total_triangles = sum(triangles_per_node.values()) // 3

    total_weighted_degree = sum(dict(tree.degree(weight="weight")).values())
    density = nx.density(tree)

    try:
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", RuntimeWarning)
            assortativity = nx.degree_assortativity_coefficient(tree)
        if not np.isfinite(assortativity):
            assortativity = 0.0
    except Exception as exc:
        logger.warning("degree_assortativity_coefficient failed: %s", exc)
        assortativity = 0.0

    transitivity = nx.transitivity(G_undirected)

    # Use the undirected graph — average_shortest_path_length on a DiGraph
    # requires strong connectivity, which most code graphs don't satisfy.
    try:
        if nx.is_connected(G_undirected):
            avg_shortest_path = nx.average_shortest_path_length(G_undirected)
        else:
            largest_cc = max(nx.connected_components(G_undirected), key=len)
            avg_shortest_path = nx.average_shortest_path_length(G_undirected.subgraph(largest_cc))
    except Exception as exc:
        logger.warning("average_shortest_path_length failed: %s", exc)
        avg_shortest_path = 0.0

    graph_features = [network_size, total_edges, total_triangles, total_weighted_degree,
                      density, assortativity, transitivity, avg_shortest_path]

    # Reduce each of the 6 node-level metrics to 8 summary statistics.
    # 6 × 8 = 48 node features + 8 graph features = 56 total.
    node_metrics = [
        list(dict(weighted_degree).values()),
        list(eigenvector_centrality.values()),
        list(page_rank.values()),
        list(two_hop.values()),
        list(local_clustering.values()),
        list(neighbour_clustering.values()),
    ]

    fingerprint = []
    for values in node_metrics:
        arr = np.array(values, dtype=float)
        if arr.size == 0:
            fingerprint.extend([0.0] * 8)
            continue
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", RuntimeWarning)
            # keepdims=True ensures .mode returns a 1-D array regardless of scipy version
            mode_val = float(mode(arr, keepdims=True).mode[0])
            fingerprint.extend([
                float(np.median(arr)),
                float(np.mean(arr)),
                float(np.std(arr)),
                float(np.var(arr)),
                float(skew(arr)) if len(arr) > 1 else 0.0,
                mode_val,
                float(np.min(arr)),
                float(np.max(arr)),
            ])

    fingerprint.extend(graph_features)
    return np.array(fingerprint, dtype=float)


def twoHop(tree):
    """Count distinct 2-hop neighbours for each node (excluding self and 1-hop nodes)."""
    two_hop = {}
    for node in tree.nodes():
        one_hop = set(tree.successors(node))
        two_hop_set = set()
        for neighbour in one_hop:
            two_hop_set.update(tree.successors(neighbour))
        two_hop_set.discard(node)
        two_hop_set -= one_hop
        two_hop[node] = len(two_hop_set)
    return two_hop


def neighbourClustering(tree, local):
    """Average the local clustering coefficient across each node's direct neighbours."""
    avg_neigh_clustering = {}
    for node in tree.nodes():
        neighbours = list(set(list(tree.successors(node)) + list(tree.predecessors(node))))
        if neighbours:
            avg_neigh_clustering[node] = float(np.mean([local[nb] for nb in neighbours]))
        else:
            avg_neigh_clustering[node] = 0.0
    return avg_neigh_clustering
