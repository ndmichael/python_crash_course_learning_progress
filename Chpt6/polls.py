poll_lists = ['jen', 'tahir', 'sarah', 'jamal', 'edward', 'phil']

poll_dict = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python'
}

for item in poll_lists:
    if item in poll_dict:
        print(f"Thanks for taking the pool {item.title()}.\n")
    else:
        print(f"Please do take the pool.\n")