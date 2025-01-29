import streamlit as st
import time
import random

# 応援メッセージ
messages = [
    "何やってるんですか　勉強してください",
    "小さいことを重ねることが、とんでもない所に行くただ一つの道",
    "誰よりも三倍、四倍、五倍勉強するもの、それが天才だ",
    "あきらめたらそこで試合終了だよ",
    "失敗したから何なのだ、失敗から学び得て、また挑戦すればいいじゃないか",
    "どんな人だって成功できる。自分に何度もこの言葉をいい聞かせていれば、絶対に成功できる。",
    "成功が上がりでもなければ、失敗が終わりでもない。肝心なのは続ける勇気である。",
    "あきらめなければ必ず道はある。",
    "今日の成果は過去の努力の結果であり、未来はこれからの努力で決まる"
]

# セッションステートの初期化
if "timer_running" not in st.session_state:
    st.session_state.timer_running = False
if "time_left" not in st.session_state:
    st.session_state.time_left = 0

st.title("勉強タイマー")
st.write("まずはスマホを置きましょう！")

# ユーザーの入力
hours = st.number_input("時間", min_value=0, max_value=10, value=0, step=1)
minutes = st.number_input("分", min_value=0, max_value=59, value=0, step=1)
seconds = st.number_input("秒", min_value=0, max_value=59, value=0, step=1)

# チェックボックス
checkbox1 = st.checkbox("スマホは置きましたか？")
checkbox2 = st.checkbox("机の上に気が散るものはないですか？")

if checkbox1 and checkbox2:
    if st.button("準備はいいですか？（スタート）"):
        st.session_state.time_left = hours * 3600 + minutes * 60 + seconds
        st.session_state.timer_running = True
        st.experimental_rerun()

# タイマー実行
if st.session_state.timer_running and st.session_state.time_left > 0:
    with st.empty():
        for i in range(3, 0, -1):
            st.write(f"{i}...")
            time.sleep(1)
        
    while st.session_state.time_left > 0 and st.session_state.timer_running:
        mins, secs = divmod(st.session_state.time_left, 60)
        time_display = f"{mins:02}:{secs:02}"
        st.write(time_display)
        st.write(random.choice(messages))
        time.sleep(1)
        st.session_state.time_left -= 1
        st.experimental_rerun()

if st.session_state.time_left == 0 and st.session_state.timer_running:
    st.write("勉強時間が終了しました！お疲れ様でした！")
    st.session_state.timer_running = False

# ストップボタン
if st.session_state.timer_running:
    if st.button("ストップ"):
        st.session_state.timer_running = False

# 再開ボタン
if not st.session_state.timer_running and st.session_state.time_left > 0:
    if st.button("再開"):
        st.session_state.timer_running = True
        st.experimental_rerun()

# リセットボタン
if st.button("リセット"):
    st.session_state.timer_running = False
    st.session_state.time_left = 0
    st.experimental_rerun()
