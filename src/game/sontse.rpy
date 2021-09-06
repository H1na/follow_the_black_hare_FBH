#init:
#    define config.mouse = { }
#    define config.mouse['default'] = [ ( "gui/mouse.png", 0, 0)]

#Функция отслеживания эмоций Аша
init python:
    # renpy.music.register_channel(music, mixer=music, loop=True)
    renpy.music.register_channel('music1', mixer="music", loop=True)
    renpy.music.register_channel('music2', mixer="music", loop=True)
    
    LEARN_CAP = 30
    DISSOLVE_TIME = .4
    config.keymap['hide_windows'] = [] 
    
    mood = 'regular'
    #вот тут мне и захотелось в рефакторинг, классы и прочие прелести вкусного кода.
    
    def my_scene(*args, **kwargs):
        renpy.transition(fade)
        #renpy.transition(Dissolve(1))
        renpy.scene(*args, **kwargs)
        return
    config.scene = my_scene
    
    def get_mood(mood):
        global angry_shown,sad_shown,surprised_shown,disgust_shown,mad_shown,fear_shown
                        
        if renpy.showing('black_hare angry_var'):
            if angry>=LEARN_CAP:
                
                if not angry_shown:
                    angry_shown = True
                    renpy.show_screen('text_message','Изучена новая эмоция: Злость') 
                
                return 'angry'
            else:
                return 'regular'
        
        if renpy.showing('black_hare sad_var'):
            if sad>=LEARN_CAP:
                return 'sad'
                if not sad_shown:
                    sad_shown = True
                    renpy.show_screen('text_message','Изучена новая эмоция: Грусть.') 
            else:
                return 'regular'
        
        if renpy.showing('black_hare surprised_var'):
            if surprised>=LEARN_CAP:
                if not surprised_shown:
                    surprised_shown = True
                    renpy.show_screen('text_message','Изучена новая эмоция: Удивление.') 
                return 'surprised'
            else:
                return 'regular'
        
        if renpy.showing('black_hare disgust_var'):
            if disgust>=LEARN_CAP:
                if not disgust_shown:
                    disgust_shown = True
                    renpy.show_screen('text_message','Изучена новая эмоция: Отвращение.') 
                return 'disgust'
            else:
                return 'regular'
        
        if renpy.showing('black_hare mad_var'):
            if mad>=LEARN_CAP:
                if not mad_shown:
                    mad_shown = True
                    renpy.show_screen('text_message','Изучена новая эмоция: Безумие.') 
                return 'mad'
            else:
                return 'regular'
        
        if renpy.showing('black_hare fear_var'):
            if fear>=LEARN_CAP:
                if not fear_shown:
                    fear_shown = True
                    renpy.show_screen('text_message','Изучена новая эмоция: Страх.') 
                return 'fear'
            else:
                return 'regular'
        
        return mood
        
    def get_highest_mood():
        global mood, angry, sad, surprised, disgust, mad, fear
        stat_max = max((angry, sad, surprised, disgust, mad, fear))
        if stat_max == 0:
            return 'regular'
        moodlist = []

        if angry == stat_max:
            moodlist.append('angry')
        if sad == stat_max:
            moodlist.append('sad')
        if surprised == stat_max:
            moodlist.append('surprised')
        if disgust == stat_max:
            moodlist.append('disgust')
        if mad == stat_max:
            moodlist.append('mad')
        if fear == stat_max:
            moodlist.append('fear')

        return renpy.random.choice(moodlist)
        

    def show_learned_message():
        global angry_shown,sad_shown,surprised_shown,disgust_shown,mad_shown,fear_shown
                        
        if all((mood == 'angry',angry>=LEARN_CAP,not angry_shown )):
            angry_shown = True
            renpy.call_screen('text_message','Изучена новая эмоция: Злость') 
        if all((mood == 'sad',sad>=LEARN_CAP,not sad_shown )):
            sad_shown = True
            renpy.call_screen('text_message','Изучена новая эмоция: Грусть.') 
        if all((mood == 'surprised',surprised>=LEARN_CAP,not surprised_shown )):
            surprised_shown = True
            renpy.call_screen('text_message','Изучена новая эмоция: Удивление.') 
        if all((mood == 'disgust',disgust>=LEARN_CAP,not disgust_shown )):
            disgust_shown = True
            renpy.call_screen('text_message','Изучена новая эмоция: Отвращение.') 
        if all((mood == 'mad',mad>=LEARN_CAP,not mad_shown )):
            mad_shown = True
            renpy.call_screen('text_message','Изучена новая эмоция: Безумие.') 
        if all((mood == 'fear',fear>=LEARN_CAP,not fear_shown )):
            fear_shown = True
            renpy.call_screen('text_message','Изучена новая эмоция: Страх.') 
        return


