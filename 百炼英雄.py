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
        sleep(3) # 防止广告延迟弹出
        wait(Template(r"tpl1719452527348.png", target_pos=7, record_pos=(0.115, -0.225), resolution=(996, 1856)))
    except:
        touch(Template(r"tpl1719462531930.png", record_pos=(0.001, 0.872), resolution=(1000, 1863)))
        sleep(1)

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

    wait(Template(r"tpl1719136215820.png", record_pos=(0.077, -0.122), resolution=(1000, 1863)))
    
def fight_for_mines(): # 1'15"
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

def fight_for_coins():
    fight_for_coins_v3()

def fight_for_coins_v1(): # $60 in 3'
    transport("王座大厅") # 23'
    
    # transport("教堂山谷")
    touch(Template(r"tpl1719136215820.png", record_pos=(0.077, -0.122), resolution=(1000, 1863)))
    touch(Template(r"tpl1719316715138.png", record_pos=(-0.267, -0.456), resolution=(1000, 1863)))
    touch(Template(r"tpl1719291686110.png", record_pos=(0.166, -0.228), resolution=(1000, 1863)))
    wait(Template(r"tpl1719136215820.png", record_pos=(0.077, -0.122), resolution=(1000, 1863)))
    swipe([525, 925], vector=[0.02, -0.02], duration=0.1)
    swipe([525, 925], vector=[0, -0.05], duration=1.8)
    sleep(1) # 独眼食人魔 28' - 9'

    transport("贫瘠营地")
    swipe([525, 925], vector=[0.05, -0.01], duration=1)
    sleep(1) # 树精领主 23'

    transport("双峰山谷")
    swipe([525, 925], vector=[-0.01, -0.07], duration=2.5)
    swipe([525, 925], vector=[0.05, -0.05], duration=0.5)
    swipe([525, 925], vector=[-0.023, -0.03], duration=2.1)
    sleep(2) # 疯牛魔王 25'
    swipe([525, 925], vector=[-0.02, -0.032], duration=7)
    sleep(2) # 火焰石像 +20'

    transport("腐烂沼泽")
    swipe([525, 925], vector=[0.03, -0.084], duration=8)
    swipe([525, 925], vector=[0.025, -0.015], duration=1)
    sleep(2) # 巨型蜘蛛 36'

    transport("寒风营地")
    swipe([525, 925], vector=[0.09, -0.02], duration=2.2)
    sleep(2) # 树精长老 25'

