# python-threading1
Python threading tutorial using David Beazley's brilliant tutorial from PyCon 2015

The tutorial can be found here: https://www.youtube.com/watch?v=MCs5OvhV9S4

Notice that David uses Python 3, so there are subtle differences in the code.
I also put some comments to help me understand what is going on, and it may be useful for you too.

### How to run

To get the fibonacci server up and running:
```
python server.py
```

To connect to the server as a client (from other terminal tabs):
```
nc localhost 25000
```

And when you are a client, you can enter in a number n and expect to get the n-th fibonacci number back.

To see the power of process pools, run 
```
python perf2.py
```
while calculating several large fibonacci numbers at a time. Since each process handles this individually, the server won't be held up
since it is using all the CPUs, without being held back by Python's Global Interpeter Lock (GIL).