###########################################################################
# Обьявление всех эмоций всех персонажей

# image black                   = 'black_regular'

#image black_hare angry1            = 'black_angry1'
#image black_hare angry2            = 'black_angry2'
#image black_hare annoyed           = 'black_annoyed' 
#image black_hare confused          = 'black_confused' 
#image black_hare disgust           = 'black_disgust'
#image black_hare disgust1          = 'black_disgust1' 
#image black_hare fear              = 'black_fear'
#image black_hare fear1             = 'black_fear1'        
#image black_hare mad1              = 'black_mad1'
#image black_hare mad2              = 'black_mad2'
#image black_hare mad3              = 'black_mad3'
#image black_hare mad4              = 'black_mad4'
#image black_hare regular           = 'black_regular'
#image black_hare regular_blood     = 'black_regular_blood'
#image black_hare regular_fear      = 'black_regular_fear'      
#image black_hare regular_confused  = 'black_regular_confused'  
#image black_hare regular_angry     = 'black_regular_angry'    
#image black_hare regular_happy2    = 'black_regular_happy2'    
#image black_hare regular_happy1    = 'black_regular_happy1'    
#image black_hare regular_surprised = 'black_regular_surprised'
#image black_hare regular_annoyed   = 'black_regular_annoyed'   
#image black_hare regular_disgust   = 'black_regular_disgust'   
#image black_hare regular_sad       = 'black_regular_sad'       
#image black_hare sad               = 'black_sad'
#image black_hare sad1              = 'black_sad1'         
#image black_hare surprised         = 'black_surprised'
#image black_hare surprised1        = 'black_surprised1'
#image black_hare regular_mad       = 'black_sad'



#image fox              = 'fox_smile'
#image fox angry        = 'fox_angry'
#image fox shock        = 'fox_shock'
#image fox smile        = 'fox_smile'
#image fox collar_angry = 'fox_collar_angry'
#image fox collar_smile = 'fox_collar_smile'
#image fox collar_shock = 'fox_collar_shock'

#image hight_fox       = 'high_fox_angry'
#image hight_fox smile = 'high_fox_smile'
#image hight_fox angry = 'high_fox_angry'
#image hight_fox shock = 'high_fox_shock'

#image wild_fox         = 'fox_wild_regular'
#image wild_fox regular = 'fox_wild_regular'
#image wild_fox crazy   = 'fox_wild_crazy'


#image maks         = 'max_regular'
#image maks regular = 'max_regular'
#image maks fight   = 'max_fight'
#image maks angry   = 'max_angry'


#image onka          = 'onka_regular'
#image onka regular  = 'onka_regular'
#image onka confused = 'onka_confused'
#image onka thinking = 'onka_thinking'
#image onka victory  = 'onka_victory'
#image onka angry    = 'onka_angry'
#image onka smile    = 'onka_smile'
#image onka sneaky   = 'onka_sneaky'
#image onka danger   = 'onka_danger'
#image onka sad      = 'onka_sad'


