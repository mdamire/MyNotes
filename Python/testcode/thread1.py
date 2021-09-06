def d1():
    i = 0
    print('iteration: ', i)
    while True:
        i += 1
        import time
        time.sleep(6)
        print('iteration: ', i)


if __name__ == "__main__":
    import threading
    t1 = threading.Thread(target=d1)
    t1.start()
    t1.join(timeout=3.0)
    print('hello')
    exit()