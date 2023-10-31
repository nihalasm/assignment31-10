file_name = input("Enter the name of the mbox file: ")

try:
    mbox_file = open(file_name, 'r')
except FileNotFoundError:
    print("File not found.")
    exit()

senders = []
for line in mbox_file:
    if line.startswith("From ") and not line.startswith("From:"):
        words = line.split()
        sender = words[1]
        senders.append(sender)

mbox_file.close()

for sender in senders:
    print(sender)

print("Number of senders:",len(senders))