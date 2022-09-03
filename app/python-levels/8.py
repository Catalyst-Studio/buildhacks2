#something with faulty defines
#missing item in def
#missing quote
#int should be str
#return should be elsewhere
def number(output)
  output = "one"
  if type(output) == int:
    output = 125
    output = output - 5 / 6
return int(output)
print(number(output))
