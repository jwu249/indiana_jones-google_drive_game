
import turtle
import random

global character
global pos
global isNotSelected
global char_str
global notStarted
global rating



def start(x, y):
  global notStarted
  notStarted = False


def choose(x, y):
  global isNotSelected
  global char_str
  if x < -30:
    char_str = "test.gif"
  elif x > 30:
    char_str = "boy2.gif"
  isNotSelected = False


def check():
  x = character.xcor()
  y = character.ycor()
  if x > 500:
    character.goto(0, 0)
  if x < -500:
    character.goto(0, 0)
  if y > 450:
    character.goto(0, 0)
  if y < -450:
    character.goto(0, 0)


def check1():
  x1 = character.xcor()
  y1 = character.ycor()
  if x1 > 200:
    startbutton1.hideturtle()
    startbutton2.hideturtle()
    startbutton3.hideturtle()
    startbutton4.hideturtle()
    startbutton5.hideturtle()
    startbutton6.hideturtle()
  if x1 < 160:
    startbutton1.hideturtle()
    startbutton2.hideturtle()
    startbutton3.hideturtle()
    startbutton4.hideturtle()
    startbutton5.hideturtle()
    startbutton6.hideturtle()
  if y1 > 130:
    startbutton1.hideturtle()
    startbutton2.hideturtle()
    startbutton3.hideturtle()
    startbutton4.hideturtle()
    startbutton5.hideturtle()
    startbutton6.hideturtle()
  if y1 < 80:
    startbutton1.hideturtle()
    startbutton2.hideturtle()
    startbutton3.hideturtle()
    startbutton4.hideturtle()
    startbutton5.hideturtle()
    startbutton6.hideturtle()

  if (character.distance(tree.xcor(), tree.ycor()) < 20):
    startbutton1.goto(0, 0)
    startbutton1.showturtle()

  if (character.distance(cactus.xcor(), cactus.ycor()) < 20):
    startbutton2.goto(0, 0)
    startbutton2.showturtle()

  if (character.distance(cat.xcor(), cat.ycor()) < 20):
    startbutton3.goto(0, 0)
    startbutton3.showturtle()

  if (character.distance(flower.xcor(), flower.ycor()) < 20):
    startbutton4.goto(0, 0)
    startbutton4.showturtle()

  if (character.distance(bush.xcor(), bush.ycor()) < 20):
    startbutton5.goto(0, 0)
    startbutton5.showturtle()

  if (character.distance(lemon.xcor(), lemon.ycor()) < 20):
    startbutton6.goto(0, 0)
    startbutton6.showturtle()

def rating11(x, y):
  rating = "Project 1 = 1 star"
  t11 = turtle.Turtle()
  t11.penup()
  t11.hideturtle()
  t11.goto(0, -100)
  t11.write("Thank you for playing. Feedback is received",
           align="center",
           font=("Ariel", 20, "bold"))
  t11.goto(0, -200)
  t11.write("Please restart and find the other projects if you can :)")
  with open("feedback.txt", "a") as f:
      f.write("\n")
      f.write(rating)


def rating12(x, y):
  rating = "Project 1 = 2 stars"
  t11 = turtle.Turtle()
  t11.penup()
  t11.hideturtle()
  t11.goto(0, -100)
  t11.write("Thank you for playing. Feedback is received",
           align="center",
           font=("Ariel", 20, "bold"))
  t11.goto(0, -200)
  t11.write("Please restart and find the other projects if you can :)")
  with open("feedback.txt", "a") as f:
      f.write("\n")
      f.write(rating)

def rating13(x, y):
  rating = "Project 1 = 3 stars"
  t11 = turtle.Turtle()
  t11.penup()
  t11.hideturtle()
  t11.goto(0, -100)
  t11.write("Thank you for playing. Feedback is received",
           align="center",
           font=("Ariel", 20, "bold"))
  t11.goto(0, -200)
  t11.write("Please restart and find the other projects if you can :)")
  with open("feedback.txt", "a") as f:
      f.write("\n")
      f.write(rating)

