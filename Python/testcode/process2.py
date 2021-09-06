from multiprocessing import  Process, Pipe

def f1(con, n):
    import time
    time.sleep(2)
    con.send(n)
    con.close()
    print('msg sent')

def f2(con):
    msg = con.recv()
    print('msg received:', msg) 

if __name__ == "__main__":
    c1, c2 = Pipe()
    p1 = Process(target=f1, args=(c1, 1))
    p2 = Process(target=f2, args=(c2,))
    p2.start()
    p1.start()
    p2.join()
    p1.join()