#Write a Python program that accepts a word from the user and reverse it.

name=input("Enter the word: ")
for i in range(len(name)-1,-1,-1):
    print(name[i],end="")