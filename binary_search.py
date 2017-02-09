
class BinarySearch(list):
  """Binary Search to traverse an ordered list, effectively
       Populate the arrays with valid content
    """

  def __init__(self, a, b):
    list.__init__(self)
    self.length = a
    self.step = b
    
    #populating the list
    for num in range(self.step, (self.length * self.step) + 1, self.step):
      self.append(num)
  
  def search(self, item):
    """Get the index of the item with an expected number of loops in\
     array [1, 2 . . . 20]
       Returns a dictionary containing {count: value, index: value}
    """
    count_and_index = {"count": 0, "index": 0}
    count = 0
    min_val = 0
    max_val = self.length - 1
    
    #return a dict with count zer0 if item is greater than max or less than min
    if item > self[max_val] or item < self[min_val]:
      return {"count": 0, "index": -1}
    
    while True:
      mid_val = (min_val + max_val) // 2
      
      #item has been found
      if self[mid_val] == item:
        count_and_index["count"] = count
        count_and_index["index"] = mid_val
        return count_and_index
      
      #item not in the list
      elif self[mid_val] > item and self[mid_val - 1] < item:
        count_and_index["count"] = count
        count_and_index["index"] = -1
        return count_and_index
      
      #item not in the list
      elif self[mid_val] < item and self[mid_val + 1] > item:
        count_and_index["count"] = count
        count_and_index["index"] = -1
        return count_and_index

      elif self[mid_val] < item:
        min_val = mid_val + 1
        count += 1
      
      else:
        max_val = mid_val - 1
        count += 1
        
      
    
    
    
      
    
  