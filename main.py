import streamlit as st
import datetime
import random

# 페이지 기본 설정
st.set_page_config(
    page_title="나만의 글로벌 남친 찾기",
    page_icon="💖",
    layout="centered"
)

# 모던하고 감성적인 CSS 디자인 적용
st.markdown("""
    <style>
    .main-title {
        font-size: 2.2rem;
        font-weight: 800;
        color: #FF4B6C;
        text-align: center;
        margin-bottom: 0.2rem;
    }
    .sub-title {
        font-size: 1.05rem;
        color: #6B7280;
        text-align: center;
        margin-bottom: 2rem;
    }
    .result-card {
        background: linear-gradient(135deg, #FFF1F2, #FFE4E6);
        border: 2px solid #FECDD3;
        border-radius: 20px;
        padding: 2rem;
        text-align: center;
        box-shadow: 0 10px 20px rgba(255, 75, 108, 0.1);
        margin-top: 1.5rem;
    }
    .tag {
        display: inline-block;
        background-color: #FF4B6C;
        color: white;
        padding: 0.3rem 0.8rem;
        border-radius: 50px;
        font-size: 0.85rem;
        font-weight: 600;
        margin-bottom: 0.8rem;
    }
    </style>
""", unsafe_allow_html=True)

# 헤더 영역
st.markdown('<p class="main-title">💖 운명의 글로벌 남친 찾기</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">내 생년월일과 운명적으로 통하는 세계 각국의 랜선 남친은 누구일까요? ✨</p>', unsafe_allow_html=True)

# 글로벌 남자 연예인 데이터베이스 (이름, 국가, 설명, 이미지 URL)
boyfriends = [
    {
        "name": "티모시 샬라메 (Timothée Chalamet)",
        "country": "🇺🇸 미국 / 프랑스",
        "desc": "예술가 같은 눈빛과 대체 불가능한 분위기의 할리우드 스윗가이 ☕",
        "image": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?auto=format&fit=crop&w=600&q=80" # 감성적인 초상화 대체 이미지 (실제 구동시 해당 연예인 이미지 링크 사용 가능)
    },
    {
        "name": "변우석",
        "country": "🇰🇷 대한민국",
        "desc": "다정다감한 눈빛과 완벽한 피지컬로 설렘을 유발하는 청춘 로맨스 장인 🌸",
        "image": "https://images.unsplash.com/photo-1500648767791-00dcc994a43e?auto=format&fit=crop&w=600&q=80"
    },
    {
        "name": "사카구치 켄타로",
        "country": "🇯🇵 일본",
        "desc": "청량하고 훈훈한 미소로 마음을 무장해제시키는 일본 대표 멜로 남신 ☀️",
        "image": "https://images.unsplash.com/photo-1492562080023-ab3db95bfbce?auto=format&fit=crop&w=600&q=80"
    },
    {
        "name": "헨리 카빌 (Henry Cavill)",
        "country": "🇬🇧 영국",
        "desc": "클래식한 영국 신사의 품격과 조각 같은 이목구비를 가진 완벽남 🎩",
        "image": "https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?auto=format&fit=crop&w=600&q=80"
    },
    {
        "name": "송강",
        "country": "🇰🇷 대한민국",
        "desc": "보고만 있어도 기분 좋아지는 화려한 비주얼과 다정한 개구쟁이 매력 💫",
        "image": "https://images.unsplash.com/photo-1519085360753-af0119f7cbe7?auto=format&fit=crop&w=600&q=80"
    },
    {
        "name": "라이언 고슬링 (Ryan Gosling)",
        "country": "🇨🇦 캐나다",
        "desc": "유머러스하고 로맨틱한 눈빛을 가진 대체 불가의 츤데레 매력남 🎬",
        "image": "https://images.unsplash.com/photo-1522075469751-3a6694fb2f61?auto=format&fit=crop&w=600&q=80"
    }
]

# 사용자 입력 영역
col1, col2 = st.columns(2)
with col1:
    user_name = st.text_input("당신의 이름을 입력해 주세요:", "김스윗")
with col2:
    birth_date = st.date_input(
        "당신의 생년월일:",
        value=datetime.date(2000, 1, 1),
        min_value=datetime.date(1950, 1, 1),
        max_value=datetime.date(2015, 12, 31)
    )

st.markdown("<br>", unsafe_allow_html=True)

# 매칭 버튼
if st.button("💘 운명의 남친 만나러 가기", type="primary", use_container_width=True):
    # 생년월일의 숫자를 조합하여 매번 일관되면서도 재미있는 결과가 나오도록 시드(Seed) 설정
    seed_value = birth_date.year * 10000 + birth_date.month * 100 + birth_date.day + len(user_name)
    random.seed(seed_value)
    
    # 랜덤하게 남친 선정
    selected_bf = random.choice(boyfriends)
    
    # 폭죽 효과
    st.balloons()
    
    # 결과 출력 카드
    st.markdown(f"""
        <div class="result-card">
            <span class="tag">{selected_bf['country']}</span>
            <h2 style="color: #1F2937; margin-top: 0.2rem; margin-bottom: 0.5rem;">{user_name}님의 운명의 남친은?</h2>
            <h1 style="color: #FF4B6C; font-size: 2rem; margin-bottom: 1rem;">✨ {selected_bf['name']} ✨</h1>
        </div>
    """, unsafe_allow_html=True)
    
    # 이미지 출력 (정중앙 배치)
    st.image(selected_bf['image'], use_container_width=True)
    
    # 설명 캡션
    st.markdown(f"""
        <div style="background-color: white; padding: 1.2rem; border-radius: 12px; text-align: center; border: 1px solid #E5E7EB; margin-top: 1rem;">
            <p style="font-size: 1.1rem; color: #4B5563; margin: 0; font-weight: 500;">💬 "{selected_bf['desc']}"</p>
        </div>
    """, unsafe_allow_html=True)

# 푸터
st.markdown("---")
st.markdown("<p style='text-align: center; color: #9CA3AF; font-size: 0.85rem;'>Made with Streamlit ❤️ Have a sweet day!</p>", unsafe_allow_html=True)
