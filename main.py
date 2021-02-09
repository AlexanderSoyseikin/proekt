import pygame as pg
import random

W = 1500
H = 500
WHITE = (0, 0, 0)
images_e = ["e_pt.png", "e_pt_a.png", "e_pt_d_1.png",
            "e_pt_d_2.png", "e_pt_d_3.png", "e_pt_d_4.png"]
images_a = ["pt.png", "pt_a.png", "pt_d_1.png",
            "pt_d_2.png", "pt_d_3.png", "pt_d_4.png"]
images_a_e = ["a_eng.png", "a_eng_d_1.png", "a_eng_d_2.png", "a_eng_d_3.png", "a_eng_d_4.png"]

h_rotate = ["a_hlk.png", "a_hlk_r.png", "a_hlk_rr.png", "a_hlk_rrr.png"]

h_rotate_attack = [["a_hlk.png", "a_hlk_a_1.png", "a_hlk_a_2.png",
                    "a_hlk_a_3.png", "a_hlk_a_4.png", "a_hlk_a_5.png"],
                   ["a_hlk_r.png", "a_hlk_r_a_1.png", "a_hlk_r_a_2.png",
                    "a_hlk_r_a_3.png", "a_hlk_a_4.png", "a_hlk_a_5.png"],
                   ["a_hlk_rr.png", "a_hlk_rr_a_1.png", "a_hlk_rr_a_2.png",
                    "a_hlk_rr_a_3.png", "a_hlk_a_4.png", "a_hlk_a_5.png"],
                   ["a_hlk_rrr.png", "a_hlk_rrr_a_1.png", "a_hlk_rrr_a_2.png",
                    "a_hlk_rrr_a_3.png", "a_hlk_a_4.png", "a_hlk_a_5.png"]]

mines_exp = ['mines.png', 'mines_a_1.png', 'mines_a_2.png', 'mines_a_3.png', 'mines_a_4.png', 'mines_a_5.png', ]

raketa_imgs = ["raketa.png", "raketa_2.png"]
raketa_enm_imgs = ["raketa_enemy.png", "raketa_enemy_2.png"]

hel_destroy = ["a_hlk_d_1.png", "a_hlk_d_2.png", "a_hlk_d_3.png",
               "a_hlk_d_4.png", "a_hlk_d_5.png", "a_hlk_d_6.png", ]

e_b_hp = 3
a_b_hp = 3

speed = 2
hlk_speed = 4
damage = 3
bl_timer = 0
bl_timer_eng = -1
fire_timer = 2

a_has_dot_1 = False


