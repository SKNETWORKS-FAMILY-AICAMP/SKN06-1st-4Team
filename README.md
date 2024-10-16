# SKN06-1st-4Team
1차 단위 프로젝트

## 🐟4조참치🐟

### 팀원
| 고성주 | 유경상 | 전하연 | 임연경 |
|--|--|--|--|
| <img src="https://images.emarteveryday.co.kr/images/app/webapps/evd_web2/share/SKU/mall/63/69/8801075016963_1.jpg" alt="image" width="200" height="200"/>| <img src="https://search.pstatic.net/common/?src=http%3A%2F%2Fshop1.phinf.naver.net%2F20230725_196%2F1690257049908lG2Mh_JPEG%2F664738786084541_238649207.jpeg&type=a340" alt="image" width="200" height="200"/>| <img src="https://search.pstatic.net/common/?src=http%3A%2F%2Fshop1.phinf.naver.net%2F20200720_117%2F1595234596314MsuHB_PNG%2F32597984812848452_971879905.png&type=sc960_832" alt="image" width="200" height="200"/>|<img src="https://search.pstatic.net/common/?src=http%3A%2F%2Fshop1.phinf.naver.net%2F20231126_131%2F17009690877927nnma_JPEG%2F50690122043041166_282999731.jpg&type=a340" alt="image" width="200" height="200"/>|
| streamlit | mysql & DB설계 | mysql & DB설계 | Crawling |



</br></br></br>
## 🚨 상황별 금천구 교통사고 현황 🚘

### ✔️ 개발 기간
2024.10.11~2024.10.15(총 5일)

</br>

### ✔️ 프로젝트 개요


교통사고는 다양한 상황과 조건에 따라 발생하며, 지역별 사고 현황을 분석하는 것은 교통안전 개선에 중요한 정보를 제공합니다. 본 프로젝트는 금천구를 중심으로 교통사고 현황을 분석하여, 다양한 상황별 사고 발생률을 시각적으로 제공함으로써, 시민들에게 유익한 안전 정보를 제공하고자 합니다.
</br>
특히, 기상 조건, 가해자 차량 유형, 연령별 사고 발생률에 대한 통계를 통해 금천구 내 교통사고의 주요 원인을 파악하고, 향후 사고를 예방하는 데 기여할 수 있는 데이터를 제공할 것입니다.

</br>


### ✔️ 제공 자료
1. 기상 조건에 따른 사고 발생률

> 날씨에 따른 교통사고 건수 및 비율을 그래프로 제공하여, 기상 악화 시 주의가 필요한 시점을 제시합니다.

2. 가해 차종별 사고 발생률과 상해정도
> 가해 차량의 차종에 따라 사고 발생률을 분석하여, 차량 유형별 사고 특성을 파악합니다.

3. 연령대별 사고율 분석
> 연령대별 사고 발생률을 분석하여, 교통사고에 취약한 연령대를 파악하고 교통안전 정책 수립에 기여합니다.

</br>


### ✔️ Stacks

