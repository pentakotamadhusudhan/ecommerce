import threading
import time
def tread():
    print("Madhu")



def thread_delay(thread_name, delay):
    count = 0
    while count < 3:
        time.sleep(delay)
        count += 1
        print(thread_name, '-------->', time.time())



# if __name__ =="__main__":
t = threading.Thread(target=tread)
t1 = threading.Thread(target=thread_delay,args=("5",5,))
t.start()
t1.start()

print("done")