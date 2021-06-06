import numpy
import random
import time
import asyncio
import os


def double_read_all():
    with open('/Users/david/Google Drive/Personal/Education/CSU-Global/CSC507 - Foundations of Operating Systems/Module 2/CSC507_Module2_PortfolioMilestone/python/file2.txt', 'r') as file:
        lines = file.readlines()

    results = []
    for line in lines:
        results.append(str(int(line.rstrip())*2))

    with open('newfile2.txt', 'w') as outfile:
        outfile.writelines('\n'.join(results)+'\n')


def line_at_a_time():
    results = []
    with open('/Users/david/Google Drive/Personal/Education/CSU-Global/CSC507 - Foundations of Operating Systems/Module 2/CSC507_Module2_PortfolioMilestone/python/file2.txt', 'r') as file:
        for value in file:
            results.append(str(int(value) * 2))

    with open('newfile2.txt', 'w') as outfile:
        outfile.writelines('\n'.join(results)+'\n')


def divide_file():
    results = []
    with open('/Users/david/Google Drive/Personal/Education/CSU-Global/CSC507 - Foundations of Operating Systems/Module 2/CSC507_Module2_PortfolioMilestone/python/file2-1.txt', 'r') as file:
        lines = file.readlines()
    for line in lines:
        results.append(str(int(line.rstrip())*2))
    with open('/Users/david/Google Drive/Personal/Education/CSU-Global/CSC507 - Foundations of Operating Systems/Module 2/CSC507_Module2_PortfolioMilestone/python/file2-2.txt', 'r') as file:
        lines2 = file.readlines()

    for line in lines2:
        results.append(str(int(line.rstrip())*2))

    with open('newfile2.txt', 'w') as outfile:
        outfile.writelines('\n'.join(results)+'\n')


def remove_file():
    if os.path.exists("file2.txt"):
        os.remove("file2.txt")


remove_file()
start_time = time.perf_counter()
double_read_all()
print("double_read_all: %s seconds" % (time.perf_counter() - start_time))
remove_file()
start_time = time.perf_counter()
line_at_a_time()
print("line_at_a_time: %s seconds" % (time.perf_counter() - start_time))
remove_file()
start_time = time.perf_counter()
divide_file()
print("divide_file: %s seconds" % (time.perf_counter() - start_time))
remove_file()
