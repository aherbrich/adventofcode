from collections import defaultdict

class Solution:
    def readFile(self, filename):
        graph = defaultdict(list)
        
        for line in open(filename):
            line = line.strip()
            parts = line.strip().split('-')
            graph[parts[0]].append(parts[1])
            graph[parts[1]].append(parts[0])
            
        return graph
            

    def solution1(self, filename):
        graph = self.readFile(filename)
        
        cliques = set()
        for node in graph:
            neighbors = graph[node]
            for n1 in neighbors:
                for n2 in neighbors:
                    if n1 == n2:
                        continue
                    
                    if node[0] != 't' and n1[0] != 't' and n2[0] != 't':
                        continue
                    
                    if n1 in graph[n2]:
                        clique = sorted([node, n1, n2])
                        cliques.add(tuple(clique))
                        
        return len(cliques)
    
    def solution2(self, filename):
        graph = self.readFile(filename)
        
        P = set(graph.keys())
        R = set()
        X = set()
        
        def bronKerbosch(R, P, X):
            if len(P) == 0 and len(X) == 0:
                return [R]
            
            res = []
            for node in P:
                res.extend(bronKerbosch(R.union([node]), P.intersection(graph[node]), X.intersection(graph[node])))
                P = P.difference([node])
                X = X.union([node])
            
            return res
        
        cliques = bronKerbosch(R, P, X)
        
        # sort cliques by length
        cliques.sort(key=lambda x: len(x), reverse=True)
        
        max_clique = cliques[0]
        
        return ",".join(sorted(max_clique))
    
print(Solution().solution1("/Users/aherbrich/src/myprojects/adventofcode24/2024/day23/input.txt"))
print(Solution().solution2("/Users/aherbrich/src/myprojects/adventofcode24/2024/day23/input.txt"))