import time
def barra_de_progreso(partes, total, largo=30):
    frac = partes/total
    completado = int(frac*largo)
    faltante = largo-completado
    barra = f"[{'#'*completado}{'-'*faltante}]{frac:.2%}"
    return barra

n = 30
for i in range (n+1):
        time.sleep(0.1)
        print(barra_de_progreso(i, n, 35), end='\r')