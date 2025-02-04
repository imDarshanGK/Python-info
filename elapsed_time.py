import time

def measure_time():
    start = time.time()
    time.sleep(1)  # Sleep for 1 second
    elapsed = round(time.time() - start)
    print(f"Elapsed time: {elapsed} second(s)")

if __name__ == "__main__":
    measure_time()
