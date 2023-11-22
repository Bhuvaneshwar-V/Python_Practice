str_x = "Emma is good developer. Emma is a writer"
count = 0
for word in str_x.split():
    print(word)
    if word == 'Emma':
        count += 1

print('Emma appeared', count, 'times')