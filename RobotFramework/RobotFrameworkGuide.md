
### 파이썬 버전 확인
> $ python --version

### Robot Framework 설치
> $ pip install robotframework   
> $ pip install robotframework-selenium2library

### 동작 확인
> $ rebot --version   
> $ robot --version

### 파이썬 확장자
> Python for VSCode   
> RobotF Extension   
> robotframework

![alt text](image.png)

### ride 설치
> $ pip install robotframework-ride   
> $ pip install -U https://github.com/robotframework/RIDE/archive/master.zip   
> $ python -m robotide.init

### Webdriver 설치
> https://chromedriver.chromium.org/downloads

### 바로가기 만들기
> 새로만들기 > 바로가기 만들기 > 항목 위치 입력에 "파이썬경로\pythonw.exe" -c "from robotide import main; main()" 입력 후 다음 클릭하여 생성   
> 예) "C:\Python312\pythonw.exe" -c "from robotide import main; main()"      

> 참조) Python 3.12버전은 ride IDE가 안생김   
> 3.11버전으로 다운그레이하여 설치해서 함   
> 대신에 버그인지 ride IDE를 바로가기로 만들어야 함

### Hello world
```
*** Settings ***
Documentation     Example using the space separated plain text format.
Library           OperatingSystem
*** Variables ***
${MESSAGE}        Hello, world!
*** Test Cases ***
My Test
    [Documentation]    Example test
    Log    ${MESSAGE}
    My Keyword    /tmp
Another Test
    Should Be Equal    ${MESSAGE}    Hello, world!
*** Keywords ***
My Keyword
    [Arguments]    ${path}
    Directory Should Exist    ${path}
```

### 실행 방법
> robot 파일이름.robot

### 참조 
https://velog.io/@starmom/Robot-Frameworks-1-1-Setup
