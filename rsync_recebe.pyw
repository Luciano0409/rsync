import os
# Sincroniza uma pasta desta de uma maquina remota pra uma pasta local.

os.system('rsync -avz luciano@192.168.1.86:/home/luciano/Desktop/luciano3/ /root/luciano')

