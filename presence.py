
import time
import discordrpc
from discordrpc import Activity

# ==================================
# Discord Application ID
# ==================================
APP_ID = 1566750842470531093

# ==================================
# GIFのURL
# ==================================
LARGE_GIF = (
    "https://raw.githubusercontent.com/THOR11186/"
    "discord-presence/main/large.gif"
)

SMALL_GIF = (
    "https://raw.githubusercontent.com/THOR11186/"
    "discord-presence/main/small.gif"
)

# ==================================
# Rich Presence設定
# ==================================

rpc = discordrpc.RPC(app_id=APP_ID)

rpc.set_activity(
    name="My Custom Presence",

    act_type=Activity.Playing,

    details="アークナイツ",
    state="アークナイツをプレイ中",

    # 大きいGIF
    large_image=LARGE_GIF,
    large_text="君を信じよう。",

    # 小さいGIF
    small_image=SMALL_GIF,
    small_text="君を信じよう。",

    # 経過時間
    ts_start=int(time.time())
)

print("Rich Presenceを起動しました！")
print("Discordを確認してください。")
print("終了するには Ctrl + C")

try:
    rpc.run()

except KeyboardInterrupt:
    print("Rich Presenceを終了します。")

finally:
    try:
        rpc.clear()
        rpc.disconnect()
    except Exception:
        pass
