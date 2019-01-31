from socket import *
from random import randint

class kratka():

	def __init__(self):
		self.matrix = [[7,8,9],[4,5,6],[1,2,3]]
		self.turn = "O"

	def restart(self):
		self.matrix = [[7,8,9],[4,5,6],[1,2,3]]
		self.turn = "O"

	def number2y(self, a):
		if a > 6:
			return 0
		if a > 3:
			return 1
		else:
			return 2

	def number2x(self, a):
		if a in [7,4,1]:
			return 0
		if a in [8,5,2]:
			return 1
		else:
			return 2

	def setSquare(self, a):
		self.matrix[self.number2y(a)][self.number2x(a)] = self.turn
		if self.turn == "O":
			self.turn = "X"
		else:
			self.turn = "O"

	def getSquare(self, a):
		return self.matrix[self.number2y(a)][self.number2x(a)]

	def show(self):
		print("               ")
		print(" ############# ")
		print(" #   #   #   # ")
		print(" #",self.getSquare(7),"#",self.getSquare(8),"#",self.getSquare(9),"# ")
		print(" #   #   #   # ")
		print(" ############# ")
		print(" #   #   #   # ")
		print(" #",self.getSquare(4),"#",self.getSquare(5),"#",self.getSquare(6),"# ")
		print(" #   #   #   # ")
		print(" ############# ")
		print(" #   #   #   # ")
		print(" #",self.getSquare(1),"#",self.getSquare(2),"#",self.getSquare(2),"# ")
		print(" #   #   #   # ")
		print(" ############# ")
		print("               ")

	def checkWin(self):
		for i in range(3):
			if self.getSquare(1+3*i) == self.getSquare(2+3*i) == self.getSquare(3+3*i):
				return self.getSquare(1+3*i)
			if self.getSquare(1+i) == self.getSquare(4+i) == self.getSquare(7+i):
				return self.getSquare(1+i)
		if self.getSquare(7) == self.getSquare(5) == self.getSquare(3):
			return self.getSquare(5)
		if self.getSquare(1) == self.getSquare(5) == self.getSquare(9):
			return self.getSquare(5)
		return "NONE"

def banner():
	print(r"__/\\\_________________/\\\\\\\\\_____/\\\\\_____/\\\_________________/\\\\\_____________________/\\\__/\\\_______/\\\_________")
	print(r"__\/\\\_______________/\\\\\\\\\\\\\__\/\\\\\\___\/\\\_______________/\\\///\\\_________________/\\\/__\///\\\___/\\\/_________")    
	print(r"___\/\\\______________/\\\/////////\\\_\/\\\/\\\__\/\\\_____________/\\\/__\///\\\_____________/\\\/______\///\\\\\\/__________")
	print(r"____\/\\\_____________\/\\\_______\/\\\_\/\\\//\\\_\/\\\____________/\\\______\//\\\__________/\\\/__________\//\\\\___________")  
	print(r"_____\/\\\_____________\/\\\\\\\\\\\\\\\_\/\\\\//\\\\/\\\___________\/\\\_______\/\\\________/\\\/_____________\/\\\\__________")    
	print(r"______\/\\\_____________\/\\\/////////\\\_\/\\\_\//\\\/\\\___________\//\\\______/\\\_______/\\\/_______________/\\\\\\________")   
	print(r"_______\/\\\_____________\/\\\_______\/\\\_\/\\\__\//\\\\\\____________\///\\\__/\\\_______/\\\/_______________/\\\////\\\_____")  
	print(r"________\/\\\\\\\\\\\\\\\_\/\\\_______\/\\\_\/\\\___\//\\\\\______________\///\\\\\/______/\\\/_______________/\\\/___\///\\\__") 
	print(r"_________\///////////////__\///________\///__\///_____\/////_________________\/////_______\///________________\///_______\///__")

def clear():
	for i in range(100):
		print()

while True:
	clear()
	banner()
	print("")
	print("1 - Hostuj")
	print("2 - Dołącz")
	print("E - Wyjście")
	print("")
	inp = input(">>> ")
	if inp == "E":
		clear()
		break
	if inp == "1":
		LAN = gethostbyname(gethostname())
		IP = ""
		LAN.split(".")
		IP = LAN[0]+"."+LAN[1]+"."+LAN[2]+"."
		LAN = LAN[3]
		s = socket()
		s.bind(("", 6861))
		gra = kratka()
		print("Adress LAN:",LAN)
		print("Oczekiwanie na przeciwnika...")
		s.listen(1)
		CONN, RHOST = s.accept()
		print(RHOST)
		print(CONN)
		while s.recv(4096).decode() == "y":
			znak = "OX"[randint()%2]
			while gra.checkWin() == "NONE":
				pass
			gra.show()
			print(gra.checkWin(), "wygrywa!")
			print("")
			rtr = input("Jeszcze raz? y/n >>> ")
			if rtr == "y":
				s.send("y".encode())
			else:
				s.send("n".encode())