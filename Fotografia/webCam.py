import cv2      # importando biblioteca

webcam = cv2.VideoCapture(0)    # capturando a webcam

if webcam.isOpened():
    validacao, frame = webcam.read()
    
    while validacao:
        validacao, frame = webcam.read()
        cv2.imshow("Video da Webcam", frame)
        key = cv2.waitKey(5)        

        if key == 70 or key == 102 or key == 27: #ESC  # Quando pressiona o esc ele interrompe o loop
            break

cv2.imwrite("foto.jpg", frame)  # cria uma imagem 

webcam.release()    # Encerra a conexão com a webcam
cv2.destroyAllWindows()     #Fecha a janela do windows