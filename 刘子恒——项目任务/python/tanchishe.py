import pygame
import random
import sys

# 初始化pygame
pygame.init()

# 游戏常量设置
WIDTH, HEIGHT = 800, 600
BLOCK_SIZE = 20
SPEED = 10
skin=0

# 颜色定义
BG_COLOR = (240, 245, 249)
GRID_COLOR = (220, 225, 229)
SNAKE_HEAD_COLOR = [(150, 58, 58),(76, 175, 80),(60, 82, 120)]
SNAKE_BODY_COLOR = [(245, 208, 208),(129, 199, 132),(224, 231, 240)]
TEXT_COLOR = (51, 51, 51)
TEXT_COLOR_PRESSED = (70, 70, 70)
GAME_OVER_BG = (255, 245, 245)
GAME_BEGIN_BG = (230, 230, 230)
GAME_OVER_TEXT=(244, 67, 54)
BORDER_COLOR = (189, 195, 199)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
RED_PRESSED =(200,0,0)
GREEN = (0, 255, 0)
GREEN_PRESSED =(0,200,0)
BLUE = (0, 0, 255)
BLUE_PRESSED =(0,0,200)
SKIN_COLOR =[RED,GREEN,BLUE]
SKIN_COLOR_PRESSED = [RED_PRESSED, GREEN_PRESSED, BLUE_PRESSED]
FOOD_COLORS = [
    (244, 67, 54), (255, 159, 64), (253, 216, 53),
    (156, 39, 176), (33, 150, 243)
]
# 创建游戏窗口
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("super斯内克")

# 时钟
clock = pygame.time.Clock()

# 字体设置
TITLE_FONT = pygame.font.SysFont(["Microsoft YaHei", "Arial", "SimHei"], 60, bold=True)
SCORE_FONT = pygame.font.SysFont(["Microsoft YaHei", "Arial", "SimHei"], 36)
MESSAGE_FONT = pygame.font.SysFont(["Microsoft YaHei", "Arial", "SimHei"], 40)


# 修复：game_over只显示提示，不退出程序
def show_game_over(msg):
    text = MESSAGE_FONT.render(msg, True,GAME_OVER_TEXT)
    text_rect = pygame.Rect(WIDTH/6-10,HEIGHT/3-10,text.get_width()+20, text.get_height()+20)
    pygame.draw.rect(screen, GAME_OVER_BG, text_rect, border_radius=10)
    pygame.draw.rect(screen, BORDER_COLOR, text_rect, 2, border_radius=10)
    screen.blit(text, [WIDTH/6, HEIGHT/3])

def show_score(score):
    text = SCORE_FONT.render(f"分数: {score}", True, TEXT_COLOR)
    screen.blit(text, [10, 10])

def draw_snake(block_size, snake_list):
    head_x, head_y = snake_list[-1]
    head_rect = pygame.Rect(head_x, head_y, block_size, block_size)
    pygame.draw.rect(screen, SNAKE_HEAD_COLOR[skin%3], head_rect, border_radius=5)
    pygame.draw.rect(screen, BORDER_COLOR, head_rect, 1, border_radius=5)
    for segment in snake_list[:-1]:
        seg_rect = pygame.Rect(segment[0], segment[1], block_size, block_size)
        pygame.draw.rect(screen, SNAKE_BODY_COLOR[skin%3], seg_rect, border_radius=4)
        pygame.draw.rect(screen, BORDER_COLOR, seg_rect, 1, border_radius=4)
def draw_background():
    screen.fill(BG_COLOR)
    for x in range(0, WIDTH, BLOCK_SIZE):
        pygame.draw.line(screen, GRID_COLOR, (x, 0), (x, HEIGHT), 1)
    for y in range(0, HEIGHT, BLOCK_SIZE):
        pygame.draw.line(screen, GRID_COLOR, (0, y), (WIDTH, y), 1)
