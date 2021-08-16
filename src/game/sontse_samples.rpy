########################
#
#    ПРИМЕР МЕНЮШКИ
#        примерно так они и строются
#        а чтоб вызвать в игре нажмите shift+o
#        и наберите> jump menu_example
#
###########################################################################



label menu_example:

    scene helpcentre
    show screen stats
    show black regular
    black 'Я ошибался и не должен был давать тебе то, что ты просила. Все мои действия во благо, стали злом. Все.'
    call screen text_message("Распознавай эмоции героя, это позволит Ушам Зайца показывать эмоции автоматически. От того,  как часто ты узнаешь эмоцию, зависит изображение на имплантах")

    while True:
        'Страха: [fear], Злости: [angry]'
        menu:                                                           #объявляем меню
            'Выбери эмоцию.'                                            #Вопрос отображаемый вместе с меню (необязательная строчка)

            "злость":                                                   #cледующий пункт (итд)
                $ angry +=10                                             #Действия если выбрать этот пункт
                show black angry_var
                'Аш может злиться'
                hide black
                show vechna smile1
                call reaction_vechna
                'Вечна может реагировать'
                hide vechna

            "грусть":                                                   #cледующий пункт (итд)
                $ sad +=10                                             #Действия если выбрать этот пункт
                show black sad_var

            "удивление":                                                   #cледующий пункт (итд)
                $ surprised +=10                                             #Действия если выбрать этот пункт
                show black surprised_var

            "отвращение":                                                   #cледующий пункт (итд)
                $ disgust +=10                                             #Действия если выбрать этот пункт
                show black disgust_var

            "безумие":                                                   #cледующий пункт (итд)
                $ mad +=10                                             #Действия если выбрать этот пункт
                show black mad_var

            "страх":                                                    #Пункт меню (кнопка)
                $ fear +=10                                             #Действия если выбрать этот пункт
                show black fear_var

                    
            '(cбросить счетчики)':
                $ fear = 0
                $ angry = 0
                show black regular
                
label fear_angry: #example label called on Choose 
    # 'Страха: [fear], Злости: [angry]'

    menu:                                                           #объявляем меню
        'Выбери эмоцию.'                                            #Вопрос отображаемый вместе с меню (необязательная строчка)

        "страх":                                                    #Пункт меню (кнопка)
            $ fear +=20                                             #Действия если выбрать этот пункт
            if fear >=60:                                           #
                show black fear                                     #
            else:                                                   #
                show black regular                                  #конец действий по выбору пункта

        "злость":                                                   #cледующий пункт (итд)
            $ angry +=20
            if angry >=60:
                show black angry1
            else:
                show black annoyed
                
        '(cбросить счетчики)':
            $ fear = 0
            $ angry = 0
            show black regular
    return
            
            


label show_sprites: #тестовая галлерея объявленных спрайтов
    scene black_background
    show black                 #  = 'black_regular'
    pause
    show black angry1          #  = 'black_angry1'
    pause
    show black angry2          #  = 'black_angry2'
    pause
    show black annoyed         #  = 'black_annoyed'
    pause
    show black confused        #  = 'black_confused'
    pause
    show black disgust         #  = 'black_disgust'
    pause
    show black fear            #  = 'black_fear'
    pause
    show black fear1           #   = 'black_fear1'        #
    pause
    show black happy1          #  = 'black_happy'
    pause
    show black happy2          #  = 'black_happy2'
    pause
    show black mad1            #  = 'black_mad1'
    pause
    show black mad2            #  = 'black_mad2'
    pause
    show black mad3            #  = 'black_mad3'
    pause
    show black regular         #  = 'black_regular'
    pause
    show black regular_blood   #  = 'black_regular_blood'
    pause
    show black sad             #  = 'black_sad'
    pause
    show black sad1            #   = 'black_sad1'         # 
    pause
    show black surprised       #  = 'black_surprised'
    pause
    show black surprised1      #   = 'black_surprised1'   # 
    pause
    show black veryangry       #  = 'black_veryangry'    
    pause
    jump show_sprites
    
    


        

