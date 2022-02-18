# TODO Load a dict file
# TODO accept a name from user
# Todo set limit = length of name
# TODO Start empty list to hold anagram phrase
# TODO While length of phrase < limi:
# TODO Generate list of dict words that fit in name
# TODO Present words to user
# TODO present remaining letters to user
# TODO present current phrase to user
# TODO ask user to input word or start over
# TODO If user input can be made from remaining letters;
# TODO Accept choice of new word or words from user
# TODO Remove letters in choice from letters in name
# TODO Return Choice and remaining letters in name
# TODO If choice is not a valid selection:
# TODO Ask user for new choice or let user start over
# TODO Add choice to phrase and show user
# TODO Generate new list of words and repeat the process
# TODO When phrase length equals limit value:
# TODO Display final phrase
# TODO Ask user to start over or to exit


import sys
from collections import Counter
import load_dict

# load file, and include 'a' and 'i' as words
dict_file = load_dict.lc_strings("2of4brif.txt")
dict_file.append("a")
dict_file.append("i")
dict_file = sorted(dict_file)

inp_name = input("Enter a name: ")


def find_anagrams(name, word_list):
    """Read the name and dictionary file then display all anagrams IN name"""
    name_letter_map = Counter(name)
    anagrams = []
    for word in word_list:
        test = ""
        word_letter_map = Counter(word.lower())
        for letter in word:
            if word_letter_map[letter] <= name_letter_map[letter]:
                test += letter
        if Counter(test) == word_letter_map:
            anagrams.append(word)
    print(*anagrams, sep="\n")
    print()
    print("Remaining letters = {}".format(name))
    print("Remaining number of letters = {}".format(len(name)))
    print("Number of remaining anagrams = {}".format(len(anagrams)))


def process_choice(name):
    """Check user choice for validity, return choice and leftover letters"""
    while True:
        choice = input(
            "\nMake a choice; otherwise press Enter to start over or # to end: "
        )
        if choice == "":
            main()
        elif choice == "#":
            sys.exit()
        else:
            candidate = "".join(choice.lower().split())
        left_over_list = list(name)
        for letter in candidate:
            if letter in left_over_list:
                left_over_list.remove(letter)
        if len(name) - len(left_over_list) == len(candidate):
            break
        else:
            print("Won't work!  Please make another choice", file=sys.stderr)
    name = "".join(left_over_list)
    return choice, name


def main():
    """Help user build anagram phrase from their name"""
    name = "".join(inp_name.lower().split())
    name = name.replace("-", "")
    limit = len(name)
    phrase = ""
    running = True

    while running:
        temp_phrase = phrase.replace(" ", "")
        if len(temp_phrase) < limit:
            print("Length of anagram phrase = {}".format(len(temp_phrase)))

            find_anagrams(name, dict_file)
            print("Current anagram phrase =", end=" ")
            print(phrase, file=sys.stderr)

            choice, name = process_choice(name)
            phrase += choice + " "
        elif len(temp_phrase) == limit:
            print("\n******FINISHED******\n")
            print("Anagram of name=", end=" ")
            print(phrase, file=sys.stderr)
            print()
            try_again = input('\n\nTry again? (Press Enter else "n" to quit)\n ')
            if try_again.lower() == "n":
                running = False
                sys.exit()
            else:
                main()


if __name__ == "__main__":
    main()
