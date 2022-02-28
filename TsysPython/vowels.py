##vowels = ['a', 'e', 'i', 'o','u']
##word = input("Provide a word to search vowels: ")
##found = {}
##for letter in word:
##    if letter in vowels:
##        found.setdefault(letter, 0)
##        found[letter] += 1
##for k,v in sorted(found.items()):
##    print(k, 'was found', v)

##found = []
##for letter in word:
##    if letter in vowels:
##        if letter not in found:
##            found.append(letter)
##for vowel in found:
##    print(vowel)

vowels = set('aeiou')
word = input("Provide a word to search vowels: ")
phrase = vowels.intersection(set(word))
print(phrase, type(phrase))
