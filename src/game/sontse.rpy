########################
#
#    ПРИМЕР МЕНЮШКИ
#        примерно так они и строются
#        а чтоб вызвать в игре нажмите shift+o
#        и наберите> jump menu_example
#
########################

image black fear = 'black_fear'
image black regular = 'black_regular'
image black angry1 = 'black_angry1'
image black annoyed = 'black_annoyed'

label menu_example:

    scene helpcentre
    show black regular
    black 'Я ошибался и не должен был давать тебе то, что ты просила. Все мои действия во благо, стали злом. Все.'
    while True:
        'Страха: [fear], Злости: [angry]'
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
                
label fear_angry: #example label called on Choose 
    # 'Страха: [fear], Злости: [angry]'
    $ fear = 0
    $ angry = 0
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