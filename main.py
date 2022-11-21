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
                'life': 100,
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
                'life': 200,
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
def takedmg(attacker,defender,attack):
    dmg = randint(attacker['stats'][f'dmg{attack}'][0],attacker['stats'][f'dmg{attack}'][1]) - defender['stats']['armor']
    defender['stats']['life'] -= dmg
    loser = defender['name']
    if defender['stats']['life'] <=0:
        print(f'{loser} foi derrotado!!!')
    else:
        print(f'{loser} tomou {dmg} de dano!!!')

def commands(player,enemy):
    battleinf.goto(0,0)
    battleinf.write('Oque Voce Deseja Fazer!?\n[1]Tocar\n[2]Bolsa\n[3]Fugir', font=("Arial", 16, "normal"))
    cmd = int(input())
    if cmd == 1:
        battleinf.clear()
        battleinf.write('selecione seu ataque!!!\n[1]ATAQUE 01\n[2]ATAQUE 02\n[3] ATAQUE 03\n', font=("Arial", 16, "normal"))
        selecatk = int(input())
        if selecatk == 1:
            battleinf.clear()
            battleinf.write('ATAQUE 1 SELECIONADO!!!', font=("Arial", 16, "normal"))
            time.sleep(1)
        elif selecatk == 2:
            battleinf.clear()
            battleinf.write('ATAQUE 2 SELECIONADO!!!', font=("Arial", 16, "normal"))
            time.sleep(1)
        elif selecatk == 3:
            battleinf.clear()
            battleinf.write('ATAQUE 3 SELECIONADO!!!', font=("Arial", 16, "normal"))
            time.sleep(1)
        else:
            battleinf.clear()
            battleinf.write('COMANDO INVALIDO, SELECIONANDO ATAQUE ALEATORIO!!!', font=("Arial", 16, "normal"))
            selecatk = randint(1,3)
            battleinf.clear()
            time.sleep(1)


        takedmg(player,enemy,selecatk)
        if enemy['stats']['life'] <= 20:
            enemy['stats']['dmg1'] = [999,999]
            selecatk = 1
            takedmg(player,enemy,selecatk)
        else:
            selecatk = 1
            takedmg(player,enemy,selecatk)
    elif cmd == 2:
        pass
        #EH AQ ONDE O AMIGAO DANIEL IRA COLOCAR A BOLSA
        selecatk = 1
        takedmg(player,enemy,selecatk)
    elif cmd == 3:
        print('VOCE NAO PODERA FUGIR DESTA BATALHA!!!')
    else:
        print('Comando Invalido!!!')  

def battle(player,enemy):
    playermodel.goto(-230,-150)
    enemymodel.goto(230,150)
    while True:
        battleinf.goto(0,0)
        battleinf.write('SUA RODADA... OQUE DESEJA FAZER???', font=("Arial", 16, "normal"))
        time.sleep(1)
        battleinf.clear()
        if enemy['stats']['life'] >= 0 and player['stats']['life'] >= 0:
            commands(player,enemy)
        else:
            print('cabo baataia')
            break
#################################################################################



#################################################################################
#CORPO PRINCIPAL DO GAME
#################################################################################
window = turtle.Screen()
window.screensize(800,600)
fps = 60
battle(player,enemy)
window.mainloop()