![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=Git&logoColor=white)
![Github](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=GitHub&logoColor=white)             
![Python](https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white) 
![pandas](https://img.shields.io/badge/pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![MySQL](https://img.shields.io/badge/mysql-4479A1?style=for-the-badge&logo=mysql&logoColor=white)
![Selenium](https://img.shields.io/badge/Selenium-43B02A?style=for-the-badge&logo=selenium&logoColor=white)
![Streamlit](https://img.shields.io/badge/streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Discord](https://img.shields.io/badge/discord-5865F2?style=for-the-badge&logo=discord&logoColor=white)



### ✔️ Requirements

streamlit == 1.39.0
</br>
pymysql == 1.1.1
</br>
pandas == 2.2.3
</br>
openpyxl== 1.1.0
</br>
sqlalchemy  == 2.0.35
</br>
configparser == 7.1.0
</br>
matplotlib == 3.9.2
</br>
xlrd == 2.0.1
</br>
seaborn == 0.13.2
</br>


### ✔️ 폴더트리
프로젝트 </br>
|-- 1. Crawling Code : Web Crawling 및 SQL 진행 파일 폴더 </br>
|---- main.py : 실행 파일. 크롤링 진행 및 SQL 입력 </br>
|---- crawling.py : 크롤링 진행 </br>
|---- sql.py : SQL 입력 </br>
| </br>
|-- 2. App Code : Streamlit 진행 파일 폴더 </br>
|---- app.py : streamlit 실행 파일 </br>
|---- database.py : streamlit에 사용할 데이터 관리 </br>
|---- graph.py : streamlit에 올라갈 그래프 생성 </br>
| </br>
|-- 3. Report : 결과물 폴더 </br>
</br>


### ✔️ ERD (데이터 베이스)
❗️ 한국도로교통공단에서 제공하는 자료를 수집 ❗️</br>
</br>
accidents 테이블 
> 사고 내용을 저장하는 테이블
> 
driver_1 테이블 
> 가해운전자 정보를 저장하는 테이블
> 
driver_2 테이블
> 피해운전자 정보를 저장하는 테이블
> 
weather_road 테이블
> 기상상태에 따른 노면상태를 저장하는 테이블
> 


![image](https://github.com/user-attachments/assets/53a8ec90-3828-4c40-837e-cfb0f9d2425e)

</br>


### ✔️ sql 정의서


![accidents sql 정의서](https://github.com/user-attachments/assets/8db329ba-f2af-4f0e-b16e-e571e3092b04)

</br>

 
</br>


### ✔️ 크롤링 결과

| 가해운전자 차종 별 사고수 | 기상 상태 별 사고수 | 
|--|--|
| <img src="https://github.com/user-attachments/assets/63ec36c2-2438-4761-b8bb-5d59a636ee8e" alt="가해운전자 차종 별 사고수" width="500" height="300"/> | <img src="https://github.com/user-attachments/assets/4a8ff576-3274-4c75-990e-6b9a0736c77a" alt="기상 상태 별 사고수" width="500" height="300"/>|
| 연령대 별 사고수 |  가해운전자 차종별 피해운전자 상해정도 비율 |
| <img src="https://github.com/user-attachments/assets/dd265a0c-80f2-4e55-b058-6737f4a7bc38" alt="연령대 별 사고수" width="500" height="300"/> |<img src="https://github.com/user-attachments/assets/83e38013-6cac-4f53-be3f-0dc603c5ab64" alt="가해운전자 차종 별 피해운전자 상해정도 비율" width="500" height="300"/>|



❗️ 연령대 별 사고수는 연령이 확실하지 않은 미확인의 값을 null값으로 지정 ❗️


</br>

### ✔️ streamlit 결과

| streamlit 메인 화면 | 기상 상태 별 사고수 | 
|--|--|
|<img src="https://github.com/user-attachments/assets/5f2a9cd8-00e6-43c7-afdc-040444db58ab" alt="streamlit 메인 화면" width="500" height="300"/>| <img src="https://github.com/user-attachments/assets/35d3a88e-ad2d-4222-a337-9482b03da31c" alt="기상 상태 별 사고수" width="500" height="300"/>|
| 가해운전자 차종 별 사고수 | 연령대 별 사고수 |
|<img src="https://github.com/user-attachments/assets/aac4e5dc-e165-4c84-90b2-62b84b751777" alt="가해운전자 차종 별 사고수" width="500" height="300"/>|<img src="https://github.com/user-attachments/assets/eae2be1b-dfbd-4071-8855-02580ca15da6" alt="연령대 별 사고수" width="500" height="300"/> |
세부내역 
<img src="https://github.com/user-attachments/assets/3dbd8b7e-90de-4076-aee1-a8941f325ab2" alt="세부내역" width="1000" height="300"/>
</br>


### ✔️ 오류

1. 크롤링
   > ① 16번의 값이 있지만 코딩으로 로딩하면 해당 위치의 값만 추출되지 않았다.
   >
   >  -> 해결 불가로 인해 excel 저장이라는 버튼을 클릭하는 방법으로 변경하였다.
   > 
   > ② 파일 저장을 한 후 이를 xlsx로 변경하는 과정에서 확장자가 xls이 아닌 html이 확장자명만 xls로 설정되어있었다.
</br>

2. MYSQL
   > ① 데이터 변환시 limit 1000개로 인해, 전체 데이터가 변경되지 않은채로 다음 구문이 실행되어 에러가 발생되었다.
   >
   > -> 데이터 갯수를 확인하여 갯수//1000+1회 for in 문을 돌려 문제를 해결하였다.
   >
   > ② ERD 추출시 한글깨짐 현상이 있었다
   >
   >  -> Preference > Appearance에서 폰트를 맑은 고딕으로 변경하여 문제를 해결하였다.
</br>


### ✔️ 팀원 회고

고성주
> Steamlit을 처음 다루어 보았으나, 예제코드 등을 활용하여 프로젝트에서 사용할수 있게 되어 만족스럽다.
> 더 많은 기능들이 있는 것으로 보여, 조금더 시간이 있었다면, 더 나은 결과물을 낼수 있지 않을까하는 아쉬움이 있다.
> 
유경상
> ~~
>
전하연
> ~~
>
임연경
> 코드를 처음부터 끝까지 코딩하는 경험은 처음이었는데 여러 오류가 발생해서 화가 나기도 했지만 오류들이 하나하나씩 해결 되는 것을 보며 성취감도 느낄 수 있었다.
>
> 크롤링에서 발생한 오류를 해결하고 싶었지만 해결이 되지 않아 방법을 바꾼 것이 아쉽기도 하다.
