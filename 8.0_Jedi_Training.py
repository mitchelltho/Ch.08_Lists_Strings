# 8.0 Jedi Training (20pts)  Name:________________

'''
1.)  AVERAGE LIST:  (3pts)
Write a single program that takes any of the three lists, and prints the average. 
Use the len function. There is a sum function I haven't told you about. 
Don't use that. Sum the numbers individually as shown in the chapter. 
Also, a common mistake is to calculate the average each time through the loop 
to add the numbers. Finish adding the numbers before you divide.
'''
'''
a_list = [3,12,3,5,3,4,6,8,5,3,5,6,3,2,4]
b_list = [4,15,2,7,8,3,1,10,9]
c_list = [5,10,13,12,5,9,2,6,1,8,8,9,11,13,14,8,2,2,6,3,9,8,10]


total = 0
chosen-list = input("Which list? ").upper()
if chosen-list == "A":
    chosen-list = a_list
elif chosen-list == "B":
    chosen-list = b_list
elif chosen-list == "C":
    chosen-list = c_list
for i in chosen-list:

    total += i

print(total / len(chosen-list))
'''
'''
2.) USERNAME:  (3pts)
Write a program that will strip the username (whatever is in front of the @ symbol)
from any e-mail address and print it. First ask the user for their e-mail address.
'''
'''
email = input("What is your email? ")
for char in email:
    if char == "@":
        break
    print(char)
'''
'''
TEXT FORMATTING:  (4pts)
3.) Make following program output the following:
     
     Score:          41,237
     High score:  1,023,407
     
     Do not use any plus sign (+) in your code.
     You should only have two double quotes in each print statement.
     '''
'''
score = 41237
highscore = 1023407
print("Score:      " + str(f"{score:,}"))
print("High score: " + str(f"{highscore:,}"))
'''

'''
4.) MONTHS PROGRAM   (5pts)
Write a user-input statement where a user enters a month number 1-12.
From the user input number, slice the string below in your program to print the three month abbreviation.
Keep repeating this until the user enters a non 1-12 number to quit.
Once the user quits, print "Goodbye!"
'''
'''
months = "JanFebMarAprMayJunJulAugSepOctNovDec"

monthnum = int(input("Month Number? "))
month = monthnum * 3
monthlast = month + 3

print(months[month - 3:monthlast - 3])
'''
'''
5.) DECRYPTION PROGRAM   (5pts)
An ENCRYPTION program was used to generate the following secret code. The encryption program converted each character 
of the string into its ASCII decimal number, applied a +/-20 algorithm to it and then converted it back to
characters. Your task is to write a DECRYPTION program to decipher the following secret code. Don't waste time changing 
your program 40 times. Use a FOR loop from -20 to +20 to generate all the possibilities in one run of your program.

Extra Challenge: Instead of printing out 41 lines of text to look at, can you determine a way to just print out the decrypted line only
along with the shift number?
'''
Secret_Message="Lxwp{j}~uj}rxw|*)bx~)l{jltnm)}qn)lxmn7)]qn)ox{ln)r|)\][XWP)r}q)x~*"


'''
for i in range(41):
    encrypted_text = ""
    for c in Secret_Message:
        x = ord(c)
        x = x + i -20
        c2 = chr(x)
        encrypted_text = encrypted_text + c2
    print(encrypted_text)
'''