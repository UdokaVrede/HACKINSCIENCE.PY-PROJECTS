def diagonals(arr):     #function initialization

  n=len(arr)            #assign the length of the arr to 'n'
  
  sum_a=0
  sum_b=0               #initizaling 'sum_a' and 'sum_b' to 0
  
  for x in range(n):    
  
    sum_a+=int(arr[x][x])       #getting the value for arr element in x and adding it to sum
    sum_b+=int(arr[x][n-x-1])   #get the value of array element in position 'x' of the length of array minus the position of x minus one
    
  return abs(sum_a - sum_b)     #return the absolute value of the difference between sum_a - sum_b
    
