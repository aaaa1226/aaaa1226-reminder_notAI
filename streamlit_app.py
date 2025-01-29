import streamlit as st
import time
import random

# ランダムで表示する言葉のリスト
motivational_quotes = [
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

st.title("勉強タイマーアプリ")

# スマホを置くメッセージ
st.subheader("まずはスマホを置きましょう")

# スマホを置いたかと机の上の確認チェックボックス
agree_smartphone = st.checkbox("スマホは置きましたか？このアプリをスマホで使っているなら、遠くにおいてスタートを押しましょう！")
agree_desk = st.checkbox("机の上に気が散るものはないですか？")

# セッション状態を初期化
if "timer_running" not in st.session_state:
    st.session_state.timer_running = False
if "motivational_quote" not in st.session_state:
    st.session_state.motivational_quote = ""
if "remaining_time" not in st.session_state:
    st.session_state.remaining_time = 0
if "start_time" not in st.session_state:
    st.session_state.start_time = None

# チェックボックスが両方チェックされている場合のみスタートボタンを表示
if agree_smartphone and agree_desk:
    st.success("準備ができました！")

    # 勉強時間の入力
    hours = st.number_input("勉強する時間(時間):", min_value=0, max_value=24, step=1, value=0)
    minutes = st.number_input("勉強する時間(分):", min_value=0, max_value=59, step=1, value=0)
    seconds = st.number_input("勉強する時間(秒):", min_value=0, max_value=59, step=1, value=0)

    total_seconds = hours * 3600 + minutes * 60 + seconds

    if total_seconds > 0:
        if st.button("準備はいいですか？（スタート）"):
            st.session_state.timer_running = True
            st.session_state.motivational_quote = random.choice(motivational_quotes)
            st.session_state.remaining_time = total_seconds
            st.session_state.start_time = time.time()

        # タイマー表示用プレースホルダー
        timer_placeholder = st.empty()
        quote_placeholder = st.empty()

        while st.session_state.timer_running and st.session_state.remaining_time > 0:
            elapsed_time = int(time.time() - st.session_state.start_time)
            st.session_state.remaining_time = max(0, total_seconds - elapsed_time)
            st.session_state.start_time = time.time()
            
            if st.session_state.remaining_time <= 0:
                st.session_state.timer_running = False
                st.success("タイマー終了！お疲れさまでした！")
                break
            
            minutes, seconds = divmod(st.session_state.remaining_time, 60)
            hours, minutes = divmod(minutes, 60)
            timer_placeholder.write(f"残り時間: {hours:02}:{minutes:02}:{seconds:02}")
            quote_placeholder.write(f"励ましの言葉: {st.session_state.motivational_quote}")
            time.sleep(1)
    else:
        st.warning("勉強時間を入力してください！")
else:
    st.info("チェックリストをすべて確認してください！")
