import sys 
  
# Using sys.getrecursionlimit() method 
# to find the current recursion limit
limit = sys.getrecursionlimit()
  
# Print the current limit 
print('Before changing, limit of stack =', limit) 
  
# New limit
Newlimit = 500
  
# Using sys.setrecursionlimit() method 
sys.setrecursionlimit(Newlimit) 
  
# Using sys.getrecursionlimit() method 
# to find the current recursion limit
limit = sys.getrecursionlimit()
  
# Print the current limit 
print('After changing, limit of stack =', limit) 
