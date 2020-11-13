# In Class Project
# Jeff Milton
# CS1030-5
# 2020-10-20
# Contributors: Jeffrey Milton, Yonas Getnet, Troy Davidson, Justin Nahayo

# Create an empty list where you can store your information.
myList = []

# Create a counter for each list item starting at zero.
numList = 0

# Create a total starting at zero
total = 0

# Create a new median value starting at zero
median = 0

# Create file to write to
answerFile = open("P5Answers.txt", "w+")

# Add header to output file
answerFile.write("# In Class Project\n# Jeff Milton\n# CS1030-5\n# 2020-10-20\n# Contributors: Jeffrey Milton, Yonas Getnet, Troy Davidson, Justin Nahayo\n\n\n")


# Read the stats.txt file
# Open the file in read mode 
text = open("stats.txt", "r") 

# Add each item to the list.
for q in text:
    myList.append(q)
# Add 1 to the counter
    numList = numList +1
# Add to the total
    total = int(total) + int(q)

# Test that items were put into list
print(myList)

# Count of numbers in the list
# numList = len(myList)
# Test that counter worked
print (numList)
# Write counter to file
answerFile.write("Total number of lines in file: " +str(numList) + "\n")

# Test that total worked
print (total)
# Write total to file:
answerFile.write("Total of all numbers in file: " +str(total) + "\n")

# Find average of all numbers
average = total / numList

# test that average worked
print (average)

# write average to file
answerFile.write("Average of all the numbers: " +str(average) + "\n")

# Median value is the middle point between the value of all the numbers. Divide total by 2.
median = total / 2
# Verify that the median was found.
print (median)

# Print the median to the file.
answerFile.write("Median value of all the numbers: " +str(median) + "\n")

# Close the file
answerFile.close()