def rating14(x, y):
  rating = "Project 1 = 4 stars"
  t11 = turtle.Turtle()
  t11.penup()
  t11.hideturtle()
  t11.goto(0, -100)
  t11.write("Thank you for playing. Feedback is received",
           align="center",
           font=("Ariel", 20, "bold"))
  t11.goto(0, -200)
  t11.write("Please restart and find the other projects if you can :)")
  with open("feedback.txt", "a") as f:
      f.write("\n")
      f.write(rating)

def rating15(x, y):
  rating = "Project 1 = 5 stars"
  t11 = turtle.Turtle()
  t11.penup()
  t11.hideturtle()
  t11.goto(0, -100)
  t11.write("Thank you for playing. Feedback is received",
           align="center",
           font=("Ariel", 20, "bold"))
  t11.goto(0, -200)
  t11.write("Please restart and find the other projects if you can :)")
  with open("feedback.txt", "a") as f:
      f.write("\n")
      f.write(rating)


def rating21(x, y):
  rating = "Project 2 = 1 star" 
  t11 = turtle.Turtle()
  t11.penup()
  t11.hideturtle()
  t11.goto(0, -100)
  t11.write("Thank you for playing. Feedback is received",
           align="center",
           font=("Ariel", 20, "bold"))
  t11.goto(0, -200)
  t11.write("Please restart and find the other projects if you can :)")
  with open("feedback.txt", "a") as f:
      f.write("\n")
      f.write(rating)


def rating22(x, y):
  rating = "Project 2 = 2 stars"
  t11 = turtle.Turtle()
  t11.penup()
  t11.hideturtle()
  t11.goto(0, -100)
  t11.write("Thank you for playing. Feedback is received",
           align="center",
           font=("Ariel", 20, "bold"))
  t11.goto(0, -200)
  t11.write("Please restart and find the other projects if you can :)")
  with open("feedback.txt", "a") as f:
      f.write("\n")
      f.write(rating)

def rating23(x, y):
  rating = "Project 2 = 3 stars"
  t11 = turtle.Turtle()
  t11.penup()
  t11.hideturtle()
  t11.goto(0, -100)
  t11.write("Thank you for playing. Feedback is received",
           align="center",
           font=("Ariel", 20, "bold"))
  t11.goto(0, -200)
  t11.write("Please restart and find the other projects if you can :)")
  with open("feedback.txt", "a") as f:
      f.write("\n")
      f.write(rating)

def rating24(x, y):
  rating = "Project 2 = 4 stars"
  t11 = turtle.Turtle()
  t11.penup()
  t11.hideturtle()
  t11.goto(0, -100)
  t11.write("Thank you for playing. Feedback is received",
           align="center",
           font=("Ariel", 20, "bold"))
  t11.goto(0, -200)
  t11.write("Please restart and find the other projects if you can :)")
  with open("feedback.txt", "a") as f:
      f.write("\n")
      f.write(rating)

def rating25(x, y):
  rating = "Project 2 = 5 stars"
  t11 = turtle.Turtle()
  t11.penup()
  t11.hideturtle()
  t11.goto(0, -100)
  t11.write("Thank you for playing. Feedback is received",
           align="center",
           font=("Ariel", 20, "bold"))
  t11.goto(0, -200)
  t11.write("Please restart and find the other projects if you can :)")
  with open("feedback.txt", "a") as f:
      f.write("\n")
      f.write(rating)

def rating31(x, y):
  rating = "Project 3 = 1 star"
  t11 = turtle.Turtle()
  t11.penup()
  t11.hideturtle()
  t11.goto(0, -100)
  t11.write("Thank you for playing. Feedback is received",
           align="center",
           font=("Ariel", 20, "bold"))
  t11.goto(0, -200)
  t11.write("Please restart and find the other projects if you can :)")
  with open("feedback.txt", "a") as f:
      f.write("\n")
      f.write(rating)


def rating32(x, y):
  rating = "Project 3 = 2 stars"
  t11 = turtle.Turtle()
  t11.penup()
  t11.hideturtle()
  t11.goto(0, -100)
  t11.write("Thank you for playing. Feedback is received",
           align="center",
           font=("Ariel", 20, "bold"))
  t11.goto(0, -200)
  t11.write("Please restart and find the other projects if you can :)")
  with open("feedback.txt", "a") as f:
      f.write("\n")
      f.write(rating)

