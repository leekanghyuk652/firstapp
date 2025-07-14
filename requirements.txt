import streamlit as st
import plotly.express as px
import pandas as pd

# 웹앱 제목
st.title("🍓 한국에서 인기 있는 과일 순위")

# 과일 데이터 (예시 데이터: 실제 통계 기반 아님)
fruits_data = {
    '과일': [
        '딸기', '사과', '바나나', '수박', '포도',
        '귤', '참외', '복숭아', '자두', '블루베리'
    ],
    '인기도 점수': [95, 90, 88, 85, 80, 78, 75, 72, 70, 68]
}

df = pd.DataFrame(fruits_data)

# Plotly 막대 그래프
fig = px.bar(
    df.sort_values(by="인기도 점수", ascending=False),
    x='과일',
    y='인기도 점수',
    color='과일',
    title='한국에서 인기 있는 과일 TOP 10',
    text='인기도 점수'
)

fig.update_traces(textposition='outside')
fig.update_layout(xaxis_title='과일', yaxis_title='인기도 점수', uniformtext_minsize=8)

# 그래프 출력
st.plotly_chart(fig)

# 설명 추가
st.markdown("""
위 그래프는 한국에서 인기 있는 과일들을 선호도 점수를 기준으로 정리한 것입니다.  
실제 소비량이나 선호도 조사를 기반으로 한 예시는 아니며, 예시 데이터를 사용하였습니다.  
다양한 과일이 계절별로 선호도가 바뀔 수 있으니 참고용으로 활용해주세요!
""")
