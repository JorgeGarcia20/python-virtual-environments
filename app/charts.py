import matplotlib.pyplot as plt
from pathlib import Path


main_path = Path('.')


def generate_bar_chart(name, labels, values):
    fig, ax = plt.subplots()
    ax.bar(labels, values)
    img_path = main_path / 'img' / f'{name}.png'
    plt.savefig(img_path)
    plt.close()

def generate_pie_chart(labels, values):
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    ax.axis('equal')

    img_path = main_path / 'img' / 'pie.png'
    plt.savefig(img_path)
    plt.close()

