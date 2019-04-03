import Settings.conf as c
import os, subprocess

def createScript(d):
'''
Create a .txt file with the script that needs to be executed by tmux
'''
  text = '''source ~/.bash_profile
source /grid/fermiapp/products/uboone/setup_uboone.sh
setup uboonecode v07_07_00 -q e17:prof
log getListFromDefinition -i %s -n 20000''' %(d)
  file = open('Commands/%s.txt' %d,'w')
  file.write(text)
  file.close()

for d in c.definitions:
  createScript(d)
  command = 'tmux new -d -s %s "Commands/%s.txt"' %(d,d)
  subprocess.Popen(command, shell=True)
