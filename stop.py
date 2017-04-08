import subprocess, signal, os
while True:
	p = subprocess.Popen(['ps', '-A'], stdout=subprocess.PIPE)
	out, err = p.communicate()

for line in out.splitlines():
	if 'manager' in line:
		pid = int(line.split(None, 1)[0])
		os.kill(pid, signal.SIGKILL)
	if 'yes' in line:
		pid = int(line.split(none, 1)[0])
		os.kill(pid, signal.SIGKILL)
