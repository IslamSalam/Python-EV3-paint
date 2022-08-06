#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile, Font
import urandom
import sys


ev3 = EV3Brick()

#реклама
NauRobot_font = Font(size = 32, bold = True)
ev3.screen.set_font(NauRobot_font)
ev3.screen.draw_text(52, 25, ' Nau')
ev3.screen.draw_text(42, 65, 'Robot')
ev3.screen.draw_circle(90, 60, 80)
ev3.screen.draw_circle(91, 60, 80)
ev3.screen.draw_circle(92, 60, 80)
ev3.screen.draw_circle(93, 60, 80) 
ev3.speaker.play_file(SoundFile.MAGIC_WAND)
while not Button.CENTER in (ev3.buttons.pressed()):
    pass
ev3.speaker.play_file(SoundFile.CLICK)
ev3.screen.clear()
wait(300)

#инициализация переменных,датчиков,моторов
choice = 1
size = 2
Morot_D = Motor(Port.D)
Morot_A = Motor(Port.A)
touch_sensor = TouchSensor(Port.S1)
color_sensor = ColorSensor(Port.S4)


while True:             #бесконечный цикл
        
        #координаты
        A_coordinates = Morot_A.angle() / 4 + 89  #это нужно чтобы рисование началось с центра
        if (A_coordinates > 0) and (A_coordinates < 175):
         A_VpredelahEkrana = True
        else:
         A_VpredelahEkrana = False

        if A_VpredelahEkrana == True:
         Morot_A.stop()
        else:
         if A_coordinates > 175:
                 Morot_A.run(-20)
         else:       
                 Morot_A.run(20)

        D_coordinates = Morot_D.angle() / 4 + 64
        if (D_coordinates > 0) and (D_coordinates < 125):
         D_VpredelahEkrana = True
        else:
         D_VpredelahEkrana = False

        if D_VpredelahEkrana == True:
         Morot_D.stop()
        else:
         if D_coordinates > 125:
                 Morot_D.run(-20)
         else: 
                 Morot_D.run(20) 
   
     
        #если датчик касания нажат - тогда можно поднять и переместить перо(координаты)
        if touch_sensor.pressed():
               
               wait(0)
       
        
        else:  #стерка 
               if color_sensor.reflection() > 50:
                 ev3.screen.draw_circle(A_coordinates, D_coordinates, size, fill=True, color=Color.WHITE)
               
               #рисовать
               else:
                 ev3.screen.draw_circle(A_coordinates, D_coordinates, size, fill=True, color=Color.BLACK)

                 
        #увеличение размера (радиуса) пера
        if Button.UP in(ev3.buttons.pressed()):
                         if size < 25:
                                 size += 1
                         else: 
                                 ev3.speaker.beep(600)
                         wait(100)

        if Button.DOWN in(ev3.buttons.pressed()):
                         if size > 1:
                                 size -= 1
                         else: 
                                 ev3.speaker.beep(600)
                         wait(100)

        #все стереть и начть заново рисовать с нуля
        if Button.CENTER in(ev3.buttons.pressed()):
                         
                         Morot_A.reset_angle(0)
                         Morot_D.reset_angle(0)
                         ev3.screen.draw_circle(A_coordinates, D_coordinates, size, fill=True, color=Color.BLACK)
                         ev3.screen.clear()
                         ev3.speaker.beep(1000)
                         wait(100)

        else:
         wait(0) 