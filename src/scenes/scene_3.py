import pygame
from src.core.settings import *

class Scene3:
    def __init__(self, scene_manager):
        self.scene_manager = scene_manager
        
        self.font = pygame.font.SysFont("Arial", 40, bold=True)
        self.small_font = pygame.font.SysFont("Arial", 25)
        
        # 1. Nạp ảnh winner.png
        try:
            self.winner_img = pygame.image.load("assets/graphics/Map/Scene3/winner.png").convert_alpha()
            self.winner_img = pygame.transform.scale(self.winner_img, (SCREEN_WIDTH, SCREEN_HEIGHT))
        except Exception as e:
            print(f"Lỗi nạp ảnh winner.png: {e}")
            self.winner_img = None

        # 2. Biến đếm thời gian (60 FPS * 10 giây = 600 frames)
        self.display_timer = 600 

    def reset(self):
        self.display_timer = 600

    def update(self, events):
        # Giảm biến đếm mỗi frame
        if self.display_timer > 0:
            self.display_timer -= 1
        else:
            # Sau 10 giây thì thoát game
            pygame.quit()
            import sys
            sys.exit()

        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                # Nếu người chơi muốn chơi lại ngay lập tức mà không đợi 10s
                self.scene_manager.switch_scene("Scene1")

    def draw(self, screen):
        # Vẽ ảnh Winner làm nền
        if self.winner_img:
            screen.blit(self.winner_img, (0, 0))
        else:
            screen.fill((50, 40, 20)) 

        #subtitle = self.small_font.render("Nhấn ENTER để chơi lại ngay.", True, WHITE)
        #screen.blit(subtitle, (SCREEN_WIDTH // 2 - subtitle.get_width() // 2, 500))s