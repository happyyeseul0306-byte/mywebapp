import streamlit as st

# 페이지 기본 설정 (와이드 모드, 제목, 아이콘)
st.set_page_config(
    page_title="MBTI 맞춤 여행지 추천",
    page_icon="✈️",
    layout="centered"
)

# 커스텀 CSS를 활용한 모던하고 깔끔한 디자인 적용
st.markdown("""
    <style>
    .main-title {
        font-size: 2.2rem;
        font-weight: 700;
        color: #1E3A8A;
        text-align: center;
        margin-bottom: 0.5rem;
    }
    .sub-title {
        font-size: 1.1rem;
        color: #4B5563;
        text-align: center;
        margin-bottom: 2rem;
    }
    .result-card {
        background-color: #F3F4F6;
        padding: 1.5rem;
        border-radius: 12px;
        border-left: 5px solid #3B82F6;
        margin-top: 1.5rem;
    }
    </style>
""", unsafe_allow_html=True)

# 헤더 영역
st.markdown('<p class="main-title">✈️ MBTI 여행지 추천기</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">나의 성향에 딱 맞는 찰떡궁합 여행지를 찾아보세요!</p>', unsafe_allow_html=True)

# MBTI 데이터베이스 (간단한 예시)
mbti_recommendations = {
    "ENFP": {"city": "스페인, 바르셀로나", "reason": "자유롭고 열정적인 당신에게 예술과 낭만이 가득한 도시가 제격이에요!"},
    "INTJ": {"city": "아이슬란드, 레이캬비크", "reason": "조용히 사색을 즐길 수 있고 대자연의 경이로움을 느낄 수 있는 곳입니다."},
    "ESTP": {"city": "미국, 라스베이거스", "reason": "스릴과 액티비티를 사랑하는 당신에게 화려한 엔터테인먼트의 도시를 추천해요!"},
    "ISFJ": {"city": "일본, 교토", "reason": "고즈넉하고 차분한 분위기 속에서 힐링할 수 있는 전통의 도시입니다."},
    "ENFJ": {"city": "프랑스, 파리", "reason": "사람들과 교감하고 아름다운 카페에서 대화를 나누기 좋은 감성 도시예요."},
    "ISTP": {"city": "캐나다, 밴쿠버", "reason": "도시와 자연을 혼자서도 쿨하게 누비며 자유를 즐길 수 있는 곳입니다."},
    "INFP": {"city": "체코, 프라하", "reason": "풍부한 감수성을 자극하는 골목길과 야경이 아름다운 낭만의 도시입니다."},
    "ENTP": {"city": "영국, 런던", "reason": "끊임없이 새로운 볼거리와 트렌드가 넘쳐나는 다채로운 메트로폴리스예요."}
}

# 기본 MBTI 목록 (전체가 아닐 경우 가장 대표적인 성향들로 구성, 나머지는 기본값 안내)
all_mbtis = list(mbti_recommendations.keys()) + ["기타 MBTI (ESTJ, INFJ, ESFP 등)"]

# 사용자 입력 영역
selected_mbti = st.selectbox("당신의 MBTI를 선택해 주세요:", all_mbtis)

# 추천 결과 출력 버튼
if st.button("내 여행지 확인하기", type="primary", use_container_width=True):
    st.balloons() # 축하 효과 애니메이션
    
    if selected_mbti in mbti_recommendations:
        rec = mbti_recommendations[selected_mbti]
        st.markdown(f"""
            <div class="result-card">
                <h3>🎯 추천 여행지: <span style="color: #2563EB;">{rec['city']}</span></h3>
                <p style="font-size: 1.05rem; margin-top: 0.5rem; color: #1F2937;">{rec['reason']}</p>
            </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
            <div class="result-card">
                <h3>🎯 추천 여행지: <span style="color: #2563EB;">스위스, 인터라켄</span></h3>
                <p style="font-size: 1.05rem; margin-top: 0.5rem; color: #1F2937;">어떤 성향이든 완벽하게 재충전할 수 있는 최고의 휴식처입니다!</p>
            </div>
        """, unsafe_allow_html=True)

# 푸터
st.markdown("---")
st.markdown("<p style='text-align: center; color: #9CA3AF; font-size: 0.85rem;'>Made with Streamlit ❤️</p>", unsafe_allow_html=True)
