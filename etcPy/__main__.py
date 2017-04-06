import argparse

from etcPy.queue import FTQueue

def main():
    """The main routine."""
    parser = argparse.ArgumentParser()

    parser.add_argument("--nodes", default=5, type=int, \
        help="Number of nodes (servers) in cluster, minimum 3 nodes")

    parser.add_argument("--label", default='queue', type=str, \
        help="Enter label for queue")

    args = vars(parser.parse_args())

    queue = FTQueue(args['nodes'], args['label'])

    # Cluster machines
    print(queue.client.machines)

    # HW Checklist
    queue.qPush('1234')
    queue.qPush('5')

    queue._get()

    queue.qPop()

    queue._get()

    print(queue.qTop())
    print(queue.qSize())

if __name__ == "__main__":
    main()
