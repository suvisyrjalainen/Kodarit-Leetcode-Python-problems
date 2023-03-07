nums = [5,4,6,9]
target = 10



class Solution:
  def __init__(self):
    self.nums = []
    self.target = 0
    
  def twoSum(self, numerolista, vastaus):
    self.nums = numerolista
    self.target = vastaus
    for x in numerolista:
      for y in numerolista:
        if numerolista.index(x) != numerolista.index(y):
          if x + y == vastaus:
              return [numerolista.index(x), numerolista.index(y)]


ratkaisu = Solution()

lista = ratkaisu.twoSum(nums, target)

print(lista)