from PIL import Image, ImageDraw

def create_scroll_icon_enhanced():
    size = 256
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Colores
    gold = (255, 215, 0)
    dark_gold = (184, 134, 11)
    brown = (139, 90, 43)
    cream = (255, 253, 208)
    
    # Círculo de fondo oscuro
    draw.ellipse([10, 10, 246, 246], fill=(20, 20, 20), outline=gold, width=8)
    draw.ellipse([30, 30, 226, 226], fill=(30, 30, 30), outline=dark_gold, width=4)
    
    # Cilindro izquierdo
    draw.rectangle([60, 80, 90, 176], fill=brown, outline=dark_gold, width=3)
    draw.ellipse([60, 70, 90, 90], fill=brown, outline=dark_gold, width=2)
    draw.ellipse([60, 166, 90, 186], fill=brown, outline=dark_gold, width=2)
    
    # Cilindro derecho
    draw.rectangle([166, 80, 196, 176], fill=brown, outline=dark_gold, width=3)
    draw.ellipse([166, 70, 196, 90], fill=brown, outline=dark_gold, width=2)
    draw.ellipse([166, 166, 196, 186], fill=brown, outline=dark_gold, width=2)
    
    # Pergamino central
    draw.rectangle([85, 85, 171, 171], fill=cream, outline=brown, width=4)
    
    # Flecha arriba
    draw.polygon([(128, 100), (118, 115), (138, 115)], fill=gold, outline=dark_gold, width=2)
    
    # Flecha abajo
    draw.polygon([(128, 156), (118, 141), (138, 141)], fill=gold, outline=dark_gold, width=2)
    
    # Línea central
    draw.line([(128, 118), (128, 138)], fill=gold, width=4)
    
    # Guardar con TODOS los tamaños de Windows
    sizes = [(256, 256), (128, 128), (96, 96), (64, 64), (48, 48), (32, 32), (24, 24), (16, 16)]
    img.save('wow_scroll.ico', format='ICO', sizes=sizes)
    
    print("✅ wow_scroll.ico creado con todos los tamaños")
    print(f"📏 Tamaños incluidos: {sizes}")
    
    # Verificar que se creó
    import os
    if os.path.exists('wow_scroll.ico'):
        file_size = os.path.getsize('wow_scroll.ico')
        print(f"📦 Tamaño del archivo: {file_size} bytes")
        if file_size > 1000:
            print("✅ Archivo válido")
        else:
            print("❌ Archivo muy pequeño, puede estar corrupto")
    else:
        print("❌ ERROR: No se creó el archivo")

if __name__ == "__main__":
    create_scroll_icon_enhanced()