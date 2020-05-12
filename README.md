This is an old project. Check out my more recent cellular automata project here: https://github.com/ImanariRoll/cellular-automata

# GameOfLife

GameOfLife members:

__init__(rows, columns)

	rows (int)
	columns (int)
	allNodes (set)
	liveNodes (set)
	activeNodes (set)
	grid (2d array)

		Node (class)

			__init__(x, y)
				alive (boolean)
				aliveNext (boolean)
				adjacent (set)
				x (int)
				y (int)

			calcNext() -> boolean 
				Calculates the next live value for the node and returns it.

	Create nodes and links

	simulate(num_games, num_evos) -> list of 3d arrays
		Runs lots of num_games games with num_evos time steps.
		Returns list of 3d arrays of game histories.

	runGame(num_evos) -> 3d array
		Runs a game with num_evos time steps and returns 3d array
	
	randomize()
		Clears liveNodes and activeNodes.
		Randomizes the live values of the nodes.

	evolveBoard()
		Evolves the state of the board.
			Calculates .aliveNext values from .alive values.
			Create addSet of points to add to activeNodes.
			Create removeSet of points to remove from activeNodes.
			Update liveNodes and activeNodes with set operations.

	

