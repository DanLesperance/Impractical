# Load digital dictionary file as a list of words
# accept a word from the user
# create an empty list to hold anagrams
# sort the user-word
# Loop through each word in the word list:
    # Sort the word
    # if word sorted is equal to user-word sorted:
    # append to anagrams list
# print anagrams list

import load_dict

word_list = load_dict.lc_strings('2of4brif.txt')

anagram_list = []

# input a SINGLE word or SINGLE name below to find anagram
name = input()
print("Input name = {}".format(name))
name = name.lower()
print("Using name = {}".format(name))

# sort name & find anagrams
name_sorted = sorted(name)
for word in word_list:
    word=word.lower()
    if word != name:
        if sorted(word) == name_sorted:
            anagram_list.append(word)

# print out list of anagrams
print()
if len(anagram_list) == 0:
    print("You need a larger dictionary or a new name!")
else:
    print("Anagrams =",*anagram_list, sep='\n')