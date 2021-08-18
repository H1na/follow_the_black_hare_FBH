
define narrator = Character(None, window_left_padding=0)
define black = Character(_('Аш'), color="#FF0000") 
define onka = Character(_('Онка'), color="#c8ffc8") 
define stub_character = Character(_('Заглушка'), color="#c8ffc8") 

define vechna = Character(_('Вечна'), color="#c8ffc8")
define digital_vechna = Character(_('Вечна цифровая'), color="#c8ffc8", )

define fox = Character(_('Лис'), color="#c8ffc8", )
define max = Character(_('Макс'), color="#c8ffc8", )

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
