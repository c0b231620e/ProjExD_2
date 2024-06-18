import os
import sys
import time
import pygame as pg
import random


WIDTH, HEIGHT = 1530, 900 #  元1600,900

DELTA={  #移動用辞書        
       pg.K_UP:(0,-5),
       pg.K_DOWN:(0,5),
       pg.K_LEFT:(-5,0),
       pg.K_RIGHT:(5,0)
}

def ang():
    kk_img = pg.transform.rotozoom(pg.image.load("fig/3.png"), 0, 2.0)
    hnkk_img=pg.transform.flip(kk_img,True,False)
    ANGLE={          
       (0,-5):pg.transform.rotozoom(hnkk_img,90,1),#上向き
       (0,5):pg.transform.rotozoom(hnkk_img,-90,1),#下向き
       (5,-5):pg.transform.rotozoom(hnkk_img,35,1),#右上向き
       (5,5):pg.transform.rotozoom(hnkk_img,-35,1),#右下向き
       (5,0):pg.transform.rotozoom(hnkk_img,0,1),#右向き
       (-5,5):pg.transform.rotozoom(kk_img,35,1),#左下
       (-5,0):pg.transform.rotozoom(kk_img,0,1),#左
       (-5,-5):pg.transform.rotozoom(kk_img,-35,1),#左上
       (0,0):kk_img
    }
    return ANGLE

os.chdir(os.path.dirname(os.path.abspath(__file__)))

def gamen(rct:pg.Rect)->tuple[bool,bool]:
    """
    引数：コウかトン　と　爆弾　のrct
    戻り値：　真理値タプル（横方向、縦方向）
    画面内True、外false
    """
    yoko,tate=True,True
    if rct.left < 0 or WIDTH < rct.right: #　横画面判定 
        yoko=False
    if rct.top < 0 or HEIGHT < rct.bottom: #  縦画面判定
        tate=False
    return yoko,tate


def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    bg_img = pg.image.load("fig/pg_bg.jpg")    
    kk_img = pg.transform.rotozoom(pg.image.load("fig/3.png"), 0, 2.0)
    kk_imgs=ang()
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
    kk_img = pg.transform.flip(kk_img, True, False)






    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:  # 罰を押したら終了するように設定
                return
            

        if  kk_rct.colliderect(bomb_rct):#ゲームオーバー要素
            # fonto = pg.font.Font(None, 80)
            # txt = fonto.render("Game Over",(255, 255, 255))
            anten=pg.Surface((WIDTH,HEIGHT))
            pg.draw.circle(anten, (255, 0, 0), (10, 10), 10)
            anten.set_alpha(200)
            screen.blit(anten, [0,0])
            pg.display.update()
            #pg.draw.rect(anten(0,0,0),(WIDTH,HEIGHT))
            time.sleep(5)
            
            return
        
        screen.blit(bg_img, [0, 0]) 
        key_lst = pg.key.get_pressed()  # 押したキーを取得
        sum_mv = [0, 0]# 移動用のリスト
        for k,v in DELTA.items():
            if key_lst[k]:
                sum_mv[0] += v[0]
                sum_mv[1] += v[1]
        kk_rct.move_ip(sum_mv)# 移動させる
        kk_img=kk_imgs[tuple(sum_mv)]
        

        if gamen(kk_rct)!=(True,True):#鳥の画面規制
            kk_rct.move_ip(-sum_mv[0],-sum_mv[1])
        screen.blit(kk_img, kk_rct)
        bomb_rct.move_ip(vx,vy)
        
        yoko,tate=gamen(bomb_rct)#画面規制確認
        if not yoko:#横の画面規制の反転
            vx *=-1
        if not tate:#縦画面規制の反転
            vy *=-1

        screen.blit(bomb_img,bomb_rct)
        pg.display.update()
        tmr += 1
        clock.tick(50)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
