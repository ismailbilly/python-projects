 #This is a program that generates acronym
    
phrase = input('Enter a phrase: ')
split_phrase = phrase.split()

for i in split_phrase:
 #This line prints the acronym on a straight line rather than the default vertical printing. Its called DYNAMIC PRINTING
    print(i[0].upper(), end ='')