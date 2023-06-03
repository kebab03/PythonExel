r = 0
mylist = [r]
while r <= 86:
    #print(r)
    
    r += 3
    # Assign the current number to the element at index r
    mylist[r-1] = r

# Print the list
print(mylist)
