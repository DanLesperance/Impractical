"""find all word pair palingrams"""
import load_dict

word_list = load_dict.lc_strings('2of4brif.txt')
def find_palingrams():
    """find dictionary palingrams"""
    pali_list=[]
    words = set(word_list)
    for word in words:
        end = len(word)
        rev_word = word[::-1]
        if end > 1:
            for i in range(end):
                if word[i:] == rev_word[:end-i] and rev_word[end-i:] in words:
                    pali_list.append((word, rev_word[end-i:]))
                if word[:i] == rev_word[end-i:] and rev_word[:end-i] in words:
                    pali_list.append((rev_word[:end-i], word))
    return pali_list
print(*find_palingrams(),sep='\n')