list = [1,2,4,6,8,0,3,5,7,1,5,8,9,3]
def remove_duplicate(list):
  empty_list = []
  #set_= set(list)
  for i in list:
    if i not in empty_list:
      empty_list.append(i)
  return empty_list

print(remove_duplicate(list))

