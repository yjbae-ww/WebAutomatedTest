## Selenium Grid 설치 및 실행 가이드

1. 필수 환경 설치
- Java JDK 설치 

    - [Java JDK Download](https://www.oracle.com/kr/java/technologies/downloads/)   
    - [Java 환경변수 설정](https://coding-factory.tistory.com/838)
 
2. Selenium-server jar 파일 다운 : Selenium Server(Grid)
   
   - [Selenium-server jar site](https://www.selenium.dev/downloads/)

-jar 파일 경로는 원하는 경로에 둔다.(테스트 할려면 c드라이브 경로 추천)

2. Node js 설치
3. selenium-side-runner 설치 (hub로 테스트를 전송하기 위해)
    > npm install -g selenium-side-runner

4. 브라우저 드라이버 설치 : 크롬,엣지 등

    [브라우저 드라이버](https://www.selenium.dev/documentation/webdriver/troubleshooting/errors/driver_location/#use-the-path-environment-variable)

5. 실행 (cmd창에서/cmd창의 경로는 jar파일 경로에서)

    5.1 독립적인 실행 (Hub,Node 둘다 포함)

    > java -jar selenium-server-버전.jar standalone   
    > 예)java -jar selenium-server-4.17.0.jar standalone   

    5.2 hub만 실행
    
    > java -jar selenium-server-버전.jar hub   
    > 예)java -jar selenium-server-4.17.0.jar hub

5.허브가 실행되는지 주소를 복사하여 웹 브라우저에서 실행

6.cmd창에서 ipconfig로 주소 확인

7.웹 브라우저 실행 확인 후 노드로 쓸 컴퓨터에 환경 세팅 구축

8.노드용 컴퓨터에 허브용 주소를 웹브라우저에 실행하여 정상 동작하는지 확인

9.노드용 컴퓨터의 cmd창에 아래 처럼 치기   
    (주소:포트번호는 허브용주소/cmd창의 경로는 jar파일 경로에서)

    java -jar selenium-server-버전.jar node --hub http://주소:포트번호/gird/register
    예)java -jar selenium-server-4.17.0.jar node --hub http://192.168.62.66:4444/gird/register

### 참조 링크)   
[selenium grid 공식 문서](https://www.selenium.dev/documentation/grid/getting_started/)   
[selenium grid hub,node 설치](https://www.whatap.io/ko/blog/39/)

### 참조

- 노드 생성
    > java -jar selenium-server-4.17.0.jar node
- 노드 포트 지정
    > java -jar selenium-server-4.17.0.jar node --port 5555
- 크롬드라이브 경로
    > C:\Users\ww\Downloads\chromedriver-win64\chromedriver-win64\