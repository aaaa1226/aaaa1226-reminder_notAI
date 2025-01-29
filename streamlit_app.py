import streamlit as st
import time
import random

# セッション状態の初期化
if 'timer_active' not in st.session_state:
    st.session_state.timer_active = False
if 'remaining_time' not in st.session_state:
    st.session_state.remaining_time = 0

# タイトルとメッセージ
st.title('勉強タイマー')
st.write('まずはスマホを置きましょう')

# 時間入力
hours = st.number_input('時間', min_value=0, max_value=23, value=0)
minutes = st.number_input('分', min_value=0, max_value=59, value=0)
seconds = st.number_input('秒', min_value=0, max_value=59, value=0)

# チェックボックス
phone_check = st.checkbox('スマホは置きましたか？このアプリをスマホで使っているなら、遠くにおいてスタートを押しましょう！')
desk_check = st.checkbox('机の上に気が散るものはないですか？')

# スタートボタン
if phone_check and desk_check and not st.session_state.timer_active:
    if st.button('準備はいいですか？'):
        st.session_state.timer_active = True
        st.session_state.remaining_time = hours * 3600 + minutes * 60 + seconds

        # カウントダウン
        for i in range(3, 0, -1):
            st.write(f'{i}...')
            time.sleep(1)
        st.write('スタート！')

# タイマー進行中の処理
if st.session_state.timer_active:
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

    placeholder = st.empty()
    message_placeholder = st.empty()

    while st.session_state.remaining_time > 0:
        mins, secs = divmod(st.session_state.remaining_time, 60)
        hours, mins = divmod(mins, 60)
        time_format = f'{hours:02d}:{mins:02d}:{secs:02d}'
        placeholder.header(f'残り時間: {time_format}')
        message_placeholder.write(random.choice(messages))

        time.sleep(1)
        st.session_state.remaining_time -= 1

        if st.button('ストップ'):
            stop_choice = st.radio('本当に辞めちゃうの…？', ('やめる', 'まだ頑張る'))
            if stop_choice == 'やめる':
                st.session_state.timer_active = False
                st.session_state.remaining_time = 0
                st.experimental_rerun()
            elif stop_choice == 'まだ頑張る':
                pass

    st.session_state.timer_active = False
    st.success('タイマー終了！お疲れ様でした！')
