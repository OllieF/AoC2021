import sys

with open(sys.argv[1]) as fp:
    input_data = fp.read()

input_list = [int(number) for number in input_data.split("\n")]

total = 0

for i in range(4,len(input_list)+1):
    print(input_list[i-3:i], ":", input_list[i-4:i-1])
    # break
    if sum(input_list[i-3:i]) > sum(input_list[i-4:i-1]):
        total += 1

print(total)