class Tnak(pg.sprite.Sprite):
    def __init__(self, x, filename, position, idd):
        self.sch = -1
        self.desint = False
        self.id = idd
        self.position = position
        pg.sprite.Sprite.__init__(self)
        self.im_name = filename
        self.image = pg.image.load(
            filename).convert_alpha()
        self.rect = self.image.get_rect(
            center=x)

        self.hp = random.randint(1, 10)
        self.enemy = None

    def update(self):
        if not self.desint:
            if self.position == "destroyed_e":
                self.chek("e")
                self.next_e()
                self.chek("e")
            elif self.position == "destroyed_a":
                self.chek("a")
                self.next_a()
                self.chek("a")

            if self.im_name == "e_pt.png" or self.im_name == "pt.png" or self.im_name == "pt_a.png":
                if self.im_name == "pt_a.png":
                    self.image = pg.image.load(
                        "pt.png").convert_alpha()
                if self.position == "tank_a":
                    self.rect.x += speed
                elif self.position == "tank_e":
                    self.rect.x -= 2

    def chek(self, side):
        if "pt" in self.im_name:
            if self.im_name in ["e_pt_d_1.png", "e_pt_d_2.png", "e_pt_d_3.png",
                                "e_pt_d_4.png", "pt_d_1.png", "pt_d_2.png",
                                "pt_d_3.png", "pt_d_4.png"]:
                self.rect.y = 316
            elif side == "e":
                if self.im_name == "e_pt.png" or self.im_name == "e_pt_a.png":
                    self.rect.y = 324
            else:
                if self.im_name == "pt.png" or self.im_name == "pt_a.png":
                    self.rect.y = 324

    def e_fire_1(self):
        global images_e
        global fire_timer
        if fire_timer > -1:
            self.image = pg.image.load(
                images_e[fire_timer]).convert_alpha()
            fire_timer -= 1

    def next_e(self):
        if self.hp > 0:
            if sprites[self.enemy].hp < 1 and self.hp > 0:
                self.position = "tank_e"
                self.image = pg.image.load(
                    "e_pt.png").convert_alpha()
                self.im_name = "e_pt.png"
            self.sch += 1
            if self.sch < 6:
                self.chek("e")
                self.image = pg.image.load(
                    images_e[self.sch]).convert_alpha()
                self.im_name = images_e[self.sch]
                self.chek("e")
                if self.hp > 0 and self.sch == 1:
                    if sprites[self.enemy].hp > 0:
                        sprites[self.enemy].hp -= random.randint(1, 3)
                        self.sch = -1
        else:
            if self.sch < 2:
                self.sch = 2
            if self.sch < 6:
                self.chek("e")
                self.image = pg.image.load(
                    images_e[self.sch]).convert_alpha()
                self.im_name = images_e[self.sch]
                self.chek("e")
                self.sch += 1

    def next_a(self):
        if "pt" in self.im_name:
            global damage
            if sprites[self.enemy].hp < 1 and self.hp > 0:
                self.position = "tank_a"
                self.image = pg.image.load(
                    "pt.png").convert_alpha()
                self.im_name = "pt.png"
            self.sch += 1
            if self.sch < 6:
                self.chek("a")
                self.image = pg.image.load(
                    images_a[self.sch]).convert_alpha()
                self.im_name = images_a[self.sch]
                self.chek("a")
                if self.hp > 0 and self.sch == 1:
                    if sprites[self.enemy].hp > 0:
                        sprites[self.enemy].hp -= random.randint(1, damage)
                        self.sch = -1

    def change_image(self, image):
        self.image = pg.image.load(
            image).convert_alpha()
        self.desint = True
        self.rect.y = 312


class Eng(pg.sprite.Sprite):
    def __init__(self, x, filename, position, idd):
        self.id = idd
        self.position = position
        pg.sprite.Sprite.__init__(self)
        self.im_name = filename
        self.image = pg.image.load(
            filename).convert_alpha()
        self.rect = self.image.get_rect(
            center=x)

        self.hp = 1
        self.enemy = None

        self.dot_fire_timer = 0

    def update(self):
        global bl_timer
        global bl_timer_eng
        if self.position == "a_eng" and self.rect.x < 300 and self.hp > 0:
            self.rect.x += 1
        if self.position == "a_eng" and self.rect.x >= 300 and self.hp > 0:
            bl_timer += 1
            if bl_timer >= 300:
                bl_timer = 0
                self.position = "a_dot"
                self.image = pg.image.load(
                    "a_dot.png").convert_alpha()
                self.im_name = "a_dot.png"
                self.hp = 100
                a_has_dot_1 = True
                self.rect.y = 280
                self.rect = self.image.get_rect(
                    center=(self.rect[0], 306))
                for i in range(_):
                    if sprites[i].position == "a_dot":
                        for j in range(_):
                            if sprites[j].position == "tank_e" or (
                                    sprites[j].position == "destroyed_e" and sprites[j].hp > 0):
                                if sprites[i].rect.colliderect(sprites[j].rect):
                                    sprites[j].position = "destroyed_e"
                                    sprites[j].hp = -100
                                    sprites[j].enemy = i
        if self.position == "a_eng_destr":
            if bl_timer_eng < 4:
                bl_timer_eng += 1
            self.image = pg.image.load(
                images_a_e[bl_timer_eng]).convert_alpha()
            self.im_name = images_a_e[bl_timer_eng]
        if self.enemy and self.position == "a_dot":
            if sprites[self.enemy].hp > 0:
                self.next_a()
            else:
                self.image = pg.image.load(
                    "a_dot.png").convert_alpha()
                self.im_name = "a_dot.png"

    def next_a(self):
        if self.position == "a_dot" and sprites[self.enemy].position != "a_dot":
            if self.hp > 0:
                self.dot_fire_timer += 1
                if self.dot_fire_timer % 2 == 1 and sprites[self.enemy].hp > 0:
                    self.image = pg.image.load(
                        "a_dot_a.png").convert_alpha()
                    self.im_name = "a_dot_a.png"
                    if sprites[self.enemy].hp > 0:
                        sprites[self.enemy].hp -= 1
                if self.dot_fire_timer % 2 == 0:
                    self.image = pg.image.load(
                        "a_dot.png").convert_alpha()
                    self.im_name = "a_dot.png"


