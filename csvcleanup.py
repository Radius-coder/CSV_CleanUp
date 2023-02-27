#csv cleaner made to replace indents with commas by Darius Arian, 2021

filename = input("Enter the file name and file tag: ")
value = input("Enter the character you wish to replace with commas: ")

file = open(filename, 'r')
output = open('c_'+filename, 'w')

for n in file:
    output.write(value.join(n.split()))
    output.write('\n')
file.close()
output.close()
