import matplotlib.pyplot as plt

def show_graph(minimax_nodes, alphabeta_nodes):

    labels = ["Minimax","Alpha-Beta"]
    values = [minimax_nodes, alphabeta_nodes]

    plt.figure(figsize=(6,5))

    bars = plt.bar(labels,values)

    for bar in bars:
        y = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, y,
                 int(y),
                 ha='center',
                 va='bottom')

    plt.title("Minimax vs Alpha-Beta Node Exploration")
    plt.ylabel("Nodes Explored")

    plt.show()