import pymysql
from sqlalchemy import create_engine
import pandas as pd


# 테이블 생성
def create_table():

    create_sql_accidents = """
    create table accidents(
    사고번호 varchar(50) primary key,
    사고일시 varchar(50) not null,
    기상상태 varchar(20) not null,
    사고내용 varchar(20) not null,
    사상자수 int
    )
    """

    create_sql_driver_1 = """
    create table driver_1(
    사고번호 varchar(50) primary key,
    가해운전자_차종 varchar(20),
    가해운전자_성별 varchar(20),
    가해운전자_연령 varchar(20),
    가해운전자_상해정도 varchar(20),
    foreign key (사고번호) references accidents (사고번호)
    )
    """

    create_sql_driver_2 = """
    create table driver_2(
    사고번호 varchar(50) primary key,
    피해운전자_차종 varchar(20),
    피해운전자_성별 varchar(20),
    피해운전자_연령 varchar(20),
    피해운전자_상해정도 varchar(20),
    foreign key (사고번호) references accidents (사고번호)
    )
    """

    create_sql_wea_road = """
    create table weather_road(
    기상상태 varchar(20) not null primary key,
    노면상태 varchar(20) not null
    )
    """


    try:
        conn = None
        conn = pymysql.connect(host='127.0.0.1', port = 3306, user='scott', password='tiger',db='accidents')
        cursor = conn.cursor()

        # 삭제 가능하도록 foreign 키 0으로 설정
        cursor.execute('set foreign_key_checks = 0')

        # 테이블 존재할 경우 삭제 후 생성
        cursor.execute('drop table if exists accidents')
        cursor.execute(create_sql_accidents)
        print('accidents table created')

        cursor.execute('drop table if exists driver_1')
        cursor.execute(create_sql_driver_1)
        print('driver_1 table created')

        cursor.execute('drop table if exists driver_2')
        cursor.execute(create_sql_driver_2)
        print('driver_2 table created')

        cursor.execute('drop table if exists weather_road')
        cursor.execute(create_sql_wea_road)
        print('weather_road table created')

    finally:
        if conn:
            cursor.close()
            conn.close()

    return

# 데이터 입력
def insert_data(df_acc, df_dr1, df_dr2, df_w_r):
    user = 'scott'
    pw = 'tiger'
    ip_add = '127.0.0.1'
    db_name = 'accidents'

    db_connection = create_engine(f'mysql+pymysql://{user}:{pw}@{ip_add}/{db_name}')

    df_acc.to_sql(name='accidents', con=db_connection, if_exists='append', index=False)
    df_dr1.to_sql(name='driver_1', con=db_connection, if_exists='append', index=False)
    df_dr2.to_sql(name='driver_2', con=db_connection, if_exists='append', index=False)
    df_w_r.to_sql(name='weather_road', con=db_connection, if_exists='append', index=False)
    print("data inserted")
    return

# 데이터 업데이트
def update_table():
    try:
        conn = None
        conn = pymysql.connect(host='127.0.0.1', port = 3306, user='scott', password='tiger',db='accidents')
        cursor = conn.cursor()

        # 데이터 수량 확인
        engine = create_engine('mysql+pymysql://scott:tiger@127.0.0.1:3306/accidents')
        query = 'SELECT 기상상태, 사고번호 FROM accidents'
        df = pd.read_sql(query, engine)
        df = df.drop_duplicates()
        count_df = df['기상상태'].value_counts().reset_index()
        count_df.columns = ['기상상태', '사고수']  # 열 이름 변경
        total_accidents = count_df['사고수'].sum()

        # 연령 str -> int 변경 작업
        # 데이터 수량//1000 + 1회 반복
        for _ in range(total_accidents//1000 + 1):
            cursor.execute("""
            UPDATE driver_1 set 가해운전자_연령 = case
            when 가해운전자_연령 = '미분류' then null
            when 가해운전자_연령 = '20 이하' then '20'
            when 가해운전자_연령 = '81 이상' then '80'
            ELSE REPLACE(가해운전자_연령, '세', '') END
            WHERE 가해운전자_연령 IS NOT NULL
            """)

        cursor.execute("""
        alter table driver_1 add 연령대 varchar(20)
        """)
        cursor.execute("""
        ALTER TABLE driver_1 MODIFY 가해운전자_연령 INT
        """)
        cursor.execute("""
        update driver_1 set 연령대 = case 
        when 가해운전자_연령 <= 19 then '10대' 
        when 가해운전자_연령 between 20 and 29 then '20대' 
        when 가해운전자_연령 between 30 and 39 then '30대' 
        when 가해운전자_연령 between 40 and 49 then '40대' 
        when 가해운전자_연령 between 50 and 59 then '50대' 
        when 가해운전자_연령 between 60 and 69 then '60대' 
        when 가해운전자_연령 between 70 and 79 then '70대' 
        when 가해운전자_연령 between 80 and 89 then '80대 이상' end
        """)
        print("driver_1 updated")

        for _ in range(total_accidents//1000 + 1):
            cursor.execute("""
            UPDATE driver_2 set 피해운전자_연령 = case 
            when 피해운전자_연령 = '미분류' then null 
            when 피해운전자_연령 = '20 이하' then '20' 
            when 피해운전자_연령 = '81 이상' then '80' 
            when 피해운전자_연령 = '12 이하' then '12' 
            ELSE REPLACE(피해운전자_연령, '세', '') END 
            WHERE 피해운전자_연령 IS NOT NULL
            """)

        cursor.execute("""
        alter table driver_2 add 연령대 varchar(20)
        """)
        cursor.execute("""
        ALTER TABLE driver_2 MODIFY 피해운전자_연령 INT
        """)
        cursor.execute("""
        update driver_2 set 연령대 = case 
        when 피해운전자_연령 between 10 and 19 then '10대 이하' 
        when 피해운전자_연령 between 20 and 29 then '20대' 
        when 피해운전자_연령 between 30 and 39 then '30대' 
        when 피해운전자_연령 between 40 and 49 then '40대' 
        when 피해운전자_연령 between 50 and 59 then '50대' 
        when 피해운전자_연령 between 60 and 69 then '60대' 
        when 피해운전자_연령 between 70 and 79 then '70대' 
        when 피해운전자_연령 between 80 and 89 then '80대 이상' end
        """)
        print("driver_2 updated")

    finally:
        if conn:
            cursor.close()
            conn.close()

    return
