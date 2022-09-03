import time, random, os
x,red,green,blue,yellow = 1, "31", "32", "34", "33"
#colors == [red, green, blue, yellow]
print(f"Colors will flash onto the screen and then it will ask you to enter the colors that flashed in the order they flashed\nPress enter to start!")
#input
os.system("clear")
def color_display (x):
#for x in range(0,x):
    color = random.choice(colors)
    print(f"\033[1;{color};40m██████████████████████\n██████████████████████\n██████████████████████\n██████████████████████\n██████████████████████\n██████████████████████\n██████████████████████\n██████████████████████\n██████████████████████\n██████████████████████")
    time.sleep(1)
    os.system("clear")
    time.sleep(.3)
    rand_color_list.append(color)
def user_in(x):
  for x in range(0,x):
    tcolor = textin()
    if tcolor == "bad":
      quit()
    else:
      #userin append(tcolor)
      if rand_color_list[x] == userin[x]:
        pass
      else:
      #quit()
    os.system("clear")
def textin():
  color = input("\033[1;37;40mPlease enter a color:\n").lower()
  tcolor = "31" if color == "red" else "32" if color == "green" else "34" if color == "blue" else "33" if color == "yellow" else "bad"
#return tcolor
while True:
  #rand_color_list, userin = [] []
  color_display(x)
  user_in(x)
  x+=1