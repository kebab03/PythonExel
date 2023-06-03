r = 1
mylist = [3]*4
print(f"mylist",mylist)
print(f"len(mylist)",len(mylist))


for u in range(4):
    print(f"r-1",u)
    mylist[u] = 6*u
    

# Print the list
print(mylist)
