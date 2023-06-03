r = 0
mylist = [3]*4
while r <= 4:
    print(r)
    
    
    # Assign the current number to the element at index r
    mylist[0] = r
    mylist[1] = 5
    mylist[r-1] = 6*r
    r += 1

# Print the list
print(mylist)
