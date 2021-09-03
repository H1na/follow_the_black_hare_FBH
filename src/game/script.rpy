
define narrator = Character(None, window_left_padding=0, color="#ffffff")

define black_hare = DynamicCharacter(_("ash_name"), color="#ff00f0") 
define onka = Character(_('Онка'), color="#ff3600") 

define vechna = Character(_('Вечна'), color="#3abf0a")
define digital_vechna = Character(_('Вечна цифровая'), color="#66e56c", )

define maks = Character(_('Макс'), color="#5a9de9", )

define natasha = Character(_('Наташа'), color="#fe84ff", )
define fox = Character(_('Облачный Лис'), color="#1d92be", )
define hight_fox = Character(_('Лис'), color="#ff2929", )
define wild_fox = Character(_('Лис из касты 3'), color="#dcbc27", )

define man = Character(_('Мужской голос'), color="#c8ffc8", )

#characters with no sprites
define robotic_voice = Character(_('Центр Копирования'), color="#5ebdff", )
define voice_from_net = Character(_('Голос из сети'), color="#c8ffc8", )
define help_center = Character(_('Центр Помощи'), color="#5ebdff", )
define camera = Character(_('КАМЕРА'), color="#c8ffc8", )
define voice_cartoon = Character(_('Голос мультяшки'), color="#c8ffc8", )
define mobile_camera = Character(_('Мобильная камера '), color="#c8ffc8", )
define alise = Character(_('Алиса'), color="#c8ffc8", )
define journalist = Character(_('Журналист'), color="#c8ffc8", )

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

    $ash_name = "Аш"
    jump scene_1
