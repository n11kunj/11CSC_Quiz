#Welcome/Start
def start():
  print("welcome to my quiz!")
  print("\n")
  input("press enter to continue!")
  print("\n")
  while True:
    n = input("enter your username:").strip()
    if n.isalpha():
      print("\n")
      print("welcome to my quiz "+ n)
      break
    else:
      print("\n")
      print("please enter your username with letters only, this is required!")

  print("\n")
  print("this quiz is about videogames tip dont type out the option instead type out the letter in lowercase enjoy!")
  print("\n")
  input("press enter to continue!")
  print("\n")
  
#Dictionary 
def quiz():
  while True:
  
  n_questions ={'1.what is the best selling videogame of all time? \n a.minecraft\n b.call of duty black ops\n c.grand theft auto 5\n Answer:' : 'a' , '\n 2.What is the name of the final course of all mario kart video games? \na.g\ghost valley\nb.bowsers castle\nc.rainbow road \n answer: ' : 'c', '\n 3.solid snake is the hero of the famous video game franchise? \na.gears of war\nb.the metal gear\nc.cod ghosts\n answer:' : 'b', '\n 4.which famous video game franchise is the game v-bucks from?\na.valorant\nb.fortnite\nc.rdr2\n answer:' : 'b' , '\n 5.who is the first character you play in injustice 2?\na.batman\nb.superman\nc.green lantern\n answer:' : 'a', '\n 6.fight night 2004 is a game about what kind of sport?\na.boxing\nb.mma\nc.karate\n answer:' : 'a', '\n 7.piemonte calcio represents which real life club in the fifa 20 video game?\na.real madrid\nb.manchester united\nc.juventus\n answer:' : 'c', '\n 8.in which game do players compete in the future version of soccer with cars?\na.forza horizon\nb.rocket league\nc.asetto corsa\n answer:' : 'b','\n 9.what is the highest grossing game of all time?\na.pokémon\nb.tetris\nc.street fighter\n answer: ' : 'a', '\n 10.whos on the cover of the video game madden nfl 18?\na.lebron james\nb.obj\nc.tom brady\n answer:' : 'c'}  
    p = input()("answer").strip().lower()
    if p.isalpha():
      print("n")
      break
    else:
      print("n")
      print("please input a letter from the following a,b,c in lowercase!")
  score = 0
  
  for n in n_questions.keys():
    user_answer = input(n)
    if n_questions.get(n) == user_answer:
      score+= 1
      print("correct")
      print("score:", score )
    else:
      print("incorrect, the answer was:",n_questions.get(n))
      print("score: " ,score)
      print("\n")
  print('thank you for playing my quiz!!!')   





start()  
quiz()
 