import os, time

# Sincroniza uma pasta desta maquina pra uma maquina remota, ou seja, envia tudo que tá nessa pasta para a maquina remota
log = os.system('rsync -avz /root/luciano/ luciano@192.168.1.86:/home/luciano/Desktop/luciano3/')
print('Núemro de log: ', log)

# Pega o horario atual de São Paulo
hora = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
print('Hora: ', hora)

if log == 0:
    msg = 'Os arquivos desta maquina foram levados para a maquina remota com sucesso! ' + hora
else:
    msg = 'Ouve algum erro! As: ' + hora

msg = 'rsync_envia.py ' + msg
    
# Registra operação no registros.log
registros = open('/root/luciano/registros.log', 'a')
registros.write(msg)
registros.write('\n')
registros.close()
