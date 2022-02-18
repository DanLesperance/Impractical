# Pseudocode
# TODO Load digital dictionary as list of words
# TODO create an empty list to hold palindromes
# TODO Loop through each word in the word list:
    # TODO  if word sliced forward is the same as word sliced backward:
        # TODO Append word to palindrome list
# TODO print palindrome list

import load_dict

word_list = load_dict.lc_strings('2of4brif.txt')
pali_list = []

for word in word_list:
    if len(word) > 1 and word == word[::-1]:
        pali_list.append(word)

print("\nNumber of palindromes found = {}\n".format(len(pali_list)))
print(*pali_list, sep='\n')