def fight_for_coins_v2(): # $50 in 2‘8“
    touch(Template(r"tpl1719136215820.png", record_pos=(0.077, -0.122), resolution=(1000, 1863)))
    touch(Template(r"tpl1719316715138.png", record_pos=(-0.267, -0.456), resolution=(1000, 1863)))
    touch(Template(r"tpl1719291686110.png", record_pos=(0.166, -0.228), resolution=(1000, 1863)))
    wait(Template(r"tpl1719136215820.png", record_pos=(0.077, -0.122), resolution=(1000, 1863)))
    swipe([525, 925], vector=[0.02, -0.02], duration=0.6)
    swipe([525, 925], vector=[0, -0.05], duration=1.6)
    sleep(1) # 独眼食人魔
    swipe([525, 925], vector=[0, 0.05], duration=1.6)
    swipe([525, 925], vector=[-0.02, 0.02], duration=0.6)

    touch(Template(r"tpl1719136215820.png", record_pos=(0.077, -0.122), resolution=(1000, 1863)))
    touch(Template(r"tpl1719291958503.png", record_pos=(-0.263, -0.329), resolution=(1000, 1863)))
    touch(Template(r"tpl1719291989573.png", record_pos=(0.164, -0.42), resolution=(1000, 1863)))
    wait(Template(r"tpl1719136215820.png", record_pos=(0.077, -0.122), resolution=(1000, 1863)))
    swipe([525, 925], vector=[0.05, -0.01], duration=1)
    sleep(1) # 树精领主
    swipe([525, 925], vector=[-0.05, 0.01], duration=1)

    touch(Template(r"tpl1719136215820.png", record_pos=(0.077, -0.122), resolution=(1000, 1863)))
    touch(Template(r"tpl1719292222638.png", record_pos=(0.163, -0.227), resolution=(1000, 1863)))
    wait(Template(r"tpl1719136215820.png", record_pos=(0.077, -0.122), resolution=(1000, 1863)))
    swipe([525, 925], vector=[-0.01, -0.07], duration=2.5)
    swipe([525, 925], vector=[0.05, -0.05], duration=0.5)
    swipe([525, 925], vector=[-0.023, -0.03], duration=2.1)
    sleep(2) # 疯牛魔王 25'
    swipe([525, 925], vector=[-0.02, -0.032], duration=7)
    sleep(2) # 火焰石像 +20'

    transport("寒风营地")
    swipe([525, 925], vector=[0.09, -0.02], duration=2.2)
    sleep(2) # 树精长老 25'
    swipe([525, 925], vector=[-0.09, 0.02], duration=2.2)

    touch(Template(r"tpl1719136215820.png", record_pos=(0.077, -0.122), resolution=(1000, 1863)))
    touch(Template(r"tpl1719316570625.png", record_pos=(-0.265, 0.043), resolution=(1000, 1863)))
    touch(Template(r"tpl1719316585336.png", record_pos=(0.166, -0.416), resolution=(1000, 1863)))
    wait(Template(r"tpl1719136215820.png", record_pos=(0.077, -0.122), resolution=(1000, 1863)))

def fight_for_coins_v3(): # $50 in 1‘52“
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
        touch(Template(r"tpl1719291958503.png", record_pos=(-0.263, -0.329), resolution=(1000, 1863)))
        touch(Template(r"tpl1719291989573.png", record_pos=(0.164, -0.42), resolution=(1000, 1863)))
        wait(Template(r"tpl1719136215820.png", record_pos=(0.077, -0.122), resolution=(1000, 1863)))
        swipe([525, 925], vector=[0.05, -0.01], duration=0.6)
        sleep(1) # 树精领主
        swipe([525, 925], vector=[-0.05, 0.01], duration=0.6)

        touch(Template(r"tpl1719136215820.png", record_pos=(0.077, -0.122), resolution=(1000, 1863)))
        touch(Template(r"tpl1719293106569.png", record_pos=(-0.262, -0.202), resolution=(1002, 1865)))
        touch(Template(r"tpl1719293144468.png", record_pos=(0.165, -0.04), resolution=(1002, 1865)))
        wait(Template(r"tpl1719136215820.png", record_pos=(0.077, -0.122), resolution=(1000, 1863)))
        swipe([525, 925], vector=[0.09, -0.018], duration=1.5)
        sleep(2) # 树精长老
        swipe([525, 925], vector=[-0.09, 0.018], duration=1.5)

        touch(Template(r"tpl1719136215820.png", record_pos=(0.077, -0.122), resolution=(1000, 1863)))
        touch(Template(r"tpl1719291958503.png", record_pos=(-0.263, -0.329), resolution=(1000, 1863)))
        touch(Template(r"tpl1719292222638.png", record_pos=(0.163, -0.227), resolution=(1000, 1863)))
        wait(Template(r"tpl1719136215820.png", record_pos=(0.077, -0.122), resolution=(1000, 1863)))
        swipe([525, 925], vector=[-0.01, -0.07], duration=2.5)
        swipe([525, 925], vector=[0.05, -0.05], duration=0.5)
        swipe([525, 925], vector=[-0.023, -0.03], duration=2.1)
        sleep(1.5) # 疯牛魔王
        swipe([525, 925], vector=[-0.02, -0.032], duration=7)
        sleep(1.5) # 火焰石像
    
    except:
        sleep(1)

    finally:
        reload()

while True:
    fight_for_coins()
