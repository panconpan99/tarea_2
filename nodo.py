class nodo_estado:
    def __init__(self, V, EP, A, N):
        self.valor = V
        self.padre = EP
        self.accion = A
        self.nivel = N
        self.distancia=None

    def get_valor(self):
        return self.valor

    def get_nivel(self):
        return self.nivel

    def get_accion(self):
        return self.accion
    
    def set_distancia(self, d):
        self.distancia = d

    def get_distancia(self):
        return self.distancia


    def get_padre(self):
        return self.padre
    
    def __eq__(self, n):
        return self.valor == n