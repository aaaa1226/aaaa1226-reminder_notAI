import streamlit as st
import time
import random

# タイマーのメッセージ
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

# タイマー処理
if 'timer_running' not in st.session_state:
    st.session_state.timer_running = False

if 'remaining_time' not in st.session_state:
    st.session_state.remaining_time = 0

# 入力セクション
st.write("まずはスマホを置きましょう")

hours = st.number_input("時間を入力してください:", min_value=0, format="%d")
minutes = st.number_input("分を入力してください:", min_value=0, max_value=59, format="%02d")
seconds = st.number_input("秒を入力してください:", min_value=0, max_value=59, format="%02d")

st.write("スマホは置きましたか？このアプリをスマホで使っているなら、遠くにおいてスタートを押しましょう！", "机の上に気が散るものはないですか？")
start_conditions_met = st.checkbox("以上を確認しました")

# スタートボタン
if start_conditions_met and not st.session_state.timer_running:
    if st.button("準備はいいですか？"):
        st.session_state.remaining_time = hours * 3600 + minutes * 60 + seconds
        st.session_state.timer_running = True
        for i in range(3, 0, -1):
            st.write(i)
            time.sleep(1)

# タイマー表示とメッセージ
if st.session_state.timer_running:
    st.write("残り時間: ", st.session_state.remaining_time, "秒")
    random_message = random.choice(messages)
    st.write(random_message)
    if st.button("ストップ"):
        if st.radio("本当に辞めちゃうの…？", ("やめる", "まだ頑張る")) == "やめる":
            st.session_state.timer_running = False
        else:
            st.session_state.timer_running = True

    if st.session_state.remaining_time > 0:
        st.session_state.remaining_time -= 1
        time.sleep(1)
    else:
        st.session_state.timer_running = False