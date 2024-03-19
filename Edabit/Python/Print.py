# Print the sum of the current number and the previous number

# Write a program to iterate the first 10 numbers, and in each iteration, print the sum of the current and previous number.

previous_num = 0

for i in range(10):
    x =previous_num + i
    print("current number",i, "previous number",previous_num, "Sum:", x)
    previous_num =i