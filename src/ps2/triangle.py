'''
CSC263 Winter 2020
Problem Set 2 Adapted from Starter Code
University of Toronto Mississauga
'''

# Do NOT add any "import" statements
from math import floor #Approved by Suschant https://mcsapps.utm.utoronto.ca/forum/t/ps2-q4-can-we-import-floor/5249/2
# Do NOT use Python dictionaries

class TriangleHashTable(object):
  """size: int"""
  def __init__(self, size):
    self.a = 0.45352364758429879433234 #example from slides
    self.b = 0.61803398874989484820458 #(sqrt(5)-1)/2
    self.c = 0.82287565553229529525080 #(sqrt(7)-1)/2
    self.table = [0] * size
    self.size = size

  def insert(self, triangle):
    '''
    Pre: triangle is a 3-tuple representing a triangle. dict is a dictionary 
    Post: increases the count of triangles for the hash value by 1
    '''
    index = floor(self.size * (((self.a*max(triangle))+(self.b*min(triangle))+(self.c*(sum(triangle)-(max(triangle)+min(triangle)))))%1))
    self.table[index] += 1

  def getKinds(self):
    '''
    Pre: No conditions
    Post: Returns the number of non-zero elements in self.table
    '''
    retval = 0
    for element in self.table:
      if element:
        retval += 1
    return retval

def num_triangle_kinds(triangles):
  '''
  Pre: triangles is a list of 3-tuples representing triangles
  Post: return the number of kinds of triangles
  '''
  hashtable = TriangleHashTable(120*len(triangles))
  for triangle in triangles:
    hashtable.insert(triangle)
  return hashtable.getKinds()



if __name__ == '__main__':

  # some small test cases
  # Case 1
  triangles = [(6, 12, 9), (9, 6, 12), (9, 6, 6), (6, 9, 9), (12, 9, 6)]
  assert 3 == num_triangle_kinds(triangles)