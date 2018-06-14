import threading, time

total = []

def update_total(n):
    global total
    if len(total) < 6:
        total.append(n)
    print(total)
    # time.sleep(2)

if __name__ == '__main__':
    for i in range(10):
        myThread = threading.Thread(target=update_total, args=(i,))
        myThread.start()