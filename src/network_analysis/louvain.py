import community as community_louvain

def detect_communities(graph):
    return community_louvain.best_partition(graph)
