import time

wait_time = 1
max_retry = 6
attempts = 0

while attempts < max_retry:
    time.sleep(wait_time)
    wait_time *= 2
    attempts += 1
    print("Attempts ",attempts + 1,"wait time ",wait_time)