def rating33(x, y):
  rating = "Project 3 = 3 stars"
  t11 = turtle.Turtle()
  t11.penup()
  t11.hideturtle()
  t11.goto(0, -100)
  t11.write("Thank you for playing. Feedback is received",
           align="center",
           font=("Ariel", 20, "bold"))
  t11.goto(0, -200)
  t11.write("Please restart and find the other projects if you can :)")
  with open("feedback.txt", "a") as f:
      f.write("\n")
      f.write(rating)

def rating34(x, y):
  rating = "Project 3 = 4 stars"
  t11 = turtle.Turtle()
  t11.penup()
  t11.hideturtle()
  t11.goto(0, -100)
  t11.write("Thank you for playing. Feedback is received",
           align="center",
           font=("Ariel", 20, "bold"))
  t11.goto(0, -200)
  t11.write("Please restart and find the other projects if you can :)")
  with open("feedback.txt", "a") as f:
      f.write("\n")
      f.write(rating)

def rating35(x, y):
  rating = "Project 3 = 5 stars"
  t11 = turtle.Turtle()
  t11.penup()
  t11.hideturtle()
  t11.goto(0, -100)
  t11.write("Thank you for playing. Feedback is received",
           align="center",
           font=("Ariel", 20, "bold"))
  t11.goto(0, -200)
  t11.write("Please restart and find the other projects if you can :)")
  with open("feedback.txt", "a") as f:
      f.write("\n")
      f.write(rating)

def rating41(x, y):
  rating = "Project 4 = 1 star"
  t11 = turtle.Turtle()
  t11.penup()
  t11.hideturtle()
  t11.goto(0, -100)
  t11.write("Thank you for playing. Feedback is received",
           align="center",
           font=("Ariel", 20, "bold"))
  t11.goto(0, -200)
  t11.write("Please restart and find the other projects if you can :)")
  with open("feedback.txt", "a") as f:
      f.write("\n")
      f.write(rating)


def rating42(x, y):
  rating = "Project 4 = 2 stars"
  t11 = turtle.Turtle()
  t11.penup()
  t11.hideturtle()
  t11.goto(0, -100)
  t11.write("Thank you for playing. Feedback is received",
           align="center",
           font=("Ariel", 20, "bold"))
  t11.goto(0, -200)
  t11.write("Please restart and find the other projects if you can :)")
  with open("feedback.txt", "a") as f:
      f.write("\n")
      f.write(rating)

def rating43(x, y):
  rating = "Project 4 = 3 stars"
  t11 = turtle.Turtle()
  t11.penup()
  t11.hideturtle()
  t11.goto(0, -100)
  t11.write("Thank you for playing. Feedback is received",
           align="center",
           font=("Ariel", 20, "bold"))
  t11.goto(0, -200)
  t11.write("Please restart and find the other projects if you can :)")
  with open("feedback.txt", "a") as f:
      f.write("\n")
      f.write(rating)

def rating44(x, y):
  rating = "Project 4 = 4 stars"
  t11 = turtle.Turtle()
  t11.penup()
  t11.hideturtle()
  t11.goto(0, -100)
  t11.write("Thank you for playing. Feedback is received",
           align="center",
           font=("Ariel", 20, "bold"))
  t11.goto(0, -200)
  t11.write("Please restart and find the other projects if you can :)")
  with open("feedback.txt", "a") as f:
      f.write("\n")
      f.write(rating)

def rating45(x, y):
  rating = "Project 4 = 5 stars"
  t11 = turtle.Turtle()
  t11.penup()
  t11.hideturtle()
  t11.goto(0, -100)
  t11.write("Thank you for playing. Feedback is received",
           align="center",
           font=("Ariel", 20, "bold"))
  t11.goto(0, -200)
  t11.write("Please restart and find the other projects if you can :)")
  with open("feedback.txt", "a") as f:
      f.write("\n")
      f.write(rating)

def rating51(x, y):
  rating = "Project 5 = 1 star"
  t11 = turtle.Turtle()
  t11.penup()
  t11.hideturtle()
  t11.goto(0, -100)
  t11.write("Thank you for playing. Feedback is received",
           align="center",
           font=("Ariel", 20, "bold"))
  t11.goto(0, -200)
  t11.write("Please restart and find the other projects if you can :)")
  with open("feedback.txt", "a") as f:
      f.write("\n")
      f.write(rating)


