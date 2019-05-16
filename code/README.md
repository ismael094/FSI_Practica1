Para implementar la búsqueda de ramificación y acotación se ha añadido un nuevo tipo de lista (Babg), para que cuando insertemos nuevos elementos 
se ordenen los elementos de mayor a menor según el path_cost.

Para implementar la búsqueda de ramificación y acotación con subestimación se ha añadido un nuevo tipo de lista (Babgh), para que cuando insertemos nuevos elementos 
se ordenen los elementos de mayor a menor según la suma del path_cost y la heurística del elemento (del nodo). Para conseguir la heurística tenemos que
pasarle a la cola el problema para que pueda acceder a ella.


Búsqueda con ramificación y acotación

Nodos visitados: 24

[Node B, Node P, Node R, Node S, Node A]

===============

Búsqueda con ramificación y acotación con subestimación

Nodos visitados: 6

[Node B, Node P, Node R, Node S, Node A]

===============

Búsqueda con ramificación y acotación

Nodos visitados: 28

[Node Z, Node A, Node S, Node R, Node C]

===============

Búsqueda con ramificación y acotación con subestimación

Nodos visitados: 11

[Node Z, Node A, Node S, Node R, Node C]

===============

Búsqueda con ramificación y acotación

Nodos visitados: 10

[Node U, Node B, Node F]

===============

Búsqueda con ramificación y acotación con subestimación

Nodos visitados: 3

[Node U, Node B, Node F]
