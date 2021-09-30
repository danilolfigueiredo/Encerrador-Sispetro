from shutil import copy
import shutil
from os import system,makedirs
import os
import time

#### - Atualiza versão baixando da pasta da rede e atualiza a local
def update():
    try:
        shutil.rmtree('C:\\SispetroCLS', ignore_errors=False, onerror=None)
    except:
        None
    try:
        makedirs('C:\\SispetroCLS')
    except:
        None
    os.system('xcopy S:\SispetroCLS C:\SispetroCLS /y /e /h')
    time.sleep(6)
#update - Fim


#### - Checa se a versão local é igual a da rede
def check_uptodate():
    def closer():
        vcloud.close()
        vlocal.close()
        
    vcloud = open('\\\\HSERVER\\scgwin\\SispetroCLS\\Programs\\ver','r')
    try:
        vlocal = open('C:\\Sispetrocls\\Programs\\ver','r')
    except:
        return False

    if vcloud.read() == vlocal.read():
        closer()
        return True
    else:
        closer()
        return False
    
#check_uptodate - Fim

#start modificado para inicialização com script python, só depende de instalar o python
    
if check_uptodate():
    os.system('''start C:\SispetroCLS\Programs\Main.pyw close''')
else:
    update()
    os.system('''start C:\SispetroCLS\Programs\Main.pyw close''')
