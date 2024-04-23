'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
phonebook = []

def main():
    with open("phonenumbers.txt") as file:
        for line in file:
            print (repr(line))
            name, number = line.split() 
            phonebook.append(name) 
            phonebook.append(number)
main()

def lookup(name):
    for i in range(len(phonebook)):
        if phonebook[i] == name:
            print("Phone number is ", phonebook[i+1])
print (phonebook)