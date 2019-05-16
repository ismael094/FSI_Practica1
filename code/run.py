# Search methods

import search

ab = search.GPSProblem('A', 'B', search.romania)
ck = search.GPSProblem('C', 'Z', search.romania)
at = search.GPSProblem('A', 'T', search.romania)
fu = search.GPSProblem('F', 'U', search.romania)
# print("Búsqueda en anchura")
# print(search.breadth_first_graph_search(ab).path())
# print("===============")
# print("Búsqueda en profundidad")
# print(search.depth_first_graph_search(ab).path())
# print("===============")
print("Búsqueda con ramificación y acotación")
print(search.bab(ab).path())
print("===============")
print("Búsqueda con ramificación y acotación con subestimación")
print(search.babH(ab).path())
# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450
print("===============")
print("Búsqueda con ramificación y acotación")
print(search.bab(ck).path())
print("===============")
print("Búsqueda con ramificación y acotación con subestimación")
print(search.babH(ck).path())

print("===============")
print("Búsqueda con ramificación y acotación")
print(search.bab(at).path())
print("===============")
print("Búsqueda con ramificación y acotación con subestimación")
print(search.babH(at).path())

print("===============")
print("Búsqueda con ramificación y acotación")
print(search.bab(fu).path())
print("===============")
print("Búsqueda con ramificación y acotación con subestimación")
print(search.babH(fu).path())