# SKN06-1st-4Team
1차 단위프로젝트

## ⭐️팀소개
### 팀명
4조참치
</br>

### 팀원
| 고성주 | 유경상 | 전하연 | 임연경 |
|--|--|--|--|
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

### ✔️ 프로젝트 내용
1. 기상 조건에 따른 사고 발생률

> 날씨에 따른 교통사고 건수 및 비율을 그래프로 제공하여, 기상 악화 시 주의가 필요한 시점을 제시합니다.

2. 가해 차종별 사고 발생률과 상해정도
> 가해 차량의 차종에 따라 사고 발생률을 분석하여, 차량 유형별 사고 특성을 파악합니다.

3. 연령대별 사고율 분석
> 연령대별 사고 발생률을 분석하여, 교통사고에 취약한 연령대를 파악하고 교통안전 정책 수립에 기여합니다.

</br>

### ✔️ 데이터 베이스


![image](https://github.com/user-attachments/assets/53a8ec90-3828-4c40-837e-cfb0f9d2425e)

</br>

### ✔️ sql정의서


![accidents sql 정의서](https://github.com/user-attachments/assets/8db329ba-f2af-4f0e-b16e-e571e3092b04)

</br>

### ✔️ 오류

1. 크롤링
   > 16번의 값이 있지만 코딩으로 로딩하면 해당 위치의 값만 추출되지 않았다.
   > -> 해결 불가로 인해 excel 저장이라는 버튼을 클릭하는 방법으로 변경하였다.
   > 파일 저장을 한 후 이를 xlsx로 변경하는 과정에서 확장자가 xls이 아닌 html이 확장자명만 xls로 설정되어있었다.
 
</br>

### ✔️ 크롤링 결과

| 가해운전자 차종 별 사고수 | 기상 상태 별 사고수 | 
|--|--|
| ![가해운전자 차종 별_사고수](https://github.com/user-attachments/assets/63ec36c2-2438-4761-b8bb-5d59a636ee8e) | ![기상상태별_사고수](https://github.com/user-attachments/assets/4a8ff576-3274-4c75-990e-6b9a0736c77a)|
| 연령대 별 사고수 |  가해운전자 차종별 피해운전자 상해정도 비율 |
| ![연령대별_사고수](https://github.com/user-attachments/assets/dd265a0c-80f2-4e55-b058-6737f4a7bc38) | ![가해운전자 차종별 피해운전자 상해정도 비율](https://github.com/user-attachments/assets/83e38013-6cac-4f53-be3f-0dc603c5ab64)
 |



</br>

### ✔️ streamlit 결과

| streamlit 첫 화면 | 기상 상태 별 사고수 | 
|--|--|
| ![2024-10-15_105858](https://github.com/user-attachments/assets/5f2a9cd8-00e6-43c7-afdc-040444db58ab) | ![2024-10-15_105922](https://github.com/user-attachments/assets/35d3a88e-ad2d-4222-a337-9482b03da31c)|
| 가해운전자 차종 별 사고수 | 연령대 별 사고수 |
| ![2024-10-15_105936](https://github.com/user-attachments/assets/aac4e5dc-e165-4c84-90b2-62b84b751777) | ![2024-10-15_105950](https://github.com/user-attachments/assets/eae2be1b-dfbd-4071-8855-02580ca15da6) |
| 세부내역 |
| ![세부내역](https://github.com/user-attachments/assets/3dbd8b7e-90de-4076-aee1-a8941f325ab2) |

