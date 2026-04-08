#1. Write a program to add two lists index-wise. Create a new list that contains the 0th index item from both the list, then the 1st index item, and so on till the last element. any leftover items will get added at the end of the new list.
#given list is
list1 = ["M", "na", "i", "Ra"]
list2 = ["y", "me", "s", "hul"]

finallist = []

#add element index wise
for a,b in zip(list1,list2):
    finallist.append(a+b)
print(finallist)

#Write a program to add item 7000 after 6000 in the following Python List
list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
#we find the len of list
print(len(list1))
#add to item in list
list1[2][2].append(7000)
print(list1)
#Suppose you are given a list of candy and another list of same size representing no of items of respective candy.
candy_list = ['Jelly Belly','Kit Kat','Double Bubble','Milky Way','Three Musketeers']
no_of_items = [10,20,34,74,32]
for candy,count in zip(candy_list,no_of_items):
    print(candy,count)

#.Running Sum on list Write a program to print a list after performing running sum on it.
#given list is
list1 = [1,2,3,4,5,6]
running_sum = []
total=0
for num in list1:
    running_sum.append(num)
total+=num
print(running_sum)
#5.You are given a list of integers. You are asked to make a list by running through elements of the list by adding all elements greater and itself.

#6.Find list of common unique items from two list. and show in increasing order
#given list is:
num1 = [23,45,67,78,89,34]
num2 = [34,89,55,56,39,67]

def comm_sorted(num1,num2):
    comm_list=set(num1) & set(num2)
    return comm_list
print(comm_sorted(num1,num2))

#7.Sort a list of alphanumeric strings based on product value of numeric character in it. If in any string there is no numeric character take it's product value as 1.
#Input:
l = ['1ac21', '23fg', '456', '098d', '1', 'kls']
l.sort(key=lambda x: eval('*'.join([c for c in x if c.isdigit()]) or '1'))
print(l)
#8.Write a program that can find the max number of each row of a matrix
#given input is
matrix=[
    [1,2,3],
    [4,5,6],
    [7,8,9]]
for i in matrix:
    max=i[0]
    for j in i:
        if j>max:
            max=j
    print(max)

#9.. Shortlist Students for a Job role Ask user to input students record and store in tuples for each record. Then Ask user to input three things he wants in the candidate- Primary Skill, Higher Education, Year of Graduation.
#Show every students record in form of tuples if matches all required criteria.
#It is assumed that there will be only one primry skill.
#If no such candidate found, print No such candidate
student=[]
s=int(input('enter number of students:'))
y=int(input('enter year:'))
for i in range(s):
    print('enter details for student:{i+1} ')
    name=input('enter name:')
    skills=input('enter basics:')
    education=input('enter education:')
    year=int(input('enter year:'))
    student.append(name)
    student.append(skills)
    student.append(education)
    student.append(year)
print('enter required details:')
r_skills=input('enter req skills:')
r_education=input('enter req education:')
r_year=input('enter req year:')
found=False
print("\nMatching Candidates:")
for s in student:
    if s[1] == r_skills and s[2] == r_education and s[3] == r_year:
        print(s)
        found = True
if not found:
    print("No such candidate")

#10.Write a program to find set of common elements in three lists using sets.
ar1 = [1, 5, 10, 20, 40, 80]
ar2 = [6, 7, 20, 80, 100]
ar3 = [3, 4, 15, 20, 30, 70, 80, 120]
comm_elemet=set(ar1) & set(ar2) & set(ar3)
print(comm_elemet)
comm_elemet=sorted(comm_elemet)
print('common elemet is:',comm_elemet)

#11.Write a program to count unique number of vowels using sets in a given string.Lowercase and upercase vowels will be taken as different.
Str1="hands-on data science mentorship progrAm with live classes at affordable fee only on CampusX"
v=set(Str1)
print(v)
diff_v=set(ch for ch in v if ch in v )
count=len(diff_v)
print('different volves',diff_v)
print('numbers of volves ',count)

#12.Intersection of two lists. Intersection of two list means we need to take all those elements which are common to both of the initial lists and store them into another list. Only use using list-comprehension.
#given list is
lst1 = {15, 9, 10, 56, 23, 78, 5, 4, 9}
lst2 = {9, 4, 5, 36, 47, 26, 10, 45, 87}
simple_intern=[item for item in lst1 if item in lst2]
print(simple_intern)
list1 = {4, 9, 1, 17, 11, 26, 28, 54, 69}
list2 = {9, 9, 74, 21, 45, 11, 63, 28, 26}
simple_demo=[item for item in list1 if item in list2]
print(simple_demo)
#Convert a list of Tuples into Dictionary.
tlist=[("akash", 10), ("gaurav", 12), ("anand", 14), ("suraj", 20), ("akhil", 25), ("ashish", 30)]
dict_form_tlist=dict(tlist)
print(dict_form_tlist)
#given input
glist=[('A', 1), ('B', 2), ('C', 3)]
dict_form_glist=dict(glist)
print(dict_form_glist)

#Write a Python function that takes a list and returns a new list with unique elements of the first list.
def uni_list():
    list1 =[]
    list_new=[]
    n=int(input("enter the number:"))
    for i in range(n):
        element=int(input("enter the element:"))
        list1.append(element)
    for j in list1:
       if j  not in list_new:
            list_new.append(j)
    else:
          pass
    return (list_new)
list=uni_list()
list.sort(reverse=True)
print('final sorted list:',list)

#Write a Python program to print the even numbers from a given list.
list=[1,2,3,4,5,6,7,8,9]
even_list=[]
for num in list:
    if num%2==0:
        even_list.append(num)
print('even numbers are',even_list)

#Write a Python function to check whether a number is perfect or not.
add=0
num=int(input("Enter a number: "))

for i in range(1,num):
    if i%2==0:
        add=add+i
if num==add:
         print('number is perfect',num)
else:
    print('number is not perfect',num)

#Write a Python function to concatenate any no of dictionaries to create a new one.
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
dic4={}
for d in (dic1, dic2, dic3):
    dic4.update(d)
print(dic4)

