import pygame, sys, random
from tkinter import *
import tkinter
from pygame import mixer
import cv2

# install pygame by "python3 -m pip install -U pygame --user"

# install cv2 by "pip install opencv-python"

def menu():
        root = Tk() 

        root.title("DA BIRD") # name of the window

        root.tk.call('wm', 'iconphoto', root._w, PhotoImage(file = 'Ressources/image-etc/Flappy_Bird_icon.png')) #set the icon

        root.resizable(width=False, height=False) #bloquer l'agrandissement de la fenêtre
        
        root.geometry("288x512") 
        
        bg = PhotoImage(file = "Ressources/image-etc/MENU/background-night.png") #image fond 

        def play_music():
            mixer.init()
            mixer.music.load("Ressources/sound/sfx_point.wav")# Apporte le son de l'aile
            mixer.music.play()

        # Label

        label1 = Label(root, image = bg) # permet de placer l'image
        label1.place(x = 0, y = 0) 
        
        label2 = Label(root, text = "Welcome to DA BIRD !", bg = 'blue' ,fg = 'black' , font ='bold' ) # TEXTE
        label2.pack(pady = 3)

        label6 = Label(root, text = "BY Lokendra BHATI", bg = '#008793' ,fg = 'orange' , font ='Serial' ) # TEXTE
        label6.pack(pady = 2)

        label3 = Label(root, text = "Sponsorised by RALIF&CO", bg = '#008793' ,fg = 'Gold' , font ='Serial 15 underline') # TEXTE
        label3.pack(pady = 0) 
        
        label4 = Label(root, text = "Choose your skin", bg = '#008793' ,fg = 'orange' , font ='Serial' ) # TEXTE
        label4.pack(pady = 0)

        label5 = Label(root, text = "Before continuing !", bg = '#008793' ,fg = 'orange' , font ='Serial' ) # TEXTE
        label5.pack(pady = 0)

        # Frame

        frame1 = Frame(root, bg = '#008793') # FRAME/SKIN BUTTON //////#contour du boutton 
        frame1.pack(pady = 10 ) 

        frame2 = Frame(root, bg = '#008793') # FRAME/HARD BUTTON
        frame2.pack(pady = 10 ) 

        frame3 = Frame(root, bg = '#00b3c2') # FRAME/SECRET BUTTON
        frame3.pack(pady = 5 ) 

        frame4 = Frame(root, bg = '#00a300') # FRAME/SKIN BUTTON
        frame4.pack(pady = 2 )

        frame5 = Frame(root, bg = '#00a300') # FRAME/SKIN BUTTON
        frame5.pack(pady = 2 ) 

        frame6 = Frame(root, bg = '#00a300') # FRAME/SKIN BUTTON
        frame6.pack(pady = 2 ) 

        frame7 = Frame(root, bg = '#00a300') # FRAME/SKIN BUTTON
        frame7.pack(pady = 2 ) 


        buttonClicked  = False # Before first click
        buttonClicked2  = False # Before first click
        buttonClicked3  = False # Before first click
        buttonClicked4  = False # Before first click

        def callback(): #lors du click pour skin
            global buttonClicked, bird1, bird2, bird3
            buttonClicked = True
            bird1 = 'Ressources/image-etc/SECRET/BIRD/bluebird-downflap.png'
            bird2 = 'Ressources/image-etc/SECRET/BIRD/bluebird-midflap.png'
            bird3 = 'Ressources/image-etc/SECRET/BIRD/bluebird-upflap.png'
            print('bird bleu choisi')
            return bird1, bird2, bird3


        def callback2(): #lors du click pour skin
            global buttonClicked, bird1, bird2, bird3
            buttonClicked2 = True
            bird1 = 'Ressources/image-etc/SECRET/BIRD/redbird-downflap.png'
            bird2 = 'Ressources/image-etc/SECRET/BIRD/redbird-midflap.png'
            bird3 = 'Ressources/image-etc/SECRET/BIRD/redbird-upflap.png'
            print('bird rouge choisi')
            return bird1, bird2, bird3

        def callback3(): #lors du click pour skin
            global buttonClicked, bird1, bird2, bird3
            buttonClicked3 = True
            bird1 = 'Ressources/image-etc/SECRET/BIRD/cyberbird-downflap.png'
            bird2 = 'Ressources/image-etc/SECRET/BIRD/cyberbird-midflap.png'
            bird3 = 'Ressources/image-etc/SECRET/BIRD/cyberbird-upflap.png'
            print('bird cyber choisi')
            return bird1, bird2, bird3

        def callback4(): #lors du click pour skin
            global buttonClicked, bird1, bird2, bird3
            buttonClicked4 = True
            bird1 = 'Ressources/image-etc/SECRET/BIRD/Sound-Flap/Sound-Secret/secretbird-flap.png'
            bird2 = 'Ressources/image-etc/SECRET/BIRD/Sound-Flap/Sound-Secret/secretbird-flap.png'
            bird3 = 'Ressources/image-etc/SECRET/BIRD/Sound-Flap/Sound-Secret/secretbird-flap.png'
            print('bird secret choisi')
            return bird1, bird2, bird3

        # Button skin

        button4 = Button(frame4, activebackground ='white', bg = '#008793', command = callback) #boutton skin
        button4.pack(pady = 3)
        im4 = tkinter.PhotoImage(file="Ressources/image-etc/SECRET/BIRD/bluebird-downflap.png")
        button4.config(image=im4)

        button5 = Button(frame5, activebackground ='white', bg = '#008793', command = callback2) #boutton skin
        button5.pack(pady = 3)
        im5 = tkinter.PhotoImage(file="Ressources/image-etc/SECRET/BIRD/redbird-downflap.png")
        button5.config(image=im5)

        button6 = Button(frame6, activebackground ='white', bg = '#008793', command = callback3) #boutton skin
        button6.pack(pady = 3)
        im6 = tkinter.PhotoImage(file="Ressources/image-etc/SECRET/BIRD/cyberbird-downflap.png")
        button6.config(image=im6)

        button7 = Button(frame7, activebackground ='white', bg = '#008793', command = callback4) #boutton skin
        button7.pack(pady = 3)
        im7 = tkinter.PhotoImage(file="Ressources/image-etc/SECRET/BIRD/Sound-Flap/Sound-Secret/secret-image.png")
        button7.config(image=im7)

        # Les gros button
        # Created by BHATI Lokendra
        button1 = Button(frame1, bg = '#008793', activebackground = 'yellow', command = lambda:[play_music(),jeu_normal(bird1, bird2, bird3)]) # NORMAL/BUTTON
        button1.pack(pady = 3) # taille contour du boutton
        im1 = tkinter.PhotoImage(file="Ressources/button/normal-button.png")
        button1.config(image=im1)


        button2 = Button(frame2, bg = '#008793', activebackground = 'red', command = lambda:[play_music(),jeu_hard(bird1, bird2, bird3)]) # HARD BUTTON
        button2.pack(pady = 2) 
        im2 = tkinter.PhotoImage(file="Ressources/button/hard-button.png")
        button2.config(image=im2)
        
        button3 = Button(frame3, bg = '#008793', activebackground = 'grey', state="disabled", command = lambda:[play_music(),jeu_secret(bird1, bird2, bird3)]) # SECRET BUTTON
        button3.pack(pady = 0) 
        im3 = tkinter.PhotoImage(file="Ressources/button/secret-button.png")
        button3.config(image=im3)


        def enableEntry(): #Permet de changer l'état du bouton 3
            button3.configure(state="normal")
            button3.update()

        def disableEntry():
            button3.configure(state="disabled")
            button3.update()

        var = StringVar()
        disableEntryRadioButton = Radiobutton(frame2, variable=var, value="0", command=disableEntry, bg = '#008793', fg='#008793', selectcolor='#008793', activebackground= '#008793') # Radio button
        disableEntryRadioButton.pack(side = 'right')
        enableEntryRadioButton = Radiobutton(frame2, variable=var, value="1", command=enableEntry, bg = '#008793', fg='#008793', selectcolor='#008793', activebackground= '#008793') # Radio button
        enableEntryRadioButton.pack(side = 'left')
        

        root.mainloop()

