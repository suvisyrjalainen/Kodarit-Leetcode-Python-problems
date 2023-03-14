roomalainen_numero = "III"




class Solution:
  def roman_to_int(self, roman):
    roomalaiset = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    lopullinen_numero = 0
    print(len(roman))
    for x in range(len(roman)):
        print(x)
        lopullinen_numero = lopullinen_numero + roomalaiset[x]

    return lopullinen_numero
                         

lopullinen_vastaus = Solution().roman_to_int(roomalainen_numero)

print(lopullinen_vastaus)
