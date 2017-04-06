import etcd

class FTQueue(object):
    """Manipulate Queue data structure"""
    def __init__(self, nodes, label):
        self.client = None
        self.label = label
        self.nodes = self._init_clients(nodes)
        self.queue = self.qCreate(self.label)


    def _init_clients(self, nodes):

        # for node in range(nodes):
        #     port = 4000 + node
        #     self.client = etcd.Client(port=port)
        self.client = etcd.Client()


    def _get(self):
        print( self.client.read(self.label).value )


    def qCreate(self, label):
        """Creates a new queue of integers; associates this \
        queue with label and returns a queue id"""

        self.client.write(label,'')
        self.label = self.client.read(label).key
        print('qCreate:', self.label)


    def qId(self):
        """Returns queue id of the queue associated with label"""

        return self.label


    def qPush(self, item):
        """Enter item in the queue"""

        queue = self.client.read(self.label).value

        for ii in item:
            queue = str(ii) + queue

        self.client.write(self.label, queue)


    def qPop(self):
        """Removes an item from the queue and returns it"""

        queue = self.client.read(self.label).value
        self.client.write(self.label, queue[:-1])

    def qTop(self):
        """Returns the value of thefirst element in the queue"""

        queue = self.client.read(self.label).value
        return queue[0]

    def qSize(self):
        """Returns the number of items in the queue"""

        queue = self.client.read(self.label).value
        return len(queue)
