import streamlit as st
import time
import random

def countdown_timer():
    if 'timer_running' not in st.session_state:
        st.session_state.timer_running = False
    
    if st.session_state.timer_running:
        if st.session_state.remaining_time > 0:
            mins, secs = divmod(st.session_state.remaining_time, 60)
            hours, mins = divmod(mins, 60)
            st.session_state.timer = f"{hours:02}:{mins:02}:{secs:02}"
            st.session_state.remaining_time -= 1
            time.sleep(1)
            st.experimental_rerun()
        else:
            st.session_state.timer_running = False
            st.session_state.timer = "00:00:00"
            st.session_state.message = "\U0001F389 勉強お疲れ様でした！\U0001F389"

def main():
    st.title("勉強タイマー ⏳")
    st.write("まずはスマホを置きましょう！")
    
    hours = st.number_input("時間", min_value=0, max_value=24, value=0, step=1)
    minutes = st.number_input("分", min_value=0, max_value=59, value=0, step=1)
    seconds = st.number_input("秒", min_value=0, max_value=59, value=0, step=1)
    
    confirm_phone = st.checkbox("スマホは置きましたか？このアプリをスマホで使っているなら、遠くにおいてスタートを押しましょう！")
    confirm_desk = st.checkbox("机の上に気が散るものはないですか？")
    
    if confirm_phone and confirm_desk:
        if st.button("準備はいいですか？スタート！"):
            total_seconds = hours * 3600 + minutes * 60 + seconds
            if total_seconds > 0:
                st.session_state.remaining_time = total_seconds
                st.session_state.timer_running = True
                st.session_state.timer = "00:00:00"
                st.session_state.message = ""
                st.experimental_rerun()
    
    st.write(f"### 残り時間: {st.session_state.get('timer', '00:00:00')}")
    countdown_timer()
    
    messages = [
        "何やってるんですか　勉強してください",
        "小さいことを重ねることが、とんでもない所に行くただ一つの道",
        "誰よりも三倍、四倍、五倍勉強するもの、それが天才だ",
        "あきらめたらそこで試合終了だよ",
        "失敗したから何なのだ、失敗から学び得て、また挑戦すればいいじゃないか",
        "どんな人だって成功できる。自分に何度もこの言葉をいい聞かせていれば、絶対に成功できる。",
        "成功が上がりでもなければ、失敗が終わりでもない。肝心なのは続ける勇気である。",
        "あきらめなければ必ず道はある。",
        "今日の成果は過去の努力の結果であり、未来はこれからの努力で決まる",
    ]
    
    if 'remaining_time' in st.session_state and st.session_state.remaining_time > 0:
        st.write(random.choice(messages))
    
    if 'message' in st.session_state:
        st.write(st.session_state.message)

if __name__ == "__main__":
    main()