def rating52(x, y):
  rating = "Project 5 = 2 stars"
  t11 = turtle.Turtle()
  t11.penup()
  t11.hideturtle()
  t11.goto(0, -100)
  t11.write("Thank you for playing. Feedback is received",
           align="center",
           font=("Ariel", 20, "bold"))
  t11.goto(0, -200)
  t11.write("Please restart and find the other projects if you can :)")
  with open("feedback.txt", "a") as f:
      f.write("\n")
      f.write(rating)

def rating53(x, y):
  rating = "Project 5 = 3 stars"
  t11 = turtle.Turtle()
  t11.penup()
  t11.hideturtle()
  t11.goto(0, -100)
  t11.write("Thank you for playing. Feedback is received",
           align="center",
           font=("Ariel", 20, "bold"))
  t11.goto(0, -200)
  t11.write("Please restart and find the other projects if you can :)")
  with open("feedback.txt", "a") as f:
      f.write("\n")
      f.write(rating)

def rating54(x, y):
  rating = "Project 5 = 4 stars"
  t11 = turtle.Turtle()
  t11.penup()
  t11.hideturtle()
  t11.goto(0, -100)
  t11.write("Thank you for playing. Feedback is received",
           align="center",
           font=("Ariel", 20, "bold"))
  t11.goto(0, -200)
  t11.write("Please restart and find the other projects if you can :)")
  with open("feedback.txt", "a") as f:
      f.write("\n")
      f.write(rating)

def rating55(x, y):
  rating = "Project 5 = 5 stars"
  t11 = turtle.Turtle()
  t11.penup()
  t11.hideturtle()
  t11.goto(0, -100)
  t11.write("Thank you for playing. Feedback is received",
           align="center",
           font=("Ariel", 20, "bold"))
  t11.goto(0, -200)
  t11.write("Please restart and find the other projects if you can :)")
  with open("feedback.txt", "a") as f:
      f.write("\n")
      f.write(rating)

def rating61(x, y):
  rating = "Project 6 = 1 star"
  t11 = turtle.Turtle()
  t11.penup()
  t11.hideturtle()
  t11.goto(0, -100)
  t11.write("Thank you for playing. Feedback is received",
           align="center",
           font=("Ariel", 20, "bold"))
  t11.goto(0, -200)
  t11.write("Please restart and find the other projects if you can :)")
  with open("feedback.txt", "a") as f:
      f.write("\n")
      f.write(rating)


def rating62(x, y):
  rating = "Project 6 = 2 stars"
  t11 = turtle.Turtle()
  t11.penup()
  t11.hideturtle()
  t11.goto(0, -100)
  t11.write("Thank you for playing. Feedback is received",
           align="center",
           font=("Ariel", 20, "bold"))
  t11.goto(0, -200)
  t11.write("Please restart and find the other projects if you can :)")
  with open("feedback.txt", "a") as f:
      f.write("\n")
      f.write(rating)

def rating63(x, y):
  rating = "Project 6 = 3 stars"
  t11 = turtle.Turtle()
  t11.penup()
  t11.hideturtle()
  t11.goto(0, -100)
  t11.write("Thank you for playing. Feedback is received",
           align="center",
           font=("Ariel", 20, "bold"))
  t11.goto(0, -200)
  t11.write("Please restart and find the other projects if you can :)")
  with open("feedback.txt", "a") as f:
      f.write("\n")
      f.write(rating)

def rating64(x, y):
  rating = "Project 6 = 4 stars"
  t11 = turtle.Turtle()
  t11.penup()
  t11.hideturtle()
  t11.goto(0, -100)
  t11.write("Thank you for playing. Feedback is received",
           align="center",
           font=("Ariel", 20, "bold"))
  t11.goto(0, -200)
  t11.write("Please restart and find the other projects if you can :)")
  with open("feedback.txt", "a") as f:
      f.write("\n")
      f.write(rating)

def rating65(x, y):
  rating = "Project 6 = 5 stars"
  t11 = turtle.Turtle()
  t11.penup()
  t11.hideturtle()
  t11.goto(0, -100)
  t11.write("Thank you for playing. Feedback is received",
           align="center",
           font=("Ariel", 20, "bold"))
  t11.goto(0, -200)
  t11.write("Please restart and find the other projects if you can :)")
  with open("feedback.txt", "a") as f:
      f.write("\n")
      f.write(rating)

def stall():
  st = turtle.Turtle()
  st.hideturtle()
  st.penup()
  st.speed(1)
  st.forward(100)


def project1(x, y):
  s.clearscreen()
  s.bgcolor("black")
  s.bgpic("project11.gif")
  stall()

  s.bgpic("project12.gif")
  stall()

  s.bgpic("project13.gif")
  stall()

  s.bgpic("project14.gif")
  stall()

  s.bgpic("project15.gif")
  stall()

  s.clearscreen()
  s.bgcolor("blue")
  t1 = turtle.Turtle()
  t1.penup()
  t1.hideturtle()
  t1.goto(0, 200)
  t1.write("Please rate your experience on project 1",
           align="center",
           font=("Ariel", 20, "bold"))

  star1 = turtle.Turtle()
  star1.penup()
  star1.goto(-200, 0)
  turtle.addshape("star1.gif")
  star1.showturtle()
  star1.shape("star1.gif")

  star2 = turtle.Turtle()  #images have to be diff
  star2.penup()
  star2.goto(-100, 0)
  turtle.addshape("star2.gif")
  star2.showturtle()
  star2.shape("star2.gif")

  star3 = turtle.Turtle()  #images have to be diff
  star3.penup()
  star3.goto(0, 0)
  turtle.addshape("star3.gif")
  star3.showturtle()
  star3.shape("star3.gif")

  star4 = turtle.Turtle()  #images have to be diff
  star4.penup()
  star4.goto(100, 0)
  turtle.addshape("star4.gif")
  star4.showturtle()
  star4.shape("star4.gif")

  star5 = turtle.Turtle()  #images have to be diff
  star5.penup()
  star5.goto(200, 0)
  turtle.addshape("star5.gif")
  star5.showturtle()
  star5.shape("star5.gif")

  if star1.onclick(rating11):
    on = "clicked"

  if star2.onclick(rating12):
    on = "clicked"

  if star3.onclick(rating13):
    on = "clicked"
  
  if star4.onclick(rating14):
    on = "clicked"
  
  if star5.onclick(rating15):
    on = "clicked"


def project2(x, y):
  s.clearscreen()
  s.bgcolor("black")

  s.bgpic("project21.gif")
  stall()

  s.bgpic("project22.gif")
  stall()

  s.bgpic("project23.gif")
  stall()

  s.bgpic("project24.gif")
  stall()

  s.bgpic("project25.gif")
  stall()

  s.clearscreen()
  s.bgcolor("blue")
  t2 = turtle.Turtle()
  t2.penup()
  t2.hideturtle()
  t2.goto(0, 200)
  t2.write("Please rate your experience on project 2",
           align="center",
           font=("Ariel", 20, "bold"))

  star1 = turtle.Turtle()
  star1.penup()
  star1.goto(-200, 0)
  turtle.addshape("star1.gif")
  star1.showturtle()
  star1.shape("star1.gif")

  star2 = turtle.Turtle()  #images have to be diff
  star2.penup()
  star2.goto(-100, 0)
  turtle.addshape("star2.gif")
  star2.showturtle()
  star2.shape("star2.gif")

  star3 = turtle.Turtle()  #images have to be diff
  star3.penup()
  star3.goto(0, 0)
  turtle.addshape("star3.gif")
  star3.showturtle()
  star3.shape("star3.gif")

  star4 = turtle.Turtle()  #images have to be diff
  star4.penup()
  star4.goto(100, 0)
  turtle.addshape("star4.gif")
  star4.showturtle()
  star4.shape("star4.gif")

  star5 = turtle.Turtle()  #images have to be diff
  star5.penup()
  star5.goto(200, 0)
  turtle.addshape("star5.gif")
  star5.showturtle()
  star5.shape("star5.gif")

  if star1.onclick(rating21):
    on = "clicked"

  if star2.onclick(rating22):
    on = "clicked"

  if star3.onclick(rating23):
    on = "clicked"
  
  if star4.onclick(rating24):
    on = "clicked"
  
  if star5.onclick(rating25):
    on = "clicked"


