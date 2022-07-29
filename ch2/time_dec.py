import time
from functools import wraps

from julia import full_run

def time_dec(fn):
    @wraps(fn)
    def inner(*args, **kwargs):
        start_time = time.time()
        result = fn(*args, **kwargs)
        print(f"Running {fn.__name__} took {time.time() - start_time}")
        return result
    return inner

@time_dec
def decorated_run():
    return full_run()

if __name__ == "__main__":
    full_run()
