import networkx as nx
import numpy as np

# Calculate the metrics
# Weighted Degree, Eigenvector Centrality, Page Rank, Two-Hop Neighbours, Local Clustering Coefficient, Average Clustering Coefficient of Neighbours
def features(tree):
    weighted_degree = tree.degree(weight="weight")
    try:
        eigenvector_centrality = nx.eigenvector_centrality(tree, weight="weight", max_iter=1000)
    except nx.PowerIterationFailedConvergence:
        eigenvector_centrality = {node: 0.0 for node in tree.nodes()}
    page_rank = nx.pagerank(tree, weight="weight")
    local_clustering = nx.clustering(tree.to_undirected())
    two_hop = twoHop(tree)
    neighbour_clustering = neighbourClustering(tree, local_clustering)
    return weighted_degree, eigenvector_centrality, page_rank, two_hop, local_clustering, neighbour_clustering

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