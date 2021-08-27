


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

    def show_learned_message():
        global angry_shown,sad_shown,surprised_shown,disgust_shown,mad_shown,fear_shown
                        
        if all((mood == 'angry',angry>=40,not angry_shown )):
            angry_shown = True
            renpy.show_screen('text_message','Изучена новая эмоция: Злость') 
        if all((mood == 'sad',sad>=40,not sad_shown )):
            sad_shown = True
            renpy.show_screen('text_message','Изучена новая эмоция: Грусть.') 
        if all((mood == 'surprised',surprised>=40,not surprised_shown )):
            surprised_shown = True
            renpy.show_screen('text_message','Изучена новая эмоция: Удивление.') 
        if all((mood == 'disgust',disgust>=40,not disgust_shown )):
            disgust_shown = True
            renpy.show_screen('text_message','Изучена новая эмоция: Отвращение.') 
        if all((mood == 'mad',mad>=40,not mad_shown )):
            mad_shown = True
            renpy.show_screen('text_message','Изучена новая эмоция: Безумие.') 
        if all((mood == 'fear',fear>=40,not fear_shown )):
            fear_shown = True
            renpy.show_screen('text_message','Изучена новая эмоция: Страх.') 
        return


###########################################################################
# Обьявление всех эмоций всех персонажей

image black                   = 'black_regular'
image black angry1            = 'black_angry1'
image black angry2            = 'black_angry2'
image black annoyed           = 'black_annoyed'
image black confused          = 'black_confused'
image black disgust           = 'black_disgust'
image black disgust1          = 'black_disgust1'     
image black fear              = 'black_fear'
image black fear1             = 'black_fear1'        
image black mad1              = 'black_mad1'
image black mad2              = 'black_mad2'
image black mad3              = 'black_mad3'
image black mad4              = 'black_mad4'
image black regular           = 'black_regular'
image black regular_blood     = 'black_regular_blood'
image black regular_fear      = 'black_regular_fear'      
image black regular_confused  = 'black_regular_confused'  
image black regular_angry     = 'black_regular_angry'    
image black regular_happy2    = 'black_regular_happy2'    
image black regular_happy1    = 'black_regular_happy1'    
image black regular_surprised = 'black_regular_surprised'
image black regular_annoyed   = 'black_regular_annoyed'   
image black regular_disgust   = 'black_regular_disgust'   
image black regular_sad       = 'black_regular_sad'       
image black sad               = 'black_sad'
image black sad1              = 'black_sad1'         
image black surprised         = 'black_surprised'
image black surprised1        = 'black_surprised1'
image black regular_mad       = 'black_sad'



image fox       = 'fox_smile'
image fox angry = 'fox_angry'
image fox shock = 'fox_shock'
image fox smile = 'fox_smile'
image fox collar_angry = 'fox_collar_angry'
image fox collar_smile = 'fox_collar_smile'
image fox collar_shock = 'fox_collar_shock'

image high_fox = 'high_fox_angry'
image high_fox smile = 'high_fox_smile'
image high_fox angry = 'high_fox_angry'
image high_fox shock = 'high_fox_shock'

image wild_fox = 'fox_wild_regular'
image wild_fox regular = 'fox_wild_regular'
image wild_fox crazy = 'fox_wild_crazy'


image maks         = 'max_regular'
image maks regular = 'max_regular'
image maks fight   = 'max_fight'
image maks angry   = 'max_angry'


image onka = 'onka_regular'
image onka regular  = 'onka_regular'
image onka confused = 'onka_confused'
image onka thinking = 'onka_thinking'
image onka victory  = 'onka_victory'
image onka angry    = 'onka_angry'
image onka smile    = 'onka_smile'
image onka sneaky   = 'onka_sneaky'
image onka danger   = 'onka_danger'
image onka sad      = 'onka_sad'


image vechna = 'vechna_thinking'
image vechna thinking = 'vechna_thinking'
image vechna angry = 'vechna_angry'
image vechna smile1 = 'vechna_smile1'
image vechna smile2 = 'vechna_smile2'
image vechna sad = 'vechna_sad' 

