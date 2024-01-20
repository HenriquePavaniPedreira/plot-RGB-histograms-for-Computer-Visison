import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

def plot_color_histograms(img_path):
	img = cv.imread("colorida.jpg")
	azul, verde, vermelho = cv.split(img)

	plt.style.use('dark_background')

	# Criar um subplot para os histogramas individuais e sobreposição
	fig, axes = plt.subplots(2, 2, figsize=(15, 10))

	# Histograma do canal azul
	axes[0, 0].hist(azul.ravel(), 256, [0, 256], color='blue')
	axes[0, 0].set_xlabel("Valor do pixel")
	axes[0, 0].set_ylabel("Frequência")
	axes[0, 0].set_title("Histograma do canal azul")

	# Histograma do canal verde
	axes[0, 1].hist(verde.ravel(), 256, [0, 256], color='green')
	axes[0, 1].set_xlabel("Valor do pixel")
	axes[0, 1].set_ylabel("Frequência")
	axes[0, 1].set_title("Histograma do canal verde")

	# Histograma do canal vermelho
	axes[1, 0].hist(vermelho.ravel(), 256, [0, 256], color='red')
	axes[1, 0].set_xlabel("Valor do pixel")
	axes[1, 0].set_ylabel("Frequência")
	axes[1, 0].set_title("Histograma do canal vermelho")

	# Sobreposição dos histogramas
	axes[1, 1].hist(azul.ravel(), 256, [0, 256], color='blue', alpha=0.5, label='Azul')
	axes[1, 1].hist(verde.ravel(), 256, [0, 256], color='green', alpha=0.5, label='Verde')
	axes[1, 1].hist(vermelho.ravel(), 256, [0, 256], color='red',alpha=0.5,label='Vermelho')

	axes[1, 1].set_xlabel("Valor do pixel")
	axes[1, 1].set_ylabel("Frequência")
	axes[1, 1].set_title("Sobreposição dos Histogramas")
	axes[1, 1].legend()

	# Ajustar o layout para evitar sobreposição
	plt.tight_layout()

	# Mostrar o gráfico
	plt.show()
print("Insira o path da imagem: ")
img_path = input()
plot_color_histograms(img_path)
	
	