#image vechna          = 'vechna_thinking'
#image vechna thinking = 'vechna_thinking'
#image vechna angry    = 'vechna_angry'
#image vechna smile1   = 'vechna_smile1'
#image vechna smile2   = 'vechna_smile2'
#image vechna sad      = 'vechna_sad' 

#image digital_vechna          = 'digital_vechna_thinking'
#image digital_vechna thinking = 'digital_vechna_thinking'
#image digital_vechna smile1   = 'digital_vechna_smile1'
#image digital_vechna smile2   = 'digital_vechna_smile2'


#image natasha         = 'natasha_regular'
#image natasha regular = 'natasha_regular'
#image natasha smile   = 'natasha_smile'
#image natasha angry   = 'natasha_angry'
#image natasha sad     = 'natasha_sad'
 
# c дефолтными анимациями
## c оффсутом
image fox:
    'fox_smile'
    tr_fox_offset
    tr_default
image fox angry:
    'fox_angry'
    tr_fox_offset
    tr_default
image fox shock:
    'fox_shock'
    tr_fox_offset
    tr_default
image fox smile:
    'fox_smile'
    tr_fox_offset
    tr_default
image fox collar_angry:
    'fox_collar_angry'
    tr_fox_offset
    tr_default
image fox collar_smile:
    'fox_collar_smile'
    tr_fox_offset
    tr_default
image fox collar_shock:
    'fox_collar_shock'
    tr_fox_offset
    tr_default

image hight_fox:
    'high_fox_angry'
    tr_fox_offset
    tr_default
image hight_fox smile:
    'high_fox_smile'
    tr_fox_offset
    tr_default
image hight_fox angry:
    'high_fox_angry'
    tr_fox_offset
    tr_default
image hight_fox shock:
    'high_fox_shock'
    tr_fox_offset
    tr_default

image wild_fox:
    'fox_wild_regular'
    tr_fox_offset
    tr_default
image wild_fox regular:
    'fox_wild_regular'
    tr_fox_offset
    tr_default
image wild_fox crazy:
    'fox_wild_crazy'
    tr_fox_offset
    tr_default



image black_hare:
    'black_hare regular'
    tr_default
image black_hare angry1:
    'black_angry1'
    tr_default
image black_hare angry2:
    'black_angry2'
    tr_default
image black_hare annoyed:
    'black_annoyed'
    tr_default
image black_hare confused:
    'black_confused'
    tr_default
image black_hare disgust:
    'black_disgust'
    tr_default
image black_hare disgust1:
    'black_disgust1'
    tr_default
image black_hare fear:
    'black_fear'
    tr_default
image black_hare fear1:
    'black_fear1'
    tr_default
image black_hare mad1:
    'black_mad1'
    tr_default
image black_hare mad2:
    'black_mad2'
    tr_default
image black_hare mad3:
    'black_mad3'
    tr_default
image black_hare mad4:
    'black_mad4'
    tr_default
image black_hare regular:
    'black_regular'
    tr_default
image black_hare regular_blood:
    'black_regular_blood'
    tr_default
image black_hare regular_fear:
    'black_regular_fear'
    tr_default
image black_hare regular_confused:
    'black_regular_confused'
    tr_default
image black_hare regular_angry:
    'black_regular_angry'
    tr_default
image black_hare regular_happy2:
    'black_regular_happy2'
    tr_default
image black_hare regular_happy1:
    'black_regular_happy1'
    tr_default
image black_hare regular_surprised:
    'black_regular_surprised'
    tr_default
image black_hare regular_annoyed:
    'black_regular_annoyed'
    tr_default
image black_hare regular_disgust:
    'black_regular_disgust'
    tr_default
image black_hare regular_sad:
    'black_regular_sad'
    tr_default
image black_hare sad:
    'black_sad'
    tr_default
image black_hare sad1:
    'black_sad1'
    tr_default
