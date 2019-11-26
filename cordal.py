import psutil
import networkx as nx

grafos = nx.DiGraph()
#grafos.add_nodes_from(['A','B','C','D'])
grafos.add_nodes_from(['A','B','C','D','E'])
#grafos.add_nodes_from(['A','B','C','D','E','F'])
#grafos.add_edges_from([('A','B'), ('A','C'), ('B','C'), ('C','D'), ('B','D')])
#grafos.add_edges_from([('A','B'), ('B','C'), ('C','D'),('D','E'),('E','A')])
#grafos.add_edges_from([('A','B'), ('B','C'), ('C','D'),('D','E'),('E','A'), ('A','D')])
grafos.add_edges_from([('A','B'), ('A','C'), ('B','C'), ('C','E'),('C','D'), ('E','D')])


print(list(nx.find_cycle(grafos, orientation='ignore')))

ciclos = list(nx.simple_cycles(grafos))
ciclos.sort(key=len)
cordaisCiclo = False
arestas = []
edges = []
print("Existem ",len(ciclos)," ciclos.")
for ciclo in ciclos:
	print("CICLO: ",ciclo)
	for edge in range(len(ciclo)):
		if edge == 0:
			primeira = ciclo[0]
			print("primeira aresta: ",primeira)
			x = ciclo[edge]
			continue
		elif len(ciclo) > 3:
			arestas.append((x,ciclo[edge]))
			edges.append((ciclo[edge],x))
			x = ciclo[edge]
	if len(ciclo) >3:
		arestas.append((primeira,x))
		edges.append((x,primeira))

	print(arestas)
	print(edges)
	cordaisCiclo = False
	if len(ciclo) == 3:
		print("O ciclo ",ciclo,"tem tamanho 3, logo é um ciclo induzido. Não define cordalidade ao grafo.")
	else:
		for vertice in ciclo:
			for v in grafos.nodes:
				aux = (vertice,v)
				print(vertice,v)
				if(vertice != v and (v in ciclo and (aux not in arestas and aux not in edges) ) ):
					print("Achou a confição: ",vertice,v)
					if(grafos.has_edge(vertice,v) or grafos.has_edge(v,vertice)):
						print("A aresta (",vertice,",",v,") não faz parte do ciclo, porém conecta dois vértices do ciclo ",ciclo,".")
						cordaisCiclo = True
					break
			if(cordaisCiclo == True):
				break
		if cordaisCiclo == False:
			print("O ciclo ",ciclo," não possui uma corda. Ou seja, o grafo não é cordal!")
			print("Uso da CPU: ",psutil.cpu_percent(),"%")
			exit()
if cordaisCiclo != False:
	print("O grafo é cordal!")
else:
	print("O grafo não é cordal!")
print("Uso da CPU: ",psutil.cpu_percent(),"%")