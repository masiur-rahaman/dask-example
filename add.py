from time import sleep
from dask import delayed
from dask.distributed import Client


def inc(x):
    sleep(1)
    return x + 1


def add(x, y):
    sleep(1)
    return x + y


if __name__ == '__main__':
    # Setup a local cluster.
    # By default this sets up 1 worker per core
    client = Client()
    client.cluster
    x = delayed(inc)(1)
    y = delayed(inc)(2)
    z = delayed(add)(x, y)
    res = z.compute()
    print(res)
    z.visualize()
    sleep(100)
