from rq import Queue
from redis import Redis
from tasks import moving_average

redis_conn = Redis(host="localhost", port=6379)
q = Queue(connection = redis_conn)

job = q.enqueue(moving_average, [10,20,30,40,50,60],3)

print("Job submitted successfully!")
print("Job ID:", job.id)
