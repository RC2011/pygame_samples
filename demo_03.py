# demo for 7-segment simulation
# using the class 'Seven_seg' in seven_seg_pg.py

from datetime import datetime
import pygame
from seven_seg_pg import Seven_seg
from lcd_font_pg import LCD_font
from lcd_font_pg import LCD_font_styles
from pygame.locals import Rect


DARK_GRAY = (40, 40, 40)
GRAY = (80, 80, 80)
RED = (255, 0, 0)
GREEN = (10, 250, 10)
CYAN = (120, 120, 250)
YELLOW = (250, 250, 20)
WHITE = (250, 250, 250)


pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode([550, 320])
pygame.display.set_caption("pygame 7-segment display simulation")
screen.fill(DARK_GRAY)


display5 = Seven_seg(screen)
display5.init_col(BLOCK_SIZE=9, BLOCK_INTV=9, COLOR_ON=(120, 200, 250), COLOR_OFF=GRAY)
display5.init_row(X_ORG=13, Y_ORG=11, COL_INTV=6)
# 上の数字


lcd1 = LCD_font(screen)
lcd1.init_col(BLOCK_SIZE=7, BLOCK_INTV=8, COLOR_ON=GREEN, COLOR_OFF=GRAY)
lcd1.init_row(X_ORG=10, Y_ORG=27, COL_INTV=6)


def LCD_display(x, y):
    lcd1.update_col(col=0)


lcd2 = LCD_font(screen)
lcd2.init_col(BLOCK_SIZE=7, BLOCK_INTV=8, COLOR_ON=RED, COLOR_OFF=GRAY)
lcd2.init_row(X_ORG=5, Y_ORG=17, COL_INTV=6)


def LCD_display(x, y):
    lcd2.update_col(col=0)


def infinite_loop():
                x_change = 0
                y_change = 0
running = True
# infinite loop top ----
while running:
    for count in range(16 ** 4):  # 0から65535まで
        # press ctrl-c or close the window to stop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        if not running:
            break
        # 「for count」のループから抜ける。whileループも抜ける。

        dt_now = datetime.now()
        time_now = (dt_now.hour * 10000
                    + dt_now.minute * 100
                    + dt_now.second)

        lcd2.update_col(col=0, code=int(str(dt_now.year)[0]))
        lcd2.update_col(col=1, code=int(str(dt_now.year)[1]))
        lcd2.update_col(col=2, code=int(str(dt_now.year)[2]))
        lcd2.update_col(col=3, code=int(str(dt_now.year)[3]))
        lcd2.update_col(col=4, code=10)
        lcd2.update_col(col=5, code=dt_now.month // 10)
        lcd2.update_col(col=6, code=dt_now.month % 10)
        lcd2.update_col(col=7, code=10)
        lcd2.update_col(col=8, code=dt_now.day // 10)
        lcd2.update_col(col=9, code=dt_now.day % 10)              # 1の位

        lcd1.update_col(col=0, code=dt_now.hour // 10)
        lcd1.update_col(col=1, code=dt_now.hour % 10)
        lcd1.update_col(col=2, code=11)
        lcd1.update_col(col=3, code=dt_now.minute // 10)
        lcd1.update_col(col=4, code=dt_now.minute % 10)
        lcd1.update_col(col=5, code=11)
        lcd1.update_col(col=6, code=dt_now.second // 10)
        lcd1.update_col(col=7, code=dt_now.second % 10)

        dt_now = datetime.now()
        time_now = (dt_now.hour * 10000
                    + dt_now.minute * 100
                    + dt_now.second)

        display5.disp_num2(zfil=True, rjust=6, num=time_now, base=10)

        pygame.display.flip()  # update_col
        clock.tick(20)  # FPS, Frame Per Second
    screen.fill(DARK_GRAY)
# infinit loop bottom ----

class LCD_font():
    def __init__(self, screen):
        self.screen = screen

    def init_col(self, BLOCK_SIZE=4, BLOCK_INTV=4, COLOR_ON=WHITE, COLOR_OFF=GRAY):
        # ひと桁、コラムの設定
        # ブロックのサイズと配置間隔をピクセル指定（インターバル）
        self.BLOCK_SIZE = BLOCK_SIZE
        self.BLOCK_INTV = BLOCK_INTV
        # on/offのカラー
        self.COLOR_ON = COLOR_ON
        self.COLOR_OFF = COLOR_OFF

    def init_row(self, X_ORG=2, Y_ORG=8, COL_INTV=6):  # 表示行の設定
        # xy空間での7セグ表示、最上位桁の左下座標をブロック数で指定
        self.X_ORG = X_ORG * self.BLOCK_INTV
        self.Y_ORG = Y_ORG * self.BLOCK_INTV
        # 各桁のブロック間隔をブロック数で指定（インターバル）
        self.COL_INTV = COL_INTV * self.BLOCK_INTV

    def update_col(self, col=0, code=0):  # ある桁にある文字を表示する関数
        # codeの文字をcol桁目に表示、桁は最上位桁の左から右へ進む。
        block_size = self.BLOCK_SIZE
        i = 0
        for y in range(7):
            for x in range(5):
                if LCD_font_styles[int(code)][i] == 1:
                    color = self.COLOR_ON
                else:
                    color = self.COLOR_OFF
                # 桁の原点
                x0 = self.X_ORG + self.COL_INTV * col
                y0 = self.Y_ORG
                # ドットの原点座標
                org1 = (x0 + x * self.BLOCK_INTV, y0 + y * self.BLOCK_INTV)
                # ドットを描く
                pygame.draw.rect(self.screen, color, Rect(org1[0], org1[1], block_size, block_size))
                i += 1

pygame.quit()
