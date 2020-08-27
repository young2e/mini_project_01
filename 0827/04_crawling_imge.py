# 이미지 크롤링
# 특정 검색으로 검색한 url을 가지고 나온 이미지들 중에서
# 이미지 주소들의 규칙을 찾고 이런 이미지 주소들을 모아서
# 03번에서 검색어를 텍스트 파일로 저장한 것처럼 이미지 파일을 저장하면 된다

# 이러한 작업을 누군가가 미리 만들어뒀다
# 라이브러리를 이용하면 된다!

# google : python google image search and download
# -> PyPI (현재 막힌 상태)
# 구글에서 제공하는 이미지 크롤링 라이브러리
# pip install google_images_download
# example code 사용

'''
from google_images_download import google_images_download   #importing the library

response = google_images_download.googleimagesdownload()   #class instantiation

arguments = {"keywords":"Polar bears,baloons,Beaches","limit":20,"print_urls":True}   #creating list of arguments
paths = response.download(arguments)   #passing the arguments to the function
print(paths)   #printing absolute paths of the downloaded images
'''
# 이미지 저장이 되지 않음
# pip uninstall google_images_download 후
# https://tiktikeuro.tistory.com/174 블로그 참조하여 크롤링 시도

# 기존 라이브러리를 수정하여 깃허브에 올려주심 능력자!!!!!
# pip install git+https://github.com/Joeclinton1/google-images-download.git

# 키워드당 최대 100개의 사진까지 다운로드
# 아래 코드는 google-images-download 디렉토리에 넣어두고 실행해야 한다

# from google_images_download import google_images_download

# response = google_images_download()

# arguments = {"keywords":"Polar bears, baloons, Beaches", "limit":20, "print_urls":True}
# paths = response.download(arguments)
# print(paths)

# 해 봤는데 안 됨
# importerror 발생 -> 추후 수정 해 보고 다른 방법 찾자

# 네이버 이미지 크롤링

# from urllib.request import urlopen
# from bs4 import BeautifulSoup as bs
# from urllib.parse import quote_plus

# baseUrl = 'https://search.naver.com/search.naver?where=image&sm=tab_jum&query='
# plusUrl = input('검색어를 입력하세요 : ')
# url = baseUrl + quote_plus(plusUrl)

# html = urlopen(url).read()
# soup = bs(html, "html.parser")
# # img = soup.find_all(class_='_img')
# img = soup.find_all("a", limit = 2) # 개수 제한

# print(img[0])

# n = 1
# for i in img:
#     imgUrl = i['data-source']
#     with urlopen(imgUrl) as f:
#         with open(plusUrl+str(n) + '.jpg', 'wb') as h:
#             img = f.read()
#             h.write(img)
#     n += 1

# print('다운로드완료')

from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
from urllib.parse import quote_plus

baseUrl = 'https://search.naver.com/search.naver?where=image&sm=tab_jum&query='
plusUrl = input('검색어를 입력하세요 : ')
url = baseUrl + quote_plus(plusUrl)

html = urlopen(url).read()
soup = bs(html, "html.parser")
img = soup.find_all(class_='_img')

print(img[0])

n = 1
for i in img:
    imgUrl = i['data-source']
    with urlopen(imgUrl) as f:
        with open(plusUrl+str(n) + '.jpg', 'wb') as h:
            img = f.read()
            h.write(img)
    n += 1

print('다운로드완료')