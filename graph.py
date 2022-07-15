import itertools
import numpy as np
import itertools

class TornamentGraph:
    def __init__(self, num_nodes,):
        self.num_nodes = num_nodes
        self.V = list(range(num_nodes))
        self.edges = [ tuple(e) for e in itertools.product(self.V, self.V) if e[0] < e[1]]
    
    def polymophism(self, arity):
        Vk = list(itertools.product(self.V, repeat=arity))
        Ak = np.array([])
        for i in range(len(Vk)):
            for j in range(len(Vk)):
                for k in range(arity):
                    if not self.exists_edges((Vk[i][k], Vk[i][k])):
                        break
                Vk.append([Vk[i], Vk[j]])
        return Vk, Ak
    
    def exists_edges(self, edge):
        return edge in self.edges
    
if __name__ == "__main__":
    t = TornamentGraph(3)
    # V, A = t.polymophism(3)
    # print(A)