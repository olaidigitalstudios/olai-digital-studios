import os
from PIL import Image, ImageDraw, ImageFont

# Dimensions and Palettes
BG_COLOR = (12, 13, 14)       # #0C0D0E Void
GOLD_COLOR = (229, 184, 105)   # #E5B869 Accent Gold
WHITE_COLOR = (250, 250, 249)  # #FAFAF9 Stone 100
MUTED_COLOR = (168, 162, 158)  # #A8A29E Stone 400
BORDER_COLOR = (40, 42, 48)    # border

FONTS_DIR = "C:/Windows/Fonts"
SERIF_BOLD = os.path.join(FONTS_DIR, "georgiab.ttf")
SERIF_REG = os.path.join(FONTS_DIR, "georgia.ttf")
SANS_BOLD = os.path.join(FONTS_DIR, "arialbd.ttf")
SANS_REG = os.path.join(FONTS_DIR, "arial.ttf")

# 1. Generate apple-touch-icon.png (180x180)
size = (180, 180)
icon = Image.new("RGBA", size, BG_COLOR)
draw = ImageDraw.Draw(icon)

# Draw gold inner border / emblem
draw.rounded_rectangle([(8, 8), (171, 171)], radius=36, outline=(229, 184, 105, 75), width=2)
# Draw central stylized 'O'
font_icon = ImageFont.truetype(SERIF_BOLD, 92)
draw.text((90, 84), "O", fill=GOLD_COLOR, font=font_icon, anchor="mm")
# Small studio dot in gold
draw.ellipse([(87, 136), (93, 142)], fill=GOLD_COLOR)

icon.convert("RGB").save("public/apple-touch-icon.png", format="PNG")
icon.resize((32, 32), Image.Resampling.LANCZOS).convert("RGBA").save("public/favicon.ico", format="ICO")
print("Generated apple-touch-icon.png and favicon.ico")

# 2. Update favicon.svg
svg_content = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32" fill="none">
  <rect width="32" height="32" rx="8" fill="#0C0D0E"/>
  <rect x="2" y="2" width="28" height="28" rx="6" stroke="#E5B869" stroke-width="1" stroke-opacity="0.3"/>
  <text x="16" y="22" font-family="Georgia, serif" font-size="18" font-weight="bold" fill="#E5B869" text-anchor="middle">O</text>
  <circle cx="16" cy="27" r="1" fill="#E5B869"/>
</svg>'''

with open("public/favicon.svg", "w", encoding="utf-8") as f:
    f.write(svg_content)
print("Updated favicon.svg")

# 3. Generate og-banner.png (1200 x 630)
W, H = 1200, 630
og = Image.new("RGB", (W, H), BG_COLOR)
og_draw = ImageDraw.Draw(og)

# Delicate geometric framing
og_draw.rectangle([(40, 40), (W - 40, H - 40)], outline=(255, 255, 255, 18), width=1)
og_draw.rectangle([(56, 56), (W - 56, H - 56)], outline=(229, 184, 105, 35), width=1)

# Subtle corner accents
corner_len = 24
for cx, cy in [(56, 56), (W - 56, 56), (56, H - 56), (W - 56, H - 56)]:
    dx = corner_len if cx == 56 else -corner_len
    dy = corner_len if cy == 56 else -corner_len
    og_draw.line([(cx, cy), (cx + dx, cy)], fill=GOLD_COLOR, width=2)
    og_draw.line([(cx, cy), (cx, cy + dy)], fill=GOLD_COLOR, width=2)

# Central Emblem / Brand Text
font_brand_main = ImageFont.truetype(SERIF_BOLD, 88)
font_brand_sub = ImageFont.truetype(SERIF_REG, 26)
font_meta = ImageFont.truetype(SANS_BOLD, 15)
font_location = ImageFont.truetype(SANS_REG, 15)

# Studio Title
og_draw.text((W // 2, 230), "OLAI", fill=WHITE_COLOR, font=font_brand_main, anchor="mm")
og_draw.text((W // 2, 310), "DIGITAL  STUDIOS", fill=GOLD_COLOR, font=font_brand_sub, anchor="mm")

# Divider line
div_w = 80
og_draw.line([(W // 2 - div_w, 360), (W // 2 + div_w, 360)], fill=(229, 184, 105, 120), width=1)

# Tagline / Studio Description
og_draw.text((W // 2, 405), "INDEPENDENT GAME DEVELOPMENT STUDIO", fill=WHITE_COLOR, font=font_meta, anchor="mm")
og_draw.text((W // 2, 435), "Mobile & Arcade Experiences • Based in Chennai, India", fill=MUTED_COLOR, font=font_location, anchor="mm")

# Bottom status badge
badge_text = "play.google.com  •  olaidigitalstudios.itch.io"
og_draw.text((W // 2, 530), badge_text, fill=(120, 113, 108), font=font_location, anchor="mm")

og.save("public/og-banner.png", format="PNG", optimize=True)
print("Generated public/og-banner.png (1200x630)")
