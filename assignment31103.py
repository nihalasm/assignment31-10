
file_name = "romeo.txt"
try:
    file = open(file_name, 'r')
except FileNotFoundError:
    print(f"File '{file_name}' not found.")
    exit()

unique_words = []
for line in file:
    words = line.split()
    for word in words:
        if word not in unique_words:
            unique_words.append(word)
unique_words.sort()
for word in unique_words:
          print(word)