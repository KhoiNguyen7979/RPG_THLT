import pygame
from src.core.settings import *

class UI:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.SysFont("Arial", 20, bold=True)
        self.state_colors = {
            "PATROL": GREEN,
            "CHASE": (255, 165, 0), # Màu cam
            "ATTACK": RED,
            "DEAD": GRAY
        }

    def draw_hud(self, player_hp, enemy_fsm):
        # 1. Vẽ thanh máu Player (Góc trên bên trái)
        pygame.draw.rect(self.screen, (50, 50, 50), (20, 20, 200, 20))
        pygame.draw.rect(self.screen, (0, 200, 0), (20, 20, player_hp * 2, 20))
        
        # 2. Hiển thị trạng thái Automata hiện tại
        current_state = enemy_fsm.get_current_state()
        color = self.state_colors.get(current_state, WHITE)
        
        # Vẽ khung nền cho Text trạng thái
        pygame.draw.rect(self.screen, (30, 30, 30), (580, 15, 200, 35), border_radius=5)
        state_surface = self.font.render(f"FSM STATE: {current_state}", True, color)
        self.screen.blit(state_surface, (595, 22))

    def draw_debug_info(self, enemy):
        # Vẽ vòng tròn bán kính nhận diện (chỉ dùng khi báo cáo)
        pygame.draw.circle(self.screen, (150, 150, 150), enemy.rect.center, CHASE_RADIUS, 1)
        pygame.draw.circle(self.screen, RED, enemy.rect.center, ATTACK_RADIUS, 1)