from nodo import nodo_estado
from collections import deque
import math
mapa=[["0","0","0","0","0","1","1","0","0","0","0"],
    ["1","0","1","1","0","1","0","0","1","1","0"],
    ["1","0","1","0","1","0","1","0","1","0","0"],
    ["1","0","1","0","0","0","1","0","1","0","1"],
    ["0","0","1","0","1","0","0","0","1","0","0"],
    ["0","1","1","0","0","1","1","1","0","1","0"],
    ["0","0","0","0","1","0","0","0","0","0","0"],
    ["0","0","1","0","1","0","1","0","1","1","1"],
    ["1","0","0","0","1","0","0","1","0","0","0"],
    ["1","0","1","0","1","0","0","0","0","1","0"]]

def ordenar_por_heuristica(e):
    return e.get_distancia()


class laberinto:
    

    def __init__(self,EI,EF):
        self.estado_inicial = nodo_estado(EI,None,"inicio",1)
        self.estado_final=[nodo_estado(EF,None,"final",None)]
        self.estado_actual=None
        self.historial=[]
        self.cola=deque()
        self.lab=mapa
        self.solucion=[]
    def es_final(self):
        return self.estado_actual in self.estado_final
    
    def agregar(self, e):
        self.cola.append(e)
        self.historial.append(e)

    def esta_historial(self,e):
        return e in self.historial
    
    def mostrar_estado(self,e):
        if e is not None:
            print("Estado\n")
            print(f"["+str(e.get_valor()[0])+","+ str(e.get_valor()[1])+"]\n")
            x = e.get_valor()
        else:
            print("Estado Actual\n")
            print(f"["+str(self.estado_actual.get_valor()[0])+","+ str(self.estado_actual.get_valor()[1])+"]\n")
            x = self.estado_actual.get_valor()
        sol=self.solucion
        i=0
        for fila in mapa:
            j=0
            texto=""
            for columna in fila:
                pos=[i,j]
                if columna == "1":
                    lugar="1"
                elif pos in sol or pos == x:
                    lugar="+"
                elif columna =="0":
                    lugar="-"
                texto+=lugar
                j+=1
            print(texto)
            i+=1
    
    def buscar_padres(self, e):
        if e.get_padre() == None:
            print(f"\n{e.get_accion()}: Nivel {e.get_nivel()}")
            self.mostrar_estado(e)
        else:
            self.buscar_padres(e.get_padre())
            self.solucion.append(e.get_padre())
            print(f"\n{e.get_accion()}: Nivel {e.get_nivel()}")
            self.mostrar_estado(e)
    
    def mover(self, direccion):
        fila,columna = self.estado_actual.get_valor()
        nueva_coordenada = [fila,columna]

        if direccion == "UP":
            if fila == 0:
                return "illegal"
            else:
                nueva_coordenada[0] = fila - 1
                nueva_coordenada[1] = columna

        elif direccion == "DOWN":
            if fila == len(mapa) - 1:
                return "illegal"
            else:
                nueva_coordenada[0] = fila + 1
                nueva_coordenada[1] = columna
        
        elif direccion == "LEFT":
            if columna == 0:
                return "illegal"
            else:
                nueva_coordenada[0] = fila
                nueva_coordenada[1] = columna - 1

        elif direccion == "RIGHT":
            if columna == len(mapa[0]) - 1:
                return "illegal"
            else:
                nueva_coordenada[0] = fila
                nueva_coordenada[1] = columna + 1

        if mapa[nueva_coordenada[0]][nueva_coordenada[1]] == "1":
            return "illegal"
        else:
            return nueva_coordenada
    
    def algoritmo_anchura(self):
        iteracion = 1
        self.estado_actual = self.estado_inicial
        movimientos = ["UP","DOWN","LEFT","RIGHT"]

        while not self.es_final():
            print("Iteracion: " + str(iteracion) + "\n")
            self.mostrar_estado(None)

            for movimiento in movimientos:
                estado_temporal = nodo_estado(self.mover(movimiento), self.estado_actual, "Mover a " + movimiento, self.estado_actual.get_nivel() + 1)
                if not self.esta_historial(estado_temporal) and not estado_temporal.get_valor() == "illegal":
                    self.agregar(estado_temporal)

            print("\nElementos en Historial: " + str(len(self.historial)) + "\n\nElementos en Cola: " + str(len(self.cola)))
            self.estado_actual = self.cola.popleft()
            iteracion += 1
        print("Iteracion: " + str(iteracion) + "\n")
        self.mostrar_estado(None)
        print("\n\n\nHa llegado a Solucion")
        self.buscar_padres(self.estado_actual)
        print("\nALGORITMO EN ANCHURA:")
        print("\nElementos en Historial: " + str(len(self.historial)) + "\n\nElementos en Cola: " + str(len(self.cola)) + "\n\n Iteraciones: " + str(iteracion))

    def add_profundidad(self, pila_sucesores):
        while pila_sucesores.__len__() > 0:
            e = pila_sucesores.popleft()
            self.historial.append(e)
            self.cola.appendleft(e)
    
    def algoritmo_profundidad(self):
        iteracion = 1
        self.estado_actual = self.estado_inicial
        movimientos = ["UP", "DOWN", "LEFT", "RIGHT"]
        sucesores = deque()

        while not self.es_final():
            print("Iteracion: " + str(iteracion) + "\n")
            self.mostrar_estado(None)

            for movimiento in movimientos:
                estado_temporal = nodo_estado(self.mover(movimiento), self.estado_actual, "Mover a " + movimiento, self.estado_actual.get_nivel() + 1)
                if not self.esta_historial(estado_temporal) and not estado_temporal.get_valor() == "illegal":
                    sucesores.append(estado_temporal)
            
            self.add_profundidad(sucesores) 

            print("\nElementos en Historial: " + str(len(self.historial)) + "\n\nElementos en Cola: " + str(len(self.cola)))

            self.estado_actual = self.cola.popleft()
            iteracion += 1

        print("Iteracion: " + str(iteracion) + "\n")
        self.mostrar_estado(None)
        print("\n\n\nHa llegado a Solucion")
        self.buscar_padres(self.estado_actual)
        print("\nALGORITMO EN PROFUNDIDAD:")
        print("\nElementos en Historial: " + str(len(self.historial)) + "\n\nElementos en Cola: " + str(len(self.cola)) + "\n\n Iteraciones: " + str(iteracion))

    def algoritmo_anchura_evalua_hijos(self):
        iteracion = 1
        self.estado_actual = self.estado_inicial
        self.historial.append(self.estado_actual)
        movimientos = ["UP", "DOWN", "LEFT", "RIGHT"]

        while not self.es_final():
            print(f"Iteración : {iteracion}\n")
            self.mostrar_estado(None)

            for movimiento in movimientos:
                estado_temporal = nodo_estado(self.mover(movimiento), self.estado_actual, "Mover a " + movimiento, self.estado_actual.get_nivel() + 1)
                if not estado_temporal.get_valor() == "illegal" and not self.esta_historial(estado_temporal):
                    self.historial.append(estado_temporal)
                    self.cola.append(estado_temporal)
                    if estado_temporal in self.estado_final:
                        break
                
            print("\nElementos en Historial: " + str(len(self.historial)) + "\n\nElementos en Cola: " + str(len(self.cola)))

            self.estado_actual = self.cola.popleft()
            iteracion += 1

        print("Iteracion: " + str(iteracion) + "\n")
        self.mostrar_estado(None)
        print("\n\n\nHa llegado a Solucion")
        self.buscar_padres(self.estado_actual)
        print("\nALGORITMO EN ANCHURA:")
        print("\nElementos en Historial: " + str(len(self.historial)) + "\n\nElementos en Cola: " + str(len(self.cola)) + "\n\n Iteraciones: " + str(iteracion))

    def algoritmo_profundidad_evalua_hijos(self):
        iteracion = 1
        self.estado_actual = self.estado_inicial
        self.historial.append(self.estado_actual)
        movimientos = ["UP", "DOWN", "LEFT", "RIGHT"]

        sucesores = deque()
        solucion = None

        while not self.es_final():
            print(f"Iteración : {iteracion}\n")
            self.mostrar_estado(None)

            for movimiento in movimientos:
                estado_temporal = nodo_estado(self.mover(movimiento), self.estado_actual, "Mover a " + movimiento, self.estado_actual.get_nivel() + 1)
                if not estado_temporal.get_valor() == "illegal" and not self.esta_historial(estado_temporal):
                    sucesores.append(estado_temporal)
                    if estado_temporal in self.estado_final:
                        solucion = estado_temporal
                        break
                
            self.add_profundidad(sucesores)
                
            print("\nElementos en Historial: " + str(len(self.historial)) + "\n\nElementos en Cola: " + str(len(self.cola)))

            #Paso al siguiente estado
            if solucion is None:
                self.estado_actual = self.cola.popleft()
            else:
                self.estado_actual = solucion
            iteracion += 1

        print("Iteracion: " + str(iteracion) + "\n")
        self.mostrar_estado(None)
        print("\n\n\nHa llegado a Solucion")
        self.buscar_padres(self.estado_actual)
        print("\nALGORITMO EN PROFUNDIDAD:")
        print("\nElementos en Historial: " + str(len(self.historial)) + "\n\nElementos en Cola: " + str(len(self.cola)) + "\n\n Iteraciones: " + str(iteracion))

    def espacios_manhattan(self,estado,final):
        d=math.fabs((final.get_valor()[0]-estado.get_valor()[0])+(final.get_valor()[1]-estado.get_valor()[1]))
        return d

    def calcular_heuristica(self, estado):
        primero = True
        for final in self.estado_final:
            if primero:
                distancia = self.espacios_manhattan(estado, final)
                primero = False
            else:
                nueva_distancia = self.espacios_manhattan(estado, final)

                if nueva_distancia < distancia:
                    distancia = nueva_distancia
        estado.set_distancia(distancia)

    def algoritmo_better_first(self):
        iteracion = 1
        self.estado_actual = self.estado_inicial
        self.historial.append(self.estado_actual)
        movimientos = ["UP", "DOWN", "LEFT", "RIGHT"]
        #movimientos = ["DOWN", "RIGHT", "UP", "LEFT"]
        #movimientos = ["DOWN","UP", "RIGHT","LEFT"]

        sucesores = []
        solucion = None

        while not self.es_final():
            print(f"Iteración : {iteracion}\n")
            self.mostrar_estado(None)

            for movimiento in movimientos:
                estado_temporal = nodo_estado(self.mover(movimiento), self.estado_actual, "Mover a " + movimiento, self.estado_actual.get_nivel() + 1)
                if not estado_temporal.get_valor() == "illegal" and not self.esta_historial(estado_temporal):
                    self.calcular_heuristica(estado_temporal)
                    sucesores.append(estado_temporal)
                    if estado_temporal in self.estado_final:
                        solucion = estado_temporal
                        break
            
            sucesores.sort(key=ordenar_por_heuristica)
            self.add_profundidad(sucesores) #mmmm
                
            print("\nElementos en Historial: " + str(len(self.historial)) + "\n\nElementos en Cola: " + str(len(self.cola)))
        
            if solucion is None:
                self.estado_actual = self.cola.popleft()
            else:
                self.estado_actual = solucion
            iteracion += 1

        print(f"Iteración : {iteracion}\n")
        self.mostrar_estado(None)

        #Solucion
        print("\n\n\nHa llegado a Solucion")
        self.buscar_padres(self.estado_actual)
        print("\nResumen Algoritmo Better First\n")
        print("\nElementos en Historial: " + str(len(self.historial)) + "\n\nElementos en Cola: " + str(len(self.cola)) + "\n\n Iteraciones: " + str(iteracion))