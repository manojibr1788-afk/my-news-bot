import google.generativeai as genai
import requests

# 1. आपकी सभी सीक्रेट चाबियाँ (बिल्कुल सही वाली)
TELEGRAM_TOKEN = "8116715672:AAFcmrhXOQ6tWkuCncy4Nts8iTf0dqBQbfY"
TELEGRAM_CHAT_ID = "616338549"
GEMINI_API_KEY = "AIzaSyDqaqir_-ZoxlcIiyrWOZXtgaYmqjC8TOw"

# 2. गूगल एआई को कॉन्फ़िगर करना (ऑफिशियल तरीका)
genai.configure(api_key=GEMINI_API_KEY)

# 3. टेस्ट के लिए एक मार्केट की खबर
MARKET_NEWS = "Reliance Q4 net profit jumps 15%, beating all market estimates. Management announces big expansion plans."

print("Gemini AI खबर का विश्लेषण कर रहा है... कृपया रुकें...")

try:
    # बिल्कुल सही और लेटेस्ट मॉडल का इस्तेमाल
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    prompt = f"You are a stock market expert. Analyze this news and give a short summary in Hindi for traders: {MARKET_NEWS}"
    response = model.generate_content(prompt)
    
    ai_analysis = response.text
    print("\n✅ Gemini AI का विश्लेषण सफल रहा!")
    print(ai_analysis)
    
    # 4. Telegram पर मैसेज भेजना
    print("\nTelegram पर मैसेज भेज रहा हूँ...")
    telegram_url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    telegram_payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": f"📊 *Market News Analysis*:\n\n{ai_analysis}",
        "parse_mode": "Markdown"
    }
    
    tele_response = requests.post(telegram_url, json=telegram_payload)
    if tele_response.status_code == 200:
        print("🚀 Telegram पर मैसेज सफलतापूर्वक चला गया!")
    else:
        print(f"❌ Telegram एरर: {tele_response.text}")

except Exception as e:
    print(f"❌ कुछ गड़बड़ हुई: {e}")