def draw_food(block_size, food_x, food_y):
    food_color = random.choice(FOOD_COLORS)
    food_center = (food_x + block_size // 2, food_y + block_size // 2)
    pygame.draw.circle(screen, food_color, food_center, block_size // 2 - 2)
    pygame.draw.circle(screen, BORDER_COLOR, food_center, block_size // 2 - 2, 1)
def draw_title():
    title = TITLE_FONT.render("super斯内克", True, TEXT_COLOR)
    screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 10))
    pygame.draw.rect(screen, BORDER_COLOR,
                     (WIDTH // 2 - title.get_width() // 2 - 10, 10,
                      title.get_width() + 20, title.get_height() + 10),
                     2, border_radius=5)
def draw_game_begin(text_color,game_begin_bg):
    game_begin = MESSAGE_FONT.render("开始游戏",True, text_color)
    text_rect = pygame.Rect(WIDTH // 2 - game_begin.get_width() // 2 - 10, HEIGHT / 3 - 10, game_begin.get_width() + 20, game_begin.get_height() + 20)
    pygame.draw.rect(screen, game_begin_bg, text_rect, border_radius=10)
    pygame.draw.rect(screen, BORDER_COLOR, text_rect, 2, border_radius=10)
    screen.blit(game_begin, [WIDTH // 2 - game_begin.get_width() // 2,HEIGHT / 3])
def draw_skin_change(n,on):
    list=["红","绿","蓝"]
    if on ==0:
        text_color = TEXT_COLOR
        color_color = SKIN_COLOR[n%3]
        skin_bg=WHITE
    elif on ==1:
        text_color = TEXT_COLOR_PRESSED
        color_color = SKIN_COLOR_PRESSED[n%3]
        skin_bg = GAME_BEGIN_BG
    skin_change =MESSAGE_FONT.render("斯内克当前颜色：",True,text_color)
    skin_color = MESSAGE_FONT.render(list[n%3],True,color_color)
    text_rect = pygame.Rect(WIDTH // 2 - skin_change.get_width() // 2 -skin_color.get_width() // 2- 10,HEIGHT / 3 + 80,
                            skin_change.get_width()+skin_color.get_width()+20, skin_change.get_height()+skin_color.get_height()+10
                            )
    pygame.draw.rect(screen, skin_bg, text_rect, border_radius=10)
    pygame.draw.rect(screen, BORDER_COLOR, text_rect, 2, border_radius=10)
    screen.blit(skin_change, [WIDTH // 2 - skin_change.get_width() // 2 -skin_color.get_width() // 2, HEIGHT / 3 + 90])
    screen.blit(skin_color,[WIDTH // 2 - skin_change.get_width() // 2 -skin_color.get_width() // 2+skin_change.get_width(),HEIGHT / 3 + 90])
def game_begin():
    begin = False
    game_over_flag = False
    shade=0
    n=0
    global skin
    game_begin = MESSAGE_FONT.render("开始游戏", True, TEXT_COLOR)
    skin_change = MESSAGE_FONT.render("斯内克当前颜色：", True, WHITE)
    skin_color = MESSAGE_FONT.render("红", True, WHITE)
    text_rect = pygame.Rect(WIDTH // 2 - skin_change.get_width() // 2 - skin_color.get_width() // 2 - 10,
                            HEIGHT / 3 + 80,
                            skin_change.get_width() + skin_color.get_width() + 20,
                            skin_change.get_height() + skin_color.get_height() + 10
                            )
    while not game_over_flag:
        while begin:
            game_loop()
        x, y = pygame.mouse.get_pos()
        draw_background()
        draw_title()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over_flag = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if WIDTH // 2 - game_begin.get_width() // 2 - 10 <= x <= WIDTH // 2 - game_begin.get_width() // 2 - 10 + game_begin.get_width() + 20 and HEIGHT / 3 - 10 <= y <= HEIGHT / 3 - 10 + game_begin.get_height() + 20:
                    skin=n
                    begin = True
                if text_rect.collidepoint(event.pos):
                    n=n+1
            if event.type == pygame.MOUSEMOTION:
                shade = text_rect.collidepoint(event.pos)
        if WIDTH // 2 - game_begin.get_width() // 2 - 10 <= x <= WIDTH // 2 - game_begin.get_width() // 2 - 10 + game_begin.get_width() + 20 and HEIGHT / 3 - 10 <= y <= HEIGHT / 3 - 10 + game_begin.get_height() + 20:
            draw_game_begin(TEXT_COLOR_PRESSED, GAME_BEGIN_BG)
        else :
            draw_game_begin(TEXT_COLOR, WHITE)
        draw_skin_change(n, shade)
        clock.tick(30)
        pygame.display.update()
    pygame.quit()
    sys.exit()
def game_loop():
    pygame.display.update()
    game_over_flag = False
    game_close = False

    x1 = WIDTH / 2
    y1 = HEIGHT / 2

    x1_change = 0
    y1_change = 0

    snake_list = []
    length_of_snake = 1

    food_x = round(random.randrange(0, WIDTH - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
    food_y = round(random.randrange(0, HEIGHT - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE

    while not game_over_flag:
        # 游戏结束界面
        while game_close:
            draw_background()
            # 显示提示，不退出
            show_game_over("游戏结束！Q-退出  C-重新开始")
            show_score(length_of_snake - 1)
            pygame.display.update()

            # 处理Q/C按键（这次能正常监听了）
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:  # Q退出
                        game_over_flag = True
                        game_close = False
                    if event.key == pygame.K_c:  # C重新开始
                        game_loop()  # 重新调用游戏循环，重置游戏

        # 正常游戏的事件监听
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x1_change == 0:
                    x1_change = -BLOCK_SIZE
                    y1_change = 0
                elif event.key == pygame.K_RIGHT and x1_change == 0:
                    y1_change = 0
                    x1_change = BLOCK_SIZE
                elif event.key == pygame.K_UP and y1_change == 0:
                    y1_change = -BLOCK_SIZE
                    x1_change = 0
                elif event.key == pygame.K_DOWN and y1_change == 0:
                    y1_change = BLOCK_SIZE
                    x1_change = 0

        # 边界检测
        if x1 >= WIDTH or x1 < 0 or y1 >= HEIGHT or y1 < 0:
            game_close = True

        # 更新蛇的位置
        x1 += x1_change
        y1 += y1_change
        draw_background()

        # 绘制食物
        draw_food(BLOCK_SIZE, food_x, food_y)

        # 更新蛇身
        snake_head = [x1, y1]  # 简化写法，替代两次append
        snake_list.append(snake_head)

        if len(snake_list) > length_of_snake:
            del snake_list[0]

        # 撞身体检测
        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_close = True

        # 绘制蛇和分数
        draw_snake(BLOCK_SIZE, snake_list)
        show_score(length_of_snake - 1)

        pygame.display.update()

        # 吃食物逻辑
        if x1 == food_x and y1 == food_y:
            food_x = round(random.randrange(0, WIDTH - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
            food_y = round(random.randrange(0, HEIGHT - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
            length_of_snake += 1
            for snake in snake_list[0:]:
                if snake[0] == food_x and snake[1] == food_y:
                    food_x = round(random.randrange(0, WIDTH - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
                    food_y = round(random.randrange(0, HEIGHT - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
        clock.tick(SPEED)

    # 退出游戏（只有按Q或关闭窗口才会到这）
    game_begin()

if __name__ == "__main__":
    game_begin()