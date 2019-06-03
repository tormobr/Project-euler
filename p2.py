

# Each new term in the Fibonacci sequence is generated 
# by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

# By considering the terms in the Fibonacci sequence whose 
# values do not exceed four million, find the sum of the even-valued terms.


summ = 0
nums = [1, 1]
while(nums[-1] < 4000000):
    new = nums[-1] + nums[-2]
    nums.append(new)
    if new % 2 == 0:
        summ += new
print(summ)
