print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

print("Bem Vindo a aventura, escolha:")
direcao = input("Vamos começar a aventura, escolha 'esquerda ou 'direita' ?")
direcao = direcao.lower()
if direcao == "esquerda":
  nadar_esperar = input("Chegamos em um rio, a balsa vai demorar 8 horas. Deseja 'nadar ou 'esperar' ?")
  nadar_esperar = nadar_esperar.lower()
  if nadar_esperar == "esperar":
    porta = input("Você esperou a balsa e atravessou seguro, chegando ao outro lado encontra a entrada da caverna de tessouros, porem existem 3 portas. Qual porta deseja acessar: 'vermelha' ou 'verde' ou 'azul'")
    porta = porta.lower()
    if porta  == "verde":
      print("Parabéns você ganhou o premio")
    elif porta =="vermelha":
      print("Você abriu a porta vermelha, acionou a armadilha e do chão começa a subir lava, você morreu queimado")
    elif porta =="azul":
      print("Você abriu a porta azul, acionando a armadilha e um a caverna começa a de preencher de agua, você morrou afogado")
    else:
      print("Você errou a porta e a armadilha foi acionada, a caverna desmorona e você morreu soterrado")
  else:
    print("O Rio era fundo, você se afogou e morreu")
else:
  print("Começou mal, caiu no buraco e morreu")