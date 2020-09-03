import threading

def print_numbers():
    for i in range(1, 11):
        print(i)

class PrintThread(threading.Thread):
    def run(self):
        for i in range(1, 11):
            print(i)


ct = threading.current_thread()
print(ct)
t1 = PrintThread()
t1.start()

t2 = threading.Thread(target=print_numbers)
t2.start()

# for i in range(100, 110):
#     print(i)
