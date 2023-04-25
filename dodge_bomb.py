import random 
import sys
import pygame as pg


delta = {
    pg.K_UP: (0, -1),
    pg.K_DOWN: (0, +1),
    pg.K_LEFT: (-1, 0),
    pg.K_RIGHT: (+1, 0),

}


def check_bound(scr_rct: pg.Rect, obj_rct: pg.Rect) -> tuple[bool, bool]:
    """
    オブジェクトが画面内か画面外かを判定し、真理値タプルを返す関数
    引数1:画面surfaceのRect
    引数2:こうかとん、または爆弾surfaceのRect
    戻り値:横方向のはみ出し判定結果（画面内:True、画面外:False）
    """
    yoko, tate = True, True
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right:
        yoko = False
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom:
        tate = False
    return yoko, tate

def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((1600, 900))
    clock = pg.time.Clock()
    bg_img = pg.image.load("ex02/fig/pg_bg.jpg")
    kk_img = pg.image.load("ex02/fig/3.png")
    kk_img = pg.transform.rotozoom(kk_img, 0, 2.0)
    tmr = 0
    bb_img = pg.Surface((20, 20))
    pg.draw.circle(bb_img, (255, 0, 0), (10, 10), 10)  # 練習1
    bb_img.set_colorkey((0, 0, 0))  #爆弾の四隅を透明にした
    x, y = random.randint(0, 1600), random.randint(0, 900)  # x,yを1600、900のランダムに設定
    screen.blit(bb_img, [x, y])  # 練習2
    vx, vy = +1, +1
    bb_rct = bb_img.get_rect()  # Rectクラスに変更
    bb_rct.center = x, y  # 初期位置をランダムに設定
    kk_rct = kk_img.get_rect()  # Rectクラスに変更
    kk_rct.center = 900, 400  #初期位置を900, 400に設定

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return 0

        tmr += 1
        key_lst = pg.key.get_pressed()
        for k, mv in delta.items():
            if key_lst[k]:
                kk_rct.move_ip(mv)

        if check_bound(screen.get_rect(), kk_rct) != (True, True):
            for k, mv in delta.items():
                if key_lst[k]:
                    kk_rct.move_ip(-mv[0], -mv[1])

        screen.blit(bg_img, [0, 0])
        screen.blit(kk_img, kk_rct)  # 練習4
        bb_rct.move_ip(vx, vy)  # 練習３
        yoko, tate = check_bound(screen.get_rect(), bb_rct)
        if not yoko:  # 横方向にはみ出たら
            vx*= -1
        if not tate:
            vy*= -1  # 縦方向にはみ出たら
        screen.blit(bb_img, bb_rct)  # 練習３

        pg.display.update()
        clock.tick(1000)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()