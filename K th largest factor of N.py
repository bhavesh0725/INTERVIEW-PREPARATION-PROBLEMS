def largestFactor(N,K):
  list1=[]
  for i in range(2,N):
    if N%i==0:
      list1.append(i)

  if not list1 :
    return 1
  elif list1:
    if K<len(list1):
      ans=list1[K-1]
      return ans
    else:
      return 1
      
    
    
  

if __name__=="__main__":
  n=int(input("Enter the value of N: "))
  k=int(input("Enter the value of K: "))
  print(largestFactor(n,k))
    
  
