def pairWithTarget(list1, target):
  l=len(list1)
  listAns=[]
  for i in range(0, l-1):
    for j in range(i+1, l):
      if list1[i] + list1[j] == target:
        listAns.append((list1[i], list1[j]))
  if not listAns :
    return "No pair found in the list."
  else:
    return listAns
                       
  

if __name__ == "__main__":
  
  list1= list(map(int, input("Enter the element in the list: ").split()))
  target= int(input("Enter the target value: "))
  ans= pairWithTarget(list1, target)

  print(ans)
  


      
      
      
      

   
