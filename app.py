import streamlit as st
from google import genai
from google.genai import types

# 앱 디자인 설정
st.set_page_config(page_title="해외 이슈 검색기", layout="wide")
st.title("🌐 나만의 해외 이슈 검색기")
st.caption("AI 공공정책 연구를 위한 실시간 해외 뉴스 요약 도구")

# 왼쪽 사이드바에 API 키 입력창 만들기
key = st.sidebar.text_input("Gemini API Key를 입력하세요", type="password")

if key:
    try:
        client = genai.Client(api_key=key)
        topic = st.text_input("검색 주제를 입력하세요", "해외 공공기관 AI 도입 우수 사례")
        
        if st.button("뉴스 검색 시작"):
            with st.spinner('해외 데이터를 분석 중입니다...'):
                # 구글 검색 도구 연결
                search_tool = types.Tool(google_search=types.GoogleSearch())
                response = client.models.generate_content(
                    model='gemini-2.0-flash',
                    contents=f"주제: {topic}. 이와 관련된 최신 외국 기사와 이슈를 찾아 한국어로 요약하고 링크를 알려줘.",
                    config=types.GenerateContentConfig(tools=[search_tool])
                )
                st.markdown("### 🔍 분석 결과")
                st.write(response.text)
    except Exception as e:
        st.error(f"연결 에러가 발생했습니다: {e}")
else:
    st.info("왼쪽 사이드바에 API 키를 입력해 주세요.")
    import streamlit as st
from google import genai
from google.genai import types
import os  # 추가!
import ssl # 추가!

# 🌟 SSL 보안 인증서 확인을 건너뛰는 마법의 코드
ssl._create_default_https_context = ssl._create_unverified_context
os.environ['CURL_CA_BUNDLE'] = ''
