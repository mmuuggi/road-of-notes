#################################################################
#                      Trabalho 02 Equipe                       #
#             1- Kelve Monteiro Cartaxo - 542485                #
#             2-Guilherme Henrique Alves Pinto - 545304         #
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
import winsound
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
playermodel.goto(500,600)
playermodel.shape('turtle')
playermodel.shapesize(4)
playermodel.color('Black')
playermodel.hideturtle()


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
enemymodel.goto(500,600)
enemymodel.shape('turtle')
enemymodel.shapesize(2.5)
enemymodel.color('Black')
enemymodel.hideturtle()

window = turtle.Screen()
window.title('Road Of Notes')
window.setup(1360,768)
window.register_shape('c:/Git Things/road-of-notes/sprites/fotofoda.gif')
window.register_shape('c:/Git Things/road-of-notes/sprites/c1.gif')
window.register_shape('c:/Git Things/road-of-notes/sprites/c2.gif')
window.register_shape('c:/Git Things/road-of-notes/sprites/c3.gif')
window.register_shape('c:/Git Things/road-of-notes/sprites/c4.gif')
window.register_shape('c:/Git Things/road-of-notes/sprites/p1.gif')
window.register_shape('c:/Git Things/road-of-notes/sprites/p2.gif')
window.register_shape('C:/Git Things/road-of-notes/sprites/title_screen.gif')

window.bgpic('c:/Git Things/road-of-notes/sprites/title_screen.gif')
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

cutext = turtle.Turtle()
cutext.hideturtle()
cutext.color("white")
cutext.penup()
cutext.speed(0)
cutext.goto(-500,-300)
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

#opções no menu inicial
def press_on_title(key):
    global selectitle
    if key == Key.up:
        selectitle = 1
    elif key == Key.down:
        selectitle = 2
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

def cutscene():
    window.bgpic('c:/Git Things/road-of-notes/sprites/c1.gif')
    cutext.write(
        'A musica rege nossa sociedade, nossas vidas, nosso mundo...\n'
        'era isso que a mamãe sempre me dizia, mas o porque?\n'
        'Por que devemos viver melhor do que os outros, acima dos outros?\n'
        'Por que vivemos em castelos no alto da cidade enquanto tem gente\n'
        'passando fome abaixo dos nossos olhos?\n'
        'Por que só nós somos permiditos de usar a magia da musica?\n'
        'Da onde vem o poder da musica? eu preciso saber, nem que pra isso\n'
        'eu tenha que fugir daqui...'
        ,
        font=("Minecraft", 16, "normal"))
    time.sleep(15.0)
    cutext.clear()
    window.bgpic('c:/Git Things/road-of-notes/sprites/c2.gif')
    cutext.write(
        'Não vou poder levar meu violino para não levantar suspeitas\n'
        'Ainda bem que descobri uma loja clandestina na periferia, é melhor eu\n'
        'comprar algum instrumento para me protejer durante a jornada.\n'
        'Duvido que aqui vai ter algum violino, mas preciso de um instrumento de corda\n'
        ,
        font=("Minecraft", 16, "normal"))
    time.sleep(12.0)
    cutext.clear()
    window.bgpic('c:/Git Things/road-of-notes/sprites/c3.gif')
    cutext.write(
        'Entrando na loja vejo um velho polindo uma espada antiga com cuidado\n'
        'Chamei ele, que ao me ver pós um olhar de despreso em mim\n'
        '"O que um sangue nobre quer aqui? se vai me matar faça logo" - ele disse\n'
        '"Só estou procurando por um instrumento novo, de preferencia de corda" - lhe disse\n'
        'Ele jogou a espada no chão e foi ate um armario e o abriu com agressividade\n'
        '"Só pega o que tu que e vai embora, a ultima coisa que eu quero são os\n'
        'os sangue nobres por perto" - disse e logo após voltou a polir a sua espada\n'
        'Entre vários instrumentos que estavam la, apenas um era de corda, um simples\n'
        'bandolim com formato estranho, mas era minha única opção. Resolvi sair de lar\n'
        'e deixar o velho em paz...'
        ,
        font=("Minecraft", 16, "normal"))
    time.sleep(20.0)
    cutext.clear()
    window.bgpic('c:/Git Things/road-of-notes/sprites/c4.gif')
    cutext.write(
        'Sai de dentro dos muros da cidade, preciso descobrir a origem da musica\n'
        'para enterder porque o mundo é como é...\n'
        'Escuto uma voz familiar e autoritaria vindo de perto\n'
        '"Aonde pensa que vai Yonlero?" - meu irmão descobriu, mas como?\n'
        '"Damer, eu preciso descobrir a origem da musica e você não vai me impedi!"\n'
        '"você não vai a lugar algum e você sabe disso" - diz após dar uma gargalhada'
        ,
        font=("Minecraft", 16, "normal"))
    time.sleep(12.0)
    cutext.clear()
    battle(player,enemy)

