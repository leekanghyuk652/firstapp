import streamlit as st
st.title('나의 첫번째 웹앱(by이강혁)')
st.title('이게 된다고?')
import streamlit as st

# 페이지 기본 설정
st.set_page_config(page_title="MBTI 직업 추천", layout="centered")

st.title("🔍 MBTI 기반 직업 추천기")
st.write("당신의 MBTI 유형을 선택하면, 그에 어울리는 직업을 추천해드려요!")

# MBTI 목록
mbti_types = [
    "ISTJ", "ISFJ", "INFJ", "INTJ",
    "ISTP", "ISFP", "INFP", "INTP",
    "ESTP", "ESFP", "ENFP", "ENTP",
    "ESTJ", "ESFJ", "ENFJ", "ENTJ"
]

# MBTI에 따른 추천 직업 딕셔너리
mbti_jobs = {
    "ISTJ": ["회계사", "관리자", "공무원"],
    "ISFJ": ["간호사", "교사", "상담사"],
    "INFJ": ["심리학자", "작가", "사회운동가"],
    "INTJ": ["과학자", "전략기획자", "엔지니어"],
    "ISTP": ["기술자", "정비사", "경찰"],
    "ISFP": ["예술가", "디자이너", "작곡가"],
    "INFP": ["작가", "상담가", "사회복지사"],
    "INTP": ["연구원", "프로그래머", "이론물리학자"],
    "ESTP": ["기업가", "세일즈 전문가", "스포츠 선수"],
    "ESFP": ["배우", "MC", "이벤트 플래너"],
    "ENFP": ["기획자", "홍보 담당자", "창작자"],
    "ENTP": ["창업가", "변호사", "기술 컨설턴트"],
    "ESTJ": ["경영자", "군인", "프로젝트 매니저"],
    "ESFJ": ["교사", "간호사", "인사담당자"],
    "ENFJ": ["코치", "상담사", "홍보 전문가"],
    "ENTJ": ["CEO", "변호사", "경영 컨설턴트"]
}

# 사용자 입력 (MBTI 선택)
selected_mbti = st.selectbox("당신의 MBTI 유형을 선택하세요", mbti_types)

# 버튼을 눌렀을 때 추천 결과 출력
if st.button("직업 추천 받기"):
    jobs = mbti_jobs.get(selected_mbti, [])
    st.subheader(f"💼 {selected_mbti} 유형에게 어울리는 직업")
    for i, job in enumerate(jobs, start=1):
        st.write(f"{i}. {job}")
