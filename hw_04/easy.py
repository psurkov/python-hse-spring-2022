import time
from multiprocessing import Process
from threading import Thread


def fibonacci(n):
    res = [0, 1]
    while len(res) < n:
        res.append(res[-1] + res[-2])
    return res[:n]


if __name__ == '__main__':
    n = 100000

    start_time = time.time()
    for _ in range(10):
        fibonacci(n)
    sync_time = time.time() - start_time

    start_time = time.time()
    threads = [Thread(target=fibonacci, args=(n,)) for _ in range(10)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    threads_time = time.time() - start_time

    start_time = time.time()
    processes = [Process(target=fibonacci, args=(n,)) for _ in range(10)]
    for process in processes:
        process.start()
    for process in processes:
        process.join()
    process_time = time.time() - start_time

    with open("artifacts/easy.txt", "w") as file:
        file.write("sync time: " + sync_time.__str__() + "s\n")
        file.write("threads time: " + threads_time.__str__() + "s\n")
        file.write("process time: " + process_time.__str__() + "s\n")
