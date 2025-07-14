import streamlit as st

# 국가별 유명 인물 데이터
famous_people = {
    "대한민국": {
        "name": "방탄소년단(BTS)",
        "reason": "K-pop을 전 세계에 알린 글로벌 슈퍼스타로, 문화 외교에도 큰 영향을 미쳤습니다."
    },
    "미국": {
        "name": "엘론 머스크 (Elon Musk)",
        "reason": "테슬라, 스페이스X 등을 통해 기술 혁신을 선도하며 세계적인 영향력을 가진 기업가입니다."
    },
    "프랑스": {
        "name": "에마뉘엘 마크롱",
        "reason": "프랑스 대통령으로 유럽 정치와 국제 무대에서 중요한 역할을 하고 있습니다."
    },
    "일본": {
        "name": "미야자키 하야오",
        "reason": "세계적인 애니메이션 감독으로, 일본 문화 콘텐츠의 대표 인물입니다."
    },
    "인도": {
        "name": "나렌드라 모디",
        "reason": "인도 총리로서 인도의 정치·경제에 막대한 영향력을 가진 지도자입니다."
    },
    "영국": {
        "name": "찰스 3세",
        "reason": "영국의 국왕으로 전통과 현대의 상징적 인물입니다."
    },
    "브라질": {
        "name": "펠레",
        "reason": "축구 역사상 최고의 선수 중 한 명으로, 브라질의 자랑이자 세계적인 스포츠 아이콘입니다."
    },
    "독일": {
        "name": "앙겔라 메르켈",
        "reason": "16년간 독일 총리를 지낸 유럽 정치의 중심 인물로 평가받고 있습니다."
    },
    "중국": {
        "name": "시진핑",
        "reason": "중국 국가주석으로서 중국의 정책과 국제 관계에 막대한 영향력을 미치고 있습니다."
    }
}

# 스트림릿 UI
st.title("국가별 가장 유명한 인물 알아보기")

selected_country = st.selectbox("국가를 선택하세요:", list(famous_people.keys()))

if selected_country:
    person = famous_people[selected_country]
    st.subheader(f"📌 {selected_country}에서 가장 유명한 인물:")
    st.markdown(f"**{person['name']}**")
    st.write(person["reason"])
