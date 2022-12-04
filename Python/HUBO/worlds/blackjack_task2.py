#
# Blackjack Game, graphics version
#

import random
import time
import sys
from cs1graphics import *

### 1. FACES and SUITS list 작성 (완료)
FACES = list(range(2,11)) + ['Jack','Queen','King','Ace']
SUITS = ['Clubs', 'Diamond', 'Hearts', 'Spades']

CARD_SIZE = (40, 80)
RADIUS = 3




class Card:
  """A card has a face and suit."""

  def __init__(self, face, suit):
    ### 2.  assert를 사용해서 face와 suit가 FACES와 SUITS에서만 뽑히도록 하고, face suit attribute 작성 (완료)
    assert face in FACES and suit in SUITS
    self.face = face
    self.suit = suit
    self.graphics = None
  
  

  def __str__(self):
    article = "a "
    if self.face in [8, "Ace"]: 
      article = "an "
    ### 3.  an 8 of diamond, a Queen of spade 같은 꼴의 str 리턴 (완료)
    return (article + str(self.face) + " of " + self.suit)

  def value(self):
    """Returns the face value of the card."""
    ### 4. J Q K는 10, A는 11 리턴 (완료)
    if type(self.face) == int:
      return self.face
    elif self.face == "Ace":
      return 11
    else:
      return 10


# --------------------------------------------------------------------

def create_clubs(symbol):
  """Create clubs on layer symbol."""
  circle1 = Circle(RADIUS, Point(0, -RADIUS))
  circle1.setFillColor('black')
  circle1.setBorderWidth(0)
  symbol.add(circle1)
            
  circle2 = Circle(RADIUS, Point(-RADIUS, 0))
  circle2.setFillColor('black')
  circle2.setBorderWidth(0)
  symbol.add(circle2)
    
  circle3 = Circle(RADIUS, Point(RADIUS, 0))
  circle3.setFillColor('black')
  circle3.setBorderWidth(0)
  symbol.add(circle3)
  
  triangle = Polygon(Point(0, 0), 
                     Point(-RADIUS*2, RADIUS*3), 
                     Point(RADIUS*2, RADIUS*3))
  triangle.setFillColor('black')
  triangle.setBorderWidth(0)
  symbol.add(triangle)
  
def create_diamonds(symbol):            
  ## 5. create diamonds
  circle1 = Circle(RADIUS, Point(0, -RADIUS))
  circle1.setFillColor('black')
  circle1.setBorderWidth(0)
  symbol.add(circle1)
            
  circle2 = Circle(RADIUS, Point(-RADIUS, 0))
  circle2.setFillColor('black')
  circle2.setBorderWidth(0)
  symbol.add(circle2)
    
  circle3 = Circle(RADIUS, Point(RADIUS, 0))
  circle3.setFillColor('black')
  circle3.setBorderWidth(0)
  symbol.add(circle3)
  
  triangle = Polygon(Point(0, 0), 
                     Point(-RADIUS*2, RADIUS*3), 
                     Point(RADIUS*2, RADIUS*3))
  triangle.setFillColor('black')
  triangle.setBorderWidth(0)
  symbol.add(triangle)
        
def create_hearts(symbol):
  ## 6. create hearts
  circle1 = Circle(RADIUS, Point(0, -RADIUS))
  circle1.setFillColor('black')
  circle1.setBorderWidth(0)
  symbol.add(circle1)
            
  circle2 = Circle(RADIUS, Point(-RADIUS, 0))
  circle2.setFillColor('black')
  circle2.setBorderWidth(0)
  symbol.add(circle2)
    
  circle3 = Circle(RADIUS, Point(RADIUS, 0))
  circle3.setFillColor('black')
  circle3.setBorderWidth(0)
  symbol.add(circle3)
  
  triangle = Polygon(Point(0, 0), 
                     Point(-RADIUS*2, RADIUS*3), 
                     Point(RADIUS*2, RADIUS*3))
  triangle.setFillColor('black')
  triangle.setBorderWidth(0)
  symbol.add(triangle)

