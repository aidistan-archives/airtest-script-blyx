# -*- encoding=utf8 -*-
from airtest.core.api import *

auto_setup(__file__)
connect_device("Windows:///?title_re=百炼英雄")

def reload():
    try:
        touch(Template(r"tpl1719453034381.png", target_pos=4, record_pos=(0.341, -0.886), resolution=(1000, 1863)))
        touch(Template(r"tpl1719453076258.png", record_pos=(0.026, -0.356), resolution=(1000, 1863)))
        sleep(5)

        connect_device("Windows:///?title_re=百炼英雄")
        wait(Template(r"tpl1719452527348.png", target_pos=7, record_pos=(0.115, -0.225), resolution=(996, 1856)))

        # 等待一会，以防活动页面延迟弹出
        sleep(3)

    except:
        sleep(1)

    finally:
        time = 0
        while time < 5 and not exists(Template(r"tpl1719452527348.png", target_pos=7, record_pos=(0.115, -0.225), resolution=(996, 1856))):
            touch([525, 1800]) # 点击底部空白关闭页面
            sleep(1)
            time += 1

def transport(place):
    if exists(Template(r"tpl1718985018429.png", record_pos=(0.401, 0.667), resolution=(1248, 2266))): # 8’
        touch(Template(r"tpl1718985018429.png", record_pos=(0.401, 0.667), resolution=(1248, 2266)))
        wait(Template(r"tpl1719452527348.png", record_pos=(0.115, -0.225), resolution=(996, 1856)))

    touch(Template(r"tpl1719452527348.png", target_pos=7, record_pos=(0.115, -0.225), resolution=(996, 1856)))

    if place == "教堂山谷":
        touch(Template(r"tpl1719316715138.png", record_pos=(-0.267, -0.456), resolution=(1000, 1863)))
        touch(Template(r"tpl1719291686110.png", record_pos=(0.166, -0.228), resolution=(1000, 1863)))
    elif place == "贫瘠营地":
        touch(Template(r"tpl1719291958503.png", record_pos=(-0.263, -0.329), resolution=(1000, 1863)))
        touch(Template(r"tpl1719291989573.png", record_pos=(0.164, -0.42), resolution=(1000, 1863)))
    elif place == "双峰山谷":
        touch(Template(r"tpl1719291958503.png", record_pos=(-0.263, -0.329), resolution=(1000, 1863)))
        touch(Template(r"tpl1719292222638.png", record_pos=(0.163, -0.227), resolution=(1000, 1863)))
    elif place == "腐烂沼泽":
        touch(Template(r"tpl1719293106569.png", record_pos=(-0.262, -0.202), resolution=(1002, 1865)))
        touch(Template(r"tpl1719293130357.png", record_pos=(0.165, -0.231), resolution=(1002, 1865)))
    elif place == "寒风营地":
        touch(Template(r"tpl1719293106569.png", record_pos=(-0.262, -0.202), resolution=(1002, 1865)))
        touch(Template(r"tpl1719293144468.png", record_pos=(0.165, -0.04), resolution=(1002, 1865)))
    elif place == "魔力之环":
        touch(Template(r"tpl1719135807947.png", record_pos=(-0.261, -0.088), resolution=(1232, 2243)))
        touch(Template(r"tpl1719315945030.png", record_pos=(0.163, -0.421), resolution=(1000, 1863)))

    elif place == "北风营地":
        touch(Template(r"tpl1719135807947.png", record_pos=(-0.261, -0.088), resolution=(1232, 2243)))
        touch(Template(r"tpl1719135822589.png", record_pos=(0.162, -0.234), resolution=(1232, 2243)))
    elif place == "王座大厅":
        touch(Template(r"tpl1719316570625.png", record_pos=(-0.265, 0.043), resolution=(1000, 1863)))
        touch(Template(r"tpl1719316585336.png", record_pos=(0.166, -0.416), resolution=(1000, 1863)))
    elif place == "炽热哨站":
        touch(Template(r"tpl1727147937752.png", record_pos=(-0.263, 0.292), resolution=(1000, 1863)))
        touch(Template(r"tpl1727147946547.png", record_pos=(0.164, -0.229), resolution=(1000, 1863)))

    wait(Template(r"tpl1719136215820.png", record_pos=(0.077, -0.122), resolution=(1000, 1863)))

def go_for_idle(place): # 前往挂机地点
    if place == "燃烧平原":
        transport("炽热哨站")
        swipe([525, 925], vector=[0.012, -0.007], duration=1)
        swipe([525, 925], vector=[0.025,  0.040], duration=4)
        swipe([525, 925], vector=[0.048, -0.018], duration=4.3)
        swipe([525, 925], vector=[0.048,  0.018], duration=13)

