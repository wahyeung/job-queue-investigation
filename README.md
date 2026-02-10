
# Python Job Queues Investigation: Celery vs. RQ

## Overview
This repository prototypes job queuing with **RQ** and **Celery**, using Redis as the broker/backend.

A dummy financial analysis job (moving average) is used for testing.

---

## Prerequisites
- Python 3
- Docker (for Redis)

---

## Start Redis (Docker)

Run Redis locally using Docker:

```bash
docker run -d -p 6379:6379 --name redis redis:latest
docker exec -it redis redis-cli ping
# Expect: PONG


⸻

RQ Prototype

Install Dependencies

pip install rq redis

Start Worker (Terminal 1)

rq worker

Submit Dummy Job (Terminal 2)

python3 rq_client.py

Expected behavior:
	•	Worker executes the moving average job successfully (~2 seconds)

⸻

Celery Prototype

Install Dependencies

pip install celery redis

Start Celery Worker (Terminal 1)

celery -A celery_app worker --loglevel=info

Submit Dummy Task (Terminal 2)

python3 celery_client.py

Expected behavior:
	•	Task submitted successfully
	•	Result returned: 50.0

⸻

Stop Redis (Optional)

After testing, stop the Redis container:

docker stop redis

To restart later:

docker start redis


⸻

Files Included
	•	tasks.py — dummy moving average job for RQ
	•	rq_client.py — enqueue job using RQ
	•	celery_app.py — Celery configuration + task definition
	•	celery_client.py — submit Celery task
	•	comparison.md — summary and recommendation

