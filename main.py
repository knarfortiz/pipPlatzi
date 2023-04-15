import matplotlib.pyplot as plt
import requests as res


def generate_pie_chart():
    labels = ['A', 'B', 'C']
    values = [200, 34, 120]

    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    plt.savefig('pie_chart.png')
    plt.close()


def get_categories():
    response = res.get("https://api.escuelajs.co/api/v1/categories")
    print(response.status_code)
    categories = response.json()
    for category in categories:
        print(category['name'])


def print_hi(name):
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


if __name__ == '__main__':
    get_categories()
    # print_hi('PyCharm')
    # generate_pie_chart()
