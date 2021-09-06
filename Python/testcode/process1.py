from multiprocessing import Process, Queue
import os

def f1(n, q):
    print(f'process {n} pid: ', os.getpid())
    print(f'process {n} ppid: ', os.getppid())
    q.put(n)

if __name__ == "__main__":
    q = Queue()
    f1('main', q)
    p1 = Process(target=f1, args=(1,q))
    p2 = Process(target=f1, args=(2,q))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print(q.qsize(), q.get())