from random import shuffle

def jumble(word):
    anagram = list(word)
    print(anagram)
    shuffle(anagram)
    return "-".join(anagram)

words = ['beetroot','carrots','potatoes']
anagrams = [] 

# for word in words:
#     anagrams.append(jumble(word)) 
# print(anagrams)

print(map(jumble,words))
print(list(map(jumble,words))) 



