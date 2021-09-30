import os
import time
import pyautogui
import psutil #listar processos windows

contParam = 60*20 #minutos

def encerra_SGF():
    print("encerra_SGF()")
    os.system("taskkill /f /im scg.exe")
    
def listen_icon():
    print("listen_icon()")
    icon_pos = pyautogui.locateOnScreen('ICON.png')
    print(icon_pos)
    if icon_pos:
        return True
    else:
        return False
    
def timer():
    global contParam
    cont = contParam
    while True:
        print("timer()")
        time.sleep(10)
        cont = cont -10
        print('cont:')
        print(cont)
        
        if listen_icon():
            print('entrou errado')
            cont = contParam
        
        if cont <= 0:
            encerra_SGF()
            cont = contParam
            time.sleep(20)

def icon():
    import PySimpleGUIQt as sg

    tray = sg.SystemTray('My Tray', filename="ICON tray.png")
    menu_item = tray.Read(timeout=0)
    #if menu_item is not None:
     #   print(menu_item)
icon()
timer()
