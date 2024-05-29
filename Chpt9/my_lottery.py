from random import sample, randint

nums = sample(range(0,10), 10)
alphabets = ['t', 'm', 'd', 'j']

winning = []

w_nums = sample(nums, 4)
w_alp = sample(alphabets, 2)

winning = w_alp + w_nums




print(winning)