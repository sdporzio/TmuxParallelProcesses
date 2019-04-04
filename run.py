import Settings.conf as c
import os, stat, subprocess

def createScript(d):
  # Open gile
  with open('Settings/sampleScript.sh','r') as inFile:
    text = inFile.read()
  # Replace text
  text = text.replace(c.var1,d)
  # Save file
  outName = 'Temp/Commands/%s.sh' %d
  file = open(outName,'w')
  file.write(text)
  file.close()
  # Make executable
  st = os.stat(outName)
  os.chmod(outName, st.st_mode | stat.S_IEXEC)

for d in c.definitions:
  createScript(d)
  command = 'tmux new -d -s %s "Temp/Commands/%s.sh"' %(d,d)
  subprocess.Popen(command, shell=True)
