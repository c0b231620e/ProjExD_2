import os
import sys
import pygame as pg
import random


WIDTH, HEIGHT = 1600, 900
DELTA={  #移動用辞書        
       pg.K_UP:(0,-5),
       pg.K_DOWN:(0,5),
       pg.K_LEFT:(-5,0),
       pg.K_RIGHT:(5,0)
}
os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    bg_img = pg.image.load("fig/pg_bg.jpg")    
    kk_img = pg.transform.rotozoom(pg.image.load("fig/3.png"), 0, 2.0)
    kk_rct = kk_img.get_rect()  # 座標系
    kk_rct.center = 900, 400
    bomb_img = pg.Surface((20, 20))#20,20の殻  を作る
    pg.draw.circle(bomb_img, (255, 0, 0), (10, 10), 10)  # カラー、中心場所、半径
    bomb_img.set_colorkey((0, 0, 0))# 黒い部分を透明化
    bomb_rct = bomb_img.get_rect()#爆弾の座標
    bomb_rct.center=random.randint(0,WIDTH),random.randint(0,HEIGHT)
    vx,vy=+5,+5 #移動速度
    clock = pg.time.Clock()
    tmr = 0
    

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:  # 罰を押したら終了するように設定
                return
        screen.blit(bg_img, [0, 0]) 

        key_lst = pg.key.get_pressed()  # 押したキーを取得
        sum_mv = [0, 0]# 移動用のリスト
        for k,v in DELTA.items():
            if key_lst[k]:
                sum_mv[0] += v[0]
                sum_mv[1] += v[1]
        kk_rct.move_ip(sum_mv)# 移動させる
        bomb_rct.move_ip(vx,vy)
        screen.blit(kk_img, kk_rct)
        screen.blit(bomb_img,bomb_rct)
        pg.display.update()
        tmr += 1
        clock.tick(50)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
