import matplotlib.pyplot as plt
"""
labels: tipo evento
values: cantidad de eventos por tipo
"""
def generate_bar_chart(labels, values):
    fig, ax = plt.subplots()
    ax.bar(labels, values)
    plt.xticks(rotation=90)
    plt.show()


def generate_pie_chart(labels, values):
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    ax.axis('equal')
    plt.show()