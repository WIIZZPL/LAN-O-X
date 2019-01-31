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
		clear()
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
		print(" #",self.getSquare(1),"#",self.getSquare(2),"#",self.getSquare(3),"# ")
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

	def getParamethers(self):
		r = ""
		for i in self.matrix:
			for j in i:
				r += str(j)
		r += self.turn
		return r

	def setParamethers(self, Paramethers):
		self.matrix = [list(Paramethers[0:3]),list(Paramethers[3:6]),list(Paramethers[6:9])]
		self.turn = Paramethers[-1]

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
		LAN = LAN.split(".")
		IP = LAN[0]+"."+LAN[1]+"."+LAN[2]+"."
		LAN = LAN[3]
		s = socket()
		s.bind(("", 6861))
		gra = kratka()
		print("Adress LAN:",LAN)
		print("Oczekiwanie na przeciwnika...")
		s.listen(1)
		c, RHOST = s.accept()
		znak = "OX"[randint(0,1)]
		gra.show()
		while True:
			if znak == "X":
				c.send("t".encode())
				gra.setParamethers(c.recv(4089).decode())
			while gra.checkWin() == "NONE":
				x = int(input(">>> "))
				gra.setSquare(x)
				gra.show()
				c.send((gra.getParamethers()).encode())
				if gra.checkWin() != "NONE":
					break
				print("Róch przeciwnika...")
				gra.setParamethers(c.recv(4089).decode())
				gra.show()
			gra.show()
			print(gra.checkWin(), "wygrywa!")
			print("")
			rtr = input("Jeszcze raz? y/n >>> ")
			if rtr == "y":
				c.send("y".encode())
			else:
				c.send("n".encode())
				break
			if c.recv(4096).decode() == "n":
				break
			gra.restart()
			gra.show()

	if inp == "2":
		LAN = gethostbyname(gethostname())
		IP = ""
		LAN = LAN.split(".")
		IP = LAN[0]+"."+LAN[1]+"."+LAN[2]+"."
		LAN = str(input("Adress LAN serwera >>> "))
		s = socket()
		s.connect((IP+LAN,6861))
		gra = kratka()
		gra.show()
		while True:
			data = s.recv(4096).decode()
			if data != "t":
				gra.setParamethers(data)
			gra.show()
			while gra.checkWin() == "NONE":
				x = int(input(">>> "))
				gra.setSquare(x)
				gra.show()
				s.send((gra.getParamethers()).encode())
				if gra.checkWin() != "NONE":
					break
				print("Róch przeciwnika...")
				gra.setParamethers(s.recv(4089).decode())
				gra.show()
			gra.show()
			print(gra.checkWin(), "wygrywa!")
			print("")
			rtr = input("Jeszcze raz? y/n >>> ")
			if rtr == "y":
				s.send("y".encode())
			else:
				s.send("n".encode())
				break
			if s.recv(4096).decode() == "n":
				break
			gra.restart()
			gra.show()