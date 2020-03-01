'''
Game of Life simmulator

Creates random simmulations of Conway's Game of Life for exploratory data analysis
02/09/2020
Brandon Spicer

''' 

import time
import random
import arcade
import numpy as np
import matplotlib.pyplot as plt
from itertools import product

# Write simulate, runGame methods
# Write animate method
# Write naive version and compare

class GameOfLife:
	def __init__(self, rows, columns):
		self.rows = rows
		self.columns = columns
		self.allNodes = set()
		self.liveNodes = set()
		self.activeNodes = set()
		self.grid = np.array([[None] * columns for _ in range(rows)])
		
		# create node class
		class Node:
			def __init__(self, x, y):
				self.alive = False
				self.aliveNext = False
				self.adjacent = set()
				self.x = x
				self.y = y

			def calcNext(self):
				liveAdj = 0
				for node in self.adjacent:
					liveAdj += node.alive
				
				if self.alive:
					return 2 <= liveAdj <= 3
				else:
					return liveAdj == 3

		# create nodes
		for i, j in product(range(self.rows), range(self.columns)):
			self.grid[i][j] = Node(i, j)
			self.allNodes.add(self.grid[i][j])

		# create links between nodes
		for i, j in product(range(self.rows), range(self.columns)):
			for k, l in product((-1, 0, 1), (-1, 0, 1)):
				if not k == l == 0:
					self.grid[i][j].adjacent.add(self.grid[(i + k) % self.rows][(j + l) % self.columns])

	# run num_games simmulations with num_evos cycles
	def simulate(self, num_games, num_evos):
		history = []
		for i in range(num_games):
			game = self.runGame(num_evos)
			history.append(game)

		return history

	# run one game with num_evos cycles
	def runGame(self, num_evos, printBoard=False):
		memory = []
		self.randomize()
		for i in range(num_evos):
			memory.append([[int(node.alive) for node in row] for row in self.grid])
			if printBoard:
				self.printBoard()
			self.evolveBoard()

		return memory

	# create random starting grid
	def randomize(self):
		self.liveNodes.clear()
		self.activeNodes.clear()
		for node in self.allNodes:
			node.alive = random.randint(0, 1) * random.randint(0, 1)
			if node.alive:
				self.liveNodes.add(node)
				self.activeNodes.add(node)
				for adj in node.adjacent:
					self.activeNodes.add(adj)

	# print the current board to the terminal
	def printBoard(self):
		for row in self.grid:
			for node in row:
				if node.alive:
					print('*', end='')
				else:
					print(' ', end='')
			print()
			
	# evolve the state of the board
	def evolveBoard(self):
		for node in self.activeNodes:
			node.aliveNext = node.calcNext()

		for node in self.activeNodes:
			node.alive = node.aliveNext

		addSet = set()
		removeSet = set()
		for node in self.activeNodes:
			if node.alive:
				self.liveNodes.add(node)
				for adj in node.adjacent:
					addSet.add(adj)
			else:
				if node in self.liveNodes:
					self.liveNodes.remove(node)
				if [adj.alive for adj in node.adjacent] == [False] * 8:
					removeSet.add(node)

		self.activeNodes = (self.activeNodes | addSet) - removeSet


