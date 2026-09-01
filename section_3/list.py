numbers = [10, 5, 7, 2, 1]
print("Original list contents:", numbers)  # Printing original list contents.

print(numbers[0]) # Accessing the list's first element.
numbers[0] = 111
print("\nPrevious list contents:", numbers)  # Printing previous list contents.

numbers[1] = numbers[4]  # Copying value of the fifth element to the second.
print("New list contents:", numbers)  # Printing current list contents.

print("\nList initial length:", len(numbers))  # Printing the list's length.

#removing the last element from the list.
del numbers[1] 
print(f"List length after removing an element: {len(numbers)}")  # Printing the list's length after removing an element.
print(numbers)

#accessing the using negative index.
print(numbers)
# Accessing the last element using negative index.
print("\nAccessing the last element using negative index:", numbers[-1]) 
print(f"Accessing the second-to-last element using negative index: {numbers[-2]}")

