import subprocess
import sys


cmd = ['ping', '8.8.8.8', '-c', '4']
enconding = 'utf_8'
system = sys.platform

if system == 'win32':
    cmd = ['ping', '8.8.8.8']
    enconding = 'cp850'

proc = subprocess.run(
    cmd, capture_output=True,
    text=True, encoding=enconding
)

print(proc.stdout)
