import rq
from redis import Redis
from tasks import fibonacci

redis_conn = Redis(host='192.168.68.169', port=6379, db=0)
queue = rq.Queue(connection=redis_conn)

worker = rq.Worker(queues=[queue])
print("Woker: start")
worker.work()

