


#Функция отслеживания эмоций Аша
init python:
    mood = 'regular'
    #вот тут мне и захотелось в рефакторинг, классы и прочие прелести вкусного кода.
    
    def get_mood(mood):
        global angry_shown,sad_shown,surprised_shown,disgust_shown,mad_shown,fear_shown
                        
        if renpy.showing('black angry_var'):
            if angry>=40:
                
                if not angry_shown:
                    angry_shown = True
                    renpy.show_screen('text_message','Изучена новая эмоция: Злость') 
                
                return 'angry'
            else:
                return 'regular'
        
        if renpy.showing('black sad_var'):
            if sad>=40:
                return 'sad'
                if not sad_shown:
                    sad_shown = True
                    renpy.show_screen('text_message','Изучена новая эмоция: Грусть.') 
            else:
                return 'regular'
        
        if renpy.showing('black surprised_var'):
            if surprised>=40:
                if not surprised_shown:
                    surprised_shown = True
                    renpy.show_screen('text_message','Изучена новая эмоция: Удивление.') 
                return 'surprised'
            else:
                return 'regular'
        
        if renpy.showing('black disgust_var'):
            if disgust>=40:
                if not disgust_shown:
                    disgust_shown = True
                    renpy.show_screen('text_message','Изучена новая эмоция: Отвращение.') 
                return 'disgust'
            else:
                return 'regular'
        
        if renpy.showing('black mad_var'):
            if mad>=40:
                if not mad_shown:
                    mad_shown = True
                    renpy.show_screen('text_message','Изучена новая эмоция: Безумие.') 
                return 'mad'
            else:
                return 'regular'
        
        if renpy.showing('black fear_var'):
            if fear>=40:
                if not fear_shown:
                    fear_shown = True
                    renpy.show_screen('text_message','Изучена новая эмоция: Страх.') 
                return 'fear'
            else:
                return 'regular'
        
        return mood

###########################################################################
# Обьявление всех эмоций всех персонажей

image black                   = 'black_regular'
image black angry1            = 'black_angry1'
image black angry2            = 'black_angry2'
image black annoyed           = 'black_annoyed'
image black confused          = 'black_confused'
image black disgust           = 'black_disgust'
image black disgust1          = 'black_disgust1'     #
image black fear              = 'black_fear'
image black fear1             = 'black_fear1'        #
image black happy1            = 'black_happy'
image black happy2            = 'black_happy2'
image black mad1              = 'black_mad1'
image black mad2              = 'black_mad2'
image black mad3              = 'black_mad3'
image black regular           = 'black_regular'
image black regular_blood     = 'black_regular_blood'
image black regular_fear      = 'regular_fear'      #
image black regular_confused  = 'regular_confused'  #
image black regular_angry     = 'black_regular_angry'      #
image black regular_happy2    = 'regular_happy2'    #
image black regular_happy1    = 'regular_happy1'    #
image black regular_surprised = 'regular_surprised' #
image black regular_annoyed   = 'black_regular_annoyed'   #
image black regular_disgusd   = 'regular_disgust'   #
image black regular_sad       = 'regular_sad'       #
image black sad               = 'black_sad'
image black sad1              = 'black_sad1'         # 
image black surprised         = 'black_surprised'
image black surprised1        = 'black_surprised1'   # 



image fox       = 'fox_smile'
image fox angry = 'fox_angry'
image fox shock = 'fox_shock'
image fox smile = 'fox_smile'
image fox neon collar = 'fox_neon_collar'


image max         = 'max_regular'
image max regular = 'max_regular'
image max fight   = 'max_fight'


image onka = 'onka'
image onka regular  = 'onka'
image onka confused = 'onka_confused'
image onka thinking = 'onka_thinking'
image onka victory  = 'onka_victory'
image onka angry    = 'onka_angry'
image onka smile    = 'onka_smile'
image onka sneaky   = 'onka_sneaky'


image vechna = 'vechna_thinking'
image vechna thinking = 'vechna_thinking'
image vechna angry = 'vechna_angry'
image vechna smile1 = 'vechna_smile1'
image vechna smile2 = 'vechna_smile2'
image vechna sad = 'vechna_sad'  #

image digital_vechna = 'vechna_thinking'
image digital_vechna thinking = 'vechna_thinking'
image digital_vechna angry = 'vechna_angry'
image digital_vechna smile1 = 'vechna_smile1'
image digital_vechna smile2 = 'vechna_smile2'

# болванчики для отсутствующих спрайтов. Удалить когда нарисуем.

image black_fear1:
    'black_fear'
    matrixcolor InvertMatrix(value=1.0)

image black_sad1:
    'black_sad'
    matrixcolor InvertMatrix(value=1.0)
  
