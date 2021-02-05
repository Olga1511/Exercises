# Write a procedure, rotate which takes as its input a string of lower case
# letters, a-z, and spaces, and an integer n, and returns the string constructed
# by shifting each of the letters n steps, and leaving the spaces unchanged.
# Note that 'a' follows 'z'. You can use an additional procedure if you
# choose to as long as rotate returns the correct string.
# Note that n can be positive, negative or zero.

def shift_n_letters(letter, n):
    return chr(ord('a') + (ord(letter) - ord('a') + n) % 26)

def rotate(s, n):
    # Your code here
    ans = ''
    for i in range(len(s)):
        if s[i] != ' ': ans += shift_n_letters(s[i], n)
        else: ans += ' '
    return ans


def process(word, n):
    print("---------------------> here " +   word)
    new_word = ""
    for i in range(len(word)):
        # print(word[i])  o
        for j in range(len(alphabet)):
            print(alphabet[j])
            if alphabet[j] == word[i]:
                if (j+n)<=26:
                    new_word += alphabet[j + n]
                else:
                    new_word += alphabet[(n - (26 - j))]
                    # new_word.append(alphabet[j + n])

    print(str(new_word) + "<--------------------------------")


#Rotate the word or change the word?
#What do I do with the space or special characters?
alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


word=str(input('Give a word to rotate'))
n = int(input("Give number for rotation? "))
process(word, n)
#
#
# def shift_n_letters(letter, n):
#     return chr(ord('a') + (ord(letter) - ord('a') + n) % 26)
#
# def rotate(s, n):
#     # Your code here
#     ans = ''
#     for i in range(len(s)):
#         if s[i] != ' ': ans += shift_n_letters(s[i], n)
#         else: ans += ' '
#     return ans


#SOS:link for ascii: http://www.asciitable.com/




