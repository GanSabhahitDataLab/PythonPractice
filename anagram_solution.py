# Method to identify whether 2 strings are anagrams without considering the
# case of the letter and spaces in the string

def is_anagram(s1 ,s2):
 s1 = s1.replace(" ","").lower()
 s2 = s2.replace(" ", "").lower()
 s1_char_count = {}
 s2_char_count = {}
 for ch in s1:
 if ch in s1_char_count:
 s1_char_count[ch] = s1_char_count[ch] + 1
 else:
 s1_char_count[ch] = 1
 for ch in s2:
 if ch in s2_char_count:
 s2_char_count[ch] = s2_char_count[ch] + 1
 else:
 s2_char_count[ch] = 1

 for k in s1_char_count :
 if k in s2_char_count and s1_char_count[k] == s2_char_count[k] :
 continue
 else:
 return False
 return True

