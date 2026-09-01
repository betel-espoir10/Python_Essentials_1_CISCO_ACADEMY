hat_list = [1, 2, 3, 4, 5]  # This is an existing list of numbers hidden in the hat.

# Step 1: write a line of code that prompts the user
    
# to replace the middle number with an integer number entered by the user.
hat_list[2] = int(input("Enter an integer to replace the middle number: "))

# Step 2: write a line of code that removes the last element from the list.
del hat_list[-1]
print("List after removing the last element:", hat_list)
# Step 3: write a line of code that prints the length of the existing list.
print(f"Length of the existing list: {len(hat_list)}")

print(hat_list)

#adding a new element to the list.
hat_list.append(int(input("Enter an integer to add to the list: ")))
print("List after adding a new element:", hat_list)

#adding a new element to specific index in the list.
hat_list.insert(3, int(input("Enter an integer to add to the list at index 3: ")))
print("List after adding a new element at index 3:", hat_list)

#creating an empty list.
my_list = []
for i in range(10):
    my_list.append(i)  # Adding numbers from 1 to 10 to the list.
print("List after adding 10 elements:", my_list)

#creating a second empty list.
second_list = []
for i in range(10):
    second_list.insert(0, i)
print("Second list after adding 10 elements:", second_list)