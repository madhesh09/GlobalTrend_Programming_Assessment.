import time
import logging

logging.basicConfig(level=logging.INFO)

def execution_time_logger(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        logging.info(f"Executed {func.__name__} in {execution_time:.4f} seconds")
        return result
    return wrapper

@execution_time_logger
def expensive_computation(n):
    total = 0
    for i in range(n):
        for j in range(n):
            total += i * j
    return total

result = expensive_computation(3)
print("Result of expensive computation:", result)
