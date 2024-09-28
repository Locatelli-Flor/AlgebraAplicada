import cv2
import matplotlib.pyplot as plt
import numpy as np


def recortar_imagen_v2(ruta_img: str, ruta_img_crop: str, x_inicial: int, x_final: int, y_inicial: int, y_final: int)-> None:
    """
    Esta función recibe una imagen y devuelve otra imagen recortada.

    Args:
      ruta_img (str): Ruta de la imagen original que se desea recortar.
      ruta_img_crop (str): Ruta donde se guardará la imagen recortada.
      x_inicial (int): Coordenada x inicial del área de recorte.
      x_final (int): Coordenada x final del área de recorte.
      y_inicial (int): Coordenada y inicial del área de recorte.
      y_final (int): Coordenada y final del área de recorte.

    Return
      None
    """
    try:
        # Abrir la imagen
        image = cv2.imread(ruta_img)

        # Obtener la imagen recortada
        image_crop = image[x_inicial:x_final, y_inicial:y_final]

        # Guardar la imagen recortada en la ruta indicada
        cv2.imwrite(ruta_img_crop, image_crop)

        print("Imagen recortada con éxito. El tamaño de la imagen es de" + str(image_crop.shape))
    except Exception as e:
        print("Ha ocurrido un error:", str(e))


# Cargar las imágenes
def load_images(ruta_img1, ruta_im2):
  img1 = cv2.imread(ruta_img1)
  img2 = cv2.imread(ruta_im2)

  return img1, img2


def grayscale_converter(imagen):
    return np.mean(imagen, axis=2).astype(np.uint8)


def is_invertible(matriz):
    det = np.linalg.det(matriz)
    return det != 0


def adjust_contrast(imagen, alpha):
    imagen_contraste = alpha * imagen
    return np.clip(imagen_contraste, 0, 255).astype(np.uint8)


# Cargar las imágenes originales
image_1_original, image_2_original = load_images("Entrega 2\imagenes\image_1_original.jpg", "Entrega 2\imagenes\image_2_original.jpg")

if image_1_original is None or image_2_original is None:
    print("Error al cargar las imágenes.")
    exit()
  

# Mostrar las imágenes
plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(image_1_original, cv2.COLOR_BGR2RGB))
plt.title('Imagen 1 original')

plt.subplot(1, 2, 2)
plt.imshow(cv2.cvtColor(image_2_original, cv2.COLOR_BGR2RGB))
plt.title('Imagen 2 original')

plt.show()

# Imprimir el tamaño de las imágenes
print(f'Tamaño de la imagen 1: {image_1_original.shape}')
print(f'Tamaño de la imagen 2: {image_2_original.shape}')

# Mostrar una de las imágenes como matriz e imprimir su tamaño
print('Matriz de la imagen 1:')
print(image_1_original)
print(f'Tamaño de la imagen 1: {image_1_original.shape}')

# Transponer las imágenes
image_1_transposed = np.transpose(image_1_original, axes=(1, 0, 2))
image_2_transposed = np.transpose(image_2_original, axes=(1, 0, 2))

# Mostrar las imágenes traspuestas
plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(image_1_transposed, cv2.COLOR_BGR2RGB))
plt.title('Imagen 1 Traspuesta')

plt.subplot(1, 2, 2)
plt.imshow(cv2.cvtColor(image_2_transposed, cv2.COLOR_BGR2RGB))
plt.title('Imagen 2 Traspuesta')

plt.show()

# Mostrar las imágenes en escala de grises
image_1_gray = grayscale_converter(image_1_original)
image_2_gray = grayscale_converter(image_2_original)

plt.subplot(1, 2, 1)
plt.imshow(image_1_gray, cmap='gray')
plt.title('Imagen 1 en Escala de Grises')

plt.subplot(1, 2, 2)
plt.imshow(image_2_gray, cmap='gray')
plt.title('Imagen 2 en Escala de Grises')

plt.show()

# Verificar si son invertibles y mostrar la inversa
if is_invertible(image_1_gray):
    inverse_image_1_gray = np.linalg.inv(image_1_gray)
    print('La imagen 1 tiene inversa. Su determinante es:', np.linalg.det(image_1_gray))
    print(inverse_image_1_gray) 
else:
    print('La imagen 1 no tiene inversa.')

if is_invertible(image_2_gray):
    inverse_image_2_gray = np.linalg.inv(image_2_gray)
    print('La imagen 2 tiene inversa. Su determinante es:', np.linalg.det(image_2_gray))
    print(inverse_image_2_gray)
else:
    print('La imagen 2 no tiene inversa.')

# Producto de una matriz por un escalar

# Caso 1: α > 1
img1_more_contrast = adjust_contrast(image_2_gray, 1.5)

# Caso 2: 0 < α < 1
img2_less_contrast = adjust_contrast(image_2_gray, 0.5)

# Mostrar los resultados
plt.subplot(1, 2, 1)
plt.imshow(img1_more_contrast, cmap='gray')
plt.title('Contraste Aumentado')

plt.subplot(1, 2, 2)
plt.imshow(img2_less_contrast, cmap='gray')
plt.title('Contraste Disminuido')

plt.show()

# Multipicación de matrices y prueba de que la multiplicación de matrices no es conmutativa
W = np.fliplr(np.eye(image_1_gray.shape[0]))

img1_turned = np.dot(W, image_1_gray)
img2_turned = np.dot(W, image_2_gray)

plt.subplot(1, 2, 1)
plt.imshow(img1_turned, cmap='gray')
plt.title('Imagen 1 Volteada')

plt.subplot(1, 2, 2)
plt.imshow(img2_turned, cmap='gray')
plt.title('Imagen 2 Volteada')

plt.show()

# Imagen negativa
negative_image_1 = 255 - image_1_gray
negative_image_2 = 255 - image_2_gray

plt.subplot(1, 2, 1)
plt.imshow(negative_image_1, cmap='gray')
plt.title('Imagen 1 Negativa')

plt.subplot(1, 2, 2)
plt.imshow(negative_image_2, cmap='gray')
plt.title('Imagen 2 Negativa')
plt.show()