def title():
    with Listener(on_press=press_on) as listener:
        listener.join()
        if command == Key.up:
            cutscene()
        elif command == Key.down:
            quit()
    while (command != Key.up or command != Key.down):
        with Listener(on_press=press_on) as listener:
            listener.join()

        if command == Key.up:
            cutscene()
        elif command == Key.down:
            quit()

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
        battleinf.goto(130,-270)
        battleinf.write(f'{loser} tomou {dmg} de dano!!!', font=("Minecraft", 16, "normal"))
        time.sleep(1.5)

def commands(player,enemy):
    battleinf.clear()
    battleinf.goto(130,-320)
    battleinf.write('Oque Voce Deseja Fazer!?\n----------------------------------\n[Space] Para Atacar\n[CapsLK]Para Bolsa\n[Enter]Para Fugir', font=("Minecraft", 16, "normal"))
    with Listener(on_press=press_on) as listener:
        listener.join()
    
    if command == Key.space:
        global selecatk
        battleinf.clear()
        battleinf.write('Selecione Sua Melodia!!!\n-----------------------------\n[F1]Flauta Envolvente\n[F2]Here Comes The Sun\n[F3]Drum Mix\n', font=("Minecraft", 16, "normal"))
        with Listener(on_press=press_on_atk) as listener:
            listener.join()
        if selecatk == 1:
            battleinf.clear()
            battleinf.goto(35,-270)
            battleinf.write('É a flauta envolvente que mexe com a mente', font=("Minecraft", 16, "normal"))
            winsound.PlaySound('songs/flautae.wav', winsound.SND_ASYNC)
            time.sleep(1.5)
        elif selecatk == 2:
            battleinf.clear()
            battleinf.goto(50,-270)
            battleinf.write("Here comes the Sun And I say It's all right", font=("Minecraft", 16, "normal"))
            winsound.PlaySound('songs/bandolin.wav', winsound.SND_ASYNC)
            time.sleep(1.5)
        elif selecatk == 3:
            battleinf.clear()
            battleinf.goto(170,-270)
            battleinf.write('Feel the magic...', font=("Minecraft", 16, "normal"))
            winsound.PlaySound('songs/tambor.wav', winsound.SND_ASYNC)
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
            winsound.PlaySound('songs/harpa.wav', winsound.SND_ASYNC)
            takedmg(enemy,player,selecatk)
        else:
            selecatk = 1
            takedmg(enemy,player,selecatk)
    elif command == Key.caps_lock:
        #EH AQ ONDE O AMIGAO DANIEL IRA COLOCAR A BOLSA
        global afinador

        if afinador> 0:
            battleinf.clear()
            battleinf.goto(60,-320)
            battleinf.write(f'Você tem {afinador} afinadores em sua Bolsa!!!\n[F4]Utilizar\n[F5]Não utilizar\n', font=("Minecraft", 16, "normal"))
            with Listener(on_press=press_on_op) as listener:
                listener.join()

            if selecop == 4:
                
                afinador= afinador - 1
                battleinf.clear()
                battleinf.goto(130,-340)
                battleinf.write('Selecione Sua Melodia!!!\n-----------------------------\n[F7]Flauta Envolvente\n[F8]Here Comes The Sun\n[F9]Drum Mix\n', font=("Minecraft", 16, "normal"))
                with Listener(on_press=press_on_atk) as listener:
                    listener.join()

                if selecatk == 7:
                    battleinf.clear()
                    battleinf.goto(35,-270)
                    battleinf.write('É a flauta envolvente que mexe com a mente', font=("Minecraft", 16, "normal"))
                    winsound.PlaySound('songs/flautae.wav', winsound.SND_ASYNC)
                    time.sleep(1.5)
                    takedmg(player,enemy,selecatk)
                elif selecatk == 8:
                    battleinf.clear()
                    battleinf.goto(50,-270)
                    battleinf.write("Here comes the Sun And I say It's all right", font=("Minecraft", 16, "normal"))
                    winsound.PlaySound('songs/bandolin.wav', winsound.SND_ASYNC)
                    time.sleep(1.5)
                    takedmg(player,enemy,selecatk)
                elif selecatk == 9:
                    battleinf.clear()
                    battleinf.goto(170,-270)
                    battleinf.write('Feel the magic...', font=("Minecraft", 16, "normal"))
                    winsound.PlaySound('songs/tambor.wav', winsound.SND_ASYNC)
                    time.sleep(1.5)
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
        battleinf.goto(60,-270)
        battleinf.write('UM MÚSICO SEMPRE TERMINA SUA MELODIA!!!', font=("Minecraft", 12, "normal"))
        time.sleep(1.5)
    else:
        battleinf.clear()
        battleinf.goto(150,-340)
        battleinf.write('COMANDO INVALIDO!!!', font=("Minecraft", 16, "normal"))
        time.sleep(1.5)

def battle(player,enemy):
    window.bgpic('c:/Git Things/road-of-notes/sprites/fotofoda.gif')
    playermodel.goto(-400,-180)
    playermodel.shape('c:/Git Things/road-of-notes/sprites/p1.gif')
    playermodel.showturtle()
    enemymodel.goto(300,100)
    enemymodel.showturtle()
    enemymodel.shape('c:/Git Things/road-of-notes/sprites/p2.gif')
    while True:
        battleinf.clear()
        battleinf.goto(40,-270)
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


#################################################################################
#battle(player,enemy)
title()
window.mainloop()
