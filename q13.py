# 13. Roman to Integer

# code ngáo
# dict = {
#     "M": 1000,
#     "CM": 900,
#     "D": 500,
#     "CD": 400,
#     "C": 100,
#     "XC": 90,
#     "L": 50,
#     "XL": 40,
#     "X": 10,
#     "IX": 9,
#     "V": 5,
#     "IV": 4,
#     "I": 1
# }

# class Solution:
#     def romanToInt(self, s: str) -> int:
#         result = 0 
#         i = 0 
#         while i < len(s):
#             if s[i] == "C":
#                 if s[i+1] == "M":
#                     i+=1
#                     result += dict["CM"]
#                 elif s[i+1] == "D":
#                     i+=1
#                     result += dict["CD"]
#                 else:
#                     result += dict["C"]

#             elif s[i] == "X":
#                 if s[i+1] == "C":
#                     i+=1
#                     result += dict["XC"]
#                 elif s[i+1] == "L":
#                     i+=1
#                     result += dict["XL"]
#                 else:
#                     result += dict["X"]

#             elif s[i] == "I":
#                 if s[i+1] == "X":
#                     i+=1
#                     result += dict["IX"]
#                 elif s[i+1] == "V":
#                     i+=1
#                     result += dict["IV"]
#                 else:
#                     result += dict["I"]
            
#             else:
#                 result += dict[s[i]]

#             i += 1

#         return result

dict = {
    "M": 1000,
    "D": 500,
    "C": 100,
    "L": 50,
    "X": 10,
    "V": 5,
    "I": 1
}

class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0 
        for i in range(len(s)-1):
            if dict[s[i]] < dict[s[i+1]]:
                result -= dict[s[i]]
            else:
                result += dict[s[i]]
        result += dict[s[-1]]
        return result

s = "MCMXCIV"
print(Solution().romanToInt(s))

