### Distributed Systems HW 2

Implementation runs a Python wrapper for etcd raft implementation.

### Running

Install etcd

```
sudo apt-get install etcd
```

Set up vituralenv

```
virturalenv env
source env/bin/activate
pip install -r requirements.txt
```

Running module

```python -m etcPy```

Interactive

```
from etcPy.queue import FTQueue

# Init cluster and view machines
queue = FTQueue(3, 'queue')
queue.machines
queue.leader

#Get log
queue.client.read('queue')

#Add to queue
queue.qPush('1234')
queue.qPush('5')

#Get queue in log
queue._get()

#Pop item from queue
queue.qPop()
queue._get()

queue.qTop()
queue.qSize()

```
