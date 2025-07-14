import streamlit as st
import plotly.express as px

# 과일 선호도 데이터
fruits = {
    "과일": ["딸기", "사과", "바나나", "샤인머스켓", "포도"],
    "선호도(%)": [21.5, 18.3, 14.7, 10.2, 9.4]
}

# Plotly 그래프
fig = px.bar(fruits, x="과일", y="선호도(%)", color="과일", title="한국 과일 선호도")
fig.update_traces(texttemplate='%{y}%', textposition='outside')

# 스트림릿에 출력
st.title("한국인의 과일 선호도 순위 🍎")
st.plotly_chart(fig)
