# 1. 프로젝트 개요
프로젝트명 : ReviewStage

주제 : 공연(뮤지컬,연극) 정보와 후기를 워드 클라우드로 시각화하기

프로젝트 참여 인원 : 3인

- [김동기](https://github.com/kdk0411)
  - Django 초기 셋팅 및 모델 정의, DB migration
  - CSV 데이터 파일을 DB 저장
  - 회원가입/로그인/로그아웃 기능
  - 테스트 코드 작성
  - DB 모델링
- [김서연](https://github.com/seoyeon83)
  - 인터파크 티켓 사이트에서 데이터 스크래핑 후 CSV 파일 저장
  - CSV 파일 전처리 및 리뷰 데이터를 워드클라우드 시각화
- [전상용](https://github.com/Sangyong-Jeon)
  - DjangoRestFramework 구현
  - 장고 템플릿 엔진으로 웹 페이지 구현
  - JS를 이용한 이미지 무한 반복 슬라이드 기능
  - ajax 요청으로 화면 데이터를 동적 변경
  - DB 모델링

### 활용 기술 및 프레임워크
- 언어 : Python 3.8.8 , JS, HTML, CSS
- 프레임워크 : Django / Django Rest Framework
- 데이터 : pandas, numpy, selenium, wordcloud
- 데이터베이스 : SQLite3
- 기타 : Slack, Notion, Github


# 2. 프로젝트 주제 선정 이유

![image](https://github.com/Sangyong-Jeon/ReviewStage/assets/80039556/90884ed8-4b1b-4c2e-acde-d2d1dda7eb92)

코로나 이후 공연 예매 증가와 함께 공연에 대한 관심이 높아졌다는 트렌드를 파악하였습니다. 이에 따라 공연 예매 플랫폼은 사용자들이 어떤 공연을 선택해야 하는지에 대한 정보를 더욱 쉽게 접근할 수 있도록 노력하고 있습니다. 저희는 이러한 환경 속에서 다수의 공연 예매 플랫폼 중 1위인 인터파크 티켓에서 많은 공연 정보와 사용자 리뷰 데이터를 보유하고 있다는 점을 고려하였습니다.

저희 ReviewStage는 이러한 상황 속에서 탄생한 프로젝트로, 공연에 대한 정보와 후기를 효과적으로 시각화하여 사용자들이 공연을 더욱 잘 이해하고 선택할 수 있도록 목표를 설정했습니다.

공연 예매 플랫폼에서는 주로 조회수와 공감수가 많은 베스트 리뷰만 쉽게 확인할 수 있는 한계가 있습니다. 따라서 저희는 공연을 관람한 모든 사용자의 리뷰 데이터를 시각화하여 공연에 대한 전반적인 느낌을 쉽게 이해할 수 있도록 함으로써 사용자들이 공연 선택을 보다 쉽게 할 수 있도록 돕고자 합니다. 이러한 노력은 공연을 처음 접하는 사용자들에게도 쉽게 받아들일 수 있는 공연 정보와 리뷰 시각화를 제공함으로써 사용자 경험을 향상시킬 수 있습니다.

# 3. 프로젝트 세부 결과

## 3-1. 주요 구현 사항

1. 데이터 분석 & 시각화
    - 인터파크 티켓 사이트에서 스크래핑한 데이터를 CSV 파일 저장
    - 스크래핑 데이터 전처리(클리닝, 토큰화)
    - 전처리된 리뷰 데이터 기반으로 워드 클라우드로 시각화 이미지 생성
2. 데이터베이스
    - 스크래핑한 CSV 파일을 읽고 DB에 저장
    - 장고의 모델 정의하여 DB 마이그레이션
3. 웹 페이지
    - MTV 패턴과 장고 템플릿 엔진 기능으로 웹페이지 구현
    - JS로 포스터 무한 반복 슬라이드 기능
    - 포스터 클릭하면 AJAX로 비동기 요청하여 해당 공연에 대한 정보와 시각화 이미지를 받아 동적 데이터 변경
4. 서버
    - 회원가입/로그인/로그아웃 구현

## 3-2. 구현 사항 설명

### 스크래핑 설명
![image](https://github.com/Sangyong-Jeon/ReviewStage/assets/80039556/e9c3db45-70a0-4b86-ab60-4ed769ece459)

- 스크래핑 전, 후기 1000건이 넘는 뮤지컬 5개, 연극 5개를 선정해 URL 정리
- URL을 통해 각 공연별 code 파악하고, 스크래핑할 정보 파악
  - 공연 정보 : 장소, 공연 기간, 공연 시간, 관람 연령
  - 관람 후기 : 작성자id, 작성일, 조회수, 공감수, 별점, 제목, 본문
- 동적인 사이트이기에 `Selenium` 활용해 크롤링 진행

### 스크래핑 진행
[interpark_scraping.py](https://github.com/Sangyong-Jeon/ReviewStage/blob/main/scraping/interpark_scraping.py) 로 스크래핑 진행

### 스크래핑 결과
공연 정보 : 총 10건
![image](https://github.com/Sangyong-Jeon/ReviewStage/assets/80039556/a4fbc3a2-152b-4f61-9cc5-a9aa085286c7)

관람 후기 : 총 24,854건
![image](https://github.com/Sangyong-Jeon/ReviewStage/assets/80039556/4a19d8be-8ae7-4439-8fe7-6d06d2448436)

### 데이터 클리닝

- 필요한 형식에 맞지 않는 데이터 전처리를 실행
- [공연 정보 데이터 전처리 파일](https://github.com/Sangyong-Jeon/ReviewStage/blob/main/preprocessing/preprocessing_info.ipynb)
  - 각 공연별로 저장한 CSV 파일 병합
  - 한 번에 수집한 공연 기간을 공연 시작일, 종료일 분할
  - 관람 연령 형식 통일
    ![image](https://github.com/Sangyong-Jeon/ReviewStage/assets/80039556/a45655aa-1408-45b0-8247-62355e098e1e)

- [관람 후기 데이터 전처리 파일](https://github.com/Sangyong-Jeon/ReviewStage/blob/main/preprocessing/preprocessing_review.ipynb)
  - 각 공연별로 저장한 CSV 파일 병합
  - view_count : 조회 없애기 (숫자만 남기기)
  - like_count : 공감 ~ \n공감하기 없애기 (숫자만 남기기)
  - user_id : id / 예매자 여부 분할
  - 베스트 리뷰 삭제 (중복)
  - 결측치 채우기
  - 라이브 리뷰 표시 삭제
  - DB와 column 이름 통일
  - 불필요한 데이터 삭제 (동일 단어 반복, 불필요한 긴 리뷰 직접 삭제)
   ![image](https://github.com/Sangyong-Jeon/ReviewStage/assets/80039556/67d65e46-2151-4229-8ae9-18d1de4872a8)
  - 특수문자 제거하여 한글만 남기고, 형태소 분석기로 명사 추출
  - 불용어 제거
  
  <img width="372" alt="image" src="https://github.com/Sangyong-Jeon/ReviewStage/assets/80039556/20641816-4ba5-4753-b0a4-d7a17ad16722">

### wordcloud 시각화
- [wordcloud 시각화 파일](https://github.com/Sangyong-Jeon/ReviewStage/blob/main/visualization/review_wordcloud.ipynb)
- 연극, 뮤지컬을 의미하는 performance emoji를 마스크로 만들어 그 모양에 맞게 구름을 그리도록 함

<img width="500" alt="image" src="https://github.com/Sangyong-Jeon/ReviewStage/assets/80039556/a8bf402c-99e6-4228-b11d-32d4ec6bf5ff">

### CSV 파일 DB 저장
- 크롤링 및 전처리 완료된 CSV 파일을 DB 저장
- [공연 CSV 데이터를 DB 저장하는 파일](https://github.com/Sangyong-Jeon/ReviewStage/blob/main/reviewstage/performance/management/commands/read_csv_performance.py)
- [리뷰 CSV 데이터를 DB 저장하는 파일](https://github.com/Sangyong-Jeon/ReviewStage/blob/main/reviewstage/performance/management/commands/read_csv_review.py)
- `python manage.py read_csv_performance csv경로` 를 터미널에 작성하여 사용
  ![image](https://github.com/Sangyong-Jeon/ReviewStage/assets/80039556/6284b898-70fe-4621-885d-a607b39dff38)
  ![image](https://github.com/Sangyong-Jeon/ReviewStage/assets/80039556/4a9f5955-8e7b-4c77-9f15-1add9493b10a)

### 웹 페이지
<img width="500" alt="image" src="https://github.com/Sangyong-Jeon/ReviewStage/assets/80039556/66bee380-c112-4762-b026-5d2184612e3b">

- Django Template Engine 을 사용하여 웹 페이지 작성
- [기본 틀 페이지](https://github.com/Sangyong-Jeon/ReviewStage/blob/main/reviewstage/performance/templates/base.html) 를 만들고 이 페이지를 상속받아서 [홈페이지](https://github.com/Sangyong-Jeon/ReviewStage/blob/main/reviewstage/performance/templates/home.html) 개발
- 포스터를 클릭하면 AJAX 비동기 요청으로 공연 정보와 리뷰 시각화 이미지가 동적으로 변함
- JS를 통해 포스터 무한 슬라이드 기능

### 회원/로그인/로그아웃
- 작성된 기준에 맞게 회원가입을 해야하며, 내용이 채워지지 않으면 회원가입 불가
- 로그인 시, 유효성 검사를 거친 뒤 로그인 실행

### DB 모델링 및 Django 모델
![image](https://github.com/Sangyong-Jeon/ReviewStage/assets/80039556/d6e5b2d0-9afa-4808-a1b1-d5eaa90d19cb)

- erdcloud 사이트를 이용하여 같이 모델링 진행
- [Django Model 파일](https://github.com/Sangyong-Jeon/ReviewStage/blob/main/reviewstage/performance/models.py)
  - [Enum 클래스 파일](https://github.com/Sangyong-Jeon/ReviewStage/blob/main/reviewstage/reviewstage/common/Enum.py)
  - 공연과 파일에는 문자열로 TYPE을 정해야하는데 수동 작성시 에러를 대처하기위해 ENUM(열거형) 클래스 생성하여 활용

# 4. 프로젝트 결론
### 프로젝트 요약

각각의 공연에 대한 모든 후기를 시각화하여 공연에 대한 전반적인 느낌을 알 수 있었습니다.

### 기술적 성취

- 웹 페이지에서 유의미한 데이터 스크래핑 및 전처리 후 CSV 파일 저장
- CSV 파일을 기반으로 워드클라우드 시각화
- Django/ RestFramework 서버에 대한 이해
- Django Template 으로 화면 구현과 MTV 패턴 이해
- 파이썬 언어에 대한 이해
- 팀원과의 협력 및 소통

### 아쉬웠던 점

처음 배운 언어와 기술을 가지고 1주일간 만들었던 프로젝트여서 어떤 방식으로 진행을 해야하고, 어떤 아키텍처 설계를 해야하는지 등 여러 고민들이 많았습니다. 팀원과의 소통에서 아이디어는 나오지만 실제로 구현하기에는 시간과 기술 이해가 부족했다는 것이 아쉬웠습니다.

- 프로젝트에서 제공하는 기능 부족
    
    유의미한 데이터가 많았고, 실제로 사용자에게 필요한 기능들을 추가하고 싶었지만 프론트/백 개발에 대한 어려움으로 실제 구현은 하지 못했었습니다.
    
    1.  데이터 스케줄링 수집 기능
        
        매일 사용자가 없는 새벽 시간에 각 공연에 대한 리뷰가 새로 생겼는지 확인하고, 새로 생겼으면 DB에 저장하는 스케줄링 기능
        
    2. 빠른 시각화
        
        리뷰에 대한 명사 분리와 카운트를 세는 통계용 DB 테이블을 만들고, 새로운 리뷰가 생기더라도 빠르게 카운트를 세거나 추가하여 시각화를 보다 빠르게 진행하여 사용자에게 보여줄 수 있는 기능
        
    3. 공연 즐겨찾기
        
        회원은 즐겨찾기한 공연에 대한 정보 및 리뷰를 확인할 수 있는 기능
