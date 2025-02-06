# Write a python program to read a file containing pairs of numbers in a file. Create a file that contains the pairs of numbers as well as addition and multiplication of the two numbers in the same line.

ip_file = open('file1.txt','r')
op_file = open('file2.txt','w')
for line in ip_file:
    num1, num2 = map(int, line.strip().split())
    add = num1 + num2
    multi = num1 * num2

op_file.write(f"First number: {num1}\nSecond number: {num2} \nAddition: {num1}+{num2}={add} \nMultipication: {num1}*{num2}={multi}")
print("Process complete")