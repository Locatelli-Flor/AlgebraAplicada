import cv2
import os
import matplotlib.pyplot as plt

# Monta tu Google Drive a la máquina virtual de Colab.
from google.colab import drive
drive.mount('/content/drive', force_remount=True)

# Cambiar el directorio actual al directorio donde se encuentra la tarea.
# Especificar la ruta donde se van a guardar los archivos que pide la tarea.
# Por ejemplo: '/content/drive/My Drive/Algebra Aplicada UCU'
os.chdir('/content/drive/My Drive/UCU/Algebra') #Modificar esta línea

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
img1 = cv2.imread('ruta_a_imagen1.jpg')
img2 = cv2.imread('ruta_a_imagen2.jpg')

# Mostrar las imágenes
plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))
plt.title('Imagen 1')

plt.subplot(1, 2, 2)
plt.imshow(cv2.cvtColor(img2, cv2.COLOR_BGR2RGB))
plt.title('Imagen 2')

plt.show()

#Imprimir el tamaño de las imágenes
print(f'Tamaño de la imagen 1: {img1.shape}')
print(f'Tamaño de la imagen 2: {img2.shape}')