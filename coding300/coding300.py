from operator import sub
import sys
from PIL import Image, ImageChops
import stepic
import numpy as np

import pytesseract
import cv2
from sudoku import Sudoku

# Abre la imagen proporcionada como argumento desde la línea de comandos
img = Image.open(sys.argv[1])

# Decodifica un valor oculto en la imagen usando esteganografía, y lo usa como semilla aleatoria
seed = int(stepic.decode(img).replace("#", ""))
np.random.seed(seed)

# Obtiene los datos de píxeles de la imagen
pix = list(img.getdata())

# Función para invertir una permutación
def invert_permutation(p):
    p = np.asanyarray(p)  # Convierte la permutación en un array, por si es un tipo diferente
    s = np.empty_like(p)   # Crea un array vacío del mismo tamaño que 'p'
    s[p] = np.arange(p.size)  # Asigna índices para invertir la permutación
    return s

# Aplica una permutación aleatoria basada en la semilla a los píxeles de la imagen
indices = list(invert_permutation(np.random.permutation(len(pix))))

# Reorganiza los píxeles según los índices permutados
newpix = []
for i in range(len(pix)):
    newpix.append(pix[indices[i]])

# Coloca los nuevos píxeles en la imagen
img.putdata(newpix)

# Tamaño de los sub-bloques (la imagen se divide en una cuadrícula de 4x4)
subsize = img.width // 4

# Crea una lista de bloques vacíos (habrá 16 bloques en total)
blocks = [None] * 16

# Guarda temporalmente la imagen procesada
img.save("tmp.png")

# Recorre los sub-bloques de la imagen (cuadrícula 4x4)
for i in range(4):
    for j in range(4):
        # Recorta cada sub-bloque de la imagen
        subimg = img.crop((i*subsize, j*subsize, (i+1)*subsize, (j+1)*subsize))
        # Decodifica los datos ocultos del sub-bloque usando esteganografía
        val = stepic.decode(subimg).replace("#", "")
        rot = int(val[:2], 2)  # Rotación a aplicar (primeros 2 bits)
        ind = int(val[2:], 2)  # Índice del bloque (resto de bits)
        
        # Rotar el sub-bloque según el valor decodificado
        blocks[ind] = subimg.rotate(-90*rot)

# Pega los bloques rotados en la imagen en sus posiciones correctas
for i in range(16):
    img.paste(blocks[i], ((i%4)*subsize, (i//4)*subsize))

# Guarda la imagen final procesada
img.save("out.png")

# Tamaño de las celdas individuales de la cuadrícula (se asume un tamaño 16x16)
cellsize = img.width // 16

# Lista para almacenar el rompecabezas (sudoku)
puzzle = []

# Función para convertir texto en entero, o devolver 0 si el texto está vacío
def defint(text):
    if text == '':
        return 0
    return int(text)

# Extrae cada celda de la imagen (16x16 celdas)
for j in range(16):
    row = []
    for i in range(16):
        # Recorta cada celda de la imagen, eliminando bordes para enfocarse en el contenido
        prep = img.crop((i*cellsize+10, j*cellsize+10, (i+1)*cellsize-10, (j+1)*cellsize-10))
        # Usa Tesseract para reconocer el número en la celda
        row.append(defint(pytesseract.image_to_string(prep, config="--psm 7 -c tessedit_char_whitelist=0123456789 digits").strip()))
    puzzle.append(row)

# Crea un objeto Sudoku con el tablero extraído de la imagen
sud = Sudoku(4, 4, board=puzzle)

# Resuelve el sudoku
sol = sud.solve()

# Convierte la solución en un string
answer = ""
for row in sol.board:
    for val in row:
        answer += str(val)

# Imprime la respuesta (solución del sudoku)
print(answer)