image digital_vechna = 'digital_vechna_thinking'
image digital_vechna thinking = 'digital_vechna_thinking'
image digital_vechna smile1 = 'digital_vechna_smile1'
image digital_vechna smile2 = 'digital_vechna_smile2'


image natasha = 'natasha_regular'
image natasha smile = 'natasha_smile'
image natasha angry = 'natasha_angry'
image natasha sad = 'natasha_sad'
 
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
                    'angry>  0','black annoyed',
                    'True','black regular_annoyed')

image black sad_var:
    ConditionSwitch('sad>=40','black sad1',
                    'sad>  0','black sad',
                    'True','black regular_sad')

image black surprised_var:
    ConditionSwitch('surprised>=40','black surprised1',
                    'True','black surprised',
                    'True','black regular_surprised')

image black disgust_var:
    ConditionSwitch('disgust>=40','black disgust1',
                    'disgust>  0','black disgust',
                    'True','black regular_disgust')

image black mad_var:
    ConditionSwitch('mad>=40','black mad',
                    'mad>  0','black mad1',
                    'True','black regular_mad1')

image black fear_var:
    ConditionSwitch('fear>=40','black fear1',
                    'fear>  0','black fear',
                    'True','black regular_fear')
                    
image black mood:
    ConditionSwitch(
                    'mood=="angry"','black angry_var',
                    'mood=="sad"','black sad_var',
                    'mood=="surprised"','black surprised_var',
                    'mood=="disgust"','black disgust_var',
                    'mood=="mad"','black mad_var',
                    'mood=="fear"','black fear_var',
                    'True','black regular')
                    
                    
image vechna reaction:
    ConditionSwitch(
    "mood == 'angry'",'vechna thinking',
    "mood == 'sad'"  ,'vechna smile1',
    "mood == 'surprised'",'vechna smile2'
    "mood == 'disgust'",   'vechna angry'
    "mood == 'mad'",    'vechna angry',
    "mood == 'fear'", 'vechna thinking',
    "True",'vechna thinking')

image onka reaction:
    ConditionSwitch(
    "mood == 'angry'",'onka',
    "mood == 'sad'",'onka confused',
    "mood == 'surprised'",'onka victory',
    "mood == 'disgust'",'onka',
    "mood == 'mad'",'onka angry',
    "mood == 'fear'",'onka',
    "True",'onka')

image fox reaction:
    ConditionSwitch(
    "mood == 'angry'",'fox angry',
    "mood == 'sad'",'fox smile',
    "mood == 'surprised'",'fox smile',
    "mood == 'disgust'",'fox shock',
    "mood == 'mad'",'fox shock',
    "mood == 'fear'",'fox shock',
    "True",'fox shock')

image max reaction:
    ConditionSwitch(
    "mood == 'angry'", 'max fight',
    "mood == 'sad'",'max regular',
    "mood == 'surprised'",'max regular',
    "mood == 'disgust'",'max fight',
    "mood == 'mad'",'max fight',
    "mood == 'fear'",'max regular',
    'True','max regular')

image natasha reaction:
    ConditionSwitch(
    "mood == 'angry'",'natasha sad',
    "mood == 'sad'",'natasha smile',
    "mood == 'surprised'",'natasha normal',
    "mood == 'disgust'",'natasha smile',
    "mood == 'mad'",'natasha angry',
    "mood == 'fear'",'natasha smile',
    "True",'natasha smile')



#виджет для отслеживания настроения аша
screen mood_tracker:
    #timer .01 repeat True action SetVariable('mood',get_mood(mood))
    text str(renpy.showing('black angry_var'))
    timer .01 repeat True action Function(show_learned_message)


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
            $ mood = 'angry'
        "Грусть":                                                    
            $ sad +=10                                     
            $ mood = 'sad'
    return

label surprised_disgust:
    menu:                                                           
        'Выбери эмоцию.'                                           
        "Удивление":                                               
            $ surprised +=10    
            $ mood = 'surprised'
        "Отвращение":                                                    
            $ disgust +=10                                     
            $ mood = 'disgust'
    return

label mad_fear:
    menu:                                                           
        'Выбери эмоцию.'                                           
        "Безумие":                                               
            $ mad +=10    
            $ mood = 'mad'
        "Страх":                                                    
            $ fear +=10                                     
            $ mood = 'fear'
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
