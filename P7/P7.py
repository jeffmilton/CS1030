# In Class Project
# Jeff Milton
# CS1030-5
# 2020-10-20
# Contributors: Jeffrey Milton, Yonas Getnet, Kyle, Garduino

# Create a new dictionary
d = dict()

# Create file to write to
answerFile = open("P7.out", "w+")

# Add header to output file
answerFile.write("# In Class Project\n# Jeff Milton\n# CS1030-5\n# 2020-11-05\n# Contributors: Jeffrey Milton, Yonas Getnet, Kyle, Garduino\n\n\n")

# Read the amend.txt file
# Open the file in read mode 
text = open("amend.txt", "r") 

# Check if item is in the dictionary.
for q in text:
    if d.__contains__(q):
        # increment key def +1
        d[q] = int(d.get(q)) +1
    # add q to dict
    else:
        d[q] = 1
        
for q in d:
    answerFile.write("key: "+q+" Value: "+str(d[q])+"\n")

# Close the file
answerFile.close()