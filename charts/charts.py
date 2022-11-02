import matplotlib.pyplot as plt


def generate_bar_chart(labels, values):
    fig, ax = plt.subplots()
    ax.bar(labels, values)
    plt.savefig('img/bar.png')
    plt.close()


def generate_pie_chart(names, values):
    fig, ax = plt.subplots()
    ax.pie(values, labels=names)
    plt.savefig('img/pie.png')
    plt.close()


"""
def generate_pie_chart():
    labels = ['A', 'B', 'C']
    values = [23, 43, 21]

    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)

    plt.savefig('charts/pie.png')
    plt.close()
"""