image black_disgust1:
    'black_disgust'
    matrixcolor InvertMatrix(value=1.0)
   
image black_surprised1:
    'black_surprised'
    matrixcolor InvertMatrix(value=1.0)
 

# спрайты случайно выбираемые 

image black angry:
    choice:
        'black angry1'
    choice:
        'black angry2'

image black happy:
    choice:
        'black happy1'
    choice:
        'black happy2'
        
image black mad:
    choice:
        'black mad2'
    choice:
        'black mad3'


# спрайты зависимые от статов

image black angry_var:
    ConditionSwitch('angry>=40','black angry',
                    'True','black annoyed')

image black sad_var:
    ConditionSwitch('sad>=40','black sad1',
                    'True','black sad')

image black surprised_var:
    ConditionSwitch('surprised>=40','black surprised1',
                    'True','black surprised')

image black disgust_var:
    ConditionSwitch('disgust>=40','black disgust1',
                    'True','black disgust')

image black mad_var:
    ConditionSwitch('mad>=40','black mad',
                    'True','black mad1')

image black fear_var:
    ConditionSwitch('fear>=40','black fear1',
                    'True','black fear')


#виджет для отслеживания настроения аша
screen mood_tracker:
    timer .01 repeat True action SetVariable('mood',get_mood(mood))


# экран со статами Аша
screen stats:
    use mood_tracker
    vbox:
        align (.9,.1)
        label mood
        hbox:
            xalign 1.0
            text 'Злость'
            bar value angry range 70 xsize 200
        hbox:
            xalign 1.0
            text 'Грусть'
            bar value sad range 70 xsize 200
        hbox:
            xalign 1.0
            text 'Удивление'
            bar value surprised range 70 xsize 200
        hbox:
            xalign 1.0
            text 'Отвращение'
            bar value disgust range 70 xsize 200
        hbox:
            xalign 1.0
            text 'Безумие'
            bar value mad range 70 xsize 200
        hbox:
            xalign 1.0
            text 'Страх'
            bar value fear range 70 xsize 200



#Окошко для отображения произвольных сообщений
screen text_message(text_msg):
    add '#0006'
    vbox:
        align (.5,.5)
        hbox:
            xsize 600
            add Text(text_msg) xalign .5
        textbutton ('ОКЕЙ') xalign .5 action [Hide('text_message'),Return()]
    
            
#менюшки выбора эмоций по тз
            
label angry_sad:
    menu:                                                           
        'Выбери эмоцию.'                                           
        "Злость":                                               
            $ angry +=10    
        "Грусть":                                                    
            $ sad +=10                                     
    return

label surprised_disgust:
    menu:                                                           
        'Выбери эмоцию.'                                           
        "Удивление":                                               
            $ surprised +=10    
        "Отвращение":                                                    
            $ disgust +=10                                     
    return

label mad_fear:
    menu:                                                           
        'Выбери эмоцию.'                                           
        "Безумие":                                               
            $ mad +=10    
        "Страх":                                                    
            $ fear +=10                                     
    return

#функции для перезаписи эмоций героев реагирующих на острые эмоции Аша

label reaction_vechna:
    if mood == 'angry':
        show vechna thinking
    elif mood == 'sad':
        show vechna smile1
    elif mood == 'surprised':
        show vechna smile2
    elif mood == 'disgust':
        show vechna angry
    elif mood == 'mad':
        show vechna angry
    elif mood == 'fear':
        show vechna thinking
    return

label reaction_onka:
    if mood == 'angry':
        show onka 
    elif mood == 'sad':
        show onka confused
    elif mood == 'surprised':
        show onka victory
    elif mood == 'disgust':
        show onka 
    elif mood == 'mad':
        show onka angry
    elif mood == 'fear':
        show onka 
    return

label reaction_fox:
    if mood == 'angry':
        show fox angry
    elif mood == 'sad':
        show fox smile
    elif mood == 'surprised':
        show fox smile
    elif mood == 'disgust':
        show fox shock
    elif mood == 'mad':
        show fox shock
    elif mood == 'fear':
        show fox shock
    return

label reaction_max:
    if mood == 'angry':
        show max fight
    elif mood == 'sad':
        show max regular
    elif mood == 'surprised':
        show max regular
    elif mood == 'disgust':
        show max fight
    elif mood == 'mad':
        show max fight
    elif mood == 'fear':
        show max regular
    return

label reaction_natasha:
    if mood == 'angry':
        show natasha sad
    elif mood == 'sad':
        show natasha smile
    elif mood == 'surprised':
        show natasha normal
    elif mood == 'disgust':
        show natasha smile
    elif mood == 'mad':
        show natasha angry
    elif mood == 'fear':
        show natasha smile
    return