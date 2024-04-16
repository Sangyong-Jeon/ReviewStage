# -*- coding: utf-8 -*-

"""
인터파크 크롤링 코드
"""

import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from time import sleep

import pandas


def interpark_scraping(title, type, key):  # 코드(키), 타입(뮤지컬/연극), 작품명
    """
    크롤링 준비 + 크롤링 함수 실행
    - driver 생성 및 get
    - 예매 안내 팝업 제거
    - info, review 크롤링
    """
    options = webdriver.ChromeOptions()
    user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.4.1.6 Safari/537.36"
    options.add_argument('user-agent=' + user_agent)

    # 드라이브 로드
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    # 사이트 접속
    driver.get('https://tickets.interpark.com/goods/' + key, )
    sleep(1)

    # 예매 안내 팝업 제거('오늘 하루 안 보기' 클릭)
    try:
        elem = driver.find_element(By.CLASS_NAME, "popupCheckLabel")
        elem.click()
    except:
        pass

    # 공연 정보 크롤링
    info_scraping(title, type, key, driver)

    # 관람 후기 크롤링
    review_scraping(title, type, key, driver)

    driver.quit()



def info_scraping(title, type, key, driver) :
    ## ul class="info"
    # performance_id, title / type location, (start_date, end_date), performance_time, age_requirement
    
    # info 데이터 크롤링
    data = [[key, title, type]]
    for element in driver.find_elements(By.CLASS_NAME, "infoItem")[:4]:
        data[0].append(element.text)

    sleep(1)
    
    # csv로 저장
    df = pandas.DataFrame(data, columns=["performance_id", "title",
                                         "performance_type", "location",
                                         "period", "performance_time",
                                         "age_requirement"])

    dir = f"../data/rawdata/{type}_{title}_info.csv"
    df.to_csv(dir, encoding='utf-8-sig', index=False)


## 관람 후기 데이터 크롤링
def review_scraping(title, type, key, driver) : # 작품명, 드라이버
    """
    관람 후기 데이터 크롤링 코드
    """
    # 관람후기 페이지 접근
    elem = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div[2]/div[2]/nav/ul/li[4]/a")
    # 만약 캐스팅정보가 없어 관람후기가 3번째일 경우 (캐스팅 정보 탭 유무에 따라 page 번호가 달라진다 (3 or 4))
    if elem.get_attribute('data-target') != "REVIEW" :
        elem = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div[2]/div[2]/nav/ul/li[3]/a")
    elem.click()
    sleep(10)
    
    # 관람후기 div (추후 다음 페이지로 이동할 때 사용)
    url = "/html/body/div[1]/div[2]/div[1]/div[2]/div[2]/div/div/div[3]/"
    # 관람후기 개수
    try : # 사이트 구조 다른 경우 예외처리 (best 리뷰 유무)
        n = int(driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div[2]/div[2]/div/div/div[3]/div[1]/div[1]/div[1]/strong/span").text)
        sleep(1)
    except :
        # url도 함께 조정
        n = int(driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div[2]/div[2]/div/div/div[4]/div[1]/div[1]/div[1]/strong/span").text)
        url = "/html/body/div[1]/div[2]/div[1]/div[2]/div[2]/div/div/div[3]/"
    sleep(1)

    data = [] # 데이터 저장 변수
    cur_p = 2 # 페이지 넘김용 변수
    review_id = 0     # 리뷰 id

    # 크롤링 진행
    for i in range(1, n//15+2) : # 페이지 별 최대 리뷰 15개(베스트 제외)
        reviews = driver.find_elements(By.CLASS_NAME, "bbsItem") # 페이지 별 리뷰들 (li class="bbsItem")

        for li in reviews : # 각 리뷰
            tmp = [key]  # 초기화
            # 공연 번호, id, 제목, 내용, 아이디, 별점, 날짜, 공감 수 조회 수

            # 공연 번호

            # 리뷰 id (후기 번호)
            tmp.append(review_id)
            review_id += 1

            # 별점
            tmp.append(li.find_element(By.CLASS_NAME, "prdStarIcon").get_attribute('data-star'))
            # 리뷰 info (아이디, 예매 유무, 날짜, 조회수, 날짜)
            l = li.find_elements(By.CLASS_NAME, "bbsItemInfoList")
            for e in l : tmp.append(e.text)

            # 리뷰 제목
            tmp.append(li.find_element(By.CLASS_NAME, "bbsTitle").text)
            # 리뷰 내용
            try :  # 리뷰 내용이 없을 경우 예외처리
                tmp.append(li.find_element(By.CLASS_NAME, "bbsText").text)
            except selenium.common.exceptions.NoSuchElementException :
                tmp.append('')


            print(f'{i} : {tmp}')  # 확인용 출력
            data.append(tmp) # 저장

        # 다음 페이지로 이동
        # 예외처리 - 마지막 페이지이기 때문에 다음 페이지가 존재하지 않아 에러가 날 경우 처리
        try :
            if i%10!=0 :  # 1~9번째일 경우
                next_page = driver.find_element(By.XPATH, url + "div[2]/ol/li["+str(cur_p)+"]/a")
                cur_p += 1
            else :  # 10번째 페이지일 경우 (> 화살표 버튼 클릭)
                next_page = driver.find_element(By.CLASS_NAME, "pageNextBtn.pageArrow")
                cur_p = 2

            next_page.click()
            sleep(1)

        except selenium.common.exceptions.NoSuchElementException :
            break

    # csv로 저장
    df = pandas.DataFrame(data, columns=["performance_id", "review_id", "rating", "user_id", "date", "view_count", "like_count", "title", "text"])
    dir = f"../data/rawdata/{type}_{title}_review.csv"
    df.to_csv(dir, encoding='utf-8-sig', index=False)

if __name__ == '__main__' :
    # 테스트용
    key = '22001159'      # 작품 코드
    title = '늘근도둑이야기'    # 작품명
    type = "연극"

    interpark_scraping(title, type, key)