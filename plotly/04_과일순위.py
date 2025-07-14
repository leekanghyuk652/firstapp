import streamlit as st
import plotly.express as px

# 타이틀
st.title("한국인의 과일 선호도 순위 🍎🍌🍇")

# 예시 데이터 (2024년 소비자 조사 기반으로 임의 구성)
fruits = {
    "과일": ["딸기", "사과", "바나나", "샤인머스켓", "포도", "복숭아", "수박", "귤", "참외", "멜론"],
    "선호도(%)": [21.5, 18.3, 14.7, 10.2, 9.4, 8.3, 6.8, 5.2, 3.6, 1.9]
}

# Plotly 그래프 생성
fig = px.bar(
    fruits,
    x="과일",
    y="선호도(%)",
    color="과일",
    title="2024년 기준 한국인이 가장 선호하는 과일 순위",
    text="선호도(%)"
)
fig.update_traces(texttemplate='%{text}%', textposition='outside')
fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')

# 그래프 표시
st.plotly_chart(fig)
