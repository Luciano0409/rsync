import os

rsync_conf_txt    = '''pid file = /var/run/rsyncd.pid
lock file = /var/run/rsync.lock
log file = /var/log/rsync.log
port = 12000

[files]
path = /home/public_rsync
comment = RSYNC FILES
read only = true
timeout = 300\n'''

rsync_conf_txt2   = '''[files]
path = /home/public_rsync
comment = RSYNC FILES
read only = true
timeout = 300
auth users = rsync1,rsync2
secrets file = /etc/rsyncd.secrets'''

rsync_txt         = '''# default: off
# description: The rsync server is a good addition to an ftp server, as it \
# allows crc checksumming etc.
service rsync
{
disable = no
flags = IPv6
socket_type = stream
port = 12000
wait = no
user = root
server = /usr/bin/rsync
server_args = --daemon
log_on_failure += USERID
}'''

rsync_secrets_txt = '''jaco1:9$AZv2%5D29S740k\njaco2:Xyb#vbfUQR0og0$6\njaco3:VU&A1We5DEa8M6^8\n'''

# Criando configurações no rsync.conf(tenho que colocar o chaminho no servidor)
rsync_conf = open('/etc/rsyncd.conf', 'w')
rsync_conf.write(rsync_conf_txt)
rsync_conf.close()
print('Foi escrito no rsync.conf\n')

os.system('rsync --daemon')
os.system('ps x | grep rsync')
print('Comando --daemon e grep rsync executados\n')

os.system("kill 'cat /var/run/rsyncd.pid'")
print('Pid rsyncd matado\n')

# adicionando a configurações no rsync
rsync = open('/etc/xinetd.d/rsync', 'w')
rsync.write(rsync_txt)
rsync.close()
print('Foi escrito em rsync\n')

os.system('/etc/init.d/xinetd restart')

# ssh.exec_cmd('rsync -rdt rsync://IPADDR:RsyncPort/')
# ssh.exec_cmd('rsync -rdt: // IPADDR: RsyncPort /home/luciano/daemon.txt/root/')

# adicionando configurações do rsync.conf
rsync_conf = open('/etc/rsyncd.conf', 'a')
rsync_conf.write(rsync_conf_txt2)
rsync_conf.close()
print('Concatenação realizada no rsync.conf')

# definir credenciais
rsync_secrets = open('/etc/rsyncd.secrets', 'w')
rsync_secrets.write(rsync_secrets_txt)
rsync_secrets.close()
print('Usuarios e senhas cadastradas')

os.system('chmod 600 /etc/rsyncd.secrets')
print('Permissão 600 feita!')
