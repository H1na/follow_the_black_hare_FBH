
define narrator = Character(None, window_left_padding=0)
define black = Character(_('Аш'), color="#FF0000") 
define onka = Character(_('Онка'), color="#c8ffc8") 
define stub_character = Character(_('Заглушка'), color="#c8ffc8") 

define vechna = Character(_('Вечна'), color="#c8ffc8")
define digital_vechna = Character(_('Вечна цифровая'), color="#c8ffc8", )


define maks = Character(_('Макс'), color="#c8ffc8", )

define natasha = Character(_('НАТАША'), color="#c8ffc8", )
define fox = Character(_('Облачный Лис'), color="#c8ffc8", )
define hight_fox = Character(_('ЛИС'), color="#c8ffc8", )
define wild_fox = Character(_('ЛИС ИЗ КАСТЫ 3'), color="#c8ffc8", )

define man = Character(_('МУЖЧИНА'), color="#c8ffc8", )

#characters with no sprites
define robotic_voice = Character(_('РОБОТИЗИРОВАННЫЙ ГОЛОС ЦК'), color="#c8ffc8", )
define voice_from_net = Character(_('ГОЛОС ИЗ СЕТИ'), color="#c8ffc8", )
define help_center = Character(_('ЦЕНТР ПОМОЩИ'), color="#c8ffc8", )
define camera = Character(_('КАМЕРА'), color="#c8ffc8", )
define voice_cartoon = Character(_('ГОЛОС МУЛЬТЯШКИ'), color="#c8ffc8", )
define mobile_camera = Character(_('МОБИЛЬНАЯ КАМЕРА'), color="#c8ffc8", )
define alise = Character(_('АЛИСА'), color="#c8ffc8", )
define journalist = Character(_('ЖУРНАЛИСТ'), color="#c8ffc8", )

###########################################################################
# Обьявление всех эмоций всех персонажей

#image black                   = 'black_regular'
#имя black ЗАРЕЗЕРВИРОВАНО СИСТЕМОЙ как дефолтный темный экран. XD
image black regular_mad       = 'black_sad'

image fox              = 'fox_smile'
image fox angry        = 'fox_angry'
image fox shock        = 'fox_shock'
image fox smile        = 'fox_smile'
image fox collar_angry = 'fox_collar_angry'
image fox collar_smile = 'fox_collar_smile'
image fox collar_shock = 'fox_collar_shock'

image hight_fox       = 'high_fox_angry'
image hight_fox smile = 'high_fox_smile'
image hight_fox angry = 'high_fox_angry'
image hight_fox shock = 'high_fox_shock'

image wild_fox         = 'fox_wild_regular'
image wild_fox regular = 'fox_wild_regular'
image wild_fox crazy   = 'fox_wild_crazy'


image maks         = 'max_regular'
image maks regular = 'max_regular'
image maks fight   = 'max_fight'
image maks angry   = 'max_angry'


image onka          = 'onka_regular'
image onka regular  = 'onka_regular'
image onka confused = 'onka_confused'
image onka thinking = 'onka_thinking'
image onka victory  = 'onka_victory'
image onka angry    = 'onka_angry'
image onka smile    = 'onka_smile'
image onka sneaky   = 'onka_sneaky'
image onka danger   = 'onka_danger'
image onka sad      = 'onka_sad'


image vechna          = 'vechna_thinking'
image vechna thinking = 'vechna_thinking'
image vechna angry    = 'vechna_angry'
image vechna smile1   = 'vechna_smile1'
image vechna smile2   = 'vechna_smile2'
image vechna sad      = 'vechna_sad' 

image digital_vechna          = 'digital_vechna_thinking'
image digital_vechna thinking = 'digital_vechna_thinking'
image digital_vechna smile1   = 'digital_vechna_smile1'
image digital_vechna smile2   = 'digital_vechna_smile2'


image natasha         = 'natasha_regular'
image natasha regular = 'natasha_regular'
image natasha smile   = 'natasha_smile'
image natasha angry   = 'natasha_angry'
image natasha sad     = 'natasha_sad'

 
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
    ConditionSwitch('angry>=LEARN_CAP','black angry',
                    'angry>  0','black annoyed',
                    'True','black regular_annoyed')

image black sad_var:
    ConditionSwitch('sad>=LEARN_CAP','black sad1',
                    'sad>  0','black sad',
                    'True','black regular_sad')

image black surprised_var:
    ConditionSwitch('surprised>=LEARN_CAP','black surprised1',
                    'True','black surprised',
                    'True','black regular_surprised')

image black disgust_var:
    ConditionSwitch('disgust>=LEARN_CAP','black disgust1',
                    'disgust>  0','black disgust',
                    'True','black regular_disgust')

image black mad_var:
    ConditionSwitch('mad>=LEARN_CAP','black mad',
                    'mad>  0','black mad1',
                    'True','black regular_mad1')

image black fear_var:
    ConditionSwitch('fear>=LEARN_CAP','black fear1',
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

label start:
    $ angry = 0
    $ sad = 0
    
    $ surprised = 0
    $ disgust = 0
    
    $ mad = 0
    $ fear = 0

    $angry_shown = False
    $sad_shown = False
    $surprised_shown = False
    $disgust_shown = False
    $mad_shown = False
    $fear_shown = False

    $text_msg = 'Тестовое послание'

    jump scene_1