def create_spades(symbol):        
  ## 7. create spades
  circle1 = Circle(RADIUS, Point(0, -RADIUS))
  circle1.setFillColor('black')
  circle1.setBorderWidth(0)
  symbol.add(circle1)
            
  circle2 = Circle(RADIUS, Point(-RADIUS, 0))
  circle2.setFillColor('black')
  circle2.setBorderWidth(0)
  symbol.add(circle2)
    
  circle3 = Circle(RADIUS, Point(RADIUS, 0))
  circle3.setFillColor('black')
  circle3.setBorderWidth(0)
  symbol.add(circle3)
  
  triangle = Polygon(Point(0, 0), 
                     Point(-RADIUS*2, RADIUS*3), 
                     Point(RADIUS*2, RADIUS*3))
  triangle.setFillColor('black')
  triangle.setBorderWidth(0)
  symbol.add(triangle)

# --------------------------------------------------------------------



class CardGraphics(object):
  """Graphical representation of a card."""
  
  def __init__(self, card, hidden = False):
    self.l = Layer()       ##card graphic

    # background of card
    self.bg = Rectangle(CARD_SIZE[0], CARD_SIZE[1])
    if hidden:
      self.bg.setDepth(0)
      self.bg.setFillColor('gray')
    else:
      self.bg.setDepth(100)
      self.bg.setFillColor('white')
    self.l.add(self.bg)
    
    # 8. symbol for center, card suit에 맞는 symbol layer을 만들어서 self.l에 add하기




    # text for left-top and right-bottom
    if card.suit in ['Diamonds', 'Hearts']:
      color = 'red'
    else:
      color = 'black'

    if type(card.face) == int:
      num = str(card.face)
    else:
      num = card.face[0]
    
    # left-top text
    lt_num = Text()
    lt_num.setMessage(num)
    lt_num.setFontColor(color)
    lt_num_dim = lt_num.getDimensions()
    lt_num.moveTo(-CARD_SIZE[0]/2 + lt_num_dim[0]/2, 
                   -CARD_SIZE[1]/2 + lt_num_dim[1]/2)
    self.l.add(lt_num)
        
    # 9. right-bottom text 작성하시오

  def show(self):
    self.bg.setDepth(100)
    self.bg.setFillColor('white')
    
# --------------------------------------------------------------------

class Deck(object):
  """A deck of cards."""
  def __init__(self):
    """Create a deck of 52 cards and shuffle them."""
    ### 10. 52개의 카드를 만들고 random module을 사용, 섞으시오 (완료)
    self.cards = []
    for suit in SUITS:
      for face in FACES:
        self.cards.append(Card(face, suit))
    random.shuffle(self.cards)


  def draw(self):
    """Draw the top card from the deck."""
    return self.cards.pop()

#---------------------------------------------------------------------
class Hand(object):                    ########## 테이블에서 보여지는 카드들 (player 별로)
  """A hand of cards displayed on a table."""

  def __init__(self, x, y, canvas):
    """Create an empty hand displayed at indicated position on canvas."""
    self.canvas = canvas
    self.x = x
    self.y = y
    self.graphics = []
    self.hand = []

  def add(self, card, hidden = False):
    """Add a new card to the hand."""
    # 11. ((((녹))))
    # hand에 card를 append 하시오  
    # card에 해당하는 graphic을 만드시오
    # graphic을 self.x + CARD_SIZE[0] * 2 * len(self.graphics), self.y 으로 이동시키시오  
    # canvas에 그래픽을 추가하시오
    # graphics list에 해당 그래픽을 append하시오



  def clear(self):
    """Make hand empty."""
    for item in self.graphics:
      self.canvas.remove(item.l)
    self.graphics = []
    self.hand = []


  def show(self):
    """Make all cards visible."""
    ## 12. 모든 그래픽을 보이게 하시오 //딜러카드 히든, 힌트 : 뎁스 사용

  def value(self):
    """Return value of the hand."""
    ## 13. total value를 반환하시오
# --------------------------------------------------------------------

