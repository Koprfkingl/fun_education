# every timer needs some calculations. this is it
"""
author: Michal Sykora
date: 17.4.2023
license: free garbage ®
"""

import time


def timer(how_long: int = 60) -> bool:
    """
    Decrement given input until zero, then return True.

    :param how_long: integer, default value is 1 hour in minutes
    :return: bool, True if triggered
    """
    # module time works with seconds by default
    how_long = int(how_long) * 60
    current_time = int(time.time())
    target_time = current_time + how_long

    print(f"current time: {time.ctime(current_time)}\n",
          f"target time: {time.ctime(target_time)}")

    # countdown to zero
    while True:
        if current_time == target_time:
            return True
        else:
            current_time = int(time.time())
            # wait a minute
            time_remaining = target_time - current_time
            print(f'time remaining: {time_remaining}')
            time.sleep(10)
            return time_remaining

if __name__ == "__main__":
    print(timer(1))
