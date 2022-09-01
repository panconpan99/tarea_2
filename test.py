from busqueda import laberinto

if __name__=="__main__":
    inicio=[0,0]
    final=[9,10]
    lab=laberinto(inicio,final)
    lab.algoritmo_anchura()
    #lab.algoritmo_profundidad()
    #lab.algoritmo_anchura_evalua_hijos()
    #lab.algoritmo_profundidad_evalua_hijos()