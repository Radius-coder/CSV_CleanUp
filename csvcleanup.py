#csv cleaner made to replace indents with commas by Darius Arian, 2021

filename = input("Enter the file name and file tag: ")

file = open(filename, 'r')
output = open('c_'+filename, 'w')

for n in file:
    output.write(','.join(n.split()))
    output.write('\n')
file.close()
output.close()
