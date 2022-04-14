print("welcome to my quiz!")
print("\n")
input("Press enter to continue!")
print("\n")
name = input ("what is you username?:")
print("\n")
print("welcome to my quiz!", name)
print("\n")
print("About the quiz: My quiz is abut videogames tip dont type out the option instead type out the letter in lowercase enjoy!")
print("\n")
input("Press enter to continue!")
print("\n")
n_questions ={'1.What is the best selling videogame of all time? \n a.Minecraft\n b.call Of Duty Black Ops\n c.Grand Theft Auto 5\n Answer:' : 'a' , '\n 2.What is the name of the final course of all mario kart video games? \na.ghost valleys\nb. bowsers castle\nc.rainbow Road \n answer: ' : 'c', '\n 3.Solid Snake is the hero of the famous video game franchise? \na.Gears of war\nb.The Metal Gear\nc.COD Ghosts\n answer:' : 'b', '\n 4.Which famous video game franchise is the game V-Bucks from? \na.Valorant\nb.Fortnite\nc.RDR2\n answer:' : 'b' , '\n 5.Who is the first character you play in Injustice 2?\na.Batman\nb.superman\nc.Green Lantern\n answer:' : 'a', '\n 6.Fight Night 2004 is a game about what kind of sport?\na.boxing\nb.mma\nc.karate\n answer:' : 'a', '\n 7.Piemonte Calcio represents which real life club in the FIFA 20 video game?\na.real madrid\nb.man united\nc.juventus\n answer:' : 'c', '\n 8.In which game do players compete in the future version of soccer with cars?\na.forza\nb.rocket leugue\nc.asetto corsa\n answer:' : 'b','\n 9.What is the highest grossing game of all time?\na.Pokémon\nb.Tetris\nc.street fighter\n answer: ' : 'a', '\n 10.Whos on the cover of the video game Madden NFL 18?\na.lebron james\nb.OBJ\nc.tom brady\n answer:' : 'c'}  
score = 0

for n in n_questions.keys():
  user_answer = input(n)
  if n_questions.get(n) == user_answer:
    score+= 1
    print("Correct")
    print("score:", score )
  else:
    print("incorrect, The answer was:",n_questions.get(n))
    print("score: " ,score)
    print("\n")
print('Thank you for playing my quiz!!!')    