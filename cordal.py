from collections import defaultdict

class Grafo():

	def __init__(self, arestas):
		self._grafo = defaultdict(set)
		self.adicionaArestas(arestas)
	#main functions
	def vizinhos(self,v):
		return self._grafo[v]

	def getVertices(self):
		return list(self._grafo.keys())

	def getArestas(self):
		return [(u,v) for k in self._grafo.keys() for v in self._grafo[k]]

	#support functions
	def adicionaArestas(self,arestas):
		for u,v in arestas:
			self._grafo[u].add(v)
			self._grafo[v].add(u)

	def existeAresta(self,u,v):
		return u in self._grafo and v in self._grafo
	
	def verificarCiclos(self, vOrigem):
		vVisitados = set()
		vRestantes = [vOrigem]	#lista de vertices a percorrer

		while vRestantes:#dfs
			vAtual = vRestantes.pop()
			vVisitados.add(vAtual)

			for vizinho in self.vizinhos(vAtual):
				if vizinho in vVisitados:
					return True	#achou um vertice já visitado, ou seja, ciclo

				vRestantes.append(vizinho)

		return False


edges = [('A','B'), ('B','C'), ('C','D'),('D','E'),('E','A')]
#edges = [('A','B'), ('B','C'), ('C','D'),('D','E'),('E','A'), ('A','D')]
grafo = Grafo(edges)

if grafo.verificarCiclos('A'):
	print('Encontrou um ciclo!\n', grafo._grafo)
else:
	print('Não encontrou um ciclo.')