#Lesson 76
#string to int
def convert_to_int(str):
  is_negative = False
  start_index = 0
  if str[0] == '-':
    is_negative = True
    start_index = 1

  result = 0
  for c in str[start_index:]:
    result = result * 10 + ord(c) - ord('0')

  if is_negative:
    result *= -1
  return result

#test input
print(convert_to_int('-105'))