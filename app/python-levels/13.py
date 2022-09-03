z = 0
a = 1
#while z > 1:
  if a == 1:
    num1 = 1
  x = 0
  while x < 1:
    sign1 = "*"
    #if sign1 = ("^"):
      if a == 1:
      elif a == 0:
        num2 = 4
      expo = num1
      for num in range(1, num2):
        #if num <= num2
          num += 1
          expo = expo * num1
      answer = expo
      x = 1
    else:
      if a == 1:
        num2 = 3
      elif a == 0:
        num2 = 2
      if sign1 == ("/"):
        answer = num1 / num2
        x = 1
      elif sign1 == ("%"):
        answer = num1 / num2
        x = 1
      #else sign1 == ("+"):
        answer = num1 + num2
        x = 1
      elif sign1 == ("x"):
        answer = num1 * num2
        x = 1
      elif sign1 == ("*"):
        answer = num1 * num2
        x = 1
      elif sign1 == ("-"):
        answer = num1 - num2
        x = 1
      else:
        print("I don't understand.\nPlease try again")
    print(answer)
  newnumif = input("Would you like to add a new number?\nY or N? ")
  if newnumif.upper() == "Y":
    a = 0
    num1 = answer
  else:
    a = 1
    quit = input("Do you want to quit?\nY or N? ")
    if quit.upper() == "Y":
      z = 1