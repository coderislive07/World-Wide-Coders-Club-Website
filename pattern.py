n=int(input("Enter the n"))
for i in range(1,n+1):
    for j in range(1,n+1):
        if(j==i):
            print("*",end="")
        else:
            print("0",end="")
    for j in range(n+2,2,-1):
          if j==n+2:
            print("*",end="")
          if j==i+2:
              print("*",end="")
          else:
              print("0",end="")

              
              
              
        
        
        

              
    print(" ")
     

  
