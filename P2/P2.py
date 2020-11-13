# Multiply all the numbers between 1 and 13
# Jeff Milton
# CS1030-5
# 2020-09-09

# Multiply all the numbers between 1 and 13
sum = 0
total = 1
for i in range (1,14):
    total = i * i
    sum = sum + total
    print (" {} x {} =".format(i, i), total)

# Print the final value to the screen
print ("\nFinal Value:", sum)

# Take that number and divide by 42
meaningoflife = 42
adams = sum / 42

#Print that number to the screen
print ("\nThe final value {} divided by the meaning of life {} =".format(sum, meaningoflife), adams)