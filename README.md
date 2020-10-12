## Run the dask app
```
conda env create -f binder/environment.yml 
conda activate dask-learning
python3 add.py
```

## Distributed scheduler
### Local cluster - 1 process worker per core
```
from dask.distributed import Client
client = Client()
```

### command line
#### start scheduler
```
command: dask-scheduler
    Scheduler at:   tcp://192.0.0.100:8786
```

#### start worker
```
Command: dask-worker tcp://192.0.0.100:8786(scheduler address)
    Start worker at:  tcp://192.0.0.1:12345
    Registered to:    tcp://192.0.0.100:8786(the sheduker process)
    (Each worker is started under the supervisio of a nanny procesd)
```

### SSH cluster
```
from dask.distributed import Client, SSHCluster
cluster = SSHCluster(
    ["localhost", "hostwithgpus", "anothergpuhost"],
    connect_options={"known_hosts": None},
    scheduler_options={"port": 0, "dashboard_address": ":8797"},
    worker_module='dask_cuda.dask_cuda_worker')
client = Client(cluster)
```

### Kubernetes cluster
```
from dask_kubernetes import KubeCluster
cluster = KubeCluster.from_yaml('worker-template.yaml')
cluster.scale(20)  # add 20 workers
cluster.adapt()    # or create and destroy workers dynamically based on workload

from dask.distributed import Client
client = Client(cluster)
```

### yarn cluster
```
from dask_yarn import YarnCluster
from dask.distributed import Client

# Create a cluster where each worker has two cores and eight GiB of memory
cluster = YarnCluster(environment='environment.tar.gz',
                      worker_vcores=2,
                      worker_memory="8GiB")
# Scale out to ten such workers
cluster.scale(10)

# Connect to the cluster
client = Client(cluster)
```


