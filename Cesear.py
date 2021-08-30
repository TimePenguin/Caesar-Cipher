def encrypt(key = None, data = open("Cesear.in", "r").readlines()[1:]):
    if key == None:
        key = int(open("Cesear.in", "r").readlines()[0])
    completed_message = ""
    for start_sentence in data:
        end_sentence = ""
        for letter in start_sentence:
            whether_cap = letter.isupper()
            letter = letter.lower()
            if ord(letter) > 96 and ord(letter) < 123:
                new_ord = (ord(letter) + key)
                new_ord = (new_ord -97) % 26
                new_ord += 97
                new_letter = chr(new_ord)
                if whether_cap == True:
                    new_letter = new_letter.upper()
            else:
                new_letter = letter
            end_sentence += new_letter
        completed_message = completed_message + end_sentence
    if open("Cesear.in", "r").readlines()[0][0].isdigit():
        open("Cesear.out", "w").write(completed_message)
    return(completed_message)
def Decode():
    encrypt(key = int(open("Cesear.in", "r").readlines()[0]) * -1)
def Brute_Force():
    to_write = open("Cesear.out", "a")
    possible_messages = [encrypt(i, open("Cesear.in", "r").readlines()) for i in range(0, 26)]
    possible_messages = [sentence.split() for sentence in possible_messages]
    possible_sentences_vowels = []
    counter = -1
    for sentence in possible_messages:
        counter += 1
        number_of_vowels = 0
        for word in sentence:
            if "a"  in word or "e" in word or "i" in word or "o" in word or "u" in word or "y" in word or "A" in word or "E" in word or "I" in word or "O" in word or "U" in word or "Y" in word:
                number_of_vowels += 1
        possible_sentences_vowels.append([number_of_vowels, counter, sentence])
    possible_sentences_vowels.sort(key = lambda x: x[0], reverse= True)
    for sentence in possible_sentences_vowels:
        compiled_sentence = ""
        for word in sentence[-1]:
            compiled_sentence += word + " "
        to_write.write(compiled_sentence + "\n")
what_to_do = open("What_to_do.in", "r").readline()
if what_to_do == "encrypt":
    encrypt()
if what_to_do == "decode":
    Decode()
if what_to_do == "brute force":
    Brute_Force()