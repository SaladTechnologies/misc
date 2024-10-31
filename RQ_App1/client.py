import rq
from redis import Redis
from tasks import fibonacci
import time

redis_conn = Redis(host='192.168.68.169', port=6379, db=0)
queue = rq.Queue(connection=redis_conn)

job1 = queue.enqueue(fibonacci, 10) 
job2 = queue.enqueue(fibonacci, 15) 
job3 = queue.enqueue(fibonacci, 20) 

jobs = [job1, job2, job3]

for job in jobs:
    while True:
        time.sleep(1)
        job_status = job.get_status() 
        if job_status == 'finished':
            print(f"Job Result: {job.result}")            
            break