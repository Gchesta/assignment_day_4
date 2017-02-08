def find_missing(list_1, list_2):
  
  #creating sets
  set_1 = set(list_1)
  set_2 = set(list_2)
  
  if set_1 == set_2:
    return 0

  #return the symmetric difference and then converts it into a list  
  else:
    return list((set_1 ^ set_2))[0]
