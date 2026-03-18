import warnings
import networkx as nx
import numpy as np
from scipy.stats import skew, mode

def features(tree):
    ## Phase 1:
    # Calculate the 6 node-level metrics
    # Weighted Degree, Eigenvector Centrality, Page Rank, Two-Hop Neighbours, 
    # Local Clustering Coefficient, Average Clustering Coefficient of Neighbours

    weighted_degree = tree.degree(weight="weight")
    try:
        eigenvector_centrality = nx.eigenvector_centrality(tree, weight="weight", max_iter=1000)
    except nx.PowerIterationFailedConvergence:
        eigenvector_centrality = {node: 0.0 for node in tree.nodes()}
    page_rank = nx.pagerank(tree, weight="weight")
    local_clustering = nx.clustering(tree.to_undirected())
    two_hop = twoHop(tree)
    neighbour_clustering = neighbourClustering(tree, local_clustering)

    ## Phase 2:
    # Calculate the 8 graph-level metrics
    # Network size, Total edges, Total triangles, Total weighted degree,
    # Density, Assortativity, Transitivity, Average shortest path length

    G_undirected = tree.to_undirected()

    network_size = tree.number_of_nodes()
    total_edges = tree.number_of_edges()

    triangles_per_node = nx.triangles(G_undirected)
    total_triangles = sum(triangles_per_node.values()) // 3

    total_weighted_degree = sum(dict(tree.degree(weight="weight")).values())
    density = nx.density(tree)

    try:
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", RuntimeWarning)
            assortativity = nx.degree_assortativity_coefficient(tree)
    except Exception:
        assortativity = 0.0

    transitivity = nx.transitivity(G_undirected)

    try:
        if nx.is_weakly_connected(tree):
            avg_shortest_path = nx.average_shortest_path_length(tree)
        else:
            largest_cc = max(nx.weakly_connected_components(tree), key=len)
            avg_shortest_path = nx.average_shortest_path_length(tree.subgraph(largest_cc))
    except Exception:
        avg_shortest_path = 0.0

    graph_features = [network_size, total_edges, total_triangles, total_weighted_degree,
                      density, assortativity, transitivity, avg_shortest_path]

    ## Phase 3: Reduce node-level metrics to fixed-size statistics
    # For each of the 6 node metrics, compute 8 stats = 48 features
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
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", RuntimeWarning)
            fingerprint.extend([
                float(np.median(arr)),
                float(np.mean(arr)),
                float(np.std(arr)),
                float(np.var(arr)),
                float(skew(arr)) if len(arr) > 1 else 0.0,
                float(mode(arr, keepdims=True).mode[0]),
                float(np.min(arr)),
                float(np.max(arr)),
            ])

    # Append the 8 graph-level features: total = 56
    fingerprint.extend(graph_features)

    return np.array(fingerprint, dtype=float)

## Two-Hop Neighbours Algorithm
# For each node, get its direct neighbours then their neighbours
# Remove the original node and the 1-hop nodes
def twoHop(tree):
    two_hop = {}
    for node in tree.nodes():
        one_hop =  set(tree.successors(node))
        two_hop_set = set()
        for neighbour in one_hop:
            two_hop_set.update(tree.successors(neighbour))
        two_hop_set.discard(node)
        two_hop_set -= one_hop
        two_hop[node] = len(two_hop_set)
    return two_hop

## Average Clustering Coefficient of Neighbourhoods
# For each node, look calculate clustering score of each of its
# neighbours and average them
def neighbourClustering(tree, local):
    avg_neigh_clustering = {}
    for node in tree.nodes():
        neighbours = list(set(list(tree.successors(node)) + list(tree.predecessors(node))))
        if neighbours:
            avg_neigh_clustering[node] = float(np.mean([local[nb] for nb in neighbours]))
        else:
            avg_neigh_clustering[node] = 0.0
    return avg_neigh_clustering