def project3(x, y):
  s.clearscreen()
  s.bgcolor("black")

  s.bgpic("project31.gif")
  stall()

  s.bgpic("project32.gif")
  stall()

  s.bgpic("project33.gif")
  stall()

  s.bgpic("project34.gif")
  stall()

  s.bgpic("project35.gif")
  stall()

  s.clearscreen()
  s.bgcolor("blue")
  t3 = turtle.Turtle()
  t3.penup()
  t3.hideturtle()
  t3.goto(0, 200)
  t3.write("Please rate your experience on project 3",
           align="center",
           font=("Ariel", 20, "bold"))

  star1 = turtle.Turtle()
  star1.penup()
  star1.goto(-200, 0)
  turtle.addshape("star1.gif")
  star1.showturtle()
  star1.shape("star1.gif")

  star2 = turtle.Turtle()  #images have to be diff
  star2.penup()
  star2.goto(-100, 0)
  turtle.addshape("star2.gif")
  star2.showturtle()
  star2.shape("star2.gif")

  star3 = turtle.Turtle()  #images have to be diff
  star3.penup()
  star3.goto(0, 0)
  turtle.addshape("star3.gif")
  star3.showturtle()
  star3.shape("star3.gif")

  star4 = turtle.Turtle()  #images have to be diff
  star4.penup()
  star4.goto(100, 0)
  turtle.addshape("star4.gif")
  star4.showturtle()
  star4.shape("star4.gif")

  star5 = turtle.Turtle()  #images have to be diff
  star5.penup()
  star5.goto(200, 0)
  turtle.addshape("star5.gif")
  star5.showturtle()
  star5.shape("star5.gif")

  if star1.onclick(rating31):
    on = "clicked"

  if star2.onclick(rating32):
    on = "clicked"

  if star3.onclick(rating33):
    on = "clicked"
  
  if star4.onclick(rating34):
    on = "clicked"
  
  if star5.onclick(rating35):
    on = "clicked"



def project4(x, y):
  s.clearscreen()
  s.bgcolor("black")

  s.bgpic("project41.gif")
  stall()

  s.bgpic("project42.gif")
  stall()

  s.bgpic("project43.gif")
  stall()

  s.bgpic("project44.gif")
  stall()

  s.bgpic("project45.gif")
  stall()

  s.clearscreen()
  s.bgcolor("blue")
  t4 = turtle.Turtle()
  t4.penup()
  t4.hideturtle()
  t4.goto(0, 200)
  t4.write("Please rate your experience on project 4",
           align="center",
           font=("Ariel", 20, "bold"))

  star1 = turtle.Turtle()
  star1.penup()
  star1.goto(-200, 0)
  turtle.addshape("star1.gif")
  star1.showturtle()
  star1.shape("star1.gif")

  star2 = turtle.Turtle()  #images have to be diff
  star2.penup()
  star2.goto(-100, 0)
  turtle.addshape("star2.gif")
  star2.showturtle()
  star2.shape("star2.gif")

  star3 = turtle.Turtle()  #images have to be diff
  star3.penup()
  star3.goto(0, 0)
  turtle.addshape("star3.gif")
  star3.showturtle()
  star3.shape("star3.gif")

  star4 = turtle.Turtle()  #images have to be diff
  star4.penup()
  star4.goto(100, 0)
  turtle.addshape("star4.gif")
  star4.showturtle()
  star4.shape("star4.gif")

  star5 = turtle.Turtle()  #images have to be diff
  star5.penup()
  star5.goto(200, 0)
  turtle.addshape("star5.gif")
  star5.showturtle()
  star5.shape("star5.gif")

  if star1.onclick(rating41):
    on = "clicked"

  if star2.onclick(rating42):
    on = "clicked"

  if star3.onclick(rating43):
    on = "clicked"
  
  if star4.onclick(rating44):
    on = "clicked"
  
  if star5.onclick(rating45):
    on = "clicked"



