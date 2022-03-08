import pandas as pd
#Use this to get the 50x50 
df = pd.read_excel('data.xlsx') 
graph = df.values.tolist()
V = len(graph)
INF = 99999

INF = 99999
V=4
def floydWarshall(graph):
	dist = list(map(lambda i: list(map(lambda j: j, i)), graph))

	for k in range(1, V):
		for i in range(1, V):
			for j in range(1, V):
				dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
	printSolution(dist)

def printSolution(dist):
	print ("Shortest distances between every pair of vertices")
	for i in range(V):
		for j in range(V):
			if(dist[i][j] == INF):
				print ("%1s" % ("INF"),end=" ")
			else:
				print ("%1d\t" % (dist[i][j]),end=' ')
			if j == V-1:
				print ()

floydWarshall(graph)
