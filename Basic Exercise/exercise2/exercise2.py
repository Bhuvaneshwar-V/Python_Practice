## Write a program to iterate the first 10 numbers, and in each iteration, print the sum of the current and previous number.
print("Printing current and previous number sum in a range(10)")
previous_num = 0
for i in range(10):
    sum = previous_num + i
    print("Current Number", i, "Previous Number", previous_num, "Sum: ", sum)
    previous_num = i
