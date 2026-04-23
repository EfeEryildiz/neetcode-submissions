class Graph:
    
    def __init__(self):
        self.graph = {}

    def addEdge(self, src: int, dst: int) -> None:
        if src not in self.graph:
            self.graph[src] = []
        if dst not in self.graph:
            self.graph[dst] = []
        if dst not in self.graph[src]:
            self.graph[src].append(dst)

    def removeEdge(self, src: int, dst: int) -> bool:
        if src not in self.graph:
            return False
        if dst in self.graph[src]:
            self.graph[src].remove(dst)
            return True
        else:
            return False

    def hasPath(self, src: int, dst: int, visit: set = None) -> bool:
        if visit is None:
            visit = set()
        if src == dst:
            return True
        if src in visit:
            return False
        visit.add(src)
        for neighbor in self.graph[src]:
            if self.hasPath(neighbor, dst, visit):
                return True
        return False
