# Celery vs. RQ — Prototype Comparison

## Test Setup
- Broker/Backend: Redis (`redis://localhost:6379/0`) via Docker
- Dummy job: Moving average on the last N prices + `sleep(2)` to simulate compute time

## RQ Prototype
**Workflow**
- Client enqueues a Python function call into Redis via `q.enqueue(...)`
- `rq worker` listens to the queue, pulls jobs, executes them, and stores results temporarily in Redis

**Observed Result**
- Job executed successfully
- Worker runtime ~2 seconds (expected due to `sleep(2)`)

## Celery Prototype
**Workflow**
- Client submits a task asynchronously via `task.delay(...)`
- `celery worker` consumes tasks from Redis broker, executes them, and stores results via the backend

**Observed Result**
- Task executed successfully
- Worker runtime ~2.015 seconds
- Result returned: `50.0`

## Comparison

| Dimension | RQ | Celery |
|---|---|---|
| Setup complexity | Very simple (minimal config) | More setup (Celery app config + worker options) |
| Features | Basic queueing | Rich features (retries, routing, scheduling, chains) |
| Reliability/ops | Simple, lightweight | Mature ecosystem for production ops |
| Distributed workloads | Works, limited orchestration | Better fit for large-scale distributed systems |
| Best fit | Simple background jobs | Production systems with complex workflows |

## Recommendation
- Choose **RQ** for quick, lightweight background processing with minimal operational overhead.
- Choose **Celery** when you need advanced workflow features and stronger support for distributed/production workloads.
