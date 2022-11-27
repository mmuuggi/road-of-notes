###############################################################
#                      Trabalho 02 Equipe                     #
#             1- Kelve Monteiro Cartaxo - 542485              #
#             2-Coloquem Seus Nomes                           #
#             3-Coloquem Seus Nomes                           #
#             4-Coloquem Seus Nomes                           #
#             5-Coloquem Seus Nomes                           #
###############################################################

###########################
#lugar dos imports
import turtle
from random import randint
from pynput.keyboard import *
import time
import os
###########################







#################################################################################
#DECLARANDO PLAYER E ENEMY, COM STATUS
#################################################################################
player  = {'name': 'Yonlero',
            'level': 12,
            'skin' : 'None',
            'stats' : {
                'life': 50,
                'dmg1': [10,15],
                'dmg2': [5,20],
                'dmg3': [0,50],
                'armor': 3
            }
}
playermodel = turtle.Turtle()
playermodel.penup()
playermodel.speed(0)
playermodel.goto(500,500)
playermodel.shape('turtle')
playermodel.shapesize(4)
playermodel.color('Black')


enemy = {'name': 'Damper',
            'level': 30,
            'skin': 'Default',
            'stats': {
                'life': 80,
                'dmg1': [5,10],
                'armor': 3
            }
}
enemymodel = turtle.Turtle()
enemymodel.penup()
enemymodel.speed(0)
enemymodel.goto(500,500)
enemymodel.shape('turtle')
enemymodel.shapesize(2.5)
enemymodel.color('Black')

#################################################################################

#################################################################################
#TEXTOS
#################################################################################
battleinf = turtle.Turtle()
battleinf.hideturtle()
battleinf.color = 'Black'
battleinf.penup()
battleinf.speed(0)
battleinf.goto(500,500)
#################################################################################


#################################################################################
#FUNCOES DA BATALHA//// TOMAR E RECEBER DANO, E OS COMANDOS
#################################################################################
def press_on(key):
    global command
    command = key
    return False

def press_on_atk(key):
    global selecatk
    if key == Key.f1:
        selecatk = 1
    elif key == Key.f2:
        selecatk = 2
    elif key == Key.f3:
        selecatk = 3
    else:
        selecatk = randint(1,3)
    return False

def takedmg(attacker,defender,attack):
    dmg = randint(attacker['stats'][f'dmg{attack}'][0],attacker['stats'][f'dmg{attack}'][1]) - defender['stats']['armor']
    defender['stats']['life'] -= dmg
    loser = defender['name']
    if defender['stats']['life'] <=0:
        battleinf.clear()
        battleinf.write(f'{loser} foi derrotado!!!', font=("Minecraft", 16, "normal"))
        time.sleep(1.5)
    else:
        battleinf.clear()
        battleinf.write(f'{loser} tomou {dmg} de dano!!!', font=("Minecraft", 16, "normal"))
        time.sleep(1.5)

def commands(player,enemy):
    battleinf.clear()
    battleinf.goto(150,-340)
    battleinf.write('Oque Voce Deseja Fazer!?\n----------------------------------\n[Space] Para Atacar\n[CapsLK]Para Bolsa\n[Enter]Para Fugir', font=("Minecraft", 16, "normal"))
    with Listener(on_press=press_on) as listener:
        listener.join()
    
    if command == Key.space:
        global selecatk
        battleinf.clear()
        battleinf.write('Selecione Sua Melodia!!!\n-----------------------------\n[F1]Bohemian Rhapsody\n[F2]Dream On\n[F3]Juliet\n', font=("Minecraft", 16, "normal"))
        with Listener(on_press=press_on_atk) as listener:
            listener.join()
        if selecatk == 1:
            battleinf.clear()
            battleinf.write('Mama, Just Killed A Man', font=("Minecraft", 16, "normal"))
            time.sleep(1.5)
        elif selecatk == 2:
            battleinf.clear()
            battleinf.write('The Past Is Gone', font=("Minecraft", 16, "normal"))
            time.sleep(1.5)
        elif selecatk == 3:
            battleinf.clear()
            battleinf.write('I am Choosen Undead', font=("Minecraft", 16, "normal"))
            time.sleep(1.5)
        else:
            battleinf.clear()
            battleinf.write('COMANDO INVALIDO, SELECIONANDO ATAQUE ALEATORIO!!!', font=("Minecraft", 16, "normal"))
            battleinf.clear()
            time.sleep(1.5)


        takedmg(player,enemy,selecatk)
        if enemy['stats']['life'] <= 20:
            enemy['stats']['dmg1'] = [999,999]
            selecatk = 1
            takedmg(enemy,player,selecatk)
        else:
            selecatk = 1
            takedmg(enemy,player,selecatk)
    elif command == Key.caps_lock:
        pass
        #EH AQ ONDE O AMIGAO DANIEL IRA COLOCAR A BOLSA
        selecatk = 1
        takedmg(enemy,player,selecatk)
        time.sleep(1.5)
    elif command == Key.enter:
        battleinf.clear()
        battleinf.goto(-50,-340)
        battleinf.write('UM MÚSICO SEMPRE TERMINA SUA MELODIA!!!', font=("Minecraft", 16, "normal"))
        time.sleep(1.5)
    else:
        battleinf.clear()
        battleinf.goto(150,-340)
        battleinf.write('COMANDO INVALIDO!!!', font=("Minecraft", 16, "normal"))
        time.sleep(1.5)
def battle(player,enemy):
    playermodel.goto(-230,-150)
    enemymodel.goto(230,150)
    while True:
        battleinf.clear()
        battleinf.goto(15,-300)
        battleinf.write('SUA RODADA... OQUE DESEJA FAZER???', font=("Minecraft", 16, "normal"))
        time.sleep(1.5)
        battleinf.clear()
        if enemy['stats']['life'] >= 0 and player['stats']['life'] >= 0:
            commands(player,enemy)
        else:
            battleinf.clear()
            battleinf.write('Batalha Encerrada', font=("Minecraft", 16, "normal"))
            time.sleep(1.5)
            quit()
#################################################################################



#################################################################################
#CORPO PRINCIPAL DO GAME
#################################################################################
window = turtle.Screen()
window.screensize(800,600)
fps = 60
battle(player,enemy)
window.mainloop()