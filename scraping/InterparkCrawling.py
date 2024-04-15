'''예전에 짰던 코드 (수정 예정)'''

# -*- coding: utf-8 -*-

# import
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from time import sleep

import pandas


## 인터파크 작품별 정보 사이트 접속 및 팝업 제거
# 추후 후기 외 다른 정보도 크롤링할 수도 있으니 접근 / 관람후기 크롤링 분리함
def IPCrawling(key, title, th) : # 코드(키), 작품명
    # 드라이브 로드
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    # 사이트 접속
    driver.get('https://tickets.interpark.com/goods/'+key)
    sleep(1)

    # 팝업 제거('오늘 하루 안 보기' 클릭)
    try :
        elem = driver.find_element(By.CLASS_NAME, "popupCheckLabel")
        elem.click()
    except :
        pass

    # 공연 정보 크롤링
    # 관람 후기 크롤링
    ReviewCrawling(title, th, driver)
    
    driver.quit()



## 관람 후기 데이터 크롤링
def ReviewCrawling(title, th, driver) : # 작품명, 드라이버
    # 관람후기 페이지 접근
    elem = driver.find_element(By.XPATH, "/html/body/div[1]/div[5]/div[1]/div[2]/div[2]/nav/div/div/ul/li[4]/a")
    # 만약 캐스팅정보가 없어 관람후기가 3번째일 경우
    if elem.get_attribute('data-target') != "REVIEW" :
        elem = driver.find_element(By.XPATH, "/html/body/div[1]/div[5]/div[1]/div[2]/div[2]/nav/div/div/ul/li[3]/a")
    elem.click()
    sleep(1)
    
    # 관람후기 div (추후 다음 페이지로 이동할 때 사용)
    url = "/html/body/div[1]/div[5]/div[1]/div[2]/div[2]/div/div/div[3]/"
    # 관람후기 개수
    try : # 사이트 구조 다른 경우 예외처리
        n = int(driver.find_element(By.XPATH, "/html/body/div[1]/div[5]/div[1]/div[2]/div[2]/div/div/div[3]/div[1]/div[1]/div[1]/strong/span").text)
    except :
        n = int(driver.find_element(By.XPATH, "/html/body/div[1]/div[5]/div[1]/div[2]/div[2]/div/div/div[4]/div[1]/div[1]/div[1]/strong/span").text)
        url = "/html/body/div[1]/div[5]/div[1]/div[2]/div[2]/div/div/div[4]/"

    data = [] # 데이터 저장 변수
    cur_p = 2 # 페이지 넘김용 변수

    # 크롤링 진행
    for i in range(1, n//15+2) : # 페이지 별 최대 리뷰 15개
        reviews = driver.find_elements(By.CLASS_NAME, "bbsItem") # 페이지 별 리뷰들 (li class="bbsItem")

        for li in reviews : # 각 리뷰
            tmp = []  # 초기화

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


            print(f'{i} : {tmp}')  # 확인 차 출력
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
    df = pandas.DataFrame(data, columns=["rating", "id", "date", "views", "like", "title", "text"])
    df.to_csv('../../data/musical_review_raw_data/review_' + title + '_' + th + '.csv', encoding='utf-8-sig')

if __name__ == '__main__' :
    # 추후 musical_crawling_info 데이터에서 작품명, 코드 가져와서 반복문 돌리기
    key = '22005764#'      # 작품 코드
    title = '유진과 유진'    # 작품명
    th = '2'               #  n연(초연, 재연, ...)

    IPCrawling(key, title, th)