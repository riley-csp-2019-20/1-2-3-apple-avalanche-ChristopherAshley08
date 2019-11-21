#   a123_apple_1.py
import turtle as trtl
import random as rand

apple_image = "apple.gif" # Store the file name of your shape
ground_height = -200
apple_letter_x_offset = -25
apple_letter_y_offset = -50

#list
screen_width = 400
screen_height = 400
letter_list = ["A","B","C","D","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

current_letter= "A"

#Apple
wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image) # Make the screen aware of the new file

#background
wn.bgpic("background.gif")
apple = trtl.Turtle()
apple.penup()
wn.tracer(False)

# given a turtle, set that turtle to be shaped by the image file

def reset_apple(active_apple):
  global current_letter
  length_of_list = len(letter_list)
  if (length_of_list != 0):
    index = rand.randint(0,length_of_list)
    current_letter =  letter_list.pop(index)
    active_apple.goto(rand.randint(-(screen_width)/2, (screen_width)/2), rand.randint(-(screen_height)/2, (screen_height)/2))
    draw_apple(active_apple, current_letter)

def draw_apple(active_apple, letter):
  active_apple.shape(apple_image)
  active_apple.st()
  draw_letter(letter,active_apple)
  wn.update()

def drop_apple():
  wn.tracer(True)
  apple.goto(apple.xcor(), ground_height)
  apple.clear()
  apple.ht()
  wn.tracer(False)
  reset_apple(apple)

def draw_letter (letter, active_apple):
  active_apple.color("white")
  remember_position = active_apple.position()
  active_apple.setpos(active_apple.xcor()+ apple_letter_x_offset,active_apple.ycor() + apple_letter_y_offset)
  active_apple.write(letter, font=("arial", 74, "bold"))
  active_apple.setpos(remember_position)

def check_letter_A():
  if (current_letter == "A"):
    drop_apple()
def check_letter_B():
  if (current_letter == "B"):
    drop_apple()
def check_letter_C():
  if (current_letter == "C"):
    drop_apple()
def check_letter_D():
  if (current_letter == "D"):
    drop_apple()
def check_letter_E():
  if (current_letter == "E"):
    drop_apple()
def check_letter_F():
  if (current_letter == "F"):
    drop_apple()
def check_letter_G():
  if (current_letter == "G"):
    drop_apple()
def check_letter_H():
  if (current_letter == "H"):
    drop_apple()
def check_letter_I():
  if (current_letter == "I"):
    drop_apple()
def check_letter_J():
  if (current_letter == "J"):
    drop_apple()
def check_letter_K():
  if (current_letter == "K"):
    drop_apple()
def check_letter_L():
  if (current_letter == "L"):
    drop_apple()
def check_letter_M():
  if (current_letter == "M"):
    drop_apple()
def check_letter_N():
  if (current_letter == "N"):
    drop_apple()
def check_letter_O():
  if (current_letter == "O"):
    drop_apple()
def check_letter_P():
  if (current_letter == "P"):
    drop_apple()
def check_letter_Q():
  if (current_letter == "Q"):
    drop_apple()
def check_letter_R():
  if (current_letter == "R"):
    drop_apple()
def check_letter_S():
  if (current_letter == "S"):
    drop_apple()
def check_letter_T():
  if (current_letter == "T"):
    drop_apple()
def check_letter_U():
  if (current_letter == "U"):
    drop_apple()
def check_letter_V():
  if (current_letter == "V"):
    drop_apple()
def check_letter_W():
  if (current_letter == "W"):
    drop_apple()
def check_letter_X():
  if (current_letter == "X"):
    drop_apple()
def check_letter_Y():
  if (current_letter == "Y"):
    drop_apple()
def check_letter_Z():
  if (current_letter == "Z" ):
    drop_apple()

draw_apple(apple,"A")
wn.onkeypress(check_letter_A,"a")
wn.onkeypress(check_letter_B,"b")
wn.onkeypress(check_letter_C,"c")
wn.onkeypress(check_letter_D,"d")
wn.onkeypress(check_letter_E,"e")
wn.onkeypress(check_letter_F,"f")
wn.onkeypress(check_letter_G,"g")
wn.onkeypress(check_letter_H,"h")
wn.onkeypress(check_letter_I,"i")
wn.onkeypress(check_letter_J,"j")
wn.onkeypress(check_letter_K,"k")
wn.onkeypress(check_letter_L,"l")
wn.onkeypress(check_letter_M,"m")
wn.onkeypress(check_letter_N,"n")
wn.onkeypress(check_letter_O,"o")
wn.onkeypress(check_letter_P,"p")
wn.onkeypress(check_letter_Q,"q")
wn.onkeypress(check_letter_R,"r")
wn.onkeypress(check_letter_S,"s")
wn.onkeypress(check_letter_T,"t")
wn.onkeypress(check_letter_U,"u")
wn.onkeypress(check_letter_V,"v")
wn.onkeypress(check_letter_W,"w")
wn.onkeypress(check_letter_X,"x")
wn.onkeypress(check_letter_Y,"y")
wn.onkeypress(check_letter_Z,"z")

wn.listen()
wn.mainloop()