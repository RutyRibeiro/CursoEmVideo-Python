# Faz o python executar um arquivo mp3
from pygame import mixer
import time
mixer.init()
escolha=input('1 - \033[34m Your love is a lie\033[m de Simple Plan \n'
              '2 - \033[34m Partilhar\033[m de AnaVitória/Rubel\n'
              'Escolha: ')

if escolha==1:
    mixer.music.load('music.mp3')
    print('Tocando:\033[34m Your love is a lie\033[m de Simple Plan')
    mixer.music.play()
    time.sleep(100)
    # Função 'time.sleep' serve como temporizador para adiar o termino do programa, o parametro é recebido em segundos
else:
    mixer.music.load('music1.mp3')
    print('Tocando: \033[34m Partilhar\033[m de AnaVitória/Rubel')
    mixer.music.play()
    time.sleep(100)

