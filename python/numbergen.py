import numpy
import random
import time
import asyncio
import os


def generate_standard():
    start_time = time.perf_counter()
    with open('file2.txt', 'w') as file:
        for i in range(1000000):
            file.write(str(random.randint(0, 32767)) + '\n')
        return time.perf_counter() - start_time


def generate_numpy():
    start_time = time.perf_counter()
    numbers = numpy.random.randint(0, high=32767, size=1000000)
    str_numbers = [str(int) for int in numbers]
    with open('file2.txt', 'w') as file:
        file.write('\n'.join(str_numbers))
        file.write('\n')
    return time.perf_counter() - start_time


async def generate_standard_hundredk():
    result = ""
    for i in range(100000):
        result += str(random.randint(0, 32767)) + "\n"
    return result


async def generate_standard_await():
    tasks = [generate_standard_hundredk(),
             generate_standard_hundredk(),
             generate_standard_hundredk(),
             generate_standard_hundredk(),
             generate_standard_hundredk(),
             generate_standard_hundredk(),
             generate_standard_hundredk(),
             generate_standard_hundredk(),
             generate_standard_hundredk(),
             generate_standard_hundredk()]
    results = await asyncio.gather(*tasks)
    for result in results:
        with open('file2.txt', 'w') as file:
            file.write(result)


async def generate_numpy_hundredk():
    result = ""
    numbers = numpy.random.randint(0, high=32767, size=100000)
    str_numbers = [str(int) for int in numbers]
    return ('\n'.join(str_numbers))


async def generate_numpy_await():
    tasks = [generate_standard_hundredk(),
             generate_standard_hundredk(),
             generate_standard_hundredk(),
             generate_standard_hundredk(),
             generate_standard_hundredk(),
             generate_standard_hundredk(),
             generate_standard_hundredk(),
             generate_standard_hundredk(),
             generate_standard_hundredk(),
             generate_standard_hundredk()]
    results = await asyncio.gather(*tasks)
    for result in results:
        with open('file2.txt', 'w') as file:
            file.write(result)


def remove_file():
    if os.path.exists("file2.txt"):
        os.remove("file2.txt")


remove_file()
start_time = time.perf_counter()
asyncio.run(generate_numpy_await())
print("Async Numpy: %s seconds" % (time.perf_counter() - start_time))
remove_file()

start_time = time.perf_counter()
asyncio.run(generate_standard_await())
print("Async Standard: %s seconds" % (time.perf_counter() - start_time))
remove_file()

print("Standard: %s seconds" % generate_standard())
remove_file()
print("Numpy: %s seconds" % generate_numpy())
remove_file()
