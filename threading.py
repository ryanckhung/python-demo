import time
import threading

CBLUE = '\33[34m'
CRED = '\033[91m'
CEND = '\033[0m'


def fct1():
    count = 1
    while True:
        print((CRED  + "fct1: {}" + CEND).format(count))
        count = count + 1
        time.sleep(1)

def fct2():
    count = 1
    while True:
        print((CBLUE  + "fct2: {}" + CEND).format(count))
        count = count + 1
        time.sleep(2)

def fct3():
    count = 1
    while True:
        print("fct3: {}".format(count))
        count = count + 1
        time.sleep(3)


threading.Thread(target=fct1).start()
threading.Thread(target=fct2).start()
threading.Thread(target=fct3).start()