import pygame

def load_spritesheet(filename, rows, cols):
    # Load ảnh và hỗ trợ độ trong suốt
    sheet = pygame.image.load(filename).convert_alpha()
    
    # Tính toán kích thước mỗi ô (frame)
    frame_width = sheet.get_width() // cols
    frame_height = sheet.get_height() // rows
    
    sprites = []
    for r in range(rows):
        row_frames = []
        for c in range(cols):
            # Xác định vùng cắt
            rect = pygame.Rect(c * frame_width, r * frame_height, frame_width, frame_height)
            # Cắt ảnh con từ ảnh gốc
            frame = sheet.subsurface(rect)
            row_frames.append(frame)
        sprites.append(row_frames)
    return sprites