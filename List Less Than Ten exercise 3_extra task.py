#  write a program that prints out all the elements of the list that are less than 5.
# Ask the user for a number and return a list that contains only elements from the original list a that are smaller
#  than that number given by the user.
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
x = int(input("Enter yout number "))
a2 = []

for list in a:
      if list < x:
          a2.append(list)

print(a2)