class Table(object):
  """A graphical Blackjack table for playing Blackjack."""
  
  def __init__(self):
    self.canvas = Canvas(600, 400, 'dark green', 'Black Jack 101')
    ## 14.
    ## self.player 이름의 Hand를 CARD_SIZE[0], CARD_SIZE[1]에 만드시오 // 핸드 오브젝트 만들라?
    ## self.dealer 이름의 Hand를 CARD_SIZE[0], 3 * CARD_SIZE[1]에 만드시오




    self.score = [ Text(), Text() ]
    for i in range(2):
      self.score[i].setFontColor('white')
      self.score[i].setFontSize(20)
      self.score[i].moveTo(self.canvas.getWidth() - CARD_SIZE[0], CARD_SIZE[1])
      self.canvas.add(self.score[i])
    self.score[1].move(0, 2 * CARD_SIZE[1])



    self.message = Text()
    self.message.setFontColor('red')
    self.message.setFontSize(20)
    dim = self.message.getDimensions()
    self.message.moveTo(self.canvas.getWidth() / 2 - dim[0] / 2, 
                        self.canvas.getHeight() - 80)
    self.canvas.add(self.message)

    self.question = Text()
    self.question.setFontColor('white')
    self.question.setFontSize(20)
    dim = self.question.getDimensions()
    self.question.moveTo(self.canvas.getWidth() / 2 - dim[0] / 2, 
                        self.canvas.getHeight() - 40)
    self.canvas.add(self.question)




  def clear(self):
    """Clear everything on the table."""
    ## 15. player, dealer hand clear하고(핸드오브젝트 클리어 적용하라는것), message, question, score를 setMessage("") method 적용



  #def set_score(self, which, text):
    ## 16. score[which]에 text를 setmessage하시오
    
  #def show_message(self, text):
    ## 17. message에 text를 setmessage하시오
    


  def ask(self, prompt):
    ## propmpt를 띄우고, user의 반응에 따라 action // 이해하라고 적어놓은 것
    self.question.setMessage(prompt)
    while True:
      e = self.canvas.wait()
      d = e.getDescription()
      if d == "canvas close":
        sys.exit(1)
      if d == "keyboard":
        key = e.getKey() 
        if key == 'y':
          self.question.setMessage("")
          return True
        if key == 'n':
          self.question.setMessage("")
          return False
  
  def close(self):
    """Close the table to end playing."""
    self.canvas.close()


#---------------------------------------------------------------------

def blackjack(table):
  """Play one round of Blackjack.
  Returns 1 if player wins, -1 if dealer wins, and 0 for a tie."""
  

  ##################### 블랙잭 한번의 라운드, player가 이기면 1을 반환, 딜러가 이기면 -1, 비기면 0 반환


  deck = Deck()
  # 18.
  # player의 hand에 한장 추가, dealer에 한장 추가 (hidden)
  # player의 hand에 한장 추가, dealer에 한장 추가
  # player의 점수를 set_score하시오 
  


  # 19. // 객체들이 달라졌으니 활용이 조금 달라질 것이다.
  # player's turn to draw cards
  # 플레이어의 total value가 21보다 작으면 "Would you like another card?" 을 물어보고, n이면 딜러 턴으로 넘어가고 
  # y이면 한장 더 주기
  # 플레이어의 score를 set해줘야함 
  # 플레이어의 카드값이 21보다 크면 "You went over 21! You lost!"를 show하고 경기 끝  
  # 플레이어가 카드를 더이상 받지 않으면, dealer의 hidden card를 보여주고 dealer의 score를 set 함
  # dealer의 value가 17보다 작으면 더 뽑고, score를 set 해줌






  # 20.
  # player의 total 점수와, dealer의 total 점수를 set 해주고 
  # "your total is 13"
  # "The dealer's total is 20"
  # 플레이어와 딜러의 점수에 따라, 
  # "You win!" set하고 1 반환 혹은
  # "The dealer went over 21! You win!" set하고 1 반환 혹은
  # "You lost" set하고 -1 반환 혹은
  # "You have a tie" 를 set하고, 0 반환

# --------------------------------------------------------------------

def game_loop():
  table = Table()
  while True:
    blackjack(table)    
    if not table.ask("Another round?"):
      break    
    table.clear()
  table.close()

game_loop()
