# 4.3
for num in range(1, 21):
    print(num, sep="", end=" ")


# 4.4
nums = list(range(1, 1_000_001))

# for num in nums:
#     print(num, end=" ")
#     if num in [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]:
#         print("\n")

print(min(nums))
print(max(nums))
print(sum(nums))


# 4.6
for i in range(1, 20, 2):
    print(i, end=" ")
print("\n")

# 4.7
print("***** Multiples of 3 *****")
mult_of_3 = [i * 3 for i in range(3, 20)]
for res in mult_of_3:
    print(res, end=" ")
print("\n")

# 4.8 4.9
print("***** Cubes *****")
mult_of_3 = [i ** 3 for i in range(1, 11)]
for res in mult_of_3:
    print(res, end=" ")