def jeu_normal(bird1, bird2, bird3):
    global score, can_score
    def draw_floor(): # défiler "base"
        screen.blit(floor_surface,(floor_x_pos,450)) #affiche l'image "base" sur l'écran ## mettre 900 pour doubler 
        screen.blit(floor_surface,(floor_x_pos + 288,450))

    def create_pipe(): #créer des "pipe" / top and bot
        random_pipe_pos = random.choice(pipe_height) # choisie la taille "pipe" au hasard
        bottom_pipe = pipe_surface.get_rect(midtop = (350,random_pipe_pos))
        top_pipe = pipe_surface.get_rect(midbottom = (350,random_pipe_pos - 150))
        return bottom_pipe, top_pipe

    def move_pipes(pipes): # fait bouger "pipe"
        for pipe in pipes:
            pipe.centerx -= 3 # vitesse "pipe"
        visible_pipes = [pipe for pipe in pipes if pipe.right > -25] # supprime les "pipe" de la liste : qui ne sont plus sur l'écran 
        return visible_pipes

    def draw_pipes(pipes): # Affiche "pipe"
        for pipe in pipes:
            if pipe.bottom >= 512:
                screen.blit(pipe_surface,pipe)
            else: 
                flip_pipe = pygame.transform.flip(pipe_surface,False,True) # tourne top "pipe"
                screen.blit(flip_pipe, pipe)

    def check_collision(pipes): # vérifier les collisions entre "bird" et "pipe"
        global score, can_score
        
        for pipe in pipes:
            if bird_rect.colliderect(pipe): # si il y a une collision
                death_sound.play() # joue le son "death"
                can_score = True
                return False
        
        if bird_rect.top <= -100 or bird_rect.bottom >= 450: # "bird" dépasse les bords
            death_sound.play() # joue le son "death"
            can_score = True
            return False

        return True

    def rotate_bird(bird): # rotation de "bird"
        new_bird = pygame.transform.rotozoom(bird, -bird_movement * 3, 1)
        return new_bird

    def bird_animation(): # mettre à la meme taille des différentes images dans rect
        new_bird = bird_frames[bird_index]
        new_bird_rect = new_bird.get_rect(center = (50, bird_rect.centery))
        return new_bird,new_bird_rect

    def score_display(game_state): # affiche "score" et "high_score"
        if game_state == 'main_game':
            score_surface = game_font.render(str(int(score)),True, (255,255,255)) # couleur et texte
            score_rect = score_surface.get_rect(center = (144, 50))
            screen.blit(score_surface, score_rect)
        
        if game_state == 'game_over':
            score_surface = game_font.render(f'Score: {int(score)}',True, (255,255,255)) # couleur et texte
            score_rect = score_surface.get_rect(center = (144, 50))
            screen.blit(score_surface, score_rect)

            high_score_surface = game_font.render(f'High Score: {int(high_score)}',True, (255,255,255)) # couleur et texte
            high_score_rect = high_score_surface.get_rect(center = (144, 425))
            screen.blit(high_score_surface, high_score_rect)

    def update_score(score, high_score): # pour que "high_score" fonctionne
        if score > high_score:
            high_score = score
        return high_score
    
    def pipe_score_check(): # permet de vérifier et d'attribuer les points du score
        global score, can_score
        

        if pipe_list:
            for pipe in pipe_list:
                if 45 < pipe.centerx < 55 and can_score:
                    score += 1
                    score_sound.play()
                    can_score = False
                if pipe.centerx < 0: 
                    can_score = True


    pygame.init() # Created by BHATI Lokendra
    screen = pygame.display.set_mode((288,512)) # define width and height
    clock = pygame.time.Clock() #set the FPS (Frames Per Second)
    game_font = pygame.font.Font('Ressources/04B_19.TTF',25) # caractéristique du texte pour "score"

    pygame.display.set_caption('DA BIRD') # name of the window
    Icon = pygame.image.load('Ressources/image-etc/Flappy_Bird_icon.png') #import the icon
    pygame.display.set_icon(Icon) # set the icon
 

    # GAME VARIABLES
    gravity = 0.25
    bird_movement = 0
    game_active = True
    score = 0
    high_score = 0
    can_score = True


    bg_surface = pygame.image.load('Ressources/image-etc/NORMAL/background-day.png').convert() # Apporte l'arrière-plan statique
    #bg_surface = pygame.transform.scale2x(bg_surface) doubler la surface "set_mode (576,1024)""

    floor_surface = pygame.image.load('Ressources/image-etc/NORMAL/base.png').convert() # Arrière-plan dynamique
    #floor_surface = pygame.transform.scale2x(floor_surface) doubler la surface "set_mode (576,1024)"
    floor_x_pos = 0

    bird_downflap = pygame.image.load(bird1).convert_alpha() # Apporte l'image "bird"
    bird_midflap = pygame.image.load(bird2).convert_alpha()
    bird_upflap = pygame.image.load(bird3).convert_alpha()
    bird_frames = [bird_downflap,bird_midflap,bird_upflap] # liste des surfaces
    # pygame.transform.scale2x(pygame.image"...") pour agrandir
    bird_index = 0
    bird_surface = bird_frames[bird_index]
    bird_rect = bird_surface.get_rect(center = (50,256)) # creer un rectangle autour de "bird"

    BIRDFLAP = pygame.USEREVENT + 1
    pygame.time.set_timer(BIRDFLAP, 200)

    #bird_surface = pygame.image.load('Ressources/image-etc/SECRET/BIRD/bluebird-midflap.png').convert_alpha() # Apporte l'image "bird"
    #bird_surface = pygame.transform.scale2x(bird_surface) doubler la surface "set_mode (576,1024)"
    #bird_rect = bird_surface.get_rect(center = (50,256)) # creer un rectangle autour de "bird"

    pipe_surface = pygame.image.load('Ressources/image-etc/NORMAL/pipe-green.png') # Apporte l'image "pipe"
    #pipe_surface = pygame.transform.scale2x(pipe_surface) doubler la surface "set_mode (576,1024)"
    pipe_list = []
    SPAWNPIPE = pygame.USEREVENT
    pygame.time.set_timer(SPAWNPIPE,1200) # Temps pour faire "SPAWN PIPE"
    pipe_height = [400,300,200] # taille "pipe"

    game_over_surface = pygame.image.load('Ressources/image-etc/message.png').convert_alpha() # Apporte image commencer
    game_over_rect = game_over_surface.get_rect(center = (144, 256)) 

    flap_sound = pygame.mixer.Sound('Ressources/sound/sfx_wing.wav') # Apporte le son de l'aile
    death_sound = pygame.mixer.Sound('Ressources/sound/sfx_hit.wav') # Apporte le son
    score_sound = pygame.mixer.Sound('Ressources/sound/sfx_point.wav') # Apporte le son
    score_sound_countdown = 100 # permet d'avoir le son du score

    while True: #boucle du jeu
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit() # quitte le jeu
                #sys.exit() #quitte python
                
            
            if event.type == pygame.KEYDOWN: # appuie touche "espace" pour faire voler "bird"
                if event.key == pygame.K_SPACE and game_active:
                    bird_movement = 0
                    bird_movement -= 6 # hauteur du saut
                    flap_sound.play() # joue le son des ailes
                if event.key == pygame.K_SPACE and game_active == False:
                    game_active = True
                    pipe_list.clear()
                    bird_rect.center = (50,256)
                    bird_movement = 0
                    score = 0
            
            if event.type == SPAWNPIPE: # fait apparaitre "pipe"
                pipe_list.extend(create_pipe())
            
            if event.type == BIRDFLAP: # loop of the different image interval time
                if bird_index < 2:
                    bird_index += 1
                else:
                    bird_index = 0
                
                bird_surface, bird_rect = bird_animation()

        screen.blit(bg_surface,(0,0)) #affiche l'image "background" sur l'écran
        
        if game_active:
            # Bird
            bird_movement += gravity
            rotated_bird = rotate_bird(bird_surface)
            bird_rect.centery += bird_movement # "bird" tombe
            screen.blit(rotated_bird,bird_rect) # affiche l'image "bird" sur l'écran
            game_active = check_collision(pipe_list)

            # Pipes
            pipe_list = move_pipes(pipe_list)
            draw_pipes(pipe_list)

            # Score
            pipe_score_check()
            score_display('main_game') # affiche "score" pendant le jeu


        else:
            screen.blit(game_over_surface, game_over_rect) # Affiche image "game_over"
            high_score = update_score(score, high_score)
            score_display('game_over') # affiche "score" après "game-over"


        # Floor
        floor_x_pos -= 1 # vitesse "base"
        draw_floor()
        if floor_x_pos <= -320: # position "base"
            floor_x_pos = 0

        pygame.display.update()
        clock.tick(120)


    # source qui a aidé ce projet: https://www.youtube.com/watch?v=UZg49z76cLw&t=4015s&ab_channel=ClearCode

