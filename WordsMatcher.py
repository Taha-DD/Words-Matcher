from collections import Counter

def max_repeated_character(str1, str2):
    
    common_chars = set(str1) & set(str2)

    count_str1 = Counter(str1)
    count_str2 = Counter(str2)

    max_repeated_char = max((char for char in common_chars if count_str1[char] == count_str2[char]), default=None)
    max_repeated_count = count_str1[max_repeated_char] if max_repeated_char is not None else 0

    if max_repeated_count > 1:
        return max_repeated_char, max_repeated_count
    return None, None

def finder(word, string_array):
    correct_match = ["N/A"]
    char = None
    repetition = 0
    
    for match in string_array:
        char_temp, rep_temp = max_repeated_character(word, match)
        if char_temp is not None and rep_temp > repetition:
            char = char_temp
            repetition = rep_temp
            correct_match.append(match)
        
    return correct_match
    
def pairs(string_array_1, string_array_2):
    pairs_arr = []
    
    for word in string_array_1:
        match = finder(word, string_array_2)
        for index in range(len(match) - 1, -1, -1):
            anti_match = finder(match[index], string_array_1)
            if match[index] not in pairs_arr and anti_match[len(anti_match)-1] == word:
                pairs_arr.append(word)
                pairs_arr.append(match[index])
                break
    return pairs_arr
    
    
str1 = ["goalkeeper", "moonlight" , "oppenheimer", "marie", "auguste", "emile",
        "ehrenfest", "edouard", "theophile", "schrodinger", "jules_emile",
        "pauli", "werner", "brillouin" , "debye", "knudsen", "Bragg",
        "kramers", "compton" , "successful", "Mississippi" , "committee" ,
        "parallel", "occurrence", "bookkeeping"]
str2 = ["keeper", "sugarboo", "light" , "einstein", "curie", "piccard", "henriot", "paul",
        "herzen", "dedonder", "erwin", "verschaffelt", "wolfgang", "heisenberg", "howard",
        "fowler", "peter", "Lawrence", "dirac", "assassination", "irrational", "millennium"
        "bookkeeper", "banana", "recurring", "accommodation", "possession", "necessity"]
paiarr = pairs(str1, str2)
print(paiarr)
