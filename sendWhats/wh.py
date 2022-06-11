#pyinstaller --onefile --console wh.py

import pyautogui,time

#time.sleep(6)

#mensajes = ["asda"]
#for i in range(300):
 #   for mensaje in mensajes:
  #      pyautogui.typewrite(mensaje+" x"+str(i+1))
   #     pyautogui.press("enter")    
mensaje = input("Ingresa el mensaje: ")
n = int(input("Cuántas veces deseas enviarlo? "))

print("Tienes 5 segundos para ir al chat de la persona")

time.sleep(6)

print("Enviando...")
for i in range(n):
    pyautogui.typewrite(mensaje)
    pyautogui.press("enter") 
print("Listo")