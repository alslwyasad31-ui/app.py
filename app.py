import os, requests, urllib.parse
from flask import Flask, render_template_string, request, jsonify
from googletrans import Translator

app = Flask(__name__)

# إعدادات المحرك - Pexels Key
PEXELS_KEY = "Imi4SXQRyfMPbc8lgtiFk4e8eyOOLQBqf3pxXyoXmH7zTFR6WB2t5mxv"
translator = Translator()

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ADFORCE AI V26.0 - Render Deploy</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        :root { --blue: #00d2ff; --bg: #0d1117; --card: #161b22; --border: #30363d; --green: #238636; }
        body { background: var(--bg); color: white; font-family: sans-serif; padding: 10px; margin: 0; }
        .container { max-width: 450px; margin: auto; background: var(--card); padding: 20px; border-radius: 15px; border: 1px solid var(--border); }
        h3 { text-align: center; color: var(--blue); font-size: 14px; margin-bottom: 15px; }
        input, select { width: 100%; padding: 12px; margin: 5px 0; background: #010409; border: 1px solid var(--border); color: white; border-radius: 8px; box-sizing: border-box; outline: none; }
        .row { display: flex; gap: 10px; }
        .btn-pixels { background: var(--green); color: white; border: none; width: 100%; padding: 15px; border-radius: 8px; font-weight: bold; cursor: pointer; margin-top: 10px; font-size: 16px; }
        .video-box { position: relative; width: 100%; border-radius: 12px; overflow: hidden; display: none; border: 2px solid var(--blue); margin-top: 20px; background: #000; }
        video { width: 100%; display: block; }
        .price-tag { position: absolute; bottom: 15px; right: 15px; background: #ff0000; color: white; padding: 5px 15px; border-radius: 50px; font-weight: bold; z-index: 5; }
        .platforms { display: grid; grid-template-columns: repeat(4, 1fr); gap: 8px; margin-top: 20px; border-top: 1px solid var(--border); padding-top: 15px; }
        .platforms button { background: #21262d; border: 1px solid var(--border); color: var(--blue); padding: 12px; border-radius: 8px; cursor: pointer; font-size: 18px; transition: 0.3s; }
        .platforms button:hover { background: var(--blue); color: white; transform: scale(1.1); }
    </style>
</head>
<body>
    <div class="container">
        <h3>ADFORCE AI V26.0 - نظام المشاركة السحابي</h3>
        <input type="text" id="pName" placeholder="وصف المنتج (مثلاً: Luxury Rolex Watch)">
        <div class="row">
            <select id="country">
                <option value="🇾🇪 اليمن">اليمن 🇾🇪</option>
                <option value="🇸🇦 السعودية">السعودية 🇸🇦</option>
            </select>
            <input type="text" id="pPrice" placeholder="السعر">
        </div>
        <input type="text" id="pPhone" value="+967779221711" placeholder="رقم الهاتف">
        <button class="btn-pixels" onclick="startEngine()">توليد ومطابقة دقيقة 🎥</button>
        <div class="video-box" id="vBox">
            <div class="price-tag" id="resPrice"></div>
            <video id="vPlayer" autoplay muted loop playsinline></video>
        </div>
        <div class="platforms">
            <button onclick="directShare('whatsapp')"><i class="fab fa-whatsapp"></i></button>
            <button onclick="directShare('facebook')"><i class="fab fa-facebook"></i></button>
            <button onclick="directShare('telegram')"><i class="fab fa-telegram"></i></button>
            <button onclick="directShare('twitter')"><i class="fab fa-twitter"></i></button>
            <button onclick="directShare('messenger')"><i class="fab fa-facebook-messenger"></i></button>
            <button onclick="directShare('linkedin')"><i class="fab fa-linkedin"></i></button>
            <button onclick="directShare('reddit')"><i class="fab fa-reddit"></i></button>
            <button onclick="directShare('pinterest')"><i class="fab fa-pinterest"></i></button>
            <button onclick="directShare('tiktok')"><i class="fab fa-tiktok"></i></button>
            <button onclick="directShare('instagram')"><i class="fab fa-instagram"></i></button>
            <button onclick="directShare('snapchat')"><i class="fab fa-snapchat"></i></button>
            <button onclick="directShare('youtube')"><i class="fab fa-youtube"></i></button>
            <button onclick="directShare('sms')"><i class="fas fa-sms"></i></button>
            <button onclick="directShare('email')"><i class="fas fa-envelope"></i></button>
            <button onclick="directShare('copy')"><i class="fas fa-copy"></i></button>
            <button onclick="window.print()"><i class="fas fa-print"></i></button>
        </div>
    </div>
    <script>
        let videoUrl = "";
        async function startEngine() {
            const name = document.getElementById('pName').value;
            if(!name) return alert("أدخل الوصف");
            const res = await fetch('/api/v26_engine', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({ name })
            });
            const data = await res.json();
            if(data.success) {
                document.getElementById('resPrice').innerText = document.getElementById('pPrice').value;
                document.getElementById('vPlayer').src = data.video;
                videoUrl = data.video;
                document.getElementById('vBox').style.display = 'block';
            }
        }
        function directShare(platform) {
            if(!videoUrl) return alert("يرجى توليد الفيديو أولاً");
            const phone = document.getElementById('pPhone').value;
            const price = document.getElementById('pPrice').value;
            const msg = `عرض رائع! السعر: ${price}. للتواصل: ${phone} \\n الرابط: ${videoUrl}`;
            const urls = {
                whatsapp: `https://api.whatsapp.com/send?phone=${phone.replace('+', '')}&text=${encodeURIComponent(msg)}`,
                facebook: `https://www.facebook.com/sharer/sharer.php?u=${encodeURIComponent(videoUrl)}`,
                telegram: `https://t.me/share/url?url=${encodeURIComponent(videoUrl)}&text=${encodeURIComponent(msg)}`,
                twitter: `https://twitter.com/intent/tweet?text=${encodeURIComponent(msg)}`,
                messenger: `fb-messenger://share/?link=${encodeURIComponent(videoUrl)}`,
                sms: `sms:${phone}?body=${encodeURIComponent(msg)}`,
                email: `mailto:?subject=طلب منتج&body=${encodeURIComponent(msg)}`
            };
            if(urls[platform]) window.open(urls[platform], '_blank');
            else if(platform === 'copy') { navigator.clipboard.writeText(msg); alert("تم نسخ النص والرابط!"); }
            else { navigator.clipboard.writeText(videoUrl); alert("تم نسخ الرابط. سيتم فتح " + platform + " الآن."); window.open(`https://www.${platform}.com`, '_blank'); }
        }
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

@app.route('/api/v26_engine', methods=['POST'])
def v26_engine():
    data = request.json
    trans = translator.translate(data['name'], src='ar', dest='en').text
    strict_query = f"{trans} product only, isolated, no office, no keyboard, cinematic lighting"
    headers = {"Authorization": PEXELS_KEY}
    v_res = requests.get(f"https://api.pexels.com/videos/search?query={urllib.parse.quote(strict_query)}&per_page=1", headers=headers).json()
    video = v_res['videos'][0]['video_files'][0]['link'] if v_res.get('videos') else ""
    return jsonify({"success": True, "video": video})

if __name__ == '__main__':
    # تعديل المنفذ ليتوافق مع Render
    port = int(os.environ.get("PORT", 8003))
    app.run(host='0.0.0.0', port=port)