def jeu_hard(bird1, bird2, bird3):
    global score, can_score
    def draw_floor(): # défiler "base"
        screen.blit(floor_surface,(floor_x_pos,450)) #affiche l'image "base" sur l'écran ## mettre 900 pour doubler 
        screen.blit(floor_surface,(floor_x_pos + 288,450))

    def create_pipe(): #créer des "pipe" / top and bot
        random_pipe_pos = random.choice(pipe_height) # choisie la taille "pipe" au hasard
        bottom_pipe = pipe_surface.get_rect(midtop = (350,random_pipe_pos))
        top_pipe = pipe_surface.get_rect(midbottom = (350,random_pipe_pos - 150))
        return bottom_pipe, top_pipe

    def move_pipes(pipes): # fait bouger "pipe"
        for pipe in pipes:
            pipe.centerx -= 3 # vitesse "pipe"
        visible_pipes = [pipe for pipe in pipes if pipe.right > -25] # supprime les "pipe" de la liste : qui ne sont plus sur l'écran 
        return visible_pipes

    def draw_pipes(pipes): # Affiche "pipe"
        for pipe in pipes:
            if pipe.bottom >= 512:
                screen.blit(pipe_surface,pipe)
            else: 
                flip_pipe = pygame.transform.flip(pipe_surface,False,True) # tourne top "pipe"
                screen.blit(flip_pipe, pipe)

    def check_collision(pipes): # vérifier les collisions entre "bird" et "pipe"
        global score, can_score
        
        for pipe in pipes:
            if bird_rect.colliderect(pipe): # si il y a une collision
                death_sound.play() # joue le son "death"
                can_score = True
                return False
        
        if bird_rect.top <= -100 or bird_rect.bottom >= 450: # "bird" dépasse les bords
            death_sound.play() # joue le son "death"
            can_score = True
            return False

        return True

    def rotate_bird(bird): # rotation de "bird"
        new_bird = pygame.transform.rotozoom(bird, -bird_movement * 3, 1)
        return new_bird

    def bird_animation(): # mettre à la meme taille des différentes images dans rect
        new_bird = bird_frames[bird_index]
        new_bird_rect = new_bird.get_rect(center = (50, bird_rect.centery))
        return new_bird,new_bird_rect

    def score_display(game_state): # affiche "score" et "high_score"
        if game_state == 'main_game':
            score_surface = game_font.render(str(int(score)),True, (255,255,255)) # couleur et texte
            score_rect = score_surface.get_rect(center = (144, 50))
            screen.blit(score_surface, score_rect)
        
        if game_state == 'game_over':
            score_surface = game_font.render(f'Score: {int(score)}',True, (255,255,255)) # couleur et texte
            score_rect = score_surface.get_rect(center = (144, 50))
            screen.blit(score_surface, score_rect)

            high_score_surface = game_font.render(f'High Score: {int(high_score)}',True, (255,255,255)) # couleur et texte
            high_score_rect = high_score_surface.get_rect(center = (144, 425))
            screen.blit(high_score_surface, high_score_rect)

    def update_score(score, high_score): # pour que "high_score" fonctionne
        if score > high_score:
            high_score = score
        return high_score
    
    def pipe_score_check(): # permet de vérifier et d'attribuer les points du score
        global score, can_score
        

        if pipe_list:
            for pipe in pipe_list:
                if 45 < pipe.centerx < 55 and can_score:
                    score += 1
                    score_sound.play()
                    can_score = False
                if pipe.centerx < 0: 
                    can_score = True

    def play_the_music(): # prêt à lancer la musique
        mixer.init()
        mixer.music.load("Ressources/sound/Cyberpunk-music.wav") # Apporte le son de l'aile
        mixer.music.play()

    pygame.init() # Created by BHATI Lokendra

    play_the_music() # joue la musique
    
    screen = pygame.display.set_mode((288,512)) # define width and height
    clock = pygame.time.Clock() #set the FPS (Frames Per Second)
    game_font = pygame.font.Font('Ressources/04B_19.TTF',25) # caractéristique du texte pour "score"

    pygame.display.set_caption('DA BIRD') # name of the window
    Icon = pygame.image.load('Ressources/image-etc/Flappy_Bird_icon.png') #import the icon
    pygame.display.set_icon(Icon) # set the icon

    # GAME VARIABLES
    gravity = 0.15
    bird_movement = 0
    game_active = True
    score = 0
    high_score = 0
    can_score = True


    bg_surface = cv2.VideoCapture("Ressources/image-etc/HARD/hard-level.mp4") # Apporte l'arrière-plan statique
    success, bg_surface_image = bg_surface.read()
    run = success


    floor_surface = pygame.image.load('Ressources/image-etc/HARD/base-bleu.png').convert() # Arrière-plan dynamique / "base"
    #floor_surface = pygame.transform.scale2x(floor_surface) doubler la surface "set_mode (576,1024)"
    floor_x_pos = 0

    bird_downflap = pygame.image.load(bird1).convert_alpha() # Apporte l'image "bird"
    bird_midflap = pygame.image.load(bird2).convert_alpha()
    bird_upflap = pygame.image.load(bird3).convert_alpha()
    bird_frames = [bird_downflap,bird_midflap,bird_upflap] # liste des surfaces
    # pygame.transform.scale2x(pygame.image"...") pour agrandir
    bird_index = 0
    bird_surface = bird_frames[bird_index]
    bird_rect = bird_surface.get_rect(center = (50,256)) # creer un rectangle autour de "bird"

    BIRDFLAP = pygame.USEREVENT + 1
    pygame.time.set_timer(BIRDFLAP, 200)

    #bird_surface = pygame.image.load('Ressources/image-etc/SECRET/BIRD/bluebird-midflap.png').convert_alpha() # Apporte l'image "bird"
    #bird_surface = pygame.transform.scale2x(bird_surface) doubler la surface "set_mode (576,1024)"
    #bird_rect = bird_surface.get_rect(center = (50,256)) # creer un rectangle autour de "bird"

    pipe_surface = pygame.image.load('Ressources/image-etc/HARD/pipe-violet.png') # Apporte l'image "pipe"
    #pipe_surface = pygame.transform.scale2x(pipe_surface) doubler la surface "set_mode (576,1024)"
    pipe_list = []
    SPAWNPIPE = pygame.USEREVENT
    pygame.time.set_timer(SPAWNPIPE,1300) # Temps pour faire "SPAWN PIPE"
    pipe_height = [450,400,350,300,250,200] # taille "pipe"

    game_over_surface = pygame.image.load('Ressources/image-etc/message.png').convert_alpha() # Apporte image commencer
    game_over_rect = game_over_surface.get_rect(center = (144, 256)) 

    death_sound = pygame.mixer.Sound('Ressources/sound/sfx_hit.wav') # Apporte le son
    score_sound = pygame.mixer.Sound('Ressources/sound/sfx_point.wav') # Apporte le son

    while True: #boucle du jeu
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit() # quitte le jeu
                #sys.exit() #quitte python
            
            if event.type == pygame.KEYDOWN: # appuie touche "espace" pour faire voler "bird"
                if event.key == pygame.K_SPACE and game_active:
                    bird_movement = 0
                    bird_movement -= 4 # hauteur du saut
                if event.key == pygame.K_SPACE and game_active == False: # Relancer le jeu lors du "game_over"
                    game_active = True
                    pipe_list.clear()
                    bird_rect.center = (50,256)
                    bird_movement = 0
                    score = 0
            
            if event.type == SPAWNPIPE: # fait apparaitre "pipe"
                pipe_list.extend(create_pipe())
            
            if event.type == BIRDFLAP: # loop of the different image interval time
                if bird_index < 2:
                    bird_index += 1
                else:
                    bird_index = 0
                
                bird_surface, bird_rect = bird_animation()

        
        success, bg_surface_image = bg_surface.read() # Affiche l'arrière plan dans le jeu
        if success:
            bg_surface_surf = pygame.image.frombuffer(
                bg_surface_image.tobytes(), bg_surface_image.shape[1::-1], "BGR")
        else:
            run = False
        screen.blit(bg_surface_surf, (0, 0))
        

        if game_active: # joue
            # Bird
            bird_movement += gravity
            rotated_bird = rotate_bird(bird_surface)
            bird_rect.centery += bird_movement # "bird" tombe
            screen.blit(rotated_bird,bird_rect) # affiche l'image "bird" sur l'écran
            game_active = check_collision(pipe_list)

            # Pipes
            pipe_list = move_pipes(pipe_list)
            draw_pipes(pipe_list)

            # Score
            pipe_score_check()
            score_display('main_game') # affiche "score" pendant le jeu


        else: # game_over
            run = False
            screen.blit(game_over_surface, game_over_rect) # Affiche image "game_over"
            high_score = update_score(score, high_score)
            score_display('game_over') # affiche "score" après "game-over"


        # Floor
        floor_x_pos -= 1 # vitesse "base"
        draw_floor()
        if floor_x_pos <= -320: # position "base"
            floor_x_pos = 0

        pygame.display.update() # ne jamais doubler sinon clignotement noir
        clock.tick(150) # vitesse du jeu

def jeu_secret(bird1, bird2, bird3):
    global score, can_score
    def draw_floor(): # défiler "base"
        screen.blit(floor_surface,(floor_x_pos,450)) #affiche l'image "base" sur l'écran ## mettre 900 pour doubler 
        screen.blit(floor_surface,(floor_x_pos + 288,450))

    def create_pipe(): #créer des "pipe" / top and bot
        random_pipe_pos = random.choice(pipe_height) # choisie la taille "pipe" au hasard
        bottom_pipe = pipe_surface.get_rect(midtop = (350,random_pipe_pos))
        top_pipe = pipe_surface.get_rect(midbottom = (350,random_pipe_pos - 180)) #espacement "pipe"
        return bottom_pipe, top_pipe

    def move_pipes(pipes): # fait bouger "pipe"
        for pipe in pipes:
            pipe.centerx -= 3 # vitesse "pipe"
        visible_pipes = [pipe for pipe in pipes if pipe.right > -25] # supprime les "pipe" de la liste : qui ne sont plus sur l'écran 
        return visible_pipes

    def draw_pipes(pipes): # Affiche "pipe"
        for pipe in pipes:
            if pipe.bottom >= 512:
                screen.blit(pipe_surface,pipe)
            else: 
                flip_pipe = pygame.transform.flip(pipe_surface,False,True) # tourne top "pipe"
                screen.blit(flip_pipe, pipe)

    def check_collision(pipes): # vérifier les collisions entre "bird" et "pipe"
        global score, can_score
        
        for pipe in pipes:
            if bird_rect.colliderect(pipe): # si il y a une collision
                death_sound.play() # joue le son "death"
                can_score = True
                return False
        
        if bird_rect.top <= -100 or bird_rect.bottom >= 450: # "bird" dépasse les bords
            death_sound.play() # joue le son "death"
            can_score = True
            return False

        return True

    def rotate_bird(bird): # rotation de "bird"
        new_bird = pygame.transform.rotozoom(bird, -bird_movement * 3, 1)
        return new_bird

    def bird_animation(): # mettre à la meme taille des différentes images dans rect
        new_bird = bird_frames[bird_index]
        new_bird_rect = new_bird.get_rect(center = (50, bird_rect.centery))
        return new_bird,new_bird_rect

    def score_display(game_state): # affiche "score" et "high_score"
        if game_state == 'main_game':
            score_surface = game_font.render(str(int(score)),True, (255,255,255)) # couleur et texte
            score_rect = score_surface.get_rect(center = (144, 50))
            screen.blit(score_surface, score_rect)
        
        if game_state == 'game_over':
            score_surface = game_font.render(f'Score: {int(score)}',True, (255,255,255)) # couleur et texte
            score_rect = score_surface.get_rect(center = (144, 50))
            screen.blit(score_surface, score_rect)

            high_score_surface = game_font.render(f'High Score: {int(high_score)}',True, (255,255,255)) # couleur et texte
            high_score_rect = high_score_surface.get_rect(center = (144, 425))
            screen.blit(high_score_surface, high_score_rect)

    def update_score(score, high_score): # pour que "high_score" fonctionne
        if score > high_score:
            high_score = score
        return high_score
    
    def pipe_score_check(): # permet de vérifier et d'attribuer les points du score
        global score, can_score
        

        if pipe_list:
            for pipe in pipe_list:
                if 45 < pipe.centerx < 55 and can_score:
                    score += 1
                    score_sound.play()
                    can_score = False
                if pipe.centerx < 0: 
                    can_score = True

    def play_the_music(): # prêt à lancer la musique
        mixer.init()
        mixer.music.load("Ressources/sound/sfx_die.wav") # Apporte le son de l'aile
        mixer.music.play()

    pygame.init() # Created by BHATI Lokendra

    play_the_music() # joue la musique
    
    screen = pygame.display.set_mode((288,512)) # define width and height
    clock = pygame.time.Clock() #set the FPS (Frames Per Second)
    game_font = pygame.font.Font('Ressources/04B_19.TTF',25) # caractéristique du texte pour "score"

    pygame.display.set_caption('DA BIRD') # name of the window
    Icon = pygame.image.load('Ressources/image-etc/Flappy_Bird_icon.png') #import the icon
    pygame.display.set_icon(Icon) # set the icon

    # GAME VARIABLES
    gravity = 0.25
    bird_movement = 0
    game_active = True
    score = 0
    high_score = 0
    can_score = True


    bg_surface = cv2.VideoCapture("Ressources/image-etc/SECRET/BIRD/Sound-Flap/Sound-Secret/secret-level.mp4") # Apporte l'arrière-plan statique
    success, bg_surface_image = bg_surface.read()
    run = success


    floor_surface = pygame.image.load('Ressources/image-etc/SECRET/Secret-level/base-brown.png').convert() # Arrière-plan dynamique
    #floor_surface = pygame.transform.scale2x(floor_surface) doubler la surface "set_mode (576,1024)"
    floor_x_pos = 0

    bird_downflap = pygame.image.load(bird1).convert_alpha() # Apporte l'image "bird"
    bird_midflap = pygame.image.load(bird2).convert_alpha()
    bird_upflap = pygame.image.load(bird3).convert_alpha()
    bird_frames = [bird_downflap,bird_midflap,bird_upflap] # liste des surfaces
    # pygame.transform.scale2x(pygame.image"...") pour agrandir
    bird_index = 0
    bird_surface = bird_frames[bird_index]
    bird_rect = bird_surface.get_rect(center = (50,256)) # creer un rectangle autour de "bird"

    BIRDFLAP = pygame.USEREVENT + 1
    pygame.time.set_timer(BIRDFLAP, 200)

    #bird_surface = pygame.image.load('Ressources/image-etc/SECRET/BIRD/bluebird-midflap.png').convert_alpha() # Apporte l'image "bird"
    #bird_surface = pygame.transform.scale2x(bird_surface) doubler la surface "set_mode (576,1024)"
    #bird_rect = bird_surface.get_rect(center = (50,256)) # creer un rectangle autour de "bird"

    pipe_surface = pygame.image.load('Ressources/image-etc/SECRET/Secret-level/pipe-brown.png') # Apporte l'image "pipe"
    #pipe_surface = pygame.transform.scale2x(pipe_surface) doubler la surface "set_mode (576,1024)"
    pipe_list = []
    SPAWNPIPE = pygame.USEREVENT
    pygame.time.set_timer(SPAWNPIPE,3600) # Temps pour faire "SPAWN PIPE"
    pipe_height = [400,300,200] # taille "pipe"

    game_over_surface = pygame.image.load('Ressources/image-etc/message.png').convert_alpha() # Apporte image commencer
    game_over_rect = game_over_surface.get_rect(center = (144, 256)) 

    flap_sound = pygame.mixer.Sound('Ressources/sound/sfx_wing.wav') # Apporte le son de l'aile
    death_sound = pygame.mixer.Sound('Ressources/sound/sfx_hit.wav') # Apporte le son
    score_sound = pygame.mixer.Sound('Ressources/sound/sfx_point.wav') # Apporte le son

    while True: #boucle du jeu
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit() # quitte le jeu
                #sys.exit() #quitte python
            
            if event.type == pygame.KEYDOWN: # appuie touche "espace" pour faire voler "bird"
                if event.key == pygame.K_SPACE and game_active:
                    bird_movement = 0
                    bird_movement -= 6 # hauteur du saut
                    flap_sound.play() # joue le son des ailes
                if event.key == pygame.K_SPACE and game_active == False: # Relancer le jeu lors du "game_over"
                    game_active = True
                    pipe_list.clear()
                    bird_rect.center = (50,256)
                    bird_movement = 0
                    score = 0
            
            if event.type == SPAWNPIPE: # fait apparaitre "pipe"
                pipe_list.extend(create_pipe())
            
            if event.type == BIRDFLAP: # loop of the different image interval time
                if bird_index < 2:
                    bird_index += 1
                else:
                    bird_index = 0
                
                bird_surface, bird_rect = bird_animation()

        
        success, bg_surface_image = bg_surface.read() # Affiche l'arrière plan dans le jeu
        if success:
            bg_surface_surf = pygame.image.frombuffer(
                bg_surface_image.tobytes(), bg_surface_image.shape[1::-1], "BGR")
        else:
            run = False
        screen.blit(bg_surface_surf, (0, 0))
        

        if game_active: # joue
            # Bird
            bird_movement += gravity
            rotated_bird = rotate_bird(bird_surface)
            bird_rect.centery += bird_movement # "bird" tombe
            screen.blit(rotated_bird,bird_rect) # affiche l'image "bird" sur l'écran
            game_active = check_collision(pipe_list)

            # Pipes
            pipe_list = move_pipes(pipe_list)
            draw_pipes(pipe_list)

            # Score
            pipe_score_check()
            score_display('main_game') # affiche "score" pendant le jeu


        else: # game_over
            run = False
            screen.blit(game_over_surface, game_over_rect) # Affiche image "game_over"
            high_score = update_score(score, high_score)
            score_display('game_over') # affiche "score" après "game-over"


        # Floor
        floor_x_pos -= 1 # vitesse "base"
        draw_floor()
        if floor_x_pos <= -320: # position "base"
            floor_x_pos = 0

        pygame.display.update() # ne jamais doubler sinon clignotement noir
        clock.tick(30) # vitesse du jeu


menu()
