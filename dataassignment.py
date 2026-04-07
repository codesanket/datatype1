#1. Write a program to add two lists index-wise. Create a new list that contains the 0th index item from both the list, then the 1st index item, and so on till the last element. any leftover items will get added at the end of the new list.

#given list is
#list1 = ["M", "na", "i", "Ra"]
#list2 = ["y", "me", "s", "hul"]

#finallist = []

#add element index wise
#for a,b in zip(list1,list2):
 #   finallist.append(a+b)
#print(finallist)

#Write a program to add item 7000 after 6000 in the following Python List
#list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
#we find the len of list
#print(len(list1))
#add to item in list
#list1[2][2].append(7000)
#print(list1)
#Suppose you are given a list of candy and another list of same size representing no of items of respective candy.
#candy_list = ['Jelly Belly','Kit Kat','Double Bubble','Milky Way','Three Musketeers']
#no_of_items = [10,20,34,74,32]
#for candy,count in zip(candy_list,no_of_items):
 #   print(candy,count)
#.Running Sum on list Write a program to print a list after performing running sum on it.
#given list is
list1 = [1,2,3,4,5,6]
running_sum = []
total=0
for num in list1:
    running_sum.append(num)
    total+=num
print(running_sum)




