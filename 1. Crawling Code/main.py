import crawling
import sql
import pandas as pd
import datetime


# 크롤링 호출
text = crawling.crawling()

# 데이터 분리 (엑셀로 우선 진행)
df = pd.read_excel('accidentInfoList.xlsx', sheet_name='Sheet1')
# print(df.info())
# print(df.head())

# 사고 테이블
df_accident = df[['사고번호', '사고일시', '기상상태', '사고내용']]
df_accident['사상자수'] = df['사망자수'] + df['중상자수'] + df['경상자수']
# print(df_accident.head())

# 가해운전자 테이블
df_driver_1 = df[['사고번호', '가해운전자 차종', '가해운전자 성별', '가해운전자 연령', '가해운전자 상해정도']]
df_driver_1.columns = ['사고번호', '가해운전자_차종', '가해운전자_성별', '가해운전자_연령', '가해운전자_상해정도']

# 피해운전자 테이블
df_driver_2 = df[['사고번호', '피해운전자 차종', '피해운전자 성별', '피해운전자 연령', '피해운전자 상해정도']]
df_driver_2.columns = ['사고번호', '피해운전자_차종', '피해운전자_성별', '피해운전자_연령', '피해운전자_상해정도']
# weather = pd.Series(df['기상상태']).unique()
# print(weather)
# road = pd.Series(df['노면상태']).unique()
# print(road)

# 기상-노면 상태 테이블
df_weather_road = pd.DataFrame([['맑음', '건조'], ['흐림','젖음/습기'], ['눈', '적설'], ['비', '젖음/습기'], ['기타', '기타' ]], columns=['기상상태', '노면상태'])


# sql 테이블 생성
sql.create_table()

# sql 데이터 입력
sql.insert_data(df_accident, df_driver_1, df_driver_2, df_weather_road)

# sql 데이터 업데이트
sql.update_table()

