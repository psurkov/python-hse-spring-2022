import functools
import multiprocessing
import os
import time
from concurrent.futures import ProcessPoolExecutor
import math


def _integrate(f, step, log, integrate_range):
    if log:
        print("Integrate range {} using process {}".format(integrate_range, os.getpid()))
    cur = integrate_range[0]
    res = 0
    while cur < integrate_range[1]:
        res += f(cur) * min(integrate_range[1] - cur, step)
        cur += step
    return res


def integrate(f, a, b, *, n_jobs=1, n_iter=1000, log=True):
    if log:
        print("Integrate function from {} to {} using {} jobs with {} iters:".format(a, b, n_jobs, n_iter))
    partial_integrate = functools.partial(_integrate, f, (b - a) / n_iter, log)
    range_step = (b - a) / n_jobs

    def next_range():
        cur = a
        while cur < b:
            next_cur = cur + range_step
            yield cur, min(next_cur, b)
            cur = next_cur

    with ProcessPoolExecutor(max_workers=n_jobs) as executor:
        return sum(executor.map(partial_integrate, next_range()))


def compare_time():
    print("Comparing time...")
    f = functools.partial(integrate, math.cos, 0, math.pi / 2, n_iter=1000000, log=False)

    res = []
    for i in range(1, 8 * 2 + 1):
        start_time = time.time()
        for _ in range(3):
            f(n_jobs=i)
        t = (time.time() - start_time) / 5
        res.append((i, t))
    print("Done!")
    return res


if __name__ == '__main__':
    print(integrate(math.cos, 0, math.pi / 2, n_jobs=10, n_iter=1000000))
    res = compare_time()
    with open("artifacts/medium_compare.txt", "w") as file:
        for i in res:
            file.write("n_jobs={}\ttime={}\n".format(*i))
