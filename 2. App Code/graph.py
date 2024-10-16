from sqlalchemy import create_engine
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def graph_weather():
    # MySQL 데이터베이스 연결
    engine = create_engine('mysql+pymysql://scott:tiger@127.0.0.1:3306/accidents')

    # SQL 쿼리 실행하여 데이터 가져오기
    query = 'SELECT 기상상태, 사고번호 FROM accidents'
    df = pd.read_sql(query, engine)

    # 중복된 행 제거
    df = df.drop_duplicates()

    # 기상 상태별 사고 수 집계
    count_df = df['기상상태'].value_counts().reset_index()
    count_df.columns = ['기상상태', '사고수']  # 열 이름 변경

    # 총 사고 수 계산
    total_accidents = count_df['사고수'].sum()

    # 한글 폰트 설정
    plt.rc('font', family='Malgun Gothic')  # Windows

    # 그래프 그리기
    plt.figure(figsize=(10, 6))  # 그래프 크기 설정
    bars = plt.bar종별 사고 수 집계
    count_df = df['가해운전자_차종'].value_counts().reset_index()
    count_df.columns = ['가해운전자 차종', '사고수']  # 열 이름 변경

    # 총 사고 수 계산
    total_accidents = count_df['사고수'].sum()

    # 한글 폰트 설정
    plt.rc('font', family='Malgun Gothic')  # Windows

    # 그래프 그리기
    plt.figure(figsize=(10, 6))  # 그래프 크기 설정
    bars = plt.bar(count_df['가해운전자 차종'], count_df['사고수'], color='b')  # 막대 그래프
    plt.title('가해운전자 차종 별 사고 수')  # 그래프 제목
    plt.xlabel('가해운전자 차종')  # x축 레이블
    plt.ylabel('사고 수')  # y축 레이블
    plt.xticks(rotation=45)  # x축 레이블 회전
    plt.grid(axis='y')  # y축 그리드 표시

    # 총 합계 표시
    plt.text(x=len(count_df) - 1, y=max(count_df['사고수']) * 0.9,
             s=f'총 사고 수: {total_accidents}',
             ha='right', fontsize=12, color='red')

    plt.tight_layout()  # 레이아웃 자동 조정

    # 그래프 이미지 저장
    plt.savefig('가해운전자 차종 별_사고수.png', dpi=300, bbox_inches='tight')  # 파일명, 해상도, 여백 조정
    return


def graph_age():
    # MySQL 데이터베이스 연결
    engine = create_engine('mysql+pymysql://scott:tiger@127.0.0.1:3306/accidents')

    # SQL 쿼리 실행하여 데이터 가져오기
    query = 'SELECT 연령대, 사고번호 FROM driver_1'
    df = pd.read_sql(query, engine)

    # 중복된 행 제거
    df = df.drop_duplicates()

    # 연령대별 사고 수 집계 및 오름차순 정렬
    count_df = df['연령대'].value_counts().reset_index()
    count_df.columns = ['연령대', '사고수']  # 열 이름 변경
    count_df = count_df.sort_values(by='연령대')  # 연령대 기준 오름차순 정렬

    # 총 사고 수 계산
    total_accidents = count_df['사고수'].sum()

    # 한글 폰트 설정
    plt.rc('font', family='Malgun Gothic')  # Windows

    # 그래프 그리기
    plt.figure(figsize=(10, 6))  # 그래프 크기 설정
    bars = plt.bar(count_df['연령대'], count_df['사고수'], color='b')  # 막대 그래프
    plt.title('연령별 사고 수')  # 그래프 제목
    plt.xlabel('연령대')  # x축 레이블
    plt.ylabel('사고 수')  # y축 레이블
    plt.xticks(rotation=45)  # x축 레이블 회전
    plt.grid(axis='y')  # y축 그리드 표시

    # 총 합계 표시
    plt.text(x=len(count_df) - 1, y=max(count_df['사고수']) * 0.9,
             s=f'총 사고 수: {total_accidents}',
             ha='right', fontsize=12, color='red')

    plt.tight_layout()  # 레이아웃 자동 조정

    # 그래프 이미지 저장
    plt.savefig('연령대별_사고수.png', dpi=300, bbox_inches='tight')  # 파일명, 해상도, 여백 조정
    return

def graph_injury():
    # 데이터베이스 연결 설정 (예시, 실제 설정에 맞게 변경해야 함)
    db_connection_str = 'mysql+pymysql://scott:tiger@127.0.0.1:3306/accidents'
    engine = create_engine(db_connection_str)

    # SQL 쿼리 실행 후 DataFrame으로 가져오기
    query = """
    SELECT 
        d1.가해운전자_차종,
        d2.피해운전자_상해정도,
        COUNT(*) AS 상해정도_수,
        (COUNT(*) / SUM(COUNT(*)) OVER (PARTITION BY d1.가해운전자_차종)) * 100 AS 상해정도_비율
    FROM 
        driver_1 d1 
    JOIN 
        driver_2 d2 ON d2.사고번호 = d1.사고번호
    GROUP BY 
        d1.가해운전자_차종, d2.피해운전자_상해정도
    ORDER BY 
        d1.가해운전자_차종, 상해정도_비율 DESC;
    """
    # 한글 폰트 설정
    plt.rc('font', family='Malgun Gothic')  # Windows

    # SQL 쿼리 결과를 pandas DataFrame으로 불러오기
    df = pd.read_sql(query, con=engine)

    # 데이터 출력 (확인용)
    # print(df.head())

    # 시각화 설정
    plt.figure(figsize=(10, 6))
    sns.barplot(x='가해운전자_차종', y='상해정도_비율', hue='피해운전자_상해정도', data=df)

    # 그래프 제목 및 축 레이블
    plt.title('가해운전자 차종별 피해운전자 상해정도 비율')
    plt.xlabel('가해운전자 차종')
    plt.ylabel('상해정도 비율 (%)')

    # 그래프 출력
    plt.xticks(rotation=45)  # x축 레이블 회전
    plt.legend(title='피해운전자 상해정도')
    plt.tight_layout()

    # 그래프 이미지 저장
    plt.savefig('가해운전자 차종별 피해운전자 상해정도 비율.png', dpi=300, bbox_inches='tight')  # 파일명, 해상도, 여백 조정

    return
