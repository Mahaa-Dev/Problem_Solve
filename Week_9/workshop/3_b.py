dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
nums = dict(list(dic1.items()) + list(dic2.items()) + list(dic3.items()))
print(nums)

#code to add a new key/value pair to the dictionary nums: (7, 70)
nums[7] = 70
print(nums)

#code to update the value of the item with key 3 in nums to 80
nums.update({3: 80})
print(nums)

#code to remove the third item from dictionary nums.
del nums[3]
print(nums)

# code to sum all the items in the dictionary nums
total = sum(nums.values())
print(total)

# code to multiply all the items in the dictionary nums
product = 1
for value in nums.values():
    product *= value
print(product)

# code to retrieve the maximum and minimum values in nums.
maximum = max(nums.values())
minimum = min(nums.values())
print("Maximum value:", maximum)
print("Minimum value:", minimum)
