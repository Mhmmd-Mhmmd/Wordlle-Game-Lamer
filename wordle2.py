from nltk.corpus import words

while 1:
    given = input().split(' ')
    wds = [word for word in words.words('en') if len(word) == 5]
    for letter in given:
        wds = [word for word in wds if letter in word]
        print(wds)
        print(len(wds))
