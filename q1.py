def count(string):
    vowels = "aeiouAEIOU"
    vowel_count = 0
    cons_count = 0
    for character in string:
        #to check if the character is alphabet or not
        if character.isalpha():
            #to check if it the character is vowel or not
            if character in vowels:
                vowel_count += 1
            else:
                cons_count += 1 
    return vowel_count, cons_count
#main
userString = input("Enter a string: ")
v_count, c_count = count(userString)
print("Number of vowels:", v_count)
print("Number of consonants:", c_count)
