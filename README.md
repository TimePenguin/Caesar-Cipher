# Caesar-Cipher
I encrypt text using a Caesar Cipher, as well as brute force decryption, using vowel recognition to predict and show the most likely decryptions

I created a Caesar Cipher, which encrypts text. It does this by shifting letters in the sentence to different letters. This is a fairly easy cipher it take an integer, and shifts
the letters by that number to the right. 

The interesting part is the brute force decryption. Because there are many possible decryptions (26 to be exact), we have to figure out which decryptions are the most likely to
be the actual initial sentence. We can figure out the more likely ones by seeing which possible sentences all how vowels in the words. This is more effective the bigger
the text we are trying to decrypt. Note that we can also use letter frequency to figure out which sentences are more likely, however vowel recognition is more accurate.

I highly reccomend you to implement a version that uses both letter frequency and vowel recognition, that would be highly effective when the text we are trying to decrypt
is short.
