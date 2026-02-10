#Python Job Queues Investigation: Celery vs .RQ

##Overview
This repo prototypes job queuing with **RQ** and **Celery**, using Redis as the broker/backend.
A dummy financial analysis job (moving average) is used for testing.

##Prerequisites
-Python 3
-Docker (for Redis)

##Start Redis (Docker)
```bash
docker run -d -p 6379:6379 --name redis redis:latest
docker exec -it redis redis-cli ping
#Expect: PONG


##RQ Prototype
##Install Dependencies
```bash
pip install rq redis
##Start Worker (Terminal 1)
```bash
rq worker
##Submit Dummy Job(Terminal 2)
```bash
python2 rq_client.py
#Expected output:
Worker executes the moving average job successfully(~2 seconds)

##Celery Prototype
##Install Dependencies
```bash
pip install celery redis
##Start Celery Worker (Terminal 1)
```bash
celery -A celery_app worker --loglevel=info
##Submit Dummy Task(Terminal 2)
```bash
Python3 celery_client.py
##Expected output:
Task Submitted successfully
Result returned: 50.0

##Stop Redis(Optional)
After testing, stop the Redis container:
```bash
docker stop redis
To restart later:
docker start redis
 
