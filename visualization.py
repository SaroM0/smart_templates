import networkx as nx
import matplotlib.pyplot as plt

def draw_graph(graph: nx.Graph) -> None:
    print("Dibujando grafo...")
    pos = nx.spring_layout(graph)
    plt.figure(figsize=(10, 8))
    nx.draw_networkx_nodes(graph, pos, node_size=700, node_color='lightblue')
    nx.draw_networkx_labels(graph, pos, font_size=10, font_family="sans-serif")
    nx.draw_networkx_edges(graph, pos, edgelist=graph.edges, width=1, alpha=0.5)
    
    edge_labels = nx.get_edge_attributes(graph, 'weight')
    formatted_edge_labels = {edge: f"{weight:.2f}" for edge, weight in edge_labels.items()}
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=formatted_edge_labels, font_size=8)

    plt.title("Query Graph and Similarity")
    plt.show()
