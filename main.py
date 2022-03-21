my_list = []
for num in range(1, 1001, 2):
    my_list.append(num ** 3)
final_sum = 0
for num in my_list:
    sum_1 = 0
    for num_1 in str(num):
        sum_1 += int(num_1)
    if sum_1 % 7 == 0:
        final_sum += num
print(final_sum)
final_sum = 0
for num in my_list:
    num += 17
    sum_1 = 0
    for num_1 in str(num):
        sum_1 += int(num_1)
    if sum_1 % 7 == 0:
        final_sum += num
print(final_sum)