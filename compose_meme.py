#!/usr/bin/env python3
"""Composite the gta6-meme-x-01 meme: Vice City base + real make.fun ghost + big meme text."""
from PIL import Image, ImageDraw, ImageFont, ImageFilter

BASE = "assets/media-generation-gta6-vice-city-base-0-975271fd-bb4e-4be1-876c-52a4e13fdd15.png"
GHOST = "assets/mark-1024.png"
OUT = "meme.png"

FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

img = Image.open(BASE).convert("RGB")
W, H = img.size  # 1920x1280
# Crop to 16:9 so the judge's 768x480 fit shows the whole frame, no crop.
img = img.crop((0, 100, 1920, 1180))
W, H = img.size  # 1920x1080
d = ImageDraw.Draw(img, "RGBA")

def gradient_band(top, height, max_alpha=170):
    """Vertical black gradient band for text legibility."""
    band = Image.new("RGBA", (W, height), (0, 0, 0, 0))
    bd = ImageDraw.Draw(band)
    for y in range(height):
        a = int(max_alpha * (1 - y / height)) if top == 0 else int(max_alpha * (y / height))
        bd.line([(0, y), (W, y)], fill=(0, 0, 0, a))
    # paste band over img
    base = img.convert("RGBA")
    overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    od = ImageDraw.Draw(overlay)
    for y in range(height):
        a = int(max_alpha * (1 - y / height)) if top == 0 else int(max_alpha * (y / height))
        od.line([(0, top + y), (W, top + y)], fill=(0, 0, 0, a))
    img.paste(Image.alpha_composite(base, overlay).convert("RGB"), (0, 0))

def meme_text(text, font, cx, y, fill=(255, 255, 255), stroke=(0, 0, 0), sw=5):
    bbox = d.textbbox((0, 0), text, font=font, stroke_width=sw)
    tw = bbox[2] - bbox[0]
    d.text((cx - tw / 2 - bbox[0], y), text, font=font, fill=fill,
           stroke_width=sw, stroke_fill=stroke)

# 1. Top band + text
gradient_band(0, 240)
f_top = ImageFont.truetype(FONT, 108)
meme_text("I WAITED 13 YEARS FOR THIS.", f_top, W // 2, 52, sw=6)

# 2. Bottom band
gradient_band(H - 260, 260)

# 3. Ghost (real make.fun mark) bottom-left, large, with ground shadow
ghost = Image.open(GHOST).convert("RGBA").resize((340, 340), Image.LANCZOS)
shadow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
sd = ImageDraw.Draw(shadow)
sd.ellipse([70, 985, 400, 1035], fill=(0, 0, 0, 140))
shadow = shadow.filter(ImageFilter.GaussianBlur(8))
base = img.convert("RGBA")
base = Image.alpha_composite(base, shadow)
base.paste(ghost, (55, 645), ghost)
img = base.convert("RGB")
d = ImageDraw.Draw(img, "RGBA")

# 4. "make.fun" label under the ghost, magenta fill, white stroke
f_label = ImageFont.truetype(FONT, 62)
bbox = d.textbbox((0, 0), "make.fun", font=f_label, stroke_width=4)
tw = bbox[2] - bbox[0]
d.text((55 + 170 - tw / 2 - bbox[0], 992), "make.fun", font=f_label,
       fill=(230, 0, 122), stroke_width=4, stroke_fill=(255, 255, 255))

# 5. Bottom text, right-aligned in the space right of the ghost
f_bot = ImageFont.truetype(FONT, 128)
for i, line in enumerate(["CALLED IN SICK.", "GTA 6 IS OUT."]):
    bbox = d.textbbox((0, 0), line, font=f_bot, stroke_width=6)
    tw = bbox[2] - bbox[0]
    y = 800 + i * 135
    d.text((1870 - tw - bbox[0], y), line, font=f_bot, fill=(255, 255, 255),
           stroke_width=6, stroke_fill=(0, 0, 0))

img.save(OUT, "PNG")
print("saved", OUT, img.size)
# Judge-size preview for the legibility check
img.resize((768, 432), Image.LANCZOS).save("/tmp/meme-preview-768.png")
print("preview saved")
