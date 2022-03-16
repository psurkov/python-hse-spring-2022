import multiprocessing
import time
from datetime import datetime
from multiprocessing import Queue
import codecs


def a_func(main_to_a: Queue, a_to_b: Queue):
    while True:
        while not main_to_a.empty():
            a_to_b.put(main_to_a.get_nowait().lower())
            time.sleep(5)


def b_func(a_to_b: Queue, b_to_main: Queue):
    while True:
        b_to_main.put(codecs.encode(a_to_b.get(), "rot_13"))


if __name__ == '__main__':
    main_to_a = Queue()
    a_to_b = Queue()
    b_to_main = Queue()
    multiprocessing.Process(target=a_func, args=(main_to_a, a_to_b), daemon=True).start()
    multiprocessing.Process(target=b_func, args=(a_to_b, b_to_main), daemon=True).start()
    while True:
        main_to_a.put(input(datetime.now().strftime("%H:%M:%S") + "> "))
        res = b_to_main.get()
        print(datetime.now().strftime("%H:%M:%S") + ">", res)
