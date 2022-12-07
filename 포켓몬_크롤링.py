#문제
#포켓몬을 번호로 검색 후 포켓몬 정보를 받아와서 출력후 포켓몬 상세 웹주소 출력과 이미지 저장하기.
#ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
#분석
#python 으로 http 프로토콜을 이용하여 포켓몬의 번호, 이름등을 크롤링하여 값을 결과로 나타내고, 웹주소를 출력하고 이미지를 파일로 저장한다.
#ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
#분해
#1. 실습 시 필요한 라이브러리를 다운로드한다.
#①pip install requests
#②pip install BeautifulSoup4
#2. 포켓몬 도감 페이지를 확인하여 추출할 포켓몬을 식별하고, 소스코드를 읽어오는 작업
#3. 검색하고자 하는 포켓몬 선택하기
#4. 포켓몬 이름까지 추출
#5. 포켓몬 사진 추출
#6. 검색 기능 추가
#7. 검색하면 포켓몬의 이름과 번호등을 출력한다.
#8. 검색하면 포켓몬의 상세 정보를 웹 주소로 출력한다.
#9. 포켓몬의 이미지를 받아올 파일을 지정한다.
#10. 지정된 파일로 포켓몬 이미지를 저장한다.
#ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
#구조화
#엑터/ 엑터 속성/ 엑터 행위 부여
#① 포켓몬/ 이름, 번호, 이미지/ 검색을 하면 이름, 번호가 출력되고, 사진이 저장된다.
#② 검색/ 검색/ 포켓몬의 이름을 입력하면 포켓몬의 정보를 출력한다.
#③ 이미지/ 파일/ 포켓몬을 검색하면 파일에 포켓몬 이미지가 저장된다.
#ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

#코드 실행 시 필요한 라이브러리를 import 하는 것이다.
import urllib.request
from urllib.request import urlopen
from urllib.parse import quote_plus
from bs4 import BeautifulSoup

#시작할때 출력해주는 문장
print("반갑다. 오박사다.")
print("검색할 포켓몬을 입력해봐~!")
p = int(input("포켓몬 번호를 입력하세요. : "))

#크롤링할 포켓몬 도감 주소로 웹 페이지 요청 (한글이 UTF-8로 표시됨.)
html = urllib.request.urlopen("https://www.pokemonkorea.co.kr/pokedex#pokedex_1")
#웹 페이지를 파싱하는 부분.
soup = BeautifulSoup(html.read(),"html.parser")
#웹 페이지 닫기.
html.close()
#하단에서 쓰일 포켓몬 이름 변수 설정
pokemon_name = soup.select('.bx-txt h3')[p].text.split()[1]

#포켓몬 번호를 크롤링하는 클래스
class poketmon_number_crawlering :
    pokemon_number = soup.select('.bx-txt h3')[p].text.split()[0]
    print("포켓몬 번호 : ", pokemon_number)

#포켓몬 이름를 크롤링하는 클래스
class poketmon_name_crawlering :
    pokemon_name = soup.select('.bx-txt h3')[p].text.split()[1]
    print("포켓몬 이름 : ", pokemon_name)

#포켓몬 정보 웹주소 크롤링하는 클래스
class poketmon_information_web_crawlering :
    #포켓몬스터 도감 주소 가져오기.
    first_url1 = 'https://pokemon.fandom.com/ko/wiki/'
    #포켓몬스터 도감 주소 앞부분과 뒷부분 채워서 웹 주소 만들기.
    url1 = first_url1 + pokemon_name + "_(포켓몬)"
    #포켓몬 정보 웹 주소 출력 하는 코드
    print("포켓몬 정보 웹 주소 : ", url1)

#포켓몬 이미지를 크롤링해서 저장하는 클래스
class poketmon_images_download :
    #네이버 검색 주소 가져오기.
    first_url2 = 'https://search.naver.com/search.naver?where=image&sm=tab_jum&query=' 
    #네이버 검색 주소 앞부분과 뒷부분 채워서 웹 주소 만들기.
    url2 = first_url2 + quote_plus(pokemon_name)
    #크롤링할 포켓몬 도감 주소로 웹 페이지 요청
    html2 = urlopen(url2)
    #웹 페이지를 파싱하는 부분.
    soup2 = BeautifulSoup(html2, "html.parser")
    #사진을 불러오는 것이 목적이기 때문에 간단하게 img라는 변수를 생성하고 개발자 도구에서 _img라는 클래스를 이용
    img = soup2.find_all(class_='_img')

    #이미지를 몇개 다운로드 할 지 물음.
    crawl_num = int(input('다운로드할 이미지 갯수 입력(최대 50개): '))
 
    #변수 n 설정
    n = 1
    #for문으로 이미지 다운로드 코드 작성.
    for i in img:
        #data-source만 뽑아 imgurl이라는 변수를 만든다.
        imgUrl = i['data-source']
        #imgUrl을 열도록하는 코드
        with urlopen(imgUrl) as f:
            #imgurl의 파일을 어떻게 저장할 것인지를 다루는 것이다.
            with open('./포켓몬 사진/' + pokemon_name + str(n)+'.jpg','wb') as h: # 이미지 + 사진번호 + 확장자는 jpg
                #f라는 코드를 읽도록하는 코드
                img = f.read()
                #h라는 코드를 파일로 저장
                h.write(img)
        #n이 1씩 증가함.
        n += 1
        #입력한 다운로드 할 이미지만큼 증가
        if n > crawl_num:
            #브레이크.
            break

    #이미지 다운로드 완료 문장 출력
    print(pokemon_name + ' 이미지 다운로드 성공.')

#포켓몬 번호 출력
poketmon_number_crawlering
#포켓몬 이름 출력
poketmon_name_crawlering
#포켓몬 정보 웹 주소 출력
poketmon_information_web_crawlering
#포켓몬 이미지 다운로드 출력
poketmon_images_download

#쉽지 않은 프로그램이었다. 크롤링을 전혀 할 줄 몰라 네이버와 구글 안 본 사이트가 없고, 문제 해석 능력이 많이 부족하여 클래스도 이정도 밖에 나누지 못하였다. 하지만 크롤링에 대하여 정확히 아는 시간이 되었고, 문제해결을 어떤식으로 해야하는지 아는 뜻 깊은 시간이 되어서 정말 좋았다.
#0~17까지의 번호를 입력하면, 11번 단데기 포켓몬까지 검색이 가능하다.