class Hlk(pg.sprite.Sprite):
    def __init__(self, x, filename, position, idd):
        self.id = idd
        self.position = position
        pg.sprite.Sprite.__init__(self)
        self.im_name = filename
        self.image = pg.image.load(
            filename).convert_alpha()
        self.rect = self.image.get_rect(
            center=x)
        self.enemy = None
        self.rotate_timer = 0
        self.attack_timer = -1
        self.hel_des = False
        self.des_timer = -1
        self.enemy_bool = False

        self.start_timer = False
        self.started_timer = 0

    def update(self):
        self.rotate_timer += 1
        if self.start_timer:
            self.started_timer += 1
        if self.hel_des:
            self.des_timer += 1
            if self.des_timer <= 5 + 10 and self.des_timer > -1 + 10:
                if self.enemy:
                    global a_has_hel
                    global t
                    del sprites[self.enemy]
                    _ = len(sprites)
                    self.enemy = None
                    a_has_hel = False
                self.image = pg.image.load(
                    hel_destroy[self.des_timer - 10]).convert_alpha()
            elif self.des_timer > 5 + 10:
                self.image = pg.image.load(
                    hel_destroy[-1]).convert_alpha()
            else:
                self.image = pg.image.load(
                    h_rotate[self.rotate_timer % 4]).convert_alpha()
                self.rect.x += int(hlk_speed)

        if self.position == "hlk_a" and not self.hel_des:
            if not self.enemy:
                self.image = pg.image.load(
                    h_rotate[self.rotate_timer % 4]).convert_alpha()
                self.rect.x += int(hlk_speed)
                if self.enemy_bool:
                    self.rect.x += int(hlk_speed) * 3
                    self.enemy_bool = False
            if self.enemy and sprites[self.enemy].position != 'raketa_e':
                self.attack_timer += 1
                self.image = pg.image.load(
                    h_rotate_attack[self.rotate_timer % 4][self.attack_timer % 6]).convert_alpha()
                if self.attack_timer % 6 == 3:
                    sprites[self.enemy].position = "destroyed_e"
                    sprites[self.enemy].hp = -100
                    sprites[self.enemy].change_image("e_pt_desintigrated.png")
                if self.attack_timer % 6 == 5:
                    self.enemy = None
                    self.enemy_bool = True

    def destroy(self):
        self.hel_des = True


class Objekt(pg.sprite.Sprite):
    def __init__(self, x, filename, position, idd, mine_number=None):
        self.mine_number = mine_number
        self.id = idd
        self.position = position
        pg.sprite.Sprite.__init__(self)
        self.im_name = filename
        self.image = pg.image.load(
            filename).convert_alpha()
        self.rect = self.image.get_rect(
            center=x)
        self.enemy = None
        self.mine_timer = 0
        self.mine_exp_timer = None
        self.r_t = 0
        self.desint = False
        self.hp = 1

    def update(self):
        if not self.desint:
            global t
            global speed
            global sprites
            global count_a
            global energy_a
            global a_has_dot_1
            global images_a_e
            global _
            global h_rotate
            if self.position == "raketa_e":
                self.rect.x -= 10
                self.image = pg.image.load(
                    raketa_enm_imgs[self.rotate_timer % 2]).convert_alpha()
            self.r_t += 1
            if self.position == "a_raketa":
                self.image = pg.image.load(
                    raketa_imgs[self.r_t % 2]).convert_alpha()
                self.rect.x += 10
            if self.position == "a_mines" and self.enemy:
                self.mine_timer += 1
                if self.mine_exp_timer is not None:
                    if self.mine_exp_timer <= 4:
                        self.mine_exp_timer += 1
                        self.image = pg.image.load(
                            mines_exp[self.mine_exp_timer]).convert_alpha()
                        if self.mine_exp_timer == 1:
                            sprites[self.enemy].change_image("e_pt_desintigrated.png")
                    else:
                        del sprites[self.mine_number]
                        _ = len(sprites)
                elif not self.mine_exp_timer and self.mine_timer >= 10:
                    self.mine_exp_timer = -1
        else:
            pass

    def destroy(self):
        self.hel_des = True


pg.init()
pg.time.set_timer(pg.USEREVENT + 1, 30)

