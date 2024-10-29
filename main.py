# main.py
from graph_manager import add_query_to_graph, G
from visualization import draw_graph
from queries import queries

if __name__ == "__main__":
    for query in queries:
        add_query_to_graph(query, G)
    
    draw_graph(G)

    print("Graph nodes:")
    for node in G.nodes:
        print(node)
    print("\nGraph edges (with similarity):")
    for edge in G.edges(data=True):
        print(edge)
