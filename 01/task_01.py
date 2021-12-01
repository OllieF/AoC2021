import sys

with open(sys.argv[1]) as fp:
    input_data = fp.read()

input_list = [int(number) for number in input_data.split("\n")]

total = 0

for i in range(1,len(input_list)+1):
    if input_list[i] > input_list[i-1]:
        total += 1

print(total)
