import pygame
import button
from const import *

# pygame.init();

# #screen 
# SCREEN_WIDTH = BOARD_WIDTH + MOVE_LOG_PANEL_WIDTH
# SCREEN_HEIGHT =  BOARD_HEIGHT

# screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
# pygame.display.set_caption("Main Menu");

# #game variable state
# # main_menu : man hinh chinh cua menu
# # play_menu: che do choi cua co vua
# # play_history : lich su dau
# screen_state = "main_menu"

# #define font
# font1 = pygame.font.SysFont("arial", 35, True)
# font2 = pygame.font.SysFont("consolas", 20)

# #define color
# TEXT_COlOR = (217,217,217);

# def draw_text(text, font, text_col, x, y):
#     img = font.render(text, True, text_col)
#     screen.blit(img, (x,y))

# #load button image
# play_image = pygame.image.load("image/play_button.png").convert_alpha()
# history_image = pygame.image.load("image/history_button.png").convert_alpha()
# exit_image = pygame.image.load("image/exit_button.png").convert_alpha()
# botplay_image = pygame.image.load("image/botplay_button.png").convert_alpha()
# humanplay_image = pygame.image.load("image/humanplay_button.png").convert_alpha()
# back_image = pygame.image.load("image/back_button.png").convert_alpha()
# blackside_image = pygame.image.load("image/Black_Side.png").convert_alpha()
# whiteside_image = pygame.image.load("image/White_Side.png").convert_alpha()

# #create button
# play_button = button.Button(304, 125, play_image, 0.5)
# history_button = button.Button(304, 250, history_image, 0.5)
# exit_button = button.Button(304, 375, exit_image, 0.5)
# botplay_button = button.Button(304, 175, botplay_image, 0.5)
# humanplay_button = button.Button(304, 325, humanplay_image, 0.5)
# back_button = button.Button(20, 10, back_image, 0.35)
# blackside_button = button.Button(304, 125, blackside_image, 0.5)
# whiteside_button = button.Button(304, 375, whiteside_image,0.5)
# #game loop 
# run = True
# while run:
#     #fill color RGB
#     screen.fill((49,46,43))
#     #check if game is paused
    
#     if screen_state == "main_menu":
#         draw_text("Welcome to Chess", font1, TEXT_COlOR, 284, 60)
#         if play_button.draw_self(screen):
#             # mở chọn chế độ chơi
#             screen_state = "play_menu"
            
#         if history_button.draw_self(screen):
#             screen_state = "play_history"

#         if exit_button.draw_self(screen):
#             run = False 
    
#     if screen_state == "play_menu":
#         if botplay_button.draw_self(screen):
#             screen_state = "bot_menu"
#             pass
#         if humanplay_button.draw_self(screen):
#             #cho phần chơi ai vào đây
#             pass
#         if back_button.draw_self(screen):
#             screen_state = "main_menu"

#     if screen_state == "play_history":
#         #lịch sử đấu để ở đây
#         draw_text("Chessplay history: ", font2, TEXT_COlOR, 104, 20)
#         if back_button.draw_self(screen):
#             screen_state = "main_menu"

#     if screen_state == "bot_menu":
#         draw_text("Choose your side ", font1, TEXT_COlOR, 104, 20)
#         if blackside_button.draw_self(screen): 
#             pass
#         if whiteside_button.draw_self(screen):
#             pass       
    
#     #event handler
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             run = False

#     pygame.display.update()

# pygame.quit()

def main_menu():

    #variable to be return 
    player1 = True
    player2 = True

    #screen 
    SCREEN_WIDTH = 800 
    SCREEN_HEIGHT = 600

    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    pygame.display.set_caption("Main Menu");

    #game variable state
    # main_menu : man hinh chinh cua menu
    # play_menu: che do choi cua co vua
    # play_history : lich su dau
    screen_state = "main_menu"

    #define font
    font1 = pygame.font.SysFont("arial", 35, True)
    font2 = pygame.font.SysFont("consolas", 20)

    #define color
    TEXT_COlOR = (217,217,217);

    def draw_text(text, font, text_col, x, y):
        img = font.render(text, True, text_col)
        screen.blit(img, (x,y))

    #load button image
    play_image = pygame.image.load("image/play_button.png").convert_alpha()
    history_image = pygame.image.load("image/history_button.png").convert_alpha()
    exit_image = pygame.image.load("image/exit_button.png").convert_alpha()
    botplay_image = pygame.image.load("image/botplay_button.png").convert_alpha()
    humanplay_image = pygame.image.load("image/humanplay_button.png").convert_alpha()
    back_image = pygame.image.load("image/back_button.png").convert_alpha()
    blackside_image = pygame.image.load("image/Black_Side.png").convert_alpha()
    whiteside_image = pygame.image.load("image/White_Side.png").convert_alpha()

    #create button
    play_button = button.Button(304, 125, play_image, 0.5)
    history_button = button.Button(304, 250, history_image, 0.5)
    exit_button = button.Button(304, 375, exit_image, 0.5)
    botplay_button = button.Button(304, 175, botplay_image, 0.5)
    humanplay_button = button.Button(304, 325, humanplay_image, 0.5)
    back_button = button.Button(20, 10, back_image, 0.35)
    blackside_button = button.Button(304, 125, blackside_image, 0.5)
    whiteside_button = button.Button(304, 375, whiteside_image,0.5)

    #game loop 
    run = True
    while run:
        #fill color RGB
        screen.fill((49,46,43))
        #check if game is paused
        
        if screen_state == "main_menu":
            draw_text("Welcome to Chess", font1, TEXT_COlOR, 284, 60)
            if play_button.draw_self(screen):
                # mở chọn chế độ chơi
                screen_state = "play_menu"
                
            if history_button.draw_self(screen):
                screen_state = "play_history"

            if exit_button.draw_self(screen):
                run = False
                
        
        if screen_state == "play_menu":
            if botplay_button.draw_self(screen):
                screen_state = "bot_menu"
                
            if humanplay_button.draw_self(screen):
                player1 = True
                player2 = True
                run = False
                
            if back_button.draw_self(screen):
                screen_state = "main_menu"

        if screen_state == "bot_menu":
            if blackside_button.draw_self(screen):
                player1 = False
                player2 = True
                run = False
            if whiteside_button.draw_self(screen):
                player1 = True
                player2 = False
                run = False
            if back_button.draw_self(screen):
                screen_state = "main_menu"

        if screen_state == "play_history":
            #lịch sử đấu để ở đây
            draw_text("Chessplay history: ", font2, TEXT_COlOR, 104, 20)
            if back_button.draw_self(screen):
                screen_state = "main_menu"
                

        #event handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()

    pygame.quit()
    return [player1, player2]

# if __name__ == "_main_menu_":
#     main_menu()