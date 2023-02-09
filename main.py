import tkinter as tk
from tkinter import filedialog, RIGHT, Y
from PIL import Image, ImageTk

#################################################################

##Funções de Modificação de imagem
def scaleOpt(sizeMethod):
    if sizeMethod == 1:
        scale_num = int(input("Em quantas vezes você deseja modificar a imagem?\n"))
        imgScaled = (imagem.size[0] * scale_num, imagem.size[1] * scale_num)
        imgResize = imagem.resize(imgScaled)
        imgResize.show()
    elif sizeMethod == 2:
        weight_resize, height_resize = int(input("\nLargura: ")), int(input("\nAltura: "))
        imgResize = imagem.resize((weight_resize, height_resize))
        imgResize.show()

def crop():
    left_x = int(input("\nInforme quantos pixels devem ser cortados da area esquerda horizontal:"))
    right_x = int(input("\nInforme quantos pixels devem ser cortados da area direita horizontal:"))
    bottom_y = int(input("\nInforme quantos pixels devem ser cortados da area de baixo:"))
    top_y = int(input("\nInforme quantos pixels devem ser cortados da area de cima:"))
    imgCrop = imagem.crop((left_x, top_y, right_x + imagem.width, bottom_y + imagem.height))
    imgCrop.show()

def flip():
    if flipOpt == 1:
        imgFlip_Horizontal = imagem.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
        imgFlip_Horizontal.show()

    elif flipOpt == 2:
        imgFlip_Vertical = imagem.transpose(Image.Transpose.FLIP_TOP_BOTTOM)
        imgFlip_Vertical.show()
    else:
        print("\nOpcao escolhida não disponivel")

def rotate(grausRot):
    imgRot = imagem.rotate(grausRot, expand=True)
    imgRot.show()

#################################################################

##Funções de tela
def open_image():
    file_path = filedialog.askopenfilename()
    global original_image
    original_image = Image.open(file_path)
    show_image()

def show_image():
    global original_image
    global image_label
    image = ImageTk.PhotoImage(original_image)
    image_label.config(image=image)
    image_label.image = image


#################################################################
#importar imagem e mostrar
imagem = Image.open('images/lontrinha.jpg')

##salvar a imagem
#nomeImagem = input("Qual o nome da nova imagem?\n")
#imagem.save(f'images/{nomeImagem}.jpg')

##informação da imagem
#print(imagem.size)
#print(imagem.filename)
#print(imagem.format)
#print(imagem.format_description)

#################################################################

##Escolher modificações na imagem
while True:
    ##Bloco de modificação de imagem
    modificador = int(input("Modificadores de imagem disponíveis:\n[1] - Redimensionar imagem\n[2] - Recortar imagem\n[3] - Espelhar imagem\n[4] - Girar imagem\n"))

    if modificador == 1:
        sizeMethod = int(input("Qual metodo de redimensionamento de imagem você deseja aplicar?\n[1] - Redimensionamento Harmonico\n[2] - Personalizado\n"))
        scaleOpt(sizeMethod)

    elif modificador == 2:
        crop()

    elif modificador == 3:
        flipOpt = int(input("Deseja espelhar Horizontalmente ou Verticalmente a imagem?\n[1] - Horizontal\n[2] - Vertical\n"))
        flip(flipOpt)

    elif modificador == 4:
        grausRot = int(input("Em quantos graus você deseja rotacionar a imagem?\n"))
        rotate(grausRot)

    elif modificador == 5:
        print("Saindo do programa...")
        break

    else: print("\nCaso escolhido não disponivel")

#################################################################

    ##Bloco de Melhoramento de imagem

#################################################################
