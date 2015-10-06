"""
The nth term of the sequence of triangle numbers is given by,
tn = ½n(n+1); so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding
to its alphabetical position and adding these values we form a word value.
For example, the word value for SKY is 19 + 11 + 25 = 55 = t10.
If the word value is a triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file
containing nearly two-thousand common English words, how many are triangle words?
"""
import time
t1 = time.clock()

FILENAME = "words.txt"
letter_dict = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7,\
               "H": 8, "I": 9, "J": 10, "K": 11, "L": 12, "M": 13, "N": 14,\
               "O": 15, "P": 16, "Q": 17, "R": 18, "S": 19, "T": 20, "U": 21,\
               "V": 22, "W": 23, "X": 24, "Y": 25, "Z": 26, "\"": 0}
triangles = []

def build_triangle_nums(n):
    for i in range(1, n + 1):
        triangles.append(int(0.5 * i * (i +1)))
    
def read_words(file):
    """ (file) -> string"""   
    words_file = open(file, 'r')
    content = words_file.read()
    word_list = content.split(',')             
    words_file.close()    
    return word_list

def word_value(s):
    value = 0
    for i in s:
        value += letter_dict[i]
    return value

# ========== main ===============
build_triangle_nums(20)

word_list = read_words(FILENAME)
total_score = 0
for word in word_list:
    if (word_value(word)) in triangles: total_score += 1
print(total_score)
print(time.clock()-t1, "seconds")