sc = pg.display.set_mode((W, H))

timer = 0
timer2 = 0
timer3 = 299
timer4 = 0
timer5 = 0
timer6 = 0
energy_a = 0
energy_e = 0

run = True
mountain = Objekt((750, 250), "pole.png", "field", 0)
sprites = [mountain]
count_e = -1
count_a = -1
count_l = 0

mines = False
sp_mines = []

a_has_hel = False

while run:
    for ev in pg.event.get():
        if ev.type == pg.QUIT:
            pg.quit()
        if ev.type == pg.USEREVENT + 1:
            timer6 += 1
            if timer < 101:
                timer += 1
            if timer2 < 21:
                timer2 += 1
            if timer3 < 301:
                timer3 += 1
            if timer4 < 101:
                timer4 += 1
            if timer5 < 101:
                timer5 += 1
            if timer >= 100:
                timer = 0
                energy_a += 1 if energy_a < 4 else 0
                energy_e += 2
            if energy_a == 0:
                sprites[0] = Objekt((750, 250), "pole.png", "field", 0)
            elif energy_a == 1:
                sprites[0] = Objekt((750, 250), "pole1.png", "field", 0)
            elif energy_a == 2:
                sprites[0] = Objekt((750, 250), "pole2.png", "field", 0)
            elif energy_a == 3:
                sprites[0] = Objekt((750, 250), "pole3.png", "field", 0)
            elif energy_a == 4:
                sprites[0] = Objekt((750, 250), "pole4.png", "field", 0)

            if energy_e > 0:
                if not a_has_hel:
                    if timer6 % 50 == 0:
                        count_e += 1
                        te = Tnak((1550, 327), "e_pt.png", "tank_e", count_e)
                        sprites.append(te)
                        te = None
                        energy_e -= 1
                else:
                    if energy_e > 1:
                        if timer6 % 300 == 0:
                            count_e += 1
                            te = Objekt((1550, 234), "raketa_enemy.png", "raketa_e", count_e)
                            sprites.append(te)
                            te = None
                            energy_e -= 2

        if ev.type == pg.MOUSEBUTTONDOWN:
            possition = ev.pos
            if e_b_hp > 0 and a_b_hp > 0:
                if not mines:
                    if possition[1] < 501 and possition[1] > 475 and possition[0] > 242 and possition[
                        0] < 291 and energy_a >= 3:
                        mnsh = None
                        if [] not in sp_mines:
                            sp_mines.append(len(sp_mines))
                            mnsh = len(sp_mines)
                        else:
                            for i in range(len(sp_mines)):
                                if sp_mines[i] == []:
                                    sp_mines[i] = i + 1
                                    mnsh = i + 1
                        count_a += 1
                        t = Objekt((50 * mnsh, 326), "mines.png", "a_mines", count_a, mnsh)
                        sprites.append(t)
                        energy_a -= 3
                        t = None

                if possition[0] < 11 and possition[1] < 11:
                    pg.quit()
                if timer2 > 20:
                    if possition[1] < 501 and possition[1] > 475 and possition[0] > -1 and possition[0] < 49:
                        if energy_a > 0:
                            timer2 = 0
                            count_a += 1
                            t = Tnak((0, 327), "pt.png", "tank_a", count_a)
                            sprites.append(t)
                            energy_a -= 1
                            t = None
                if timer4 >= 100:
                    if possition[1] < 501 and possition[1] > 475 and possition[0] > 97 and possition[0] < 145:
                        if energy_a > 2:
                            timer4 = 0
                            count_a += 1
                            t = Hlk((90, 280), "a_hlk.png", "hlk_a", count_a)
                            sprites.append(t)
                            energy_a -= 3
                            t = None
                            a_has_hel = True
                if timer3 > 300:
                    if possition[1] < 501 and possition[1] > 475 and possition[0] > 48 and possition[0] < 97:
                        if energy_a > 1:
                            if not a_has_dot_1:
                                timer3 = 0
                                count_a += 1
                                t2 = Eng((0, 327), "a_eng.png", "a_eng", count_a)
                                sprites.append(t2)
                                energy_a -= 2
                                t2 = None
                if timer5 >= 100:
                    if possition[1] < 501 and possition[1] > 475 and possition[0] > 146 and possition[0] < 195:
                        if energy_a > 1:
                            timer5 = 0
                            count_a += 1
                            t2 = Objekt((0, 234), "raketa.png", "a_raketa", count_a)
                            sprites.append(t2)
                            energy_a -= 2
                            t2 = None
                if possition[1] < 501 and possition[1] > 475 and possition[0] > 194 and possition[
                    0] < 244 and energy_a >= 2:
                    if count_l == 0:
                        speed = 3
                        energy_a -= 2
                        count_l += 1
                    elif count_l == 1:
                        count_l += 1
                        damage = 5
                        energy_a -= 2
                    else:
                        speed += 1
                        energy_a -= 2
                if possition[1] < 501 and possition[1] > 475 and possition[0] > 290 and possition[0] < 339:
                    hlk_speed = hlk_speed ** 0.5
            else:
                if possition[1] < 501 and possition[1] > 448 and possition[0] > -1 and possition[0] < 243:
                    sprites = [Objekt((750, 250), "pole.png", "field", 0)]
                    e_b_hp = 3
                    a_b_hp = 3
                    timer = 0
                    timer2 = 0
                    energy_a = 0
                    count_e = -1
                    count_a = -1
                    speed = 2
                    damage = 3
                    count_l = 0
                    timer3 = 299

    sc.fill(WHITE)
    _ = len(sprites)
    for i in range(_):
        if sprites[i].position == "tank_e":
            for j in range(_):
                if sprites[j].position == "tank_a" or (
                        sprites[j].position == "destroyed_a" and sprites[j].hp > 0):
                    if sprites[i].rect.colliderect(sprites[j].rect):
                        sprites[i].position = "destroyed_e"
                        sprites[i].enemy = j
                        sprites[j].position = "destroyed_a"
                        sprites[j].enemy = i
                elif sprites[j].position == "a_eng":
                    if sprites[i].rect.colliderect(sprites[j].rect):
                        sprites[j].e_fire_1()
                        sprites[j].position = "a_eng_destr"
                elif sprites[j].position == "a_dot":
                    if sprites[i].rect.colliderect(sprites[j].rect):
                        sprites[i].position = "destroyed_e"
                        sprites[i].enemy = j
                        sprites[j].enemy = i
                elif sprites[j].position == "a_mines":
                    if sprites[i].rect.colliderect(sprites[j].rect):
                        sprites[j].enemy = i
                elif sprites[j].position == "hlk_a":
                    if sprites[i].position != "raketa_e":
                        if sprites[i].rect.colliderect(sprites[j].rect):
                            sprites[j].enemy = i
        elif sprites[i].position == "tank_a":
            for j in range(_):
                if sprites[j].position == "tank_e" or (
                        sprites[j].position == "destroyed_e" and sprites[j].hp > 0):
                    if sprites[i].rect.colliderect(sprites[j].rect):
                        sprites[i].position = "destroyed_a"
                        sprites[i].enemy = j
                        sprites[j].position = "destroyed_e"
                        sprites[j].enemy = i
        elif sprites[i].position == "raketa_e":
            for j in range(len(sprites)):
                if sprites[j].position == "hlk_a":
                    if sprites[i].rect.colliderect(sprites[j].rect):
                        sprites[j].destroy()
                        sprites[j].enemy = i
    for i in range(_):
        sc.blit(sprites[i].image, sprites[i].rect)
        if sprites[i].rect.x > 1600 and sprites[i].position != 'a_eng':
            count_a -= 1
            e_b_hp -= 1
            del sprites[i]
            _ = len(sprites)
            for j in range(i - 1, _):
                sc.blit(sprites[j].image, sprites[j].rect)
            break
        elif sprites[i].rect.x < -100 and "raketa" not in sprites[i].position:
            count_e -= 1
            a_b_hp -= 1
            del sprites[i]
            _ = len(sprites)
            for i in range(i - 1, _):
                sc.blit(sprites[i].image, sprites[i].rect)
            break

    if e_b_hp <= 0:
        sc.fill(WHITE)
        sprites = [Objekt((750, 250), "win.png", "field", 0)]
        sc.blit(sprites[0].image, sprites[0].rect)
    elif a_b_hp <= 0:
        sc.fill(WHITE)
        sprites = [Objekt((750, 250), "lose.png", "field", 0)]
        sc.blit(sprites[0].image, sprites[0].rect)

    pg.display.update()
    pg.time.delay(50)

    for i in sprites:
        i.update()
