# What is time complexity 

# Time taken to run the code is called as time complexity (False definition);

# This definition is not correct bcz different persons on different systems can have different result time to execute a piece of software.

# Rate of increase in time with respect to input size is called time complexity.

# It is measured in Big O, Big Omega and Big Theta notation.

for i in range(1,6):
  print("G o shaka")

# Rules to find time complexity:
# 1. Ignore constant factors
# 2. Always consider the worst case
# 3. Consider only the highest order term
# 4. Ignore lower order terms


#! Worst case time complexity

age = int(input("Enter your age: "))
if age>=80:
  print("You are senior citizen")
elif age>=60 and age <80:
  print("You are just a senior")
elif age>=24 and age<60:
  print("Working")
elif age>=16 and age<24:
  print("teen")
else:
  print("You are a kid")

# Total time/worst case would be O(1) + O(1) + O(1) + O(1) + O(1) + O(1) = O(6)

# Avoid constant values

# TC ==> O( 8N^6 + 4N^3 + 2N^8 + 38 )
# Ignore constant values
# O( N^8 )


# Nested loops

# O(N^2)
for i in range(1,6):
  for j in range(1,6):
    print("*",end="")
  print()

print("A", "B", "C", sep="-")  # Output: A-B-C