from threading import Timer
QUANTUM = 5
COUNT = 0
INDEXLIB = []
def start_time(*args, **kwargs):
    global COUNT, INDEXLIB
    INDEXLIB.append(COUNT)
    COUNT = COUNT + 1
    print(INDEXLIB)
    t = Timer(QUANTUM, start_time, (QUANTUM,))
    t.start()

start_time()