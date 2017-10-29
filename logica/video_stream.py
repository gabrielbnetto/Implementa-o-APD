import numpy as np
import cv2

def play_video(nome, url):
    
    cap = carregar_video(url)

    if(cap == None):
        print("Não foi possível carregar o filme")
        return
    
    while(True):
        # Captura de frame por frame
        ret, frame = cap.read()

        # Mostra o resultado, pintando na tela
        cv2.imshow(nome, frame)
        # Ouve se o usuário digitar alguma tecla e saí do while se for o 'Q'
        if cv2.waitKey(50) & 0xFF == ord('q'):
            break

    # Quando tudo acabar, libera o video e fecha a janela
    cap.release()
    cv2.destroyAllWindows()


def carregar_video(url):
    
    cap = cv2.VideoCapture(url)
    
    if(cap.isOpened()):
        return cap
    return None
