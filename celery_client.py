from celery_app import moving_average

#Submit task asynchronously
result = moving_average.delay([10, 20, 30, 40, 50, 60],3)

print("Task submitted successfully!")
print("Task ID:", result.id)

#Wait for result (demo purpose)
print("Result:", result.get(timeout = 10))
