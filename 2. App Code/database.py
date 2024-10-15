# HR 데이터베이스에서 필요한 SQL 작업 처리 모듈
import pymysql
import pymysql.cursors


class ACCDao:
    SELECT_STATEMENT = "SELECT a.사고번호, a.사고일시, w.기상상태, w.노면상태, a.사고내용, d.가해운전자_상해정도, d2.피해운전자_상해정도, concat(a.사상자수,'명') as 사상자수"

    def __init__(self, host: str, port: int, user: str, password: str, db: str):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.db = db
        self.join_sql = """"""

    def get_connection(self) -> pymysql.Connection:
        return pymysql.connect(host=self.host, port=self.port, user=self.user, password=self.password, db=self.db)

    def select_car(self):
        """
        차량 조회 메소드
        return tuple[job_id, job_name]
        """
        sql = "SELECT 가해운전자_차종 FROM driver_1 GROUP BY 가해운전자_차종"
        with self.get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(sql)
                return cursor.fetchall()

    def select_weather(self):
        """
        날씨 조회 메소드
        return tuple[dept_id, dept_name, loc]
        """
        sql = "SELECT 기상상태 FROM weather_road"
        with self.get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(sql)
                return cursor.fetchall()

    def select_age(self):
        """
        날씨 조회 메소드
        return tuple[dept_id, dept_name, loc]
        """
        sql = "SELECT 연령대 FROM driver_1 GROUP BY 연령대 ORDER BY 연령대"
        with self.get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(sql)
                return cursor.fetchall()


    def select_acc_by_wea(self, 기상상태: str):
        """
        날씨를 조건으로 사고 조회
        return list[dict{column명:value}]
        """
        sql = f"""
        {ACCDao.SELECT_STATEMENT}
        FROM accidents a 
        LEFT JOIN weather_road w
        ON a.기상상태 = w.기상상태 
        LEFT JOIN driver_1 d
        ON a.사고번호 = d.사고번호
        LEFT JOIN driver_2 d2
        ON a.사고번호 = d2.사고번호
        WHERE a.기상상태 = %s
        """
        with self.get_connection() as conn:
            with conn.cursor(pymysql.cursors.DictCursor) as cursor:  # DataFrame 생성 하기 위해 DictCursor 사용
                cursor.execute(sql, [기상상태])
                return cursor.fetchall()

    def select_acc_by_car(self, 가해운전자_차종: str):
        """
        차종을 조건으로 직원 조회
        return list[dict{column명:value}]
        """
        # dept_id가 없는 직원은 나오면 안된다. 그래서 inner join. job_id가 없더라도 대상 dept_id의 직원은 나와야 하므로 dept와는 left outer join
        sql = f"""
        {ACCDao.SELECT_STATEMENT}
        FROM accidents a 
        LEFT JOIN weather_road w
        ON a.기상상태 = w.기상상태 
        LEFT JOIN driver_1 d
        ON a.사고번호 = d.사고번호
        LEFT JOIN driver_2 d2
        ON a.사고번호 = d2.사고번호
        WHERE d.가해운전자_차종 = %s
        """
        with self.get_connection() as conn:
            with conn.cursor(pymysql.cursors.DictCursor) as cursor:
                cursor.execute(sql, [가해운전자_차종])
                return cursor.fetchall()

    def select_acc_by_age(self, 연령대: str):
        """
        차종을 조건으로 직원 조회
        return list[dict{column명:value}]
        """
        # dept_id가 없는 직원은 나오면 안된다. 그래서 inner join. job_id가 없더라도 대상 dept_id의 직원은 나와야 하므로 dept와는 left outer join
        sql = f"""
        {ACCDao.SELECT_STATEMENT}
        FROM accidents a 
        LEFT JOIN weather_road w
        ON a.기상상태 = w.기상상태 
        LEFT JOIN driver_1 d
        ON a.사고번호 = d.사고번호
        LEFT JOIN driver_2 d2
        ON a.사고번호 = d2.사고번호
        WHERE d.연령대 = %s
        """
        with self.get_connection() as conn:
            with conn.cursor(pymysql.cursors.DictCursor) as cursor:
                cursor.execute(sql, [연령대])
                return cursor.fetchall()

    #
    # def select_all_acc(self):
    #     """
    #     모든 직원 조회
    #     return list[dict{column명:value}]
    #     """
    #     sql = f"""
    #     {ACCDao.SELECT_STATEMENT}
    #     FROM accidents a LEFT JOIN weather_road w
    #     ON a.기상상태 = w.기상상태
    #     """
    #     with self.get_connection() as conn:
    #         with conn.cursor(pymysql.cursors.DictCursor) as cursor:
    #             cursor.execute(sql)
    #             return cursor.fetchall()


if __name__ == "__main__":
    from pprint import pprint
    import pandas as pd

    dao = ACCDao("127.0.0.1", 3306, "scott", "tiger", "accidnets")
    print(dao.select_weather())
    # print(dao.select_dept())
    # print(pd.DataFrame(dao.select_emp_by_job('FI_ACCOUNT')))
    # print(pd.DataFrame(dao.select_emp_by_dept('10')))
    # df = pd.DataFrame(dao.select_all_emp())
    # print(df.shape)
