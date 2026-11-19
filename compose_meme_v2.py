#!/usr/bin/env python3
"""Composite the gta6-meme-x-01 meme v2 (WASTED): slumped-wait scene + GTA WASTED text
+ real make.fun ghost in-scene. Text is composited with PIL (never baked by the
generator) so it stays razor-sharp at the judge's 768px shrink."""
from PIL import Image, ImageDraw, ImageFont, ImageFilter

BASE = "assets/media-generation-meme-wasted-scene-0-125bf1d3-0375-4c81-bc20-0abb0b30987b.webp"
GHOST = "assets/mark-1024.png"
OUT = "meme.png"

FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

img = Image.open(BASE).convert("RGB")
# Crop/resize to 1920x1080 (16:9).
w, h = img.size
target_ratio = 1920 / 1080
if w / h > target_ratio:
    nw = int(h * target_ratio)
    x0 = (w - nw) // 2
    img = img.crop((x0, 0, x0 + nw, h))
else:
    nh = int(w / target_ratio)
    y0 = (h - nh) // 2
    img = img.crop((0, y0, w, y0 + nh))
img = img.resize((1920, 1080), Image.LANCZOS)
W, H = img.size
d = ImageDraw.Draw(img, "RGBA")


def soft_band(y0, y1, max_alpha=110):
    """Soft dark band behind center text for legibility."""
    overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    od = ImageDraw.Draw(overlay)
    mid = (y0 + y1) // 2
    for y in range(y0, y1):
        dist = abs(y - mid) / max(1, (y1 - y0) / 2)
        a = int(max_alpha * (1 - dist))
        od.line([(0, y), (W, y)], fill=(0, 0, 0, a))
    base = img.convert("RGBA")
    img2 = Image.alpha_composite(base, overlay).convert("RGB")
    return img2


# 1. WASTED — giant, GTA-style: light grey fill, heavy black stroke, centered.
img = soft_band(300, 620)
d = ImageDraw.Draw(img, "RGBA")
f_wasted = ImageFont.truetype(FONT, 300)
text = "WASTED"
bbox = d.textbbox((0, 0), text, font=f_wasted, stroke_width=10)
tw = bbox[2] - bbox[0]
d.text((W // 2 - tw / 2 - bbox[0], 330), text, font=f_wasted,
       fill=(200, 200, 200), stroke_width=10, stroke_fill=(0, 0, 0))

# 2. Subtext under WASTED.
f_sub = ImageFont.truetype(FONT, 72)
sub = "13 YEARS WAITING FOR GTA 6"
bbox = d.textbbox((0, 0), sub, font=f_sub, stroke_width=5)
tw = bbox[2] - bbox[0]
d.text((W // 2 - tw / 2 - bbox[0], 640), sub, font=f_sub,
       fill=(255, 255, 255), stroke_width=5, stroke_fill=(0, 0, 0))

# 3. Ghost (real make.fun mark) bottom-left on the curb, with ground shadow.
ghost = Image.open(GHOST).convert("RGBA").resize((260, 260), Image.LANCZOS)
shadow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
sd = ImageDraw.Draw(shadow)
sd.ellipse([60, 985, 310, 1015], fill=(0, 0, 0, 150))
shadow = shadow.filter(ImageFilter.GaussianBlur(8))
base = img.convert("RGBA")
base = Image.alpha_composite(base, shadow)
base.paste(ghost, (45, 725), ghost)
img = base.convert("RGB")
d = ImageDraw.Draw(img, "RGBA")

# 4. "make.fun" label under the ghost.
f_label = ImageFont.truetype(FONT, 50)
bbox = d.textbbox((0, 0), "make.fun", font=f_label, stroke_width=4)
tw = bbox[2] - bbox[0]
d.text((45 + 130 - tw / 2 - bbox[0], 995), "make.fun", font=f_label,
       fill=(230, 0, 122), stroke_width=4, stroke_fill=(255, 255, 255))

img.save(OUT, "PNG")
print("saved", OUT, img.size)
img.resize((768, 432), Image.LANCZOS).save("/tmp/meme-v2-preview-768.png")
print("preview saved")
