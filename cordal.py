from collections import defaultdict
import networkx as nx

grafos = nx.DiGraph()
grafos.add_nodes_from(['A','B','C','D','E'])
grafos.add_edges_from([('A','B'), ('B','C'), ('C','D'),('D','E'),('E','A')])
#edges = [('A','B'), ('B','C'), ('C','D'),('D','E'),('E','A'), ('A','D')]

ciclos = list(nx.simple_cycles(grafos))
ciclos.sort(key=len)
cordaisCiclo = False
for ciclo in ciclos:
	if len(ciclo) == 3:
		print("O ciclo ",ciclo,"tem tamanho 3, logo é um ciclo induzido. Não define cordalidade ao grafo.")
	else:
		for vertice in ciclo:
			for v in grafos.nodes:
				if(vertice != v and vertice not in grafos.neighbors(v) and v not in grafos.neighbors(vertice) and (grafos.has_edge(vertice,v) or grafos.has_edge(v,vertice))):
					print("A aresta (",vertice,",",v,") não faz parte do ciclo, porém conecta dois vértices do ciclo ",ciclo,".")
					cordaisCiclo = True
					break
			break
		if cordaisCiclo == False:
			print("O ciclo ",ciclo," não possui uma corda. Ou seja, o grafo não é cordal!")
			break
