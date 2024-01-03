# This code uses the combo
# of while loop, if and input function

prompt = "Enter anything and I will repeat it back to you."
prompt += "\nEnter 'quit' to stop: "

msg = ""

while msg.lower() != 'quit':
    msg = input(prompt)

    if msg.lower() != 'quit':
        print(msg, end="\n\n")
    else:
        print("Program terminated.")