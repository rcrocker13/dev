# Squaring algorithm
x = 3
ans = 0

# Set the iteration variable outside of the loop
itersLeft = x

# Test to see when our iteration condition is met
while(itersLeft != 0):
    ans = ans + x
    # increment the counter to avoid infinite loop
    itersLeft = itersLeft - 1
    
# Print out the result of our program
print(str(x) + '*' + str(x) + '=' + str(ans))
