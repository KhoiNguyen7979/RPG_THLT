import pygame
import sys
from src.core.settings import *
from src.entities.enemy import Minion, Scout 
from src.core.ui import UI

# Khởi tạo Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("FSM Hunter - CTU Automata Project")
clock = pygame.time.Clock()
ui_manager = UI(screen)

# Khởi tạo nhóm kẻ địch
enemies = pygame.sprite.Group()
enemies.add(Minion(200, 300))
enemies.add(Scout(600, 150))
enemies.add(Minion(400, 500)) # Thêm thêm 1 con nữa cho vui mắt

player_hp = 100

while True:
    # 1. Xử lý sự kiện
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 2. Cập nhật logic
    # Mouse_pos đóng vai trò là vị trí của Player để test FSM
    mouse_pos = pygame.mouse.get_pos()
    enemies.update(mouse_pos) 

    # 3. Vẽ Scene
    screen.fill((40, 40, 40)) # Nền tối trung tính
    
    # Vẽ các thực thể (Nhân vật)
    enemies.draw(screen)
    
    # --- ĐIỂM CẦN BỔ SUNG: Vẽ Alert (Dấu !) cho từng kẻ địch ---
    for enemy in enemies:
        enemy.draw_alert(screen)
    
    # 4. Vẽ HUD và Giao diện lớp trên cùng
    if len(enemies.sprites()) > 0:
        # Chọn kẻ địch gần chuột nhất hoặc kẻ địch đầu tiên để hiển thị trạng thái FSM
        first_enemy = enemies.sprites()[0]
        ui_manager.draw_hud(player_hp, first_enemy.fsm)
        
        # Nếu muốn xem vòng tròn logic khi debug, hãy bỏ comment dòng dưới
        # ui_manager.draw_debug_info(first_enemy)

    pygame.display.flip()
    clock.tick(FPS)