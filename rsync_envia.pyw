import os
# Sincroniza uma pasta desta maquina pra uma maquina remota, ou seja, envia tudo que tá nessa pasta para a maquina remota

os.system('rsync -avz /root/luciano/ luciano@192.168.1.86:/home/luciano/Desktop/luciano3/')

