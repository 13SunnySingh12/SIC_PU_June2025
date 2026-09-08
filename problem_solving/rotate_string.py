'''
Charlie has a magic mirror that shows right-rotated versions of a word. A right rotation of a word is formed by writing the word in a circle and reading it clockwise starting from any character.

For example, the right rotations of "sample" are:

---> "sample", "amples", "mplesa", "plesam", "lesamp", "esampl"

Write a function isSameReflection(word1, word2) that:

---> Takes two strings as input

---> Returns 1 if word1 and word2 are right rotations of the same original word

---> Returns -1 if they are not

'''

def is_right_rotation(original, rotated):
    if len(original) != len(rotated):
        return -1 
    else:
        if rotated in (original * 2):
            return 1  
        else:
            return -1  
    
original_string = input("Enter the original string: ")
rotated_string = input("Enter the rotated string: ")


print(is_right_rotation(original_string, rotated_string))