def project5(x, y):
  s.clearscreen()
  s.bgcolor("black")

  s.bgpic("project51.gif")
  stall()

  s.bgpic("project52.gif")
  stall()

  s.bgpic("project53.gif")
  stall()

  s.bgpic("project54.gif")
  stall()

  s.bgpic("project55.gif")
  stall()

  s.clearscreen()
  s.bgcolor("blue")
  t5 = turtle.Turtle()
  t5.penup()
  t5.hideturtle()
  t5.goto(0, 200)
  t5.write("Please rate your experience on project 5",
           align="center",
           font=("Ariel", 20, "bold"))

  star1 = turtle.Turtle()
  star1.penup()
  star1.goto(-200, 0)
  turtle.addshape("star1.gif")
  star1.showturtle()
  star1.shape("star1.gif")

  star2 = turtle.Turtle()  #images have to be diff
  star2.penup()
  star2.goto(-100, 0)
  turtle.addshape("star2.gif")
  star2.showturtle()
  star2.shape("star2.gif")

  star3 = turtle.Turtle()  #images have to be diff
  star3.penup()
  star3.goto(0, 0)
  turtle.addshape("star3.gif")
  star3.showturtle()
  star3.shape("star3.gif")

  star4 = turtle.Turtle()  #images have to be diff
  star4.penup()
  star4.goto(100, 0)
  turtle.addshape("star4.gif")
  star4.showturtle()
  star4.shape("star4.gif")

  star5 = turtle.Turtle()  #images have to be diff
  star5.penup()
  star5.goto(200, 0)
  turtle.addshape("star5.gif")
  star5.showturtle()
  star5.shape("star5.gif")

  if star1.onclick(rating51):
    on = "clicked"

  if star2.onclick(rating52):
    on = "clicked"

  if star3.onclick(rating53):
    on = "clicked"
  
  if star4.onclick(rating54):
    on = "clicked"
  
  if star5.onclick(rating55):
    on = "clicked"


  
def project6(x, y):
  s.clearscreen()
  s.bgcolor("black")

  s.bgpic("project61.gif")
  stall()

  s.bgpic("project62.gif")
  stall()

  s.bgpic("project63.gif")
  stall()

  s.bgpic("project64.gif")
  stall()

  s.bgpic("project65.gif")
  stall()

  s.clearscreen()
  s.bgcolor("blue")
  t6 = turtle.Turtle()
  t6.penup()
  t6.hideturtle()
  t6.goto(0, 200)
  t6.write("Please rate your experience on project 6",
           align="center",
           font=("Ariel", 20, "bold"))

  star1 = turtle.Turtle()
  star1.penup()
  star1.goto(-200, 0)
  turtle.addshape("star1.gif")
  star1.showturtle()
  star1.shape("star1.gif")

  star2 = turtle.Turtle()  #images have to be diff
  star2.penup()
  star2.goto(-100, 0)
  turtle.addshape("star2.gif")
  star2.showturtle()
  star2.shape("star2.gif")

  star3 = turtle.Turtle()  #images have to be diff
  star3.penup()
  star3.goto(0, 0)
  turtle.addshape("star3.gif")
  star3.showturtle()
  star3.shape("star3.gif")

  star4 = turtle.Turtle()  #images have to be diff
  star4.penup()
  star4.goto(100, 0)
  turtle.addshape("star4.gif")
  star4.showturtle()
  star4.shape("star4.gif")

  star5 = turtle.Turtle()  #images have to be diff
  star5.penup()
  star5.goto(200, 0)
  turtle.addshape("star5.gif")
  star5.showturtle()
  star5.shape("star5.gif")

  if star1.onclick(rating61):
    on = "clicked"

  if star2.onclick(rating62):
    on = "clicked"

  if star3.onclick(rating63):
    on = "clicked"
  
  if star4.onclick(rating64):
    on = "clicked"
  
  if star5.onclick(rating65):
    on = "clicked"


# Move with arrows (boy character)


def up():
  character.setheading(90)
  character.forward(10)
  check()
  check1()


def down():
  character.setheading(270)
  character.forward(10)
  check()
  check1()


def left():
  character.setheading(180)
  character.forward(10)
  check()
  check1()


def right():
  character.setheading(0)
  character.forward(10)
  check()
  check1()


#Sets up screen 1
s = turtle.getscreen()
s.bgpic("cloud.gif")

