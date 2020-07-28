import turtle

class Board:
   def __init__(self):
       self.draw = turtle.Turtle()
       self.draw.speed(0)
       self.draw.penup()
       self.draw.goto(-100,200)
       self.draw.pendown()
       self.draw.goto(-100,-200)
       self.draw.penup()
       self.draw.goto(100,200)
       self.draw.pendown()
       self.draw.goto(100,-200)
       self.draw.penup()
       self.draw.goto(-250,75)
       self.draw.pendown()
       self.draw.goto(250, 75)
       self.draw.penup()
       self.draw.goto(-250, -75)
       self.draw.pendown()
       self.draw.goto(250,-75)
       self.draw.ht()
       self.spots = {1: [None,(-250,200)], 2: [None,(0,200)], 3: [None,(250,200)], 4: [None,(-250,0)], 5: [None,(0,0)], 6: [None,(250,0)], 7: [None,(-250,-250)], 8: [None,(0,-250)], 9: [None,(250,-250)]}

   def checkWinner(self, player):
       if (self.spots[1][0]==player.name and self.spots[2][0]==player.name and self.spots[3][0]==player.name) or (self.spots[4][0]==player.name and self.spots[5][0]==player.name and self.spots[6][0]==player.name) or (self.spots[7][0]==player.name and self.spots[8][0]==player.name and self.spots[9][0]==player.name):
           return player.name
       if (self.spots[1][0]==player.name and self.spots[4][0]==player.name and self.spots[7][0]==player.name) or (self.spots[2][0]==player.name and self.spots[5][0]==player.name and self.spots[8][0]==player.name) or (self.spots[3][0]==player.name and self.spots[6][0]==player.name and self.spots[9][0]==player.name):
           return player.name
       if (self.spots[1][0]==player.name and self.spots[5][0]==player.name and self.spots[9][0]==player.name) or (self.spots[3][0]==player.name and self.spots[5][0]==player.name and self.spots[7][0]==player.name):
           return player.name


class Player:
   def __init__(self):
       self.name = input("Enter your name: ")
       self.pen = turtle.Turtle()
       self.pen.penup()
       self.symbol = input("Enter symbol: ")

   def makeMove(self, boardobj):
       condition = True
       while condition:
           userBox = int(input("Choose box number: "))
           if boardobj.spots[userBox][0] is None:
               boardobj.spots[userBox][0] = self.name
               self.pen.goto(boardobj.spots[userBox][1])
               self.pen.write(self.symbol)
               condition = False
           else:
               print("That's been chosen already! Try again!")


def main():
   board = Board()
   p1 = Player()
   p2 = Player()
   game = True
   while game:
       p1.makeMove(board)
       status = board.checkWinner(p1)

       if status == p1.name:
           game = False
           print(p1.name, “has won")

       else:
           p2.makeMove(board)
           status = board.checkWinner(p2)

           if status == p2.name:
               game = False
               print(p2.name, “has won")

main()
