from nltk.corpus import words
from itertools import permutations

alphs = "a b c d e f g h i j k l m n o p q r s t u v w x y z".split(' ')

# given = input()
# while given != '!':
#   given = input()
#  word_list = [word for word in word_list if given not in word_list]
# print(word_list)
#
# first = ([word for word in words.words('en') if len(word) == 5])
# second = first
#
# for i in range(21):
#     given = input()
#     word_list = [word for word in first if given not in word]
#     print(word_list)
#     print(len(word_list))
#     first = word_list

first = ([word for word in words.words('en') if len(word) == 5])


def exclude(exc, wl):
    wl = [word for word in wl if exc not in word]
    return wl


def include(inc, wl):
    a = inc[0]
    b = int(inc[1]) - 1
    wl = [word for word in wl if a != word[b] and a in word]
    return wl


def abs_include(ab, wl):
    a = ab[0]
    b = int(ab[1]) - 1
    wl = [word for word in wl if a == word[b]]
    return wl


# print(exclude('c', first))
# print(include('m', first))
# print(abs_include('n4', first))
print(len(first))
given = input()

while given != '!':
    if given == '1':
        letter = input()
        first = exclude(letter,first)
        print(first)
    elif given == '2':
        letter = input()
        first = include(letter, first)
        print(first)
    elif given == '3':
        letter = input()
        first = abs_include(letter, first)
        print(first)
    print(len(first))
    given = input()

