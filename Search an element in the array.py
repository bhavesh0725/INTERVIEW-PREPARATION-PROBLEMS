def search(list1, target):
  for i in range(len(list1)):
    if list1[i]==target:
      return f"The element is present at index {i}"

  else:
    return "The element is not present in the given list."


if __name__=="__main__":
  list1=list(map(int, input("Enter the element of the list: ").split()))
  target=int(input("Find the element you want to search: "))
  print(search(list1,target))
