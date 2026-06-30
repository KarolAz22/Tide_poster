# -*- coding: utf-8 -*-
"""Inline QR codes + links into the Tide poster/landing HTML.
Edit the two URLs below and re-run to regenerate."""
import io, base64, qrcode

# ======== CONFIG — edite aqui ========
PROTO_URL   = "https://chatbot-menopausa-pjsy4k7cw3nxkvdjbb88wj.streamlit.app/"
LANDING_URL = "https://TROQUE-PELO-LINK-DA-LANDING.exemplo"   # <- depois de hospedar, cole o link real e rode de novo
# =====================================

BASE = r"C:\Users\karol\Downloads\Tide_Poster"

def qr_datauri(url, fg="#13262B"):
    qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_M, box_size=16, border=2)
    qr.add_data(url); qr.make(fit=True)
    img = qr.make_image(fill_color=fg, back_color="white").convert("RGB")
    buf = io.BytesIO(); img.save(buf, format="PNG")
    return "data:image/png;base64," + base64.b64encode(buf.getvalue()).decode("ascii")

proto_uri   = qr_datauri(PROTO_URL)
landing_uri = qr_datauri(LANDING_URL, fg="#0A4A55")

def build(src, dst):
    with open(src, "r", encoding="utf-8") as f:
        html = f.read()
    html = (html.replace("__QR_PROTO__", proto_uri)
                .replace("__QR_LANDING__", landing_uri)
                .replace("__PROTO_URL__", PROTO_URL)
                .replace("__LANDING_URL__", LANDING_URL))
    with open(dst, "w", encoding="utf-8") as f:
        f.write(html)
    print("built", dst)

build(BASE + r"\tela.src.html",  BASE + r"\tela.html")
build(BASE + r"\index.src.html", BASE + r"\index.html")
print("PROTO_URL  =", PROTO_URL)
print("LANDING_URL=", LANDING_URL)
