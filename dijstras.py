class Graph():

	def __init__(self, vertices):
		self.V = vertices
		self.graph = [[0 for column in range(vertices)]
					for row in range(vertices)]

	def printSol(self, dist):
		print("Vertex \tDistance from Source")
		for node in range(self.V):
			print(node, "\t", dist[node])
	
	def printAns(self, dist, src, lst):
		print(f"The distance from node {src} to node {lst} is {dist[lst]}")

	def minD(self, dist, nodeSet):

		# Initialize minimum distance for next node
		min = 1e7

		for v in range(self.V):
			if dist[v] < min and nodeSet[v] == False:
				min = dist[v]
				min_index = v

		return min_index

	def dij(self, src):

		dist = [1e7] * self.V
		dist[src] = 0
		nodeSet = [False] * self.V

		for cout in range(self.V):

			u = self.minD(dist, nodeSet)
			nodeSet[u] = True
			for v in range(self.V):
				if (self.graph[u][v] > 0 and nodeSet[v] == False and dist[v] > dist[u] + self.graph[u][v]):
					dist[v] = dist[u] + self.graph[u][v]

		self.printSol(dist)
		self.printAns(dist, 0, 3)


# Driver program
g = Graph(9)
g.graph = [[0, 6, 0, 0, 0, 0, 0, 12, 0],
		[2, 0, 9, 0, 0, 0, 0, 10, 0],
		[0, 7, 0, 6, 0, 5, 0, 0, 3],
		[0, 0, 8, 0, 10, 15, 0, 0, 0],
		[0, 0, 0, 7, 0, 10, 0, 0, 0],
		[0, 0, 5, 11, 9, 0, 4, 0, 0],
		[0, 0, 0, 0, 0, 3, 0, 1, 5],
		[8, 11, 0, 0, 0, 0, 1, 0, 8],
		[0, 0, 4, 0, 0, 0, 7, 7, 0]
		]

g.dij(0)
#Test
