import streamlit as st
import time
import random

# 페이지 기본 설정
st.set_page_config(
    page_title="귀염뽀짝 저녁 메뉴 돌림판",
    page_icon="🎡",
    layout="centered"
)

# 귀엽고 아기자기한 디자인을 위한 커스텀 CSS 적용
st.markdown("""
    <style>
    .main-title {
        font-size: 2.3rem;
        font-weight: 800;
        color: #FF6B81;
        text-align: center;
        margin-bottom: 0.2rem;
    }
    .sub-title {
        font-size: 1.1rem;
        color: #706fd3;
        text-align: center;
        margin-bottom: 2rem;
    }
    .slot-box {
        background-color: #ffeaa7;
        border: 3px dashed #fdcb6e;
        border-radius: 20px;
        padding: 2rem;
        text-align: center;
        font-size: 2rem;
        font-weight: bold;
        color: #d63031;
        margin: 1.5rem 0;
    }
    .result-box {
        background: linear-gradient(135deg, #ff9ff3, #feca57);
        border-radius: 20px;
        padding: 2rem;
        text-align: center;
        color: white;
        box-shadow: 0 8px 16px rgba(0,0,0,0.1);
        margin-top: 1.5rem;
    }
    </style>
""", unsafe_allow_html=True)

# 헤더 영역
st.markdown('<p class="main-title">🎡 오늘의 저녁 메뉴 돌림판</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">뭐 먹을지 고민될 땐? 돌림판에게 운명을 맡겨보세요! 💛</p>', unsafe_allow_html=True)

# 기본 저녁 메뉴 리스트
default_menus = ["치킨 🍗", "떡볶이 🌶️", "삼겹살 🥩", "초밥 🍣", "파스타 🍝", "짜장면 🍜", "피자 🍕", "햄버거 🍔"]

# 사이드바에서 메뉴 커스텀마이징 기능 제공
with st.sidebar:
    st.header("✨ 메뉴 커스텀하기")
    st.write("원하는 메뉴를 추가하거나 빼보세요!")
    
    # 텍스트 영역을 통해 메뉴를 줄바꿈으로 입력받음
    menu_input = st.text_area(
        "메뉴 목록 (줄바꿈으로 구분)",
        value="\n".join(default_menus),
        height=200
    )
    
    # 입력된 텍스트를 리스트로 변환 (빈 줄 제거)
    custom_menus = [m.strip() for m in menu_input.split("\n") if m.strip()]

# 메인 화면 - 현재 등록된 메뉴 미리보기
st.info(f"현재 돌림판에 들어간 메뉴 총 **{len(custom_menus)}개**! 🎯")

# 돌림판 실행 버튼
if st.button("🎲 돌림판 돌리기!", type="primary", use_container_width=True):
    if len(custom_menus) < 2:
        st.warning("돌림판을 돌리려면 메뉴가 최소 2개 이상 필요해요!")
    else:
        # 돌림판이 돌아가는 듯한 연출 (애니메이션 효과)
        slot_placeholder = st.empty()
        
        # 빠르게 메뉴가 바뀌는 효과
        for _ in range(12):
            temp_menu = random.choice(custom_menus)
            slot_placeholder.markdown(f'<div class="slot-box">🌀 {temp_menu} 🌀</div>', unsafe_allow_html=True)
            time.sleep(0.08) # 0.08초 간격으로 변경
            
        # 최종 당첨 메뉴 선정
        winner = random.choice(custom_menus)
        
        # 폭죽 애니메이션 효과
        st.balloons()
        
        # 최종 결과 출력
        slot_placeholder.markdown(f"""
            <div class="result-box">
                <h2 style="margin: 0; font-size: 1.8rem; text-shadow: 2px 2px 4px rgba(0,0,0,0.2);">🎉 당첨 메뉴! 🎉</h2>
                <h1 style="margin: 0.5rem 0 0 0; font-size: 2.8rem; color: #fff; text-shadow: 2px 2px 4px rgba(0,0,0,0.3);">{winner}</h1>
                <p style="margin-top: 1rem; font-size: 1.1rem;">오늘 저녁은 이거다! 맛있게 드세요 😋</p>
            </div>
        """, unsafe_allow_html=True)

# 푸터
st.markdown("---")
st.markdown("<p style='text-align: center; color: #b2bec3; font-size: 0.85rem;'>Made with Streamlit ✨ Enjoy your meal!</p>", unsafe_allow_html=True)
