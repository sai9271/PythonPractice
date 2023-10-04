a=input()
print(a)

#write a program that reads a word and prints the word and "###" on two lines.
# Note:The characters used in "###" are three hash symbols.
# Input: The input will be a single line containing a string.
# Output: The first line of output should be a string containing the given word.
# The second line of output should be a string contating "###"
# Explination:
# For example if the given word is Algebra the output should be 
# Algera
# ###
# sample input1 :Algebra
# sampleoutput1: Algebra
#                ### 
# sample input2: 1a2b3c
# sample output2:1a2b3c
#                  ###


-------------------------------
3.Write a program that reads the  two words and prints the words on two lines
#input The first line of input contains a string
#the second  line of input contains a string
#Output The first line  of output should  be a string containing the first word.
# The second line of output should be a string containing the second word.
#For example if the given words are apple and banana, the output should be
# Apple
# Banana

# sample Input 1
# Apple 
# Banana

# sample output 1
#Apple 
#Banana

# sample input 2
# Hi
# Hello

# sample output 2
# Hi
# Hello

# Solution:
print(input())
print(input())

# 4. For this problem you need to write to read two lines of input and print the second line of input 
#output: print  the second line of input
# sample input: Fundamentals 
                #python
# sample output: python
# sample input :tom
#              jerry
#sample output:jerry

# solution
war=input()
war2=input()
print(war2)

# write a program that reads two lines of input and prints those  two lines in the reverse order.(print the message given in the second line of input before the firt line of input)
#Explination:In the given example, the first line of input is " Book " and the second line of input is "pen", so the output should be
# pen
# book

# sample input1
# book
# pen
# sample output1
#pen 
# book
#sample input 2
#4
#5
#sample output 2
#5
#4

# solution
obj=input()
obj1=input()
print(obj1)
print(obj)

# 5.write a program that takes a word W as input and prints "Hello" followed by the given word W.
# NOTE : There should be a space after Hello
# sample input: world
# sample output: Hello world
# sample input2: Anjali
# sample output2:Hello Anjali

# solution
sample =input()
sam="Hello"
print(sam + " "+ sample)


#For this problem you need to write code to read a single line  of input  and print the line after the message "Given input:"
#sample input : Happy coding
#sample output: Given input: Happy coding
#sample input : Tech Foundations
#sample output: Given input : Tech Foundations

# solution

sam = input()
print("Given input: "+sam)

# write a program that reads two words and prints the resultant word by joining  the  two words.
#input: The  first line  of input contains  a string
#       The second  line  of input contains a string

#output: the output should be a single line containing a string obtained by joining the two words
#explination: for example if  the given words are milk and shake. the output should be milkshake.
#sample input:milk
#              shake
#sample output:milkshake
#sample input: cater
#               pillar
#sample output: caterpillar

#solution:
a=input()
b=input()
print(a+b)

# A job applicant is filling out an application form.He entered his first name and last name. Your task is to print his full name by joining his first name and last name with a space
# input: The first line of input contains a string(first name).
#        The second line of input contains a string(last name).
#output:The output should be as single line containing a string obtained by joining the first name and the last name with a space
# explination:for example if the given first name is harry and the given last name is potter the output should be harry potter as the first name and last name are joined with a space
# sample input: harry
#                potter
#sample output:harry potter
#sample input1: hugo 
#               clive
#sample output: hugo clive

# solution

a=input()
b=input()
print(a+" "+b)