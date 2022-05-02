# AdCap Ripoff

from ast import While
from multiprocessing import Manager
from turtle import ycor
import pygame
pygame.init()


#color library
red = (255, 0, 0)
green = (0, 255,0)
blue = (0,0,255)
white = (255, 255, 255)
black = (0,0,0)
purple = (175,0,255)
orange = (255,165,0)
yellow = (255,255,0)

# general variables
screen = pygame.display.set_mode([500, 680])
pygame.display.set_caption("Toltally not a ripoff of a popular idle game")
background = black
framerate = 60
font = pygame.font.Font('freesansbold.ttf', 16)
timer = pygame.time.Clock()
draw_red = False
draw_orange = False
draw_yellow = False
draw_green = False
draw_blue = False
draw_purple = False
red_length = 0
orange_length = 0
yellow_length = 0
green_length = 0
blue_length = 0
purple_length = 0
red_speed = 6
red_upgraded_speed = 12
red_upgraded_speed2 = 24
orange_speed = 5
yellow_speed = 4
green_speed = 3
blue_speed = 2
purple_speed = 1
score = 0


#draw buttons 

#red buttons
redCost = 1
redOwned = False
redManagerCost = 100
redAmount = 0

#orange button
orangeCost = 2
orangeOwned = False
orangeManagerCost = 500
orangeAmount = 0

#yellow button
yellowCost = 3
yellowOwned = False
yellowManagerCost = 1900
yellowAmount = 0

#green button
greenCost = 4
greenOwned = False
greenManagerCost = 4000
greenAmount = 0 

#blue button
blueCost = 5
blueOwned = False
blueManagerCost = 10000
blueAmount = 0

#purple button
purpleCost = 6
purpleOwned = False
purpleManagerCost = 100000
purpleAmount = 0





#game variables
red_value = 1
orange_value = 2
yellow_value = 3
green_value = 4
blue_value = 5
purple_value = 6

def draw_task(color, yCord, value, draw, length, speed, amountOwned):
    global score
    if draw and length < 200:
        length += speed
    elif length >= 200:
        draw = False 
        length = 0
        score += value 
    task = pygame.draw.circle(screen, color, (175, yCord ), 20, 5)
    pygame.draw.rect(screen, color, [200, yCord - 15, 200, 30])
    pygame.draw.rect(screen, black, [205, yCord - 10, 190, 20])
    pygame.draw.rect(screen, color, [200,yCord - 15, length,30])
    value_text = font.render(str(round(value, 2)), True, white)
    screen.blit(value_text, (160, yCord - 10))
    Amount_Owned = font.render('Amount Owned:'+str(round(amountOwned)), True, white)
    screen.blit(Amount_Owned,(10, yCord - 10))
    return task, length, draw

def draw_button(color, xCord,yCord, cost, owned, managerCost):
    color_button = pygame.draw.rect(screen, color, [xCord, yCord, 60, 40])
    color_cost = font.render(str(round(cost, 1)), True, black)
    screen.blit(color_cost, (xCord + 1, yCord))
    yCord = yCord + 80
    if not owned:
        managerButton = pygame.draw.rect(screen, color, [xCord, yCord, 60, 40])
        managerText = color_cost = font.render(str(round(managerCost, 2)), True, black)
        screen.blit(managerText, (xCord + 1, yCord))
    else:
        managerButton = pygame.draw.rect(screen, black, [xCord, yCord, 60, 40])
    return color_button, managerButton
    
    
    
#if game is running do this
running = True
while running:
    timer.tick(framerate)
    
    #if manager is owned auto get moneys
    #red
    if redOwned and not draw_red:
        draw_red = True
    #orange
    if orangeOwned and not draw_orange:
        draw_orange = True
    #yellow
    if yellowOwned and not draw_yellow:
        draw_yellow = True
    #green
    if greenOwned and not draw_green:
        draw_green = True
    #blue
    if blueOwned and not draw_blue:
        draw_blue = True
    #purple
    if purpleOwned and not draw_purple:
        draw_purple = True
    
    
    #quit function
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            
            #Red button dection
            if task1.collidepoint(event.pos):
                draw_red = True
            if redManagerBuy.collidepoint(event.pos) and score >= redManagerCost and not redOwned:
                redOwned = True
                score -= redManagerCost
            if redBuy.collidepoint(event.pos) and score >= redCost:
                red_value += .15
                score -= redCost
                redCost += .19
                redAmount += 1
            if redAmount >= 100:
                red_speed = red_upgraded_speed2
            elif redAmount >=10:
                red_speed = red_upgraded_speed
            
                
                
            #Orange button detection
            if task2.collidepoint(event.pos):
                draw_orange = True
            if orangeManagerBuy.collidepoint(event.pos) and score >= orangeManagerCost and not orangeOwned:
                orangeOwned = True
                score -= orangeManagerCost 
            if orangeBuy.collidepoint(event.pos) and score >= orangeCost:
                orange_value += .20
                score -= orangeCost 
                orangeCost += .21
                orangeAmount += 1
            if orangeAmount >= 100:
                orange_speed = orange_upgraded_speed2
            elif orangeAmount >=10:
                orange_speed = orange_upgraded_speed
                               
            #yellow button detection
            if task3.collidepoint(event.pos):
                draw_yellow = True
            if yellowManagerBuy.collidepoint(event.pos) and score >= yellowManagerCost and not yellowOwned:
                yellowOwned = True
                score -= yellowManagerCost    
            if yellowBuy.collidepoint(event.pos) and score >= yellowCost:
                yellow_value += .30
                score -= yellowCost 
                yellowCost += .35  
                yellowAmount += 1
            if yellowAmount >= 100:
                yellow_speed = yellow_upgraded_speed2
            elif yellowAmount >=10:
                yellow_speed = yellow_upgraded_speed                
                 
            #green button detection
            if task4.collidepoint(event.pos):
                draw_green = True
            if greenManagerBuy.collidepoint(event.pos) and score >= greenManagerCost and not greenOwned:
                greenOwned = True
                score -= greenManagerCost
            if greenBuy.collidepoint(event.pos) and score >= greenCost:
                green_value += .35
                score -= greenCost 
                greenCost += .4
                greenAmount =+ 1
            if redAmount >= 100:
                green_speed = green_upgraded_speed2
            elif greenAmount >=10:
                green_speed = green_upgraded_speed



            #blue button detection
            if task5.collidepoint(event.pos):
                draw_blue = True
            if blueManagerBuy.collidepoint(event.pos) and score >= blueManagerCost and not blueOwned:
                blueOwned = True
                score -= blueManagerCost  
            if blueBuy.collidepoint(event.pos) and score >= blueCost:
                blue_value += .40
                score -= blueCost 
                blueCost += .5
                blueAmount += 1
            if blueAmount >= 100:
                blue_speed = blue_upgraded_speed2
            elif blueAmount >=10:
                blue_speed = blue_upgraded_speed


            #purple button detectection
            if task6.collidepoint(event.pos):
                draw_purple = True                
            if purpleManagerBuy.collidepoint(event.pos) and score >= purpleManagerCost and not purpleOwned:
                purpleOwned = True
                score -= purpleManagerCost
            if purpleBuy.collidepoint(event.pos) and score >= purpleCost:
                purple_value += 1
                score -= purpleCost 
                purpleCost += 1.2  
                purpleAmount += 1
            if purpleAmount >= 100:
                purple_speed = purple_upgraded_speed2
            elif purpleAmount >=10:
                purple_speed = purple_upgraded_speed                
                                        
                
    # makes the play area populated with task to do
    screen.fill(background)
    
    #red task
    task1, red_length, draw_red = draw_task(red, 50, red_value, draw_red, red_length, red_speed, redAmount)
    redBuy, redManagerBuy = draw_button(red, 10, 410, redCost, redOwned, redManagerCost)
    
     #orange task
    task2, orange_length, draw_orange = draw_task(orange, 110, orange_value, draw_orange, orange_length, orange_speed, orangeAmount)
    orangeBuy, orangeManagerBuy = draw_button(orange, 80, 410, orangeCost, orangeOwned, orangeManagerCost)
    
    #yellow task
    task3, yellow_length, draw_yellow = draw_task(yellow, 170, yellow_value, draw_yellow, yellow_length, yellow_speed, yellowAmount)
    yellowBuy, yellowManagerBuy = draw_button(yellow, 150, 410, yellowCost, yellowOwned, yellowManagerCost)
    
    #green task
    task4, green_length, draw_green = draw_task(green, 230, green_value, draw_green, green_length, green_speed, greenAmount)
    greenBuy, greenManagerBuy = draw_button(green, 220, 410, greenCost, greenOwned, greenManagerCost)
    
    #blue task
    task5, blue_length, draw_blue = draw_task(blue, 290, blue_value, draw_blue, blue_length, blue_speed, blueAmount)
    blueBuy, blueManagerBuy = draw_button(blue, 290, 410, blueCost, blueOwned, blueManagerCost)
    
    #purple task
    task6, purple_length, draw_purple = draw_task(purple, 350, purple_value, draw_purple, purple_length, purple_speed, purpleAmount)
    purpleBuy, purpleManagerBuy= draw_button(purple, 360, 410, purpleCost, purpleOwned, purpleManagerCost)

 

 
    
    display_score = font.render('Money: $'+str(round(score,2)),True, white, black)
    screen.blit(display_score, (10, 5))
    
    #writes buy more?
    buyMore = font.render("Buy More", True, white)
    screen.blit(buyMore, (10, 385) )
    #writes buy managers
    buyManagers = font.render("Buy Managers", True, white)
    screen.blit(buyManagers, (10, 465) )
    #write the instructions for the game In a wierd way since pygame for soome reason cant do muli line text
    info = font.render('INFO:Press the circle buttons to gain the amount of money-', True, white)
    screen.blit(info, (20, 550))
    info = font.render('that is listed in said circle. once you have enough money-', True, white)
    screen.blit(info, (20, 565))
    info = font.render('you can buy managers to do all the work for you. You can-', True, white)
    screen.blit(info, (20, 580))
    info = font.render('also buy more products and increase your revenue output.', True, white)
    screen.blit(info, (20, 595))
    info = font.render('once you own 10 of an item the speed doubles same thing-', True, white)
    screen.blit(info, (20, 610))
    info = font.render('happenes once again when you own 100 of an item', True, white)
    screen.blit(info, (20, 625))
    #writes how much somthing will bring when you press a button
    priceInfo = font.render('Price', True, white)
    screen.blit(priceInfo, (158, 5))
    
    pygame.display.flip()

pygame.quit
            
            
    
    