t = turtle.Turtle()
t.penup()
t.hideturtle()
t.goto(0, 40)
t.write("Welcome!", align="center", font=("Ariel", 45, "bold"))
t.goto(0, -20)
t.write(
  "Our project aims to provide students with an interactive experience viewing the computer science projects we have done.",
  align="center",
  font=("Ariel", 12, "bold"))
t.goto(0, -50)
t.write(
  "The project will be a fun spin-off of the existing Google Drive program that allows people to organize documents.",
  align="center",
  font=("Ariel", 12, "bold"))

startbutton = turtle.Turtle()
turtle.addshape("start.gif")
startbutton.shape("start.gif")
startbutton.penup()
startbutton.goto(0, -100)

notStarted = True
while notStarted:
  startbutton.onclick(start)

s.clearscreen()
s.bgcolor("black")

#Allows the user to pick a character
text = turtle.Turtle()
text.penup()
text.hideturtle()
text.goto(0, 100)
text.color("white")
text.write("Please pick a character and start the hunt for projects!",
           False,
           align='center',
           font=('Arial', 25, 'bold'))

boy = turtle.Turtle()
boy.penup()
boy.goto(50, -25)
turtle.addshape("boy2.gif")
boy.showturtle()
boy.shape("boy2.gif")

girl = turtle.Turtle()
girl.penup()
girl.goto(-50, -25)
turtle.addshape("test.gif")
girl.showturtle()
girl.shape("test.gif")

s.listen()

isNotSelected = True
while isNotSelected:
  boy.onclick(choose)
  girl.onclick(choose)

s.clearscreen()
s.bgpic("map.gif")

tree = turtle.Turtle()
tree.penup()
tree.goto(180, 110)
turtle.addshape("tree.gif")
tree.showturtle()
tree.shape("tree.gif")

lemon = turtle.Turtle()
lemon.penup()
lemon.goto(-215, 260)
turtle.addshape("lemon.gif")
lemon.showturtle()
lemon.shape("lemon.gif")

cactus = turtle.Turtle()
cactus.penup()
cactus.goto(-389, -255)
turtle.addshape("cactus.gif")
cactus.showturtle()
cactus.shape("cactus.gif")

bush = turtle.Turtle()
bush.penup()
bush.goto(220, 30)
turtle.addshape("bush.gif")
bush.showturtle()
bush.shape("bush.gif")

flower = turtle.Turtle()
flower.penup()
flower.goto(-399, 45)
turtle.addshape("flower.gif")
flower.showturtle()
flower.shape("flower.gif")

cat = turtle.Turtle()
cat.penup()
cat.goto(389, -255)
turtle.addshape("cat.gif")
cat.showturtle()
cat.shape("cat.gif")

startbutton1 = turtle.Turtle()
startbutton1.penup()
turtle.addshape("start.gif")
startbutton1.hideturtle()
startbutton1.shape("start.gif")

startbutton2 = turtle.Turtle()
startbutton2.penup()
turtle.addshape("start.gif")
startbutton2.hideturtle()
startbutton2.shape("start.gif")

startbutton3 = turtle.Turtle()
startbutton3.penup()
turtle.addshape("start.gif")
startbutton3.hideturtle()
startbutton3.shape("start.gif")

startbutton4 = turtle.Turtle()
startbutton4.penup()
turtle.addshape("start.gif")
startbutton4.hideturtle()
startbutton4.shape("start.gif")

startbutton5 = turtle.Turtle()
startbutton5.penup()
turtle.addshape("start.gif")
startbutton5.hideturtle()
startbutton5.shape("start.gif")

startbutton6 = turtle.Turtle()
startbutton6.penup()
turtle.addshape("start.gif")
startbutton6.hideturtle()
startbutton6.shape("start.gif")

character = turtle.Turtle()
character.shape(char_str)
character.penup()
character.goto(0, 0)

s.listen()

s.onkey(up, "Up")
s.onkey(down, "Down")
s.onkey(left, "Left")
s.onkey(right, "Right")

if startbutton1.onclick(project1):
  test = 1

if startbutton2.onclick(project2):
  test = 2

if startbutton3.onclick(project3):
  test = 3

if startbutton4.onclick(project4):
  test = 4

if startbutton5.onclick(project5):
  test = 5

if startbutton6.onclick(project6):
  test = 6

s.mainloop()
