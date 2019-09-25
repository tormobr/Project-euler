summ = 0
nums = [1, 1]
while(nums[-1] < 4000000):
    new = nums[-1] + nums[-2]
    nums.append(new)
    if new % 2 == 0:
        summ += new
print(summ)
