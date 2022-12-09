#################################################################
#                      Trabalho 02 Equipe                       #
#             1- Kelve Monteiro Cartaxo - 542485                #
#             2-Coloquem Seus Nomes                             #
#             3- Daniel Anderson Gonçalves de Oliveira - 540835 #
#             4-Coloquem Seus Nomes                             #
#             5-Coloquem Seus Nomes                             #
#################################################################

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
                #ATKS Buffados, estão sujeitos a balanceamento#
                'dmg7': [25,30],
                'dmg8': [35,40],
                'dmg9': [50,60],
                ################################################
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


window = turtle.Screen()
window.title('Road Of Notes')
window.setup(1360,768)
window.register_shape('c:/Git Things/road-of-notes/sprites/fotofoda.gif')
window.bgpic('c:/Git Things/road-of-notes/sprites/fotofoda.gif')
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
#################################################################################]

#################################################################################
#VARIAVEL RESPONSAVEL PELA QTD DOS AFINADORES
#################################################################################
afinador = 3
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
    #Aproveitando a função do Kel para ataques buffados
    elif key == Key.f7:
        selecatk = 7
    elif key == Key.f8:
        selecatk = 8
    elif key == Key.f9:
        selecatk = 9
    #############################
    else:
        selecatk = randint(1,3)
    return False

#Opções da mochila
def press_on_op(key):
    global selecop
    if key == Key.f4:
        selecop = 4
    elif key == Key.f5:
        selecop = 5
    else:
        selecop = 5
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
        #EH AQ ONDE O AMIGAO DANIEL IRA COLOCAR A BOLSA
        global afinador

        if afinador> 0:
            battleinf.clear()
            battleinf.write(f'Você tem {afinador} afinadores em sua Bolsa!!!\n[F4]Utilizar\n[F5]Não utilizar\n', font=("Minecraft", 16, "normal"))
            with Listener(on_press=press_on_op) as listener:
                listener.join()

            if selecop == 4:
                
                afinador= afinador - 1
                battleinf.clear()
                battleinf.write('Selecione Sua Melodia!!!\n-----------------------------\n[F7]Bohemian Rhapsody\n[F8]Dream On\n[F9]Juliet\n', font=("Minecraft", 16, "normal"))
                with Listener(on_press=press_on_atk) as listener:
                    listener.join()

                if selecatk == 7:
                    battleinf.clear()
                    battleinf.write('Mama, Just Killed A Man', font=("Minecraft", 16, "normal"))
                    time.sleep(1)
                    takedmg(player,enemy,selecatk)
                elif selecatk == 8:
                    battleinf.clear()
                    battleinf.write('The Past Is Gone', font=("Minecraft", 16, "normal"))
                    time.sleep(1)
                    takedmg(player,enemy,selecatk)
                elif selecatk == 9:
                    battleinf.clear()
                    battleinf.write('I am Choosen Undead', font=("Minecraft", 16, "normal"))
                    time.sleep(1)
                    takedmg(player,enemy,selecatk)
                else:
                    battleinf.clear()
                    battleinf.write('COMANDO INVALIDO!!!', font=("Arial", 16, "normal"))
                    selecatk = 1
                    battleinf.clear()
                    time.sleep(1)
                
            elif selecop == 5:
                selecatk = 1
                time.sleep(1.5)
                
        else:
            battleinf.clear()
            battleinf.write(f'SUA BOLSA ESTÁ VAZIA!!!\n', font=("Minecraft", 16, "normal"))
            time.sleep(1.5)
            selecatk = 1
        
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
    playermodel.goto(-400,-280)
    enemymodel.goto(300,-40)
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

battle(player,enemy)
window.mainloop()
