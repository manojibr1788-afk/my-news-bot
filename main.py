import os
from flask import Flask
import requests

app = Flask(__name__)

# आपकी वर्किंग चाबियाँ
TELEGRAM_TOKEN = "8116715672:AAFcmrhXOQ6tWkuCncy4Nts8iTf0dqBQbfY"
TELEGRAM_CHAT_ID = "616338549"
import os
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")

@app.route('/')
def home():
    # यह सैंपल न्यूज़ है जो टेस्ट के लिए टेलीग्राम पर जाएगी
    MARKET_NEWS = "Reliance Q4 net profit jumps 15%, beating all market estimates. Management announces big expansion plans."
    
    # गूगल जेमिनी का लेटेस्ट स्टेबल एंडपॉइंट
    gemini_url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={GEMINI_API_KEY}"
    gemini_payload = {
        "contents": [{
            "parts": [{
                "text": f"Analyze this stock market news and give a 1-line sharp summary in Hindi stating if it is Bullish, Bearish, or Neutral for Nifty. News: {MARKET_NEWS}"
            }]
        }]
    }
    
    try:
        gemini_response = requests.post(gemini_url, json=gemini_payload)
        gemini_data = gemini_response.json()
        
        if 'candidates' in gemini_data:
            ai_analysis = gemini_data['candidates'][0]['content']['parts'][0]['text'].strip()
            
            # टेलीग्राम पर मैसेज भेजने का लॉजिक
            telegram_url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
            telegram_payload = {
                "chat_id": TELEGRAM_CHAT_ID,
                "text": f"🤖 *AI न्यूज़ फ़िल्टर अलर्ट*\n\n📰 *खबर:* {MARKET_NEWS}\n\n🧠 *AI का विश्लेषण:* {ai_analysis}",
                "parse_mode": "Markdown"
            }
            requests.post(telegram_url, json=telegram_payload)
            return f"🎉 सफलता! टेलीग्राम पर मैसेज भेज दिया गया है। AI का जवाब: {ai_analysis}"
        else:
            return f"❌ जेमिनी एरर: {gemini_data}"
    except Exception as e:
        return f"❌ गड़बड़ हुई भाई: {str(e)}"

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
