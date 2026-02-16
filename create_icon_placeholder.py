from PIL import Image, ImageDraw
import os

def create_placeholder_icon():
    # Create 256x256 image with dark background
    img = Image.new('RGB', (256, 256), color='#1A1A1A')
    draw = ImageDraw.Draw(img)

    # Draw cyan square (registry cube placeholder)
    margin = 50
    draw.rectangle([margin, margin, 256-margin, 256-margin], fill='#00FFFF')

    # Draw simple blue shape (code symbol placeholder)
    # Just a diagonal line for slash
    draw.line([(160, 200), (210, 50)], fill='#0077FF', width=20)
    
    # Draw simple orange line (arrow placeholder)
    draw.line([(40, 180), (220, 180)], fill='#FFA500', width=10)

    # Save as .ico
    target_path = 'src/regutility/assets/icon.ico'
    img.save(target_path, format='ICO', sizes=[(256, 256), (128, 128), (64, 64), (48, 48), (32, 32), (16, 16)])
    print(f"Created placeholder icon at {target_path}")

if __name__ == '__main__':
    create_placeholder_icon()
