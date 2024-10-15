import streamlit as st
import database as db
import configparser as parser
from PIL import Image
import graph

st.set_page_config("상황에 따른 사고 현황", layout="wide")

@st.cache_resource
def get_dao():
    """
    ACCDao 생성 함수.
    """
    # props = parser.ConfigParser()  # parser 생성
    # props.read("./config.ini")     # ini 파일 읽기
    # config = props['MYSQL']        # section 이름으로 읽기
    dao = db.ACCDao(host='127.0.0.1', port=3306, user='scott', password='tiger', db='accidents')
    return dao

dao = get_dao()

@st.cache_data
def get_weather():
    """
    전체 날씨 조회 함수
    return
        tuple[기상상태]
    """
    return dao.select_weather()

@st.cache_data
def get_car():
    """
    전체 차종 함수
    return
        tuple[가해운전자_차종]
    """
    return dao.select_car()

@st.cache_data
def get_age():
    """
    전체 연령대 함수
    return
        tuple[연령대]
    """
    return dao.select_age()


# sidebar 생성
by = st.sidebar.radio(
    "다음중 하나를 선택하세요",
    ["날씨로 검색", "가해자 차종으로 검색", "연령대로 검색"],
    index=None # 아무것도 선택되지 않도록 설정
)

# 검색 조건 입력폼들 정의
weather_option = None
car_option = None
age_option = None

if by == "날씨로 검색":
    weather_option = st.sidebar.selectbox(
        label="검색할 날씨 선택.",
        options=get_weather(),
        format_func=lambda x: x[0]
    )

elif by == "가해자 차종으로 검색":
    car_option = st.sidebar.selectbox(
        label="검색할 차종 선택",
        options=get_car(),
        format_func=lambda x: x[0]
    )

elif by == "연령대로 검색":
    age_option = st.sidebar.selectbox(
        label="검색할 연령대 선택",
        options=get_age(),
        format_func=lambda x: x[0]
    )

# 선택 조건에 따른 Data를 Dao를 이용해 DB로 부터 조회
if weather_option: # 날씨로 검색한 결과 출력
    df = dao.select_acc_by_wea(weather_option)
    keyword = f"{weather_option} 날씨로 검색한 결과 - {len(df)} 건"
elif car_option: # 가해자 차종으로 검색한 결과 출력
    df = dao.select_acc_by_car(car_option)
    keyword = f"{car_option} 가해자 차종으로 검색한 결과 - {len(df)} 건"
elif age_option: # 연령대로 검색한 결과 출력
    df = dao.select_acc_by_age(age_option)
    keyword = f"{age_option} 연령대로 검색한 결과 - {len(df)} 건"

# 그래프 생성
graph.graph_weather()
graph.graph_car()
graph.graph_age()
graph.graph_injury()


# 결과 화면
st.title("21~23년 금천구 상황에 따른 사고 현황")
st.divider()

try:
    st.markdown(keyword)
    if weather_option:
        st.header(':star2:기상상태별 그래프:star2:')
        img = Image.open('기상상태별_사고수.png')
        st.image(img)
    elif car_option:
        st.header(':star2:가해운전자 차량별 그래프:star2:')
        img = Image.open('가해운전자 차종별 피해운전자 상해정도 비율.png')
        st.image(img)
        img = Image.open('가해운전자 차종 별_사고수.png')
        st.image(img)
    elif age_option:
        st.header(':star2:연령대별 그래프:star2:')
        img = Image.open('연령대별_사고수.png')
        st.image(img)

    st.divider()
    st.header(':star2:세부 내역 테이블:star2:')
    st.dataframe(df, use_container_width=True)
except:
    st.subheader("검색조건을 선택하세요.")
    img = Image.open('a.png')
    st.image(img)
