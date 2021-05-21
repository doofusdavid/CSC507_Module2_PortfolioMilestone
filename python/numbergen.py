from numpy import random

numbers = random.randint(0, high=32767, size=1000)
str_numbers = [str(int) for int in numbers]
with open('file2.txt', 'w') as file:
    file.write('\n'.join(str_numbers))
    file.write('\n')
