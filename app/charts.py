import matplotlib.pyplot as plt


def generate_bar_chart(name, labels, values):
    fig, ax = plt.subplots()
    ax.bar(labels, values)
    plt.xticks(rotation=90)
    plt.savefig(f'./imgs/{name}_bar.png')

def generate_pie_chart(name, labels, values):
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    ax.axis('equal')
    plt.savefig(f'./imgs/{name}_pie.png')

if __name__ == '__main__':
    labels = ['a', 'b', 'c']
    values = [100, 200, 400]
    generate_bar_chart('example', labels, values)
    generate_pie_chart('example', labels, values)
