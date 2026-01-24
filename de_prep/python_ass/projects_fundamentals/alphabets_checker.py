charin = input("Enter the character: ")

if len(charin) != 1:
    print("please enter one character only!") #we need only 1 char
elif charin in "aeiouAEIOU": 
   print("its a vowel") # only if vowels
elif ('A' <= charin <= 'Z') or ('a' <= charin <= 'z'): # alphabets not in vowels included but it wont reach if input is vowel
    print("its a consonant") 
else:
    print("enter valid char") # single character input not alphabet