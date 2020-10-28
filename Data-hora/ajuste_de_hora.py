import os, time

# Comando que irá ajustar a hora e data da maquino ao padrão UTF da localização São Paulo
os.system('timedatectl set-timezone America/Sao_Paulo')

# Pega o horario formatado
hora = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
print(hora)

msg = 'Hora do sistema foi atualizada por motivos de reinicialização as: ' + hora

# Registrar que este script foi executado
# Nome do arquivo ajuste_de_hora.log
registros = open('ajuste_de_hora.log','a')
print(msg)
registros.write(msg) 
registros.close()
