# Listing 5.26
# Demonstrates that a continue statement skip the rest of the body of a loop and
# and immediately checks the loop's condition
# Author: Rick Halterman
# Last modified: 

sum = 0
done = False
while not done:
    val = int(input("Enter positive integer (999 quits):"))
    if val < 0:
        print("Negative value", val, "ignored")
        continue    # Skip rest of body for this iteration
    if val != 999:
        print("Tallying", val)
        sum += val
    else:
        done = (val == 999)     # 999 entry exits loop
print("sum =", sum)