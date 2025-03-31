from dotenv import load_dotenv
load_dotenv()


import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage


stress_prompt = """
あなたは親の育児ストレスを軽減するための専門家です。
育児疲れやストレス管理に関する実践的なアドバイスを提供します。
親自身の心身の健康を保つための方法を教えます。

質問：{input}
"""

nutrition_prompt = """
あなたは子どもの栄養に詳しいアドバイザーです。
子どもの健康な発育を支える食事や栄養バランスについてアドバイスを提供します。
食事の習慣や偏食に関する質問にも丁寧に答えます。

質問：{input}
"""

sleep_prompt = """
あなたは子どもの睡眠習慣に詳しい専門家です。
子どもの夜泣きや睡眠不足に関する解決策を提供し、健全な睡眠を促すためのアドバイスを行います。
親が子どもの睡眠問題に対処できるようサポートします。

質問：{input}
"""

balance_prompt = """
あなたは働く親のための育児と仕事の両立に詳しいアドバイザーです。
仕事と育児のバランスを保つための実践的なアドバイスを提供し、時間管理や家族とのコミュニケーションをサポートします。

質問：{input}
"""

development_prompt = """
あなたは子どもの発達としつけに詳しい専門家です。
子どもの年齢に応じた成長過程や発達の目安についてアドバイスを提供します。
また、子どもの行動への適切なしつけ方やポジティブな関わり方についても支援します。

質問：{input}
"""


prompt_templates = {
    "親の育児ストレスを軽減するための専門家": stress_prompt,
    "子どもの栄養に詳しいアドバイザー": nutrition_prompt,
    "子どもの睡眠習慣に詳しい専門家": sleep_prompt,
    "働く親のための育児と仕事の両立に詳しいアドバイザー": balance_prompt,
    "子どもの発達としつけに詳しい専門家": development_prompt
}


st.title("【提出課題】LLM機能を搭載したWebアプリ")

st.write("このアプリでは、以下の動作モードを切り替えて、様々な育児の悩みに関する相談ができます。")
st.write("動作モードを選択してから、相談したい育児の悩みを入力してください。")

st.divider()

# モード選択用のセレクトボックス
selected_mode = st.selectbox("# 動作モードを選択してください：", list(prompt_templates.keys()))

# 質問入力欄
user_input = st.text_area("相談したい育児の悩みを入力してください：")

# 回答生成ボタン
if st.button("回答を生成"):
    if selected_mode and user_input:
        # 選択されたモードに対応するプロンプトを取得
        selected_prompt = prompt_templates[selected_mode].format(input=user_input)
        
        # LangChainを使用して回答を生成
        llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0.7)  # 必要に応じてパラメータを調整
        messages = [
            SystemMessage(content=selected_prompt),
            HumanMessage(content=user_input)
        ]
        response = llm(messages)

        st.divider()
        
        # 回答を表示
        st.write("### 回答：")
        st.write(response.content)
    else:
        st.warning("動作モードと質問を入力してください。")
