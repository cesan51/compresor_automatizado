from PIL import Image   #PIL (Python Imaging Library) es una biblioteca de procesamiento de imágenes para Python

import os               #os para el manejo del sistema operativo

downloadsFolder = "/Users/Usuario/Downloads/"     #seleccion de la carpeta a usar
picturesFolder = "/Users/Usuario/Pictures/"

if __name__ == "__main__":
    for filename in os.listdir(downloadsFolder):      #si es que el archivo lo estamos ejecutando en la terminal  
        name, extension = os.path.splitext(downloadsFolder + filename)        #se iteran todos los archivos dentro de la carpeta

        if extension in [".jpg", ".jpeg", ".png"]:         #si su extension se encuentra en
            picture = Image.open(downloadsFolder + filename)  #se abre el archivo
            picture.save(picturesFolder + filename, optimize=True, quality=60)    #luego se guarda en la misma carpeta downloadFolder
            os.remove(downloadsFolder + filename)          #se eliminan las imagenes ya comprimidas
            print(name + ":" + extension)

            #despues se optimiza y se le da calidad a la imagen


        if extension in [".mp3"]:                                              #mover los archivos de la carpeta descargas o music
            musicFolder = "/Users/Usuario/Music/"
            os.rename(downloadsFolder + filename, musicFolder + filename)

        
        if extension in [".mp4"]:                                             #mover los archivos de la carpeta descargas o music
            videoFolder = "/Users/Usuario/Videos/"
            os.rename(downloadsFolder + filename, videoFolder + filename)


