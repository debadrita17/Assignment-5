#Assignment5
#task2
#Write a Python program to creates a list of numbers from 1 to 10.
# Extracts the first five elements from the list.
# Reverses these extracted elements.
# Prints both the extracted list and the reversed list

List = [1,2,3,4,5,6,7,8,9,10]
print('Original List: ',List)
l1 = List[:5]
l1.reverse()
print("The extracted five elements: ",l1)
print("The reversed extracted elements: ",l1)
