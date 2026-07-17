# -*- coding: utf-8 -*-
"""Inline QR codes + institutional logos into the A0 poster. Edit URLs/paths and re-run."""
import io, base64, qrcode

# ======== CONFIG — edite aqui ========
DEMO_URL     = "https://chatbot-menopausa-pjsy4k7cw3nxkvdjbb88wj.streamlit.app/"
PROJETO_URL  = "https://karolaz22.github.io/Tide_poster/"                       # landing page do projeto
LINKEDIN_URL = "https://www.linkedin.com/in/karol-azevedo-b721931aa/"
LOGO_UFMG    = r"C:\Users\karol\Downloads\logo ufmg.png"
LOGO_SBC     = r"C:\Users\karol\Downloads\Logo_SBC_Transparente.jpeg"
# =====================================

BASE = r"C:\Users\karol\OneDrive\Documentos\Tide_Poster"

def qr_datauri(url, fg="#0A4A55"):
    qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_M, box_size=16, border=2)
    qr.add_data(url); qr.make(fit=True)
    img = qr.make_image(fill_color=fg, back_color="white").convert("RGB")
    buf = io.BytesIO(); img.save(buf, format="PNG")
    return "data:image/png;base64," + base64.b64encode(buf.getvalue()).decode("ascii")

def img_datauri(path):
    ext = path.lower().rsplit(".", 1)[-1]
    mime = "image/png" if ext == "png" else "image/jpeg"
    with open(path, "rb") as f:
        return f"data:{mime};base64," + base64.b64encode(f.read()).decode("ascii")

with open(BASE + r"\poster.src.html", encoding="utf-8") as f:
    html = f.read()
html = (html.replace("__QR_DEMO__",     qr_datauri(DEMO_URL))
            .replace("__QR_PROJETO__",  qr_datauri(PROJETO_URL))
            .replace("__QR_LINKEDIN__", qr_datauri(LINKEDIN_URL))
            .replace("__DEMO_URL__",    DEMO_URL)
            .replace("__LOGO_UFMG__",   img_datauri(LOGO_UFMG))
            .replace("__LOGO_SBC__",    img_datauri(LOGO_SBC)))
with open(BASE + r"\poster.html", "w", encoding="utf-8") as f:
    f.write(html)
print("built poster.html")
