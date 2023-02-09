import sys

class Graph():
	def __init__(self, vertices, graph):
		self.V = vertices
		self.graph = graph

	def printSolution(self, dist):
		print("Vértice  | Distância desde o início")
		for node in range(self.V):
			print(node, "\t |", dist[node])

	# A utility function to find the vertex with
	# minimum distance value, from the set of vertices
	# not yet included in shortest path tree
	def minDistance(self, dist, sptSet):

		# Initialize minimum distance for next node
		min = sys.maxsize

		# Search not nearest vertex not in the
		# shortest path tree
		for u in range(self.V):
			if dist[u] < min and sptSet[u] == False:
				min = dist[u]
				min_index = u

		return min_index

	# Function that implements Dijkstra's single source
	# shortest path algorithm for a graph represented
	# using adjacency matrix representation
	def dijkstra(self, src):

		dist = [sys.maxsize] * self.V # guarda as dist
		dist[src] = 0 # dist do src até ele msm
		sptSet = [False] * self.V

		for cout in range(self.V):

			# Pick the minimum distance vertex from
			# the set of vertices not yet processed.
			# x is always equal to src in first iteration
			x = self.minDistance(dist, sptSet)

			# Put the minimum distance vertex in the
			# shortest path tree
			sptSet[x] = True

			# Update dist value of the adjacent vertices
			# of the picked vertex only if the current
			# distance is greater than new distance and
			# the vertex in not in the shortest path tree
			for y in range(self.V):
				if self.graph[x][y] > 0 and sptSet[y] == False and \
						dist[y] > dist[x] + self.graph[x][y]:
					dist[y] = dist[x] + self.graph[x][y]

		self.printSolution(dist)


# Driver's code
graph = [
    [0,  4, 0,  0,  0,  0, 0,  8, 0],
	[4,  0, 8,  0,  0,  0, 0, 11, 0],
	[0,  8, 0,  7,  0,  4, 0,  0, 2],
	[0,  0, 7,  0,  9, 14, 0,  0, 0],
	[0,  0, 0,  9,  0, 10, 0,  0, 0],
	[0,  0, 4, 14, 10,  0, 2,  0, 0],
	[0,  0, 0,  0,  0,  2, 0,  1, 6],
	[8, 11, 0,  0,  0,  0, 1,  0, 7],
	[0,  0, 2,  0,  0,  0, 6,  7, 0]
]

vertices = len(graph)

g = Graph(vertices, graph)
g.dijkstra(0)

# Código editado a partir do feito por 
# Divyanshu Mehta e atualizado por Pranav Singh Sambyal

# Código por Geeks For Geeks:
# https://www.geeksforgeeks.org/dijkstras-shortest-path-algorithm-greedy-algo-7/
