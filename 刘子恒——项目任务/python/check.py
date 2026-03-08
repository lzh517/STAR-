import pygame
import random
import sys

# 初始化pygame
pygame.init()

# 游戏常量设置
WIDTH, HEIGHT = 800, 600
BLOCK_SIZE = 20
SPEED = 10

# 颜色定义
BG_COLOR = (240, 245, 249)
GRID_COLOR = (220, 225, 229)
SNAKE_HEAD_COLOR = (76, 175, 80)
SNAKE_BODY_COLOR = (129, 199, 132)
TEXT_COLOR = (51, 51, 51)
TEXT_COLOR_PRESSED = (70, 70, 70)
GAME_OVER_BG = (255, 245, 245)
GAME_BEGIN_BG = (230, 230, 230)
GAME_OVER_TEXT = (244, 67, 54)
BORDER_COLOR = (189, 195, 199)
WHITE = (255, 255, 255)
# 彩色标题的颜色列表
TITLE_COLORS = [
    (244, 67, 54), (255, 159, 64), (253, 216, 53),
    (76, 175, 80), (33, 150, 243), (156, 39, 176)
]

# 创建游戏窗口、时钟、字体
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("贪吃蛇小游戏")
clock = pygame.time.Clock()
TITLE_FONT = pygame.font.SysFont(["Microsoft YaHei", "Arial", "SimHei"], 60, bold=True)
SCORE_FONT = pygame.font.SysFont(["Microsoft YaHei", "Arial", "SimHei"], 36)
MESSAGE_FONT = pygame.font.SysFont(["Microsoft YaHei", "Arial", "SimHei"], 40)


# ---------------------- 修复：补充draw_skin_change函数 ----------------------
def draw_skin_change(n, shade):
    """皮肤切换函数：绘制皮肤提示，n为皮肤索引，shade为颜色/亮度"""
    # 绘制皮肤切换文字
    skin_text = MESSAGE_FONT.render(f"皮肤 {n + 1} | 按↑↓切换", True, shade)
    text_rect = pygame.Rect(WIDTH - 220, 10, skin_text.get_width() + 20, skin_text.get_height() + 10)
    pygame.draw.rect(screen, WHITE, text_rect, border_radius=8)
    pygame.draw.rect(screen, BORDER_COLOR, text_rect, 2, border_radius=8)
    screen.blit(skin_text, (WIDTH - 210, 15))

    # 根据shade更新蛇的颜色
    global SNAKE_HEAD_COLOR, SNAKE_BODY_COLOR
    skin_colors = [
        [(76, 175, 80), (129, 199, 132)],  # 绿色（默认）
        [(244, 67, 54), (255, 159, 64)],  # 红色
        [(33, 150, 243), (156, 39, 176)]  # 蓝色
    ]
    if 0 <= n < len(skin_colors):
        SNAKE_HEAD_COLOR, SNAKE_BODY_COLOR = skin_colors[n]


# 彩色标题绘制函数
def draw_colorful_title():
    title_text = "贪吃蛇小游戏"
    start_x = WIDTH // 2 - (TITLE_FONT.size(title_text)[0] // 2)
    current_x = start_x
    y = 10

    for i, char in enumerate(title_text):
        char_surface = TITLE_FONT.render(char, True, TITLE_COLORS[i])
        screen.blit(char_surface, (current_x, y))
        current_x += char_surface.get_width()

    title_total_width = TITLE_FONT.size(title_text)[0]
    border_rect = pygame.Rect(
        start_x - 10, y,
        title_total_width + 20, TITLE_FONT.size(title_text)[1] + 10
    )
    pygame.draw.rect(screen, BORDER_COLOR, border_rect, 2, border_radius=5)


# 其他基础函数（和之前一致）
def show_game_over(msg):
    text = MESSAGE_FONT.render(msg, True, GAME_OVER_TEXT)
    text_rect = pygame.Rect(WIDTH / 6 - 10, HEIGHT / 3 - 10, text.get_width() + 20, text.get_height() + 20)
    pygame.draw.rect(screen, GAME_OVER_BG, text_rect, border_radius=10)
    pygame.draw.rect(screen, BORDER_COLOR, text_rect, 2, border_radius=10)
    screen.blit(text, [WIDTH / 6, HEIGHT / 3])


def show_score(score):
    text = SCORE_FONT.render(f"分数: {score}", True, TEXT_COLOR)
    screen.blit(text, [10, 10])


def draw_snake(block_size, snake_list):
    head_x, head_y = snake_list[-1]
    head_rect = pygame.Rect(head_x, head_y, block_size, block_size)
    pygame.draw.rect(screen, SNAKE_HEAD_COLOR, head_rect, border_radius=5)
    pygame.draw.rect(screen, BORDER_COLOR, head_rect, 1, border_radius=5)
    for segment in snake_list[:-1]:
        seg_rect = pygame.Rect(segment[0], segment[1], block_size, block_size)
        pygame.draw.rect(screen, SNAKE_BODY_COLOR, seg_rect, border_radius=4)
        pygame.draw.rect(screen, BORDER_COLOR, seg_rect, 1, border_radius=4)


