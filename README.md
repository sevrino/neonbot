<h1 align="center">
    <a href="https://discord.gg/PAC6dvw"><img src="http://i.imgur.com/VOKVy0m.jpg" width="256px" alt="neonbot"></a>
  <br>
    neonbot
  <br>
<h4 align="center">서버 관리를 위한 디스코드 봇</h4>
<h6 align="center">Rem-v2의 README를 참고하여 만들었습니다.</h6>
    
<p align="center">
      <a href="https://discord.gg/PAC6dvw" target="_blank"><img src="https://img.shields.io/badge/discord-server!-blue?logo=discord" alt="Discord"
      </a>
    <a href="https://discordapp.com/oauth2/authorize?client_id=559709567903072256&scope=bot" target="_blank"><img src="https://img.shields.io/badge/bot-add!-blue?logo=discord" alt="license">
    </a>
    <a href="https://www.python.org/downloads" target="_blank"><img src="https://img.shields.io/badge/python-%E2%89%A53.5-blue" alt="ver">
    </a>
  <a href="https://www.python.org/downloads" target="_blank"><img src="https://img.shields.io/github/license/sevrino/neonbot" alt="license">
  </a>
  <a href="https://github.com/sevrino/neonbot/issues" target="_blank"><img src="https://img.shields.io/github/issues/sevrino/neonbot" alt="license">
  </a>
  <a href="https://www.codacy.com/manual/sevrino/neonbot?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=sevrino/neonbot&amp;utm_campaign=Badge_Grade" target="_blank"><img src="https://api.codacy.com/project/badge/Grade/e106e496272445a2974cb3fb7f918d8e"></a>
  </p>
  

-------------------
# 봇 사전 설정

## 봇 요구 사항
* Raspberry Pi 2 성능 이상 권장
* Python 3.5 이상

## Python 설정
* shell을 봇이 설치된 폴더에서 열어서 `pip install -r requirements.txt` 를 입력해 필요한 패키지를 다운로드 합니다.

## json 설정하기
* 봇을 다운로드 받으셨다면, config/setting.json 파일을 엽니다.
* `bot_token` 에는 디스코드 봇 토큰을 붙여넣기 합니다.
* `riot-api` 에는 Riot Developer Portal 에서 발급받은 API 키를 입력합니다.
* `youtube-api` 에는 Google Developer 에서 발급받은 Youtube API(`YouTube Data API v3`) 키를 입력합니다.

## 봇 실행
* shell에서 `python3 app.py`를 입력합니다.

### 백그라운드에서 실행시키고자 할 경우(ubuntu 기준)
* nohup 명령어를 사용하여 백그라운드에서 실행시킵니다.
* shell에서 `sudo nohup sudo python3 app.py &` 를 입력하고 엔터키를 누릅니다.

# 봇 사용법

## 기본적인 명령어들
* command : 도움말을 호출합니다.
* invite : 봇 초대 링크를 호출합니다.
* github : 봇 github 주소를 호출합니다.

## 게임 관련 명령어
* lol [username] : [username]의 솔로 랭크 티어를 조회합니다.

## 서버 관리 명령어
* clean : 메시지를 [number]개 만큼 삭제합니다.
* kick : 서버에서 강제 추방합니다.
* ban : @username을 [reason]이라는 이유로 서버에서 차단합니다.