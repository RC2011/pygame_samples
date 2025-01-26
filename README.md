# pygame_samples
 - ステップ2
ウィンドウサイズ
screen = pygame.display.set_mode([640, 480])
円の色と位置と大きさ(大きい方)![alt text]({14588630-5BF3-473C-8E8F-B863C601E9E2}.png)
pygame.draw.circle(screen, (176, 176, 222), (320, 240), 120)
円の色と位置と大きさ(小さい方)![alt text]({7312F7AD-FD66-4E10-993A-871E471086C4}.png)
pygame.draw.circle(screen, (222, 176, 222), (120, 120), 20)
pygame.draw.circle(screen, (222, 176, 222), (120, 120), 20)
![alt text]({46636B95-25B5-431A-AA03-A88BB4894132}.png)
長方形の色と位置と大きさ
pygame.draw.rect(screen, (120, 120, 120), Rect(120, 120, 200, 120))