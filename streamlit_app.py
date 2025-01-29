import streamlit as st
import time
import random

# ランダムなメッセージを設定
messages = [
    "何やってるんですか 勉強してください",
    "小さいことを重ねることが、とんでもない所に行くただ一つの道",
    "誰よりも三倍、四倍、五倍勉強するもの、それが天才だ",
    "あきらめたらそこで試合終了だよ",
    "失敗したから何なのだ、失敗から学び得て、また挑戦すればいいじゃないか",
    "どんな人だって成功できる。自分に何度もこの言葉をいい聞かせていれば、絶対に成功できる。",
    "成功が上がりでもなければ、失敗が終わりでもない。肝心なのは続ける勇気である。",
    "あきらめなければ必ず道はある。",
    "今日の成果は過去の努力の結果であり、未来はこれからの努力で決まる"
]

# タイトルの表示
st.title("勉強のタイマーアプリ")

# 勉強時間の入力
st.write("まずはスマホを置きましょう")

hours = st.number_input("時間を入力してください", min_value=0, format="%d")
minutes = st.number_input("分を入力してください", min_value=0, format="%d")
seconds = st.number_input("秒を入力してください", min_value=0, format="%d")

# チェックボックス
smartphone_check = st.checkbox("スマホは置きましたか？このアプリをスマホで使っているなら、遠くにおいてスタートを押しましょう！")
distract_free_check = st.checkbox("机の上に気が散るものはないですか？")

# 準備完了かどうかを確認
if smartphone_check and distract_free_check:
    if st.button("準備はいいですか？"):

        # カウントダウン 3, 2, 1, Start
        for i in range(3, 0, -1):
            st.write(f"{i}")
            time.sleep(1)

        st.write("スタート")

        # タイマー計測の開始
        total_seconds = hours * 3600 + minutes * 60 + seconds
        start_time = time.time()

        stop_timer = False

        while total_seconds > 0:
            elapsed_time = int(time.time() - start_time)
            remaining_time = total_seconds - elapsed_time

            if stop_timer:
                break

            # 残り時間を表示
            st.write(f"残り時間: {remaining_time // 3600:02}:{(remaining_time % 3600) // 60:02}:{remaining_time % 60:02}")

            # ランダムなメッセージの表示
            st.write(random.choice(messages))

            time.sleep(1)

            if st.button("ストップ"):
                stop_timer = True

                if st.radio("本当に辞めちゃうの…？", ("やめる", "まだ頑張る")) == "やめる":
                    break
                else:
                    start_time = time.time() - elapsed_time
                    stop_timer = False

        st.write("タイマー終了")

else:
    st.write("チェックを入れてからスタートボタンを押してください。")