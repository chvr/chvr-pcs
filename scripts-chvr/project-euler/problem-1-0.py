# Multiples of 3 and 5 by chvr (https://repl.it/BJ9p)
# Problem 1
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we 
# get 3, 5, 6 and 9. The sum of these multiples is 23.

# Find the sum of all the multiples of 3 or 5 below 1000.

# The sum of the numbers start to end assuming that i is a multiple of 3 or 5
x = 0
for i in range(1000):
#for i in range(10): Testing the sample input...
    if (i % 3 == 0 or i % 5 == 0): # Add x if i is a multiple of either 3 or 5
        x += i
        
print(x) # Print the result