def draw_background():
    screen.fill(BG_COLOR)
    for x in range(0, WIDTH, BLOCK_SIZE):
        pygame.draw.line(screen, GRID_COLOR, (x, 0), (x, HEIGHT), 1)
    for y in range(0, HEIGHT, BLOCK_SIZE):
        pygame.draw.line(screen, GRID_COLOR, (0, y), (WIDTH, y), 1)


def draw_food(block_size, food_x, food_y):
    food_color = random.choice([(244, 67, 54), (255, 159, 64), (253, 216, 53), (156, 39, 176), (33, 150, 243)])
    food_center = (food_x + block_size // 2, food_y + block_size // 2)
    pygame.draw.circle(screen, food_color, food_center, block_size // 2 - 2)
    pygame.draw.circle(screen, BORDER_COLOR, food_center, block_size // 2 - 2, 1)


def draw_game_begin_btn(is_hover):
    text_color = TEXT_COLOR_PRESSED if is_hover else TEXT_COLOR
    bg_color = GAME_BEGIN_BG if is_hover else WHITE
    game_begin_text = MESSAGE_FONT.render("开始游戏", True, text_color)
    btn_rect = pygame.Rect(
        WIDTH / 6 - 10,
        HEIGHT / 3 - 10,
        game_begin_text.get_width() + 20,
        game_begin_text.get_height() + 20
    )
    pygame.draw.rect(screen, bg_color, btn_rect, border_radius=10)
    pygame.draw.rect(screen, BORDER_COLOR, btn_rect, 2, border_radius=10)
    screen.blit(game_begin_text, [WIDTH / 6, HEIGHT / 3])
    return btn_rect


# ---------------------- 修复：初始化shade和n变量 ----------------------
def game_begin():
    running = True
    game_begin_text = MESSAGE_FONT.render("开始游戏", True, TEXT_COLOR)
    btn_rect = pygame.Rect(
        WIDTH / 6 - 10,
        HEIGHT / 3 - 10,
        game_begin_text.get_width() + 20,
        game_begin_text.get_height() + 20
    )
    is_hover = False
    # 修复：初始化shade和n变量（关键）
    shade = TEXT_COLOR  # shade设为文字默认颜色
    n = 0  # 皮肤索引初始化为0（默认绿色）

    while running:
        draw_background()
        draw_colorful_title()
        # 现在调用函数时，shade和n都有值，不会报错
        draw_skin_change(n, shade)
        draw_game_begin_btn(is_hover)

        # 事件处理（新增皮肤切换逻辑）
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and btn_rect.collidepoint(event.pos):
                    game_loop()
            if event.type == pygame.MOUSEMOTION:
                is_hover = btn_rect.collidepoint(event.pos)
            # 按↑↓切换皮肤
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    n = (n + 1) % 3  # 循环切换3种皮肤
                if event.key == pygame.K_DOWN:
                    n = (n - 1) % 3

        pygame.display.update()
        clock.tick(SPEED)


def game_loop():
    game_over = False
    game_close = False

    x1 = WIDTH / 2
    y1 = HEIGHT / 2
    x1_change = 0
    y1_change = 0

    snake_list = []
    length_of_snake = 1

    food_x = round(random.randrange(0, WIDTH - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
    food_y = round(random.randrange(0, HEIGHT - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE

    while not game_over:
        while game_close:
            draw_background()
            draw_colorful_title()
            show_game_over(f"游戏结束！得分: {length_of_snake - 1} 按Q退出/按C重新开始")
            show_score(length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x1_change != BLOCK_SIZE:
                    x1_change = -BLOCK_SIZE
                    y1_change = 0
                elif event.key == pygame.K_RIGHT and x1_change != -BLOCK_SIZE:
                    x1_change = BLOCK_SIZE
                    y1_change = 0
                elif event.key == pygame.K_UP and y1_change != BLOCK_SIZE:
                    y1_change = -BLOCK_SIZE
                    x1_change = 0
                elif event.key == pygame.K_DOWN and y1_change != -BLOCK_SIZE:
                    y1_change = BLOCK_SIZE
                    x1_change = 0

        if x1 >= WIDTH or x1 < 0 or y1 >= HEIGHT or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        draw_background()
        draw_food(BLOCK_SIZE, food_x, food_y)

        snake_head = [x1, y1]
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_close = True

        draw_snake(BLOCK_SIZE, snake_list)
        show_score(length_of_snake - 1)
        draw_colorful_title()
        pygame.display.update()

        if x1 == food_x and y1 == food_y:
            food_x = round(random.randrange(0, WIDTH - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
            food_y = round(random.randrange(0, HEIGHT - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
            length_of_snake += 1

        clock.tick(SPEED)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    game_begin()