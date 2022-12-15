import matplotlib.pyplot as plt
import numpy as np
import psutil
from concurrent.futures import ThreadPoolExecutor


def histogram():
    for i in range(10):
        n = np.random.normal(100, 8, 250000)
        plt.hist(n)
        plt.show()


def cpu():
    for i in range(50):
        print(psutil.cpu_percent(interval=1))


def main():
    with ThreadPoolExecutor() as exe:
        exe.submit(cpu)
        exe.submit(histogram)


if __name__ == 'main':
    main()