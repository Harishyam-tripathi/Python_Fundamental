#Creating a list in Python

my_list = [1,2,3,4]
print (my_list)
print (type(my_list))

my_list2 =[1, "Hello", 3.14, [1,2,3], True]
print (my_list2)
print (type(my_list2))

#Accessing elements in a list - Indexing and Slicing
list1 = [10, 20, 30, 40, 50]
print (list1[0]) # Output: 10
print (list1[2]) # Output: 30
print (list1[-1]) # Output: 50
print (list1[1:4]) # Output: [20, 30, 40]
print (list1[::2]) # Output: [10, 30, 50]

#Slicing with step
my_list2 = [10, 20, 30, 40, 50,60,100]
print (my_list2[1:6:2]) # Output: [20, 40, 60]
print (my_list2[0:3]) # Output: [10, 20, 30]
print (my_list2[3:]) # Output: [40, 50, 60, 100]
print (my_list2[:4]) # Output: [10, 20, 30, 40]
print (my_list2[-3:]) # Output: [60, 100] 
print (my_list2[::-2]) # Output: [10, 20, 30, 40, 50]
print (my_list2[::2]) # Output: [10, 20, 30, 40, 50, 60, 100]
print (my_list2[1:6:3]) # Output: [20, 50]
print (my_list2[1:6:4]) # Output: [20, 60]  
print (my_list2[::-1]) # Output: [100, 60, 50, 40, 30, 20, 10]

# List Modifying 
#Lists are mutable, which means you can change their content without changing their identity. You can modify a list by assigning new values to its elements or by using various list methods.
#Changing an element in a list

Fruits = ['Apple', 'Banana', 'Cherry']
Fruits[1] = 'Blueberry'
print (Fruits) # Output: ['Apple', 'Blueberry', 'Cherry']

#Adding elements to a list
Fruits.append("Mango")
print(Fruits) 

#Removing elements from a list
   
def remove_fruit_from_list(fruits):
    # Ask the user for input inside the function
    remove_element = input("Enter the element you want to remove: ")
    
    # Check if the element exists in the list
    if remove_element in fruits:
        fruits.remove(remove_element)
        print(f"'{remove_element}' has been removed from the list.")
    else:
        print(f"'{remove_element}' is not in the list.")
    
    return fruits

# --- How to use it ---
my_fruits = ['Apple', 'Banana', 'Cherry']
updated_list = remove_fruit_from_list(my_fruits)
print("Updated list:", updated_list)

# Replacing elements in a list
my_fruits[0] = "Grapes"
print(my_fruits) # Output: ['Grapes', 'Banana', 'Cherry']

#list Methods

#1.Append
fruits = ['Apple', 'Banana', 'Cherry']
fruits.append('Mango')
print(fruits) # Output: ['Apple', 'Banana', 'Cherry', 'Mango'])


#3. Insert
fruits = ['Apple', 'Banana', 'Cherry']
fruits.insert(1, 'Mango')
print(fruits) # Output: ['Apple', 'Mango', 'Banana', 'Cherry']

#4. Remove
fruits = ['Apple', 'Banana', 'Cherry']
fruits.remove('Banana')
print(fruits) # Output: ['Apple', 'Cherry']

#5. Clear
fruits = ['Apple', 'Banana', 'Cherry'] 
fruits.clear()
print(fruits) # Output: []

#6 Finding index
fruits = ['Apple', 'Banana', 'Cherry']
index = fruits.index('Banana') 
print(index) # Output: 1

#7 Finding index - with a range
fruits = ['Apple', 'Banana', 'Cherry', 'Banana']
index = fruits.index('Banana', 2)  # Start searching from index 2
print(index) # Output: 3

#8. Count occurrences
fruits = ['Apple', 'Banana', 'Cherry', 'Banana']
count = fruits.count('Banana')
print(count) # Output: 2

#9 Reverse
fruits = ['Apple', 'Banana', 'Cherry']
fruits.reverse()
print(fruits) # Output: ['Cherry', 'Banana', 'Apple']

#10. Sort
fruits = ['Banana', 'Apple', 'Cherry']
fruits.sort()
print(fruits) # Output: ['Apple', 'Banana', 'Cherry']

#11. Copy
fruits = ['Apple', 'Banana', 'Cherry']
fruits_copy = fruits.copy()
print(fruits_copy) # Output: ['Apple', 'Banana', 'Cherry']

#12. Extend
fruits = ['Apple', 'Banana', 'Cherry']
more_fruits = ['Mango', 'Grapes']
fruits.extend(more_fruits)
print(fruits) # Output: ['Apple', 'Banana', 'Cherry', 'Mango', 'Grapes']

#13. Pop
fruits = ['Apple', 'Banana', 'Cherry']
popped_fruit = fruits.pop(0)
print(popped_fruit) # Output: 'Apple'
print(fruits) # Output: ['Banana', 'Cherry']

# jion List
list1 = [1,2,3]
list2 = ['a', 'b', 'c']
 
# using + operator
final_list = (list1 + list2)
print(final_list)

# using Append method
for x in list2:
    list1.append(x)
print(list1)

#using Extend method
list1.extend(list2)
print(list1)

X = "python"
print(X[::-1])
print(X[2:3])