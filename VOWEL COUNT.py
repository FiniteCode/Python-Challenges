print ("Vowel Counter")
word = 0
vowel_count = 0
while 2 > 0:
    vowel_count = 0
    word = input("Input Word: ")
    vowel_count = vowel_count+word.count("a")
    vowel_count = vowel_count+word.count("e")
    vowel_count = vowel_count+word.count("i")
    vowel_count = vowel_count+word.count("o")
    vowel_count = vowel_count+word.count("u")
    vowel_count = vowel_count+word.count("A")
    vowel_count = vowel_count+word.count("E")
    vowel_count = vowel_count+word.count("I")
    vowel_count = vowel_count+word.count("O")
    vowel_count = vowel_count+word.count("U")
    print ("Number Of Vowels: "+str(vowel_count))
    