image black_hare surprised:
    'black_surprised'
    tr_default
image black_hare surprised1:
    'black_surprised1'
    tr_default
image black_hare regular_mad:
    'black_sad'
    tr_default



image black angry1:
    'black_angry1'
    tr_default
image black angry2:
    'black_angry2'
    tr_default
image black annoyed:
    'black_annoyed'
    tr_default
image black confused:
    'black_confused'
    tr_default
image black disgust:
    'black_disgust'
    tr_default
image black disgust1:
    'black_disgust1'
    tr_default
image black fear:
    'black_fear'
    tr_default
image black fear1:
    'black_fear1'
    tr_default
image black mad1:
    'black_mad1'
    tr_default
image black mad2:
    'black_mad2'
    tr_default
image black mad3:
    'black_mad3'
    tr_default
image black mad4:
    'black_mad4'
    tr_default
image black regular:
    'black_regular'
    tr_default
image black regular_blood:
    'black_regular_blood'
    tr_default
image black regular_fear:
    'black_regular_fear'
    tr_default
image black regular_confused:
    'black_regular_confused'
    tr_default
image black regular_angry:
    'black_regular_angry'
    tr_default
image black regular_happy2:
    'black_regular_happy2'
    tr_default
image black regular_happy1:
    'black_regular_happy1'
    tr_default
image black regular_surprised:
    'black_regular_surprised'
    tr_default
image black regular_annoyed:
    'black_regular_annoyed'
    tr_default
image black regular_disgust:
    'black_regular_disgust'
    tr_default
image black regular_sad:
    'black_regular_sad'
    tr_default
image black sad:
    'black_sad'
    tr_default
image black sad1:
    'black_sad1'
    tr_default
image black surprised:
    'black_surprised'
    tr_default
image black surprised1:
    'black_surprised1'
    tr_default
image black regular_mad:
    'black_sad'
    tr_default





image maks:
    'max_regular'
    tr_default
image maks regular:
    'max_regular'
    tr_default
image maks fight:
    'max_fight'
    tr_default
image maks angry:
    'max_angry'
    tr_default


image onka:
    'onka_regular'
    tr_default
image onka regular:
    'onka_regular'
    tr_default
image onka confused:
    'onka_confused'
    tr_default
image onka thinking:
    'onka_thinking'
    tr_default
image onka victory:
    'onka_victory'
    tr_default
image onka angry:
    'onka_angry'
    tr_default
image onka smile:
    'onka_smile'
    tr_default
image onka sneaky:
    'onka_sneaky'
    tr_default
image onka danger:
    'onka_danger'
    tr_default
image onka sad:
    'onka_sad'
    tr_default


image vechna:
    'vechna_thinking'
    tr_default
image vechna thinking:
    'vechna_thinking'
    tr_default
image vechna angry:
    'vechna_angry'
    tr_default
image vechna smile1:
    'vechna_smile1'
    tr_default
image vechna smile2:
    'vechna_smile2'
    tr_default
image vechna sad:
    'vechna_sad'
    tr_default

image digital_vechna:
    'digital_vechna_thinking'
    tr_default
image digital_vechna thinking:
    'digital_vechna_thinking'
    tr_default
image digital_vechna smile1:
    'digital_vechna_smile1'
    tr_default
image digital_vechna smile2:
    'digital_vechna_smile2'
    tr_default


image natasha:
    'natasha_regular'
    tr_default
image natasha regular:
    'natasha_regular'
    tr_default
image natasha smile:
    'natasha_smile'
    tr_default
image natasha angry:
    'natasha_angry'
    tr_default
image natasha sad:
    'natasha_sad'
    tr_default

 

# дефолтная анимация появления/исчезновения
transform tr_default:
    # alpha .8
    # ease .2 alpha 1.0
    
    on hide:
        alpha 1.0
        ease .2 alpha .0
        
    on show:
        alpha .0
        easeout_quint .3 alpha 1.0
    
        
