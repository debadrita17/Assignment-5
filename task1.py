#Assignment5
#task1
#write a Python program to Creates a dictionary where student names are keys and their marks are values.
#Asks the user to input a student's name.
#Retrieves and displays the corresponding marks.
#If the student’s name is not found, display an appropriate message.

name = input("enter a student's name: ")
dictionary = {'Nil':'95','Dev':'85',"Piku":'75'}
if name in dictionary:
    print(name,"'s marks: ",dictionary[name])
else:
    print('student not found')








































