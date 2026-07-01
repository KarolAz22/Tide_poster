# -*- coding: utf-8 -*-
"""Inline the 3 QR codes into the A0 poster. Edit the URLs and re-run."""
import io, base64, qrcode

# ======== CONFIG — edite aqui ========
DEMO_URL     = "https://chatbot-menopausa-pjsy4k7cw3nxkvdjbb88wj.streamlit.app/"
GITHUB_URL   = "https://github.com/SEU-USUARIO/menopausa-informada"     # <- troque pelo link real
LINKEDIN_URL = "https://www.linkedin.com/in/SEU-PERFIL"                 # <- troque pelo link real
# =====================================

BASE = r"C:\Users\karol\Downloads\Tide_Poster"

def qr_datauri(url, fg="#12315C"):
    qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_M, box_size=16, border=2)
    qr.add_data(url); qr.make(fit=True)
    img = qr.make_image(fill_color=fg, back_color="white").convert("RGB")
    buf = io.BytesIO(); img.save(buf, format="PNG")
    return "data:image/png;base64," + base64.b64encode(buf.getvalue()).decode("ascii")

with open(BASE + r"\poster.src.html", encoding="utf-8") as f:
    html = f.read()
html = (html.replace("__QR_DEMO__",     qr_datauri(DEMO_URL))
            .replace("__QR_GITHUB__",   qr_datauri(GITHUB_URL))
            .replace("__QR_LINKEDIN__", qr_datauri(LINKEDIN_URL))
            .replace("__DEMO_URL__",    DEMO_URL))
with open(BASE + r"\poster.html", "w", encoding="utf-8") as f:
    f.write(html)
print("built poster.html")
print("DEMO   =", DEMO_URL)
print("GITHUB =", GITHUB_URL)
print("LINKEDIN =", LINKEDIN_URL)
