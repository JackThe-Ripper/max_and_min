#test1 min
test_list = [1, -5, 107, -278, 0 , 2, 54, -4]
minimum = test_list[0]

for num in test_list:
    if num < minimum:
        minimum = num

print('min is ', minimum)

#test2 max

maximum = test_list[0]
for num2 in test_list:
    if num2 > maximum:
        maximum = num2

print('max is ', maximum)