transform tr_fox_offset:
    yoffset 40
 
# спрайты случайно выбираемые 

image black_hare angry:
    choice:
        'black_hare angry1'
    choice:
        'black_hare angry2'
    tr_default

image black_hare happy:
    choice:
        'black_hare happy1'
    choice:
        'black_hare happy2'
    tr_default
        
image black_hare mad:
    choice:
        'black_hare mad3'
    choice:
        'black_hare mad4'
    tr_default


# спрайты зависимые от статов

image black_hare angry_var:
    ConditionSwitch('angry>=LEARN_CAP','black_hare angry',
                    'angry>  0','black_hare annoyed',
                    'True','black_hare regular_annoyed')
    tr_default
    

image black_hare sad_var:
    ConditionSwitch('sad>=LEARN_CAP','black_hare sad1',
                    'sad>  0','black_hare sad',
                    'True','black_hare regular_sad')
    tr_default

image black_hare surprised_var:
    ConditionSwitch('surprised>=LEARN_CAP','black_hare surprised1',
                    'surprised> 0','black_hare surprised',
                    'True','black_hare regular_surprised')
    tr_default

image black_hare disgust_var:
    ConditionSwitch('disgust>=LEARN_CAP','black_hare disgust1',
                    'disgust>  0','black_hare disgust',
                    'True','black_hare regular_disgust')
    tr_default

image black_hare mad_var:
    ConditionSwitch('mad>=LEARN_CAP','black_hare mad',
                    'mad>  0','black_hare mad1',
                    'True','black_hare regular_sad') # REGULAR MAD ОТСУТСТВУЕТ В КАРТИНКАХ!!!
    tr_default

image black_hare fear_var:
    ConditionSwitch('fear>=LEARN_CAP','black_hare fear1',
                    'fear>  0','black_hare fear',
                    'True','black_hare regular_fear')
    tr_default
                    
image black_hare mood:
    ConditionSwitch(
                    'mood=="angry"',      'black_hare angry_var',
                    'mood=="sad"',        'black_hare sad_var',
                    'mood=="surprised"',  'black_hare surprised_var',
                    'mood=="disgust"',    'black_hare disgust_var',
                    'mood=="mad"',        'black_hare mad_var',
                    'mood=="fear"',       'black_hare fear_var',
                    'True',               'black_hare regular')
    tr_default

image black_hare highest_mood:
    ConditionSwitch(
                    'get_highest_mood()=="angry"',      'black_hare angry_var',
                    'get_highest_mood()=="sad"',        'black_hare sad_var',
                    'get_highest_mood()=="surprised"',  'black_hare surprised_var',
                    'get_highest_mood()=="disgust"',    'black_hare disgust_var',
                    'get_highest_mood()=="mad"',        'black_hare mad_var',
                    'get_highest_mood()=="fear"',       'black_hare fear_var',
                    'True',                             'black_hare regular')
    tr_default

                    
                    
image vechna reaction:
    ConditionSwitch(
    "mood == 'angry'",     'vechna thinking',
    "mood == 'sad'"  ,     'vechna smile1',
    "mood == 'surprised'", 'vechna smile2',
    "mood == 'disgust'",   'vechna angry',
    "mood == 'mad'",       'vechna angry',
    "mood == 'fear'",      'vechna thinking',
    "True",                'vechna thinking')
    tr_default

image onka reaction:
    ConditionSwitch(
    "mood == 'angry'",      'onka',
    "mood == 'sad'",        'onka confused',
    "mood == 'surprised'",  'onka victory',
    "mood == 'disgust'",    'onka',
    "mood == 'mad'",        'onka angry',
    "mood == 'fear'",       'onka',
    "True",'onka')
    tr_default

