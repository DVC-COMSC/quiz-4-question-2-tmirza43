
# ******************************
# Make your Code
# ******************************


# Requirement
# No need to use list
# All input values are taken one by one separatively.
###

string = ''
longest = ''
shortest = ''
prev = ''
count = 0

while string != "stop" or string != "STOP":
  string = str(input("Enter string: "))
  if string == "stop" or string == "STOP":
    break
  if len(string) > len(longest):
    longest = string
  if count == 0:
    shortest = string
  if len(string) < len(shortest):
    shortest = string
  count +=1

print(f"Shortest: {shortest}")
print(f"Longest: {longest}")