# -*- coding: utf-8 -*-
"""Gera os assets (QR codes + fotos otimizadas) em img/ e monta index.html / tela.html.
As imagens são referenciadas por arquivo (img/...), não mais embutidas em base64."""
import os, qrcode
from PIL import Image

# ======== CONFIG — edite aqui ========
PROTO_URL   = "https://chatbot-menopausa-pjsy4k7cw3nxkvdjbb88wj.streamlit.app/"
LANDING_URL = "https://karolaz22.github.io/Tide_poster/"
# fotos: nome de saída (referenciado no site) -> arquivo de origem em img/
PHOTOS = [("karolina.jpg", "karolina.jpg"),
          ("mirella.jpg",  "mirella.png"),
          ("michele.jpg",  "michele.png"),
          ("leticia.jpg",  "leticia.png")]
# =====================================

BASE = r"C:\Users\karol\OneDrive\Documentos\Tide_Poster"
IMG  = os.path.join(BASE, "img")

def save_qr(url, path, fg="#0A4A55"):
    qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_M, box_size=16, border=2)
    qr.add_data(url); qr.make(fit=True)
    qr.make_image(fill_color=fg, back_color="white").convert("RGB").save(path)
    print("  QR:", os.path.basename(path))

def optimize_photo(out_name, src_name, size=320):
    src = os.path.join(IMG, src_name); out = os.path.join(IMG, out_name)
    if not os.path.exists(src):
        if os.path.exists(out): print("  foto ok (mantida):", out_name); return
        print("  !! fonte ausente:", src_name); return
    im = Image.open(src).convert("RGB")
    w, h = im.size; s = min(w, h)
    im = im.crop(((w-s)//2, (h-s)//2, (w-s)//2 + s, (h-s)//2 + s)).resize((size, size))
    im.save(out, format="JPEG", quality=82)
    print("  foto:", out_name, str(os.path.getsize(out)//1024) + " KB")

print("Gerando assets em img/ ...")
save_qr(PROTO_URL,   os.path.join(IMG, "qr_prototipo.png"), "#13262B")
save_qr(LANDING_URL, os.path.join(IMG, "qr_landing.png"),   "#0A4A55")
for out_name, src_name in PHOTOS:
    optimize_photo(out_name, src_name)

def build(src, dst):
    html = open(src, encoding="utf-8").read()
    html = html.replace("__PROTO_URL__", PROTO_URL).replace("__LANDING_URL__", LANDING_URL)
    open(dst, "w", encoding="utf-8").write(html)
    print("built", os.path.basename(dst))

build(os.path.join(BASE, "tela.src.html"),  os.path.join(BASE, "tela.html"))
build(os.path.join(BASE, "index.src.html"), os.path.join(BASE, "index.html"))
print("OK")
