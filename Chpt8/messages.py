def show_messages(msgs, sent_msgs):
    while msgs:
        show_msg = msgs.pop()

        print(f"print: {show_msg.title()}")
        sent_msgs.append(show_msg)


def send_messages(sent_msgs):
    print("\n")
    while sent_msgs:
        sent  = sent_msgs.pop()
        print(f"{sent.title()}")

msgs = ["How", "hey", "how are you"]
sent_msgs = []

show_messages(msgs, sent_msgs)
send_messages(sent_msgs)
