import requests
import os

def main(context):
    context.log("✅ اجرای فانکشن آغاز شد")

    BOT_TOKEN = os.environ.get("Bale_BOT_TOKEN")
    CHAT_ID = 1423205711  # شناسهٔ خودت در Bale

    if not BOT_TOKEN or not CHAT_ID:
        context.error("❌ Bot token یا chat_id موجود نیست")
        return context.res.text("توکن یا چت آیدی تنظیم نیست")

    try:
        response = requests.post(
            f"https://tapi.bale.ai/bot{BOT_TOKEN}/sendMessage",
            json={
                "chat_id": CHAT_ID,
                "text": "✅ پیام تستی از Appwrite به Bale ارسال شد!"
            }
        )
        context.log("📤 پاسخ Bale:", response.text)
        return context.res.text("پیام ارسال شد")
    except Exception as e:
        context.error(f"❌ خطا در ارسال پیام: {str(e)}")
        return context.res.text("ارسال پیام ناموفق بود")
