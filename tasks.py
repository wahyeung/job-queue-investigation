import time

def moving_average(prices, window = 5):
	print("Running moving average job....")
	time.sleep(2)
	return sum(prices[-window:]) /window
