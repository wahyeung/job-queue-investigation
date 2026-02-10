from celery import Celery
import time

#Celery app configuration (Redis as broker + backend)
app = Celery(
	"demo",
	broker = "redis://localhost:6379/0",
	backend ="redis://localhost:6379/0",
)

#Dummy financial analysis task: moving average
@app.task
def moving_average(prices, window =5):
	print("Running moving average jov in Celery...")
	time.sleep(2)
	return sum(prices[-window:])/window