def fight_for_mines(): # 153 mines in 1'15"
    transport("北风营地")
    swipe([525, 925], vector=[-0.038, 0.012], duration=5)
    sleep(1)
    swipe([525, 925], vector=[-0.014, -0.028], duration=0.8)
    sleep(1)
    swipe([525, 925], vector=[-0.014, -0.028], duration=1.8)
    sleep(1)
    swipe([525, 925], vector=[-0.01, 0.003], duration=2.5)
    sleep(1)
    swipe([525, 925], vector=[-0.035, -0.019], duration=2.8)
    sleep(1)
    swipe([525, 925], vector=[-0.03, 0.023], duration=2.2)
    sleep(2)
    swipe([525, 925], vector=[-0.03, 0.023], duration=1)
    sleep(2)
    swipe([525, 925], vector=[0.05, 0.005], duration=5.5)
    sleep(1.5)
    swipe([525, 925], vector=[0.005, 0.05], duration=2)
    sleep(2)

def fight_for_coins(): # $50 in 1‘56“
    try:
        touch(Template(r"tpl1719452527348.png", target_pos=7, record_pos=(0.115, -0.225), resolution=(996, 1856)))
        touch(Template(r"tpl1719291686110.png", record_pos=(0.166, -0.228), resolution=(1000, 1863)))
        wait(Template(r"tpl1719136215820.png", record_pos=(0.077, -0.122), resolution=(1000, 1863)))
        swipe([525, 925], vector=[0.02, -0.02], duration=0.6)
        swipe([525, 925], vector=[0, -0.05], duration=1)
        sleep(1) # 独眼食人魔
        swipe([525, 925], vector=[0, 0.05], duration=1)
        swipe([525, 925], vector=[-0.02, 0.02], duration=0.6)

        touch(Template(r"tpl1719136215820.png", record_pos=(0.077, -0.122), resolution=(1000, 1863)))
        touch(Template(r"tpl1719316570625.png", record_pos=(-0.265, 0.043), resolution=(1000, 1863)))
        touch(Template(r"tpl1719316585336.png", record_pos=(0.166, -0.416), resolution=(1000, 1863)))
        wait(Template(r"tpl1719136215820.png", record_pos=(0.077, -0.122), resolution=(1000, 1863)))

        touch(Template(r"tpl1719136215820.png", record_pos=(0.077, -0.122), resolution=(1000, 1863)))
        touch(Template(r"tpl1719293106569.png", record_pos=(-0.262, -0.202), resolution=(1002, 1865)))
        touch(Template(r"tpl1719293144468.png", record_pos=(0.165, -0.04), resolution=(1002, 1865)))
        wait(Template(r"tpl1719136215820.png", record_pos=(0.077, -0.122), resolution=(1000, 1863)))
        swipe([525, 925], vector=[0.09, -0.018], duration=1.5)
        sleep(2) # 树精长老
        swipe([525, 925], vector=[-0.09, 0.018], duration=1.5)

        touch(Template(r"tpl1719136215820.png", record_pos=(0.077, -0.122), resolution=(1000, 1863)))
        touch(Template(r"tpl1719291958503.png", record_pos=(-0.263, -0.329), resolution=(1000, 1863)))
        touch(Template(r"tpl1719291989573.png", record_pos=(0.164, -0.42), resolution=(1000, 1863)))
        wait(Template(r"tpl1719136215820.png", record_pos=(0.077, -0.122), resolution=(1000, 1863)))
        swipe([525, 925], vector=[0.05, -0.01], duration=0.6)
        sleep(1) # 树精领主
        swipe([525, 925], vector=[-0.05, 0.01], duration=0.6)

        touch(Template(r"tpl1719136215820.png", record_pos=(0.077, -0.122), resolution=(1000, 1863)))
        touch(Template(r"tpl1719292222638.png", record_pos=(0.163, -0.227), resolution=(1000, 1863)))
        wait(Template(r"tpl1719136215820.png", record_pos=(0.077, -0.122), resolution=(1000, 1863)))
        swipe([525, 925], vector=[-0.01, -0.07], duration=2.5)
        swipe([525, 925], vector=[0.05, -0.05], duration=0.5)
        swipe([525, 925], vector=[-0.023, -0.03], duration=2.1)
        sleep(1.5) # 疯牛魔王
        swipe([525, 925], vector=[-0.02, -0.032], duration=7)
        sleep(1.5) # 火焰石像

        touch(Template(r"tpl1718985018429.png", record_pos=(0.401, 0.667), resolution=(1248, 2266)))
        wait(Template(r"tpl1719452527348.png", record_pos=(0.115, -0.225), resolution=(996, 1856)))

    except:
        reload()

while True:
    fight_for_coins()
