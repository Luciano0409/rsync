import os, time

# Sincroniza uma pasta desta de uma maquina remota pra uma pasta local.
log = os.system('rsync -avz luciano@192.168.1.86:/home/luciano/Desktop/luciano3/ /root/luciano')
print('Número de log: ', log)

# Pega o horario atual de São Paulo
hora = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
print('Hora: ', hora)

if log == 0:
    msg = 'Arquivos do diretorio da maquina remota foram trazidos para este com sucesso! ' + hora
else:
    msg = 'Ouve algum erro! As: ' + hora

msg = 'rsync_recebe.py ' + msg

# Registra operação no registros.log
registros = open('/root/luciano/registros.log', 'a')
registros.write(msg)
registros.write('\n')
registros.close()
