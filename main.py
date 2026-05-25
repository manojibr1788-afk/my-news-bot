import requests

# 1. आपकी सीक्रेट चाबियाँ (बिल्कुल सही वाली सेट हैं भाई)
TELEGRAM_TOKEN = "8116715672:AAFcmrhXOQ6tWkuCncy4Nts8iTf0dqBQbfY"
TELEGRAM_CHAT_ID = "616338549"
GEMINI_API_KEY = "AIzaSyDqaqir_-ZoxlcIiyrWOZXtgaYmqjC8TOw"

# 2. टेस्ट के लिए एक मार्केट की खबर (Sample News)
MARKET_NEWS = "Reliance Q4 net profit jumps 15%, beating all market estimates. Management announces big expansion plans."

print("Gemini AI खबर का विश्लेषण कर रहा है... कृपया रुकें...")

# 3. Gemini AI को news भेजना (यहाँ v1beta को बदलकर स्टेबल v1 और सही API Key सेट कर दी है)
gemini_url = f"https://generativelanguage.googleapis.com/v1/models/gemini-1.5-flash:generateContent?key={GEMINI_API_KEY}"

gemini_payload = {
    "contents": [{
        "parts": [{
            "text": f"You are a stock market expert. Analyze this news and give a short summary in Hindi for traders: {MARKET_NEWS}"
        }]
    }]
}

try:
    response = requests.post(gemini_url, json=gemini_payload)
    result = response.json()
    
    if response.status_code == 200:
        # AI का जवाब निकालना
        ai_analysis = result['candidates'][0]['content']['parts'][0]['text']
        print("\n✅ Gemini AI का विश्लेषण:")
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
            
    else:
        print(f"❌ Google AI की तरफ से एरर आया है:")
        print(f"मेसेज: {result.get('error', {}).get('message', 'Unknown Error')}")

except Exception as e:
    print(f"❌ कुछ गड़बड़ हुई: {e}")
