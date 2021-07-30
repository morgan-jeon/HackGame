from random import *

def semStep(step: int):
	semStep = [0,2,0,0,0]
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
	'우리가 울랄라 대장의 이메일 주소를 알아냈어.\n이 주소로 백도어가 심어진 PPT파일을 보내야 해.\n먼저 PPT파일에 백도어를 심어보자.',
	'울랄라 대장의 이메일은\ngshs_decode@gmail.com\n이야. 여기에 만든 파일을 보내자.',
	'''It's Step 3!''',
	'''It's Step 4!''',
	'''It's Step 5!''',
	'''It's Step 6!''',
	'''It's Step 7!'''
	]

	return(tip[step])

def newTip(step: int, count: int):
	# print(step, count)
	if count == semStep(step):
		return '다음 단계로 넘어가자'
	nTip = ['',
	['좋아 IP주소를 알아냈지?','잘했어 이제 그 파일을 대장에게 보내보자!'],
	'']
	newTip = nTip[step][count]
	return newTip

def isCorrect(cmd: str, step: int, count: int):
	# print(cmd, step, count)
	lis = ['',
	['ipconfig','newbackdoor'],
	'',
	'']
	if lis[step][count] == cmd:
		# print(True)
		return True 

if __name__=="__main__":
	print(result('ipsec --ip 95.199.85.12 --port 54185'))