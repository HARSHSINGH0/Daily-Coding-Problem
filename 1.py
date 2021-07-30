# This problem was asked by Apple.

# Implement a job scheduler which takes in a function f and an integer n,
#  and calls f after n milliseconds.
import sched, time
s = sched.scheduler(time.time, time.sleep)
def do_something(sc): 
    print("Doing stuff... after 10 miliseconds")
    # do your stuff
    s.enter(1/100, 1, do_something, (sc,))

s.enter(1/100, 1, do_something, (s,))#1/10 for 10 miliseconds basically 1 seconds has 1000 miliseconds
s.run()
