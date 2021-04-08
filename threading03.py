import threading
import time

tLock = threading.Lock()


def timer(name, delay, repeat):
    print("Timer: " + name + " Started")



    while repeat > 0:

        tLock.acquire()
        print(name + " Has Acquired the lock")

        time.sleep(delay)
        print(name + ": " + str(time.ctime(time.time())))
        repeat -= 1
        tLock.release()

        print(name + " is releasing the lock")


    print("Timer: " + name + " Completed")


t1 = threading.Thread(target=timer, args=("Timer1", 1, 5))
t2 = threading.Thread(target=timer, args=("Timer2", 2, 5))
t1.start()
t2.start()

print("Main complete")
