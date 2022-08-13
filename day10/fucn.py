import time
from functools import lru_cache


@lru_cache(maxsize=1)
def some_work(n):
    # some task is goin on
    time.sleep(n)
    return n

if __name__ == '__main__':
    print('NOW SOME WORK IS GOING ON')
    some_work(5)
    print('WORK FUNCTION IS CALLING AGAIN')
    some_work(5)
    some_work(5)
    print("work is done")
    print('_______________')
    some_work(4)
    print('+++++++++++++++++++')
    some_work(4)
    some_work(4)
    print("&&&&&&&&&&&&&&&&&&")
    some_work(6)
    print("######################") 
    some_work(6)
    some_work(6)
    print("*****************")
    some_work(7)
    print("delay of 7 second")
    some_work(7)
    print("delay after 7 seconds")
    some_work(8)
    print("delay of 8 second")
    some_work(8)
    print("delay after 8 seconds")
    print("now running some work")
    some_work(3)
    some_work(2)
    print("done.....calling again")
    input()
    some_work(2)
    print("skiping the value 2")
    some_work(3)
    print("called again")
    