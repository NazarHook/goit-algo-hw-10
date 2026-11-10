import random

import matplotlib.pyplot as plt
import numpy as np


def f(x):
    return x ** 2


a = 0  # нижня межа
b = 2  # верхня межа


def monte_carlo_integral(points):
    """Кидаємо точки у прямокутник [a, b] x [0, max f]. Площа під графіком = частка точок під кривою * площа прямокутника."""
    height = f(b)
    inside = 0
    for _ in range(points):
        x = random.uniform(a, b)
        y = random.uniform(0, height)
        if y <= f(x):
            inside += 1
    return inside / points * (b - a) * height


def draw_graph():
    x = np.linspace(-0.5, 2.5, 400)
    y = f(x)

    fig, ax = plt.subplots()
    ax.plot(x, y, "r", linewidth=2)

    ix = np.linspace(a, b)
    iy = f(ix)
    ax.fill_between(ix, iy, color="gray", alpha=0.3)

    ax.set_xlim([x[0], x[-1]])
    ax.set_ylim([0, max(y) + 0.1])
    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")
    ax.axvline(x=a, color="gray", linestyle="--")
    ax.axvline(x=b, color="gray", linestyle="--")
    ax.set_title("Графік інтегрування f(x) = x^2 від " + str(a) + " до " + str(b))
    plt.grid()
    plt.show()


def main():
    random.seed(42)
    exact = 8 / 3  # інтеграл x^2 від 0 до 2 = 2^3 / 3

    print(f"Аналітичне значення: {exact:.6f}")
    print("Точок   | Монте-Карло | Похибка")
    for points in [100, 1000, 10000, 100000, 1000000]:
        value = monte_carlo_integral(points)
        print(f"{points:>7} | {value:>11.6f} | {abs(value - exact):.6f}")

    draw_graph()


if __name__ == "__main__":
    main()