image fox reaction:
    ConditionSwitch(
    "mood == 'angry'",        'fox angry',
    "mood == 'sad'",         'fox smile',
    "mood == 'surprised'",   'fox smile',
    "mood == 'disgust'",    'fox shock',
    "mood == 'mad'",        'fox shock',
    "mood == 'fear'",       'fox shock',
    "True",                 'fox shock')
    tr_default

image maks reaction:
    ConditionSwitch(
    "mood == 'angry'",      'maks fight',
    "mood == 'sad'",        'maks regular',
    "mood == 'surprised'",  'maks regular',
    "mood == 'disgust'",    'maks fight',
    "mood == 'mad'",        'maks fight',
    "mood == 'fear'",       'maks regular',
    'True',                 'maks regular')
    tr_default

image natasha reaction:
    ConditionSwitch(
    "mood == 'angry'",      'natasha sad',
    "mood == 'sad'",        'natasha smile',
    "mood == 'surprised'",  'natasha regular',
    "mood == 'disgust'",    'natasha smile',
    "mood == 'mad'",        'natasha angry',
    "mood == 'fear'",       'natasha smile',
    "True",                 'natasha smile')
    tr_default



#виджет для отслеживания настроения аша


screen mood_tracker:
    #timer .01 repeat True action SetVariable('mood',get_mood(mood))
    #text str(renpy.showing('black angry_var'))
    timer .1 repeat True action Function(show_learned_message)


# экран со статами Аша
screen stats:
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

image message_box = Frame('gui/textbox.png',left=26,right=26,bottom=26,top=43)

screen text_message(text_msg):
    add '#0006'
    fixed:
        xysize (700,400)
        align (.5,.3)
        add 'message_box'
        vbox:
            align (.5,.5)
            hbox:
                xsize 600
                add Text(text_msg,text_align = .5) xalign .5
            null height 40
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
    $ renpy.block_rollback()            
    $ show_learned_message()
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
    $ renpy.block_rollback()            
    $ show_learned_message()
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
    $ renpy.block_rollback()            
    $ show_learned_message()
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

label reaction_maks:
    if mood == 'angry':
        show maks fight
    elif mood == 'sad':
        show maks regular
    elif mood == 'surprised':
        show maks regular
    elif mood == 'disgust':
        show maks fight
    elif mood == 'mad':
        show maks fight
    elif mood == 'fear':
        show maks regular
    return

label reaction_natasha:
    if mood == 'angry':
        show natasha sad
    elif mood == 'sad':
        show natasha smile
    elif mood == 'surprised':
        show natasha regular
    elif mood == 'disgust':
        show natasha smile
    elif mood == 'mad':
        show natasha angry
    elif mood == 'fear':
        show natasha smile
    return



#вероятно неверно набранные картинки
image helpcentre = 'helpcenter'



# экраны

label splashscreen:
    scene screen_bg
    show stiame:
        truecenter
        alpha .0
        ease 1 alpha 1.0
        1.0
        ease 1 alpha .0
    pause 3
    hide stiame
    show splashscreen_logo:
        alpha .0
        ease 1 alpha 1.0
        2.0
        ease 1 alpha .0
    pause 4
    hide logo_screen
    return 
    
label main_menu:
    call screen main_menu() with dissolve
    return
    
label first_choice:
    "Обучите искусственный интеллект Ушей Зайца распознавать все эмоции."
    "Прогресс распознавания доступен в меню, во вкладке “прогресс эмоций"
    call screen text_message("Обучите искусственный интеллект Ушей Зайца распознавать все эмоции.")
    call screen text_message("Прогресс распознавания доступен в меню, во вкладке “прогресс эмоций")
    return
    
label end_card:
    scene black
    show end_card:
        subpixel True
        alpha .0
        align (.5,.5)
        zoom 1.1
        parallel:
            ease 2.5 alpha 1.0
        parallel:
            ease 20 zoom 1.0
    pause
    show end_card:
        alpha 1.0
        linear 3 alpha .0
    pause 3
    return
