test_str = "GeeksforGeeks is best for Geeks"

# initializing substring 
test_sub = "Geeks"

# printing original string 
print("The original string is : " + test_str) 

# printing substring 
print("The substring to find : " + test_sub) 

# using list comprehension + startswith() 
# All occurrences of substring in string 
res = [i for i in range(len(test_str)) if test_str.startswith(test_sub, i)] 

# printing result 
print("The start indices of the substrings are : " + str(res)) 
