label scene_1:
    #Здесь мы рассказываем о том, где они живую и что это - опасное место. Где бояться нужно не только природы, но и себя. Аш винит себя, что это он подвел Вечну к копированию. В сцене герой должен быть крут и логичен. Он рассказывает о законе копирования.
    pause 0.2
    scene dark
    play music1 'music/newman_stars.mp3' fadein 3
    #(Появляется фон.)
    #(Начинается музыка.)
    #(На фоне музыки раздается вздох молодого парня.)
    #(Появляется текст.)
    narrator "В начале XXI века самыми большими страхами людей были высота и темнота. "
    narrator "В XXII веке большая часть населения Земли вынуждена десять лет жить на Луне. "
    narrator "Все — ради науки. "
    narrator "А люди больше всего на свете боятся разгерметизации лунных станций. "
    narrator "В ту ночь я спал в кроличьем Куполе, созданном для спасения животных при авариях."
    #(CG — спящий кролик. Раздается звук сирены. )
    #(Сменяется: CG — спящий кролик в красном, аварийном освящении.)
    play sound 'audio/dome_door.mp3'
    narrator "Я услышал, как закрылся люк моего крошечного купола."
    #(Звук закрытия механического люка на фоне сирены и тишина.)
    narrator "Внутрь кто-то проскользнул... Это была моя девятилетняя сестра."
    play sound 'audio/sirena3.mp3'
    narrator "Раздался звук сирены, а поверхность Луны отозвалась вибрацией."
    #(Кролик в аварийном освящении погружается в полную темноту.)
    narrator "Вечна ладонями закрыла мне глаза. Кролики вокруг задрожали."
    #(Эффект вибрации. Музыка развивается, становится активной.)
    #(Звук разрушения, крики, звон стекла.)
    narrator "Я не мог ничего видеть, но... я слышал."
    #(Стук ладоней по Куполу.)
    narrator "Смерть... К нам стучались. К нам ломились! "
    narrator "Вечна могла открыть, верно? Но она не сделала этого."
    pause
    #(Пауза, темный экран и просто музыка 1 секунду.)
    narrator "Это мое самое страшное воспоминание. Но так же и самое любимое."
    narrator "Я понял, что есть та, которая найдет меня, даже когда мир рухнет."
    pause 0.2
    scene blood_room
    narrator "Когда он расщепится на атомы в отголосках памяти."
    show black_hare regular_sad
    black_hare "Ее погубило мое изобретение. "
    black_hare "У любой технологии есть темная сторона."
    black_hare "Желая обучить программный код распознавать эмоции, я создал монстра..."
    black_hare "...Сделал её монстром... А поплатилась за это она..."
    black_hare "Поплатилась три часа назад."
    hide black_hare
    jump scene_2


label scene_2 :
    pause 0.2
    scene station_corridor2
    #В этой сцене мы должны увидеть, как герой стал крутым парнем из сцены 1. Он шел чтоб спасти девушку от закона копирования, но не смог. Виртуальная Вечна удалила реальную. Как? Это останется загадкой, но потом выясниться – что это Онка
    narrator "Тремя часами ранее."
    pause
    narrator "Он несся по коридорам станции, пока не остановился перед Центром Копирования."
    show black_hare regular_confused
    narrator "В голове парня мелькнула мысль: \"Что она там делает?\""
    show black_hare regular_fear
    narrator "Аш чувствовал, что плохой конец ближе, чем он думал."
    narrator "По ту сторону стекла, лежала его сестра."
    show black_hare regular_angry
    play sound 'audio/knocking.mp3'
    narrator "Аш попытался попасть внутрь, но Центр Копирования был занят, а значит, и доступ закрыт."
    show black_hare regular_annoyed
    black_hare "Вечна, все в порядке?"
    hide black_hare
    pause 0.2
    scene helpcenter
    narrator "Девушка рассматривала потолок."
    show vechna smile2
    narrator "Ее тело было намертво зафиксировано на кушетке."
    narrator "Попытки Аша докричаться заглушил голос:"
    robotic_voice "Оцифровка прошла успешно. Поздравляем!"
    show vechna smile1
    narrator "Девушка заметила брата и повернула голову в его сторону."
    show vechna smile1
    vechna "Замечательно! Можете меня расстегнуть? За мной пришли."
    robotic_voice "Мы обязаны вас выключить, по запросу о сохранении индивидуальности."
    show vechna thinking
    narrator "На ее лице на секунду мелькнуло непонимание. "
    narrator "А затем радость сменилась нарастающим чувством тревоги."
    robotic_voice "Причина: копия в сети признана первичной личностью."
    show vechna angry
    hide robotic_voice
    vechna "Эм, как так? Стоп-стоп-стоп! Обычно все наоборот!"
    hide vechna
    show digital_vechna smile1
    play sound 'audio/gologram1.mp3'
    narrator "Перед глазами Вечны развернулась голограмма. "
    narrator "Девушка посмотрела на нее сосредоточенным взглядом."
    narrator "Это были ее собственные глаза, но такие холодные и чужие..."
    hide digital_vechna
    show vechna sad
    narrator "В горле настоящей Вечны стоял ком. "
    narrator "Она абсолютно точно понимала, как поступит девушка с холодными глазами. "
    show vechna thinking
    narrator "Ведь она поступила бы точно так же."
    show vechna angry
    vechna "Не удаляй меня! Слышишь?!"
    vechna "Здесь же Аш, как ты можешь?.."
    narrator "Ее крик взорвал стены Центра Копирования. Но дошли ли ее слова до копии?"
    hide vechna
    show digital_vechna thinking
    hide vechna
    digital_vechna "Его не должно здесь быть. К тому же, на моем месте ты поступила бы также. "
    digital_vechna "Мы обе это понимаем, верно?.. Я не могу делить с кем-то свою индивидуальность."
    digital_vechna "Мы не можем существовать в двух экземплярах."
    hide digital_vechna
    show vechna sad
    narrator "Лежа на кушетке, девушка глубоко дышала, пытаясь собраться с мыслями."
    pause
    narrator "Оригинальная версия проглотила ком, ресницы перестали дрожать. "
    narrator "Она облизнула губы, и ее голос зазвучал спокойно."
    show vechna smile2
    vechna "Я знаю, почему мы поступаем именно так. "
    vechna "И ты, так же как и я, знаешь основное допущение. Которое ломает все аргументы."
    vechna "Зачем тебе индивидуальность? "
    show digital_vechna thinking
    hide vechna
    digital_vechna "Могу ли я допустить, чтобы кто-то еще использовал мой интеллект? Я пока не настолько открыта новому."
    hide digital_vechna
    show vechna sad
    narrator "Эти слова сильно задели девушку на кушетке. "
    narrator "Ирония в том, что это были слова копии в сети, но они удивительно точно передавали ее собственные недавние размышления."
    show vechna thinking
    vechna "Ты и так получаешь мою мечту, дрянь!"
    show vechna angry
    vechna "Я не смогу сама попасть в сеть! Это можешь сделать только ты — моя копия. "
    vechna "Ты! Ты получишь вычислительные мощности!"
    show digital_vechna smile1
    hide vechna
    digital_vechna "Именно поэтому цифровая копия — ведущее сознание. "
    digital_vechna "В цифре я сделаю больше, чем две \"настоящие\" Вечны. "
    digital_vechna "Ты сама знаешь про уговор!"
    show vechna sad
    hide digital_vechna
    vechna "Это ошибка! Такого уговора не было!.."
    narrator "Девушка перешла на шепот, всем лицом выражая мольбу."
    narrator "Пространство вокруг сжалось, и не осталось ничего, кроме слов. Слов входящих и исходящих."
    vechna "Я откажусь от всего. Не убивай меня! "
    show vechna thinking
    vechna "Это я — исходная личность! Почему решаешь ты?"
    show digital_vechna smile1
    hide vechna
    digital_vechna "Мне помогли... И, знаешь... Через год или два ты удалила бы меня!"
    show vechna sad
    hide digital_vechna
    vechna "Но мы так не договаривались! Как же брат?.."
    hide vechna
    show digital_vechna smile1
    narrator "Цифровая Вечна повернулась к стеклу, разделяющему ее и Аша. "
    play sound 'audio/knocking.mp3'
    narrator "Парень ломился в дверь."
    pause
    show digital_vechna smile1
    digital_vechna "У него буду я."
    hide digital_vechna
    show vechna sad
    narrator "Ответ был пронизан холодом. Она могла стерпеть что угодно, но это был удар ножом в спину. "
    show vechna sad
    vechna "Как же я безжалостна к себе!"
    narrator "Она плакала, ее руки тряслись. Отчаянный смех пробивался сквозь слезы обреченности."
    narrator "\"Славно\" вот так лежать, осознавая, что собственными руками изобрел самый оригинальный способ самоубийства."
    hide vechna
    show digital_vechna smile2
    narrator "Безнадежное положение, в котором тебя убивает твоя собственная копия."
    hide digital_vechna
    show vechna thinking
    narrator "Выход есть всегда? "
    narrator "Только не здесь. Все это напоминает Луну, где за пределами купола тебя ждут лишь тьма, холод и смерть."
    show vechna thinking
    vechna "Ты в сговоре с этим богатым ублюдком! "
    show vechna angry
    vechna "Он обманул меня! И тебя ждет такая же участь, не сомневайся!"
    show vechna sad
    narrator "Она взглянула на Аша."
    narrator "Затянувшуюся на несколько секунд тишину разрезал полный бесконечного отчаяния крик девушки:"
    show vechna angry
    vechna "Это все он!!!"
    narrator "Ее заглушил голос станции:"
    robotic_voice "Автоматическая подача газа запущена."
    hide vechna
    show vechna sad
    hide vechna
    pause 0.2
    scene station_corridor2
    narrator "Аш не мог проверить в происходящее."
    show black_hare regular_angry
    hide vechna
    black_hare "Нет! Отключите! Отключите, это ошибка! Живая девушка, — исходная личность! Не наоборот!"
    hide black_hare
    pause 0.2
    scene helpcenter
    narrator "Пальцы ее рук онемели."
    show vechna sad
    narrator "Девушка понимала, что у нее нет шансов выстоять против самой себя. Она умирает. "
    narrator "Слезы теплым ручьем струились из глаз, стекая по вискам."
    narrator "Вскоре фиксирующие браслеты, удерживавшие девушку на кушетке, перестали натягиваться."
    hide vechna
    narrator "Кисти безжизненно повисли, приобретая мертвый синий оттенок."
    pause 0.2
    scene station_corridor2
    narrator "Внутрь помещения вошли чистые до блеска роботы и подняли тело девушки."
    show black_hare regular_angry
    hide vechna
    black_hare "Нет! Пустите меня к ней! Пустите!"
    hide black_hare
    pause 0.2
    scene helpcenter
    narrator "Копия отвечала как ни в чем не бывало."
    show digital_vechna smile1
    hide black_hare
    digital_vechna "Не плачь! Я же здесь!"
    hide digital_vechna
    pause 0.2
    scene station_corridor2
    play sound 'audio/knocking.mp3'
    narrator "Он жалел, что копию нельзя разорвать на части."
    show black_hare regular_angry
    hide digital_vechna
    black_hare "Как ты это сделала? Как ты стала главной?!"
    black_hare "Ты мне не сестра! Ты — чудовище!"
    black_hare "Копии — не люди! Они не принимают решения!"
    hide black_hare
    pause 0.2
    scene helpcenter
    narrator "Цифровая Вечна отказывалась принимать на себя вину."
    play sound 'audio/gologram2.mp3'
    show digital_vechna thinking
    hide black_hare
    digital_vechna "Я покажу тебе, я все объясню..."
    narrator "А затем, внезапно, даже цифровая копия сестры покинула его."
    hide digital_vechna
    jump scene_3


label scene_3:
    pause 0.2
    scene station_corridor2
    narrator "Исчезла, словно не по своей воле."
    narrator "Его разум никак не мог осознать произошедшее. "
    show black_hare regular_sad
    narrator "В голове раз за разом крутилась лишь одна фраза: \"Это все он…\"."
    show black_hare regular_sad
    black_hare "Зачем я дал ей код! Это я во всем виноват!"
    narrator "Как же быстро все произошло… "
    narrator "Аш лишь поднял голову, собираясь уходить, а комната уже была стерильно чиста."
    narrator "Словно ничего и не произошло. "
    narrator "Будто еще несколько минут назад здесь трагически не оборвалась жизнь."
    play sound 'audio/notification1.mp3'
    narrator "Перед ним высветилось сообщение в смешанной реальности: \"Центр Копирования свободен, отправьте запрос...\""
    stop music1 fadeout 3
    hide black_hare
    jump scene_4


label scene_4 :
    pause 0.2
    scene planet
    #Показывая свою планету, она уговаривает его дать доступ к коду Ушей и объясняет для чего ей это. Он соглашается, но просит ее быть на выступлении и уходит
    play music2 'music/newman_classic.mp3' fadein 3
    narrator "3 месяца назад..."
    pause
    show black_hare regular_surprised
    narrator "Аш посмотрел под ноги. Песок. Но не такой, как лунный грунт, и не такой, как любой песок с Земли. "
    show black_hare regular
    narrator "Похож на перемолотые кристаллы красно-рубинового цвета. "
    narrator "Над головой — атмосфера. Она кажется настолько густой и насыщенной парами... "
    narrator "...что розовые скопления облаков, того и гляди, начнут падать под собственной тяжестью."
    show vechna smile1
    hide black_hare
    vechna "Круто, да? "
    vechna "Такие облака образуются только между темной и светлой сторонами планеты. "
    show vechna smile2
    vechna "Там такие перепады температур — сдохнуть можно!"
    hide vechna
    show black_hare regular_surprised
    narrator "Парень посмотрел вверх."
    show black_hare sad_var
    black_hare "Как я скучаю по небу."
    show vechna smile2
    hide black_hare
    vechna "Все, кто под куполом, скучают по небу. "
    vechna "Но есть сеть: тут тебе и земное небо, и небо, спроектированное мной!"
    narrator "Она сделала несколько движений пальцами — и раскрылась модель галактики. "
    narrator "Вечна отмотала изображение куда-то влево, на периферию Млечного Пути."
    vechna "Это невообразимо далеко. Ровер добирался туда восемьдесят лет, Ашик!"
    show black_hare angry_var
    hide vechna
    black_hare "Ты своим \"Ашиком\" весь драматизм ситуации убила."
    show black_hare regular
    narrator "В густых красных облаках засверкали молнии."
    play sound 'audio/grom.mp3'
    narrator "Казалось, небеса захлестнула электронная музыка."
    hide black_hare
    show vechna smile1
    narrator "Вечна в нетерпении захлопала в ладоши и вытянула шею, будто бы желая стать хоть чуточку ближе к облакам."
    show black_hare regular_confused
    hide vechna
    black_hare "Что-то начинается?"
    hide black_hare
    show vechna smile2
    narrator "Видя, что сестра смотрит на небо и не реагирует, парень тоже решил уделить ему все свое внимание."
    narrator "Тучи разразились красными, сверкающими, будто бы кровавыми, слезами-каплями."
    narrator "Крупные кристаллы дождем посыпались на их головы."
    hide vechna
    show black_hare regular_fear
    hide vechna
    black_hare "Ааа!"
    narrator "Аш испугался. Но кристаллы не коснулись его."
    show black_hare regular_surprised
    black_hare "Они проходят насквозь?"
    show vechna sad
    hide black_hare
    vechna "Пока не доделаю, на мир можно только смотреть, но не чувствовать."
    show black_hare regular_confused
    hide vechna
    black_hare "Почему?"
    hide black_hare
    show vechna thinking
    narrator "Вечна сделала недовольное лицо. "
    show vechna sad
    narrator "Присела на корточки и попыталась зачерпнуть розовый кристальный песок."
    show vechna sad
    vechna "Я не успела проработать все подробно. "
    vechna "За обработку данных с исследовательских устройств мне не платят."
    show black_hare regular_happy1
    hide vechna
    black_hare "Не переживай, ты найдешь себе именно такую работу, как хочешь!"
    hide black_hare
    show vechna smile2
    narrator "Девушка встала, и он обнял ее за плечи. Она ответила ему усталой улыбкой. "
    narrator "Словно давно, уже в который раз, пыталась что-то ему объяснить."
    show vechna sad
    vechna "Лучшее, что может быть, — это полное отсутствие причин заниматься чем-то другим, кроме создания далеких миров."
    vechna "А у меня и нет их, этих причин... Но и возможностей заниматься только этим тоже нет."
    hide vechna
    show black_hare sad_var
    narrator "Лицо брата изменилось. "
    narrator "Вечна заметила это."
    show vechna thinking
    hide black_hare
    vechna "Нет смысла грустить."
    show black_hare angry_var
    hide vechna
    black_hare "Ты ругаешь меня за мои чувства?"
    narrator "Его глаза выражали осуждение, Вечна же свои закатила."
    show vechna thinking
    hide black_hare
    vechna "Нет. Но и ты тоже не обижайся на меня за мои чувства."
    vechna "Тем более, что ты можешь мне помочь..."
    show black_hare angry_var
    hide vechna
    black_hare "Ты опять за свое."
    show vechna thinking
    hide black_hare
    vechna "Эээх!"
    show black_hare regular
    hide vechna
    black_hare "Лучше я займусь едой."
    show vechna sad
    hide black_hare
    vechna "Как хочешь. "
    vechna "Что ж, пока я тут, нужно закрыть пару задач по работе."
    hide vechna
    narrator "Аш вышел из сети."
    jump scene_5


label scene_5:
    pause 0.2
    scene home
    narrator "Поднявшись, и немного попрыгав на месте, Вечна потянулась и сделала колесо."
    show vechna thinking
    vechna "Когда находишься в реальности, почти все время приходится упражняться."
    show black_hare sad_var
    hide vechna
    black_hare "Потому что ты любую свободную минуту проводишь в сети."
    hide black_hare
    show vechna thinking
    narrator "Вечна схватила с дивана плюшевую коалу и резко надавила."
    play sound 'audio/chpok.mp3'
    narrator " Голова отделилась от плюшевого тела."
    hide vechna
    show black_hare regular
    hide vechna
    black_hare "Я починю, не переживай."
    show vechna thinking
    hide black_hare
    vechna "Я хочу вечером начать обработку новых данных от ровера. "
    vechna "Мой рейтинг ниже, чем у копий в сети! "
    vechna "Конечно, легко иметь высокие показатели, если можешь работать 24/7. "
    vechna "Меня хватает только на четырнадцать часов в день! "
    show vechna angry
    vechna "Да и то через неделю выдыхаюсь."
    vechna "Еще и все эти уборки, уход за собой, спорт..."
    narrator "Ее передернуло."
    show black_hare angry_var
    hide vechna
    black_hare "Ты давно не занималась уборкой."
    hide black_hare
    show vechna thinking
    narrator "Она всплеснула руками, раздражаясь."
    show vechna thinking
    vechna "XXII век на дворе! А пыль все равно не победили. Под куполом, блин, на Луне!"
    show black_hare angry_var
    hide vechna
    black_hare "Ты отлично знаешь, что это пыль из пещер. Гигантские тоннели все равно будут пылить."
    show vechna thinking
    hide black_hare
    vechna "Жестокая жизнь колонистов."
    narrator "Она вздохнула."
    vechna "Еда готова?"
    show black_hare regular_happy2
    hide vechna
    black_hare "Сегодня праздник. Поэтому есть кое-что особенное."
    show vechna thinking
    hide black_hare
    vechna "Сегодня день траура, милый. "
    vechna "24 августа 2025 года, под куполом было шестьсот пятьдесят человек. "
    vechna "А через пятнадцать минут осталось всего двести."
    show black_hare regular_sad
    hide vechna
    black_hare "Но нам же повезло. Хотя после всего нас могли бы и вернуть на Землю."
    show vechna thinking
    hide black_hare
    vechna "Нам скорее повезло, потому что ты спал с животинками. "
    vechna "Вообще, \"везение\" — веселенькое понятие. "
    vechna "Смотри, нам \"повезло\" выиграть на Земле в лотерею, чтоб свалить в космос, а потом \"повезло\" чуть не умереть в первый месяц! "
    show vechna smile1
    vechna "Получается — везение на невезение."
    hide vechna
    show black_hare regular_happy1
    narrator "Брат взял плюшевую голову коалы и кинул в сестру."
    show vechna smile2
    hide black_hare
    vechna "Ты со своей едой самым подлым образом отвлекаешь меня от работы."
    show vechna smile1
    vechna "А-та-та. Три кота. А голова у них - одна."
    narrator "Она залилась смехом."
    show black_hare regular_happy1
    hide vechna
    black_hare "Очень черный юмор. Тебе же нужно есть, чтобы работать."
    hide black_hare
    play sound 'audio/plates-putting.mp3'
    narrator "Он с чем-то копался на кухне. "
    pause 0.2
    scene home_lights
    narrator "Комнату заполнили светлячки."
    show vechna smile1
    hide black_hare
    vechna "Божечки-кошечки! Если можно получить разрыв сердца из-за красоты, я его получу!"
    vechna "Ты ведь не всех выпустил их фудрариума? "
    narrator "Младший брат был доволен, что угодил сестре."
    show black_hare regular_happy1
    hide vechna
    black_hare "Конечно, я оставил светлячков на салат. Хотя они и симпатичные, но в первую очередь — еда. "
    show black_hare regular
    black_hare "Об этом нужно помнить."
    hide black_hare
    show vechna smile1
    narrator "Вечна хлопала в ладоши, пока брат в полумраке расставлял посуду с едой: салат с бабочками, рагу из сверчков и пирожные."
    show vechna sad
    show vechna sad
    vechna "Ты такой хороший."
    hide vechna
    show black_hare regular_confused
    hide vechna
    black_hare "Ты чего это загрустила?"
    hide black_hare
    show vechna sad
    narrator "Вечна положила пластиковые палочки рядом с тарелкой."
    show vechna sad
    vechna "Мне грустно от твоих слов, что я тут будто бы и не живу..."
    vechna "Я не могу работать меньше... Напротив, стремлюсь делать как можно больше."
    show black_hare regular
    hide vechna
    black_hare "Разве ты не сделала все, что могла? Ты что, хочешь совсем не спать?"
    show vechna sad
    hide black_hare
    vechna "Ну, раньше так и было. А сейчас ты можешь мне помочь."
    show black_hare angry_var
    hide vechna
    black_hare "Опять? Твои идеи это слишком."
    show vechna thinking
    hide black_hare
    vechna "Идея это — фантазия. "
    vechna "А у тебя — есть готовое решение для меня!"
    hide vechna
    show black_hare regular_angry
    narrator "Аш напрягся. Он знал, что сестра может мыслить слишком нестандартно, и при этом не знает границ."
    show vechna smile2
    hide black_hare
    vechna "Ты же написал софт для обучения Ушей, который распознает эмоции и выводит их на импланты. "
    vechna "Если ты можешь научить распознавать эмоции, значит, можно научить распознавать и другие активности мозга."
    vechna "А значит, можно что-то засечь. А то, что можно засечь — можно изменить."
    vechna "Софт Ушей ведь работает на основе чипа, с помощью которого мы выходим в сеть. "
    vechna "Эта железяка может усиливать или ослаблять связи. "
    show vechna smile1
    vechna "Я могу хакнуть себя, понимаешь? Могу стать продуктивнее!"
    pause
    show vechna smile2
    vechna "Дашь доступ к коду?"
    hide vechna
    show black_hare regular
    call angry_sad
    show black_hare mood
    narrator "Аш подавился светлячком и выплюнул его в тарелку. Тот, конечно, постарался улизнуть. "
    play sound 'audio/plate_short.mp3'
    narrator "Вечна с омерзением отодвинула свой салат."
    show vechna thinking
    hide black_hare
    vechna "Ты опять не умертвил их в вакуумном шкафу? Это уже слишком. "
    vechna "Есть живых запрещено везде, кроме парочки отсталых стран."
    hide vechna
    show black_hare regular
    narrator "Парень пристально смотрел в свою тарелку..."
    show black_hare angry_var
    black_hare "Почему-то мне это не нравится."
    show vechna smile2
    hide black_hare
    vechna "Так дашь доступ к BitBacket? Я просто посмотрю код. Что там, да как."
    show black_hare regular
    hide vechna
    black_hare "Уже 10:00. Мне нужно на презентацию."
    show vechna smile2
    hide black_hare
    vechna "Ты ведь видел мой проект! Разве он не потрясный?"
    show vechna smile1
    vechna "По набору нулей и единичек я воссоздаю настолько далекие миры, что мы с тобой умрем, пока долетим туда!"
    show vechna sad
    vechna "Ну, пожалуйста! Ты же мне доверяешь?"
    show black_hare sad_var
    hide vechna
    black_hare "Доверяю... Я поделюсь доступом. "
    black_hare "Но будь на моей презентации."
    show vechna smile1
    hide black_hare
    vechna "Спасибо, спасибо! Ты самый лучший!"
    vechna "Можно доступ прямо сейчас?"
    show black_hare regular
    hide vechna
    black_hare "Только приходи в реальности, не в сети. Мне так спокойней. "
    show black_hare regular_happy1
    black_hare "Я могу получить отличные инвестиции, и сделать Уши массовым продуктом на Луне и Земле."
    show vechna smile1
    hide black_hare
    vechna "Эх... Кому нужны Луна или Земля, когда можно пройтись по мирам, не имеющим названий?"
    show black_hare regular_annoyed
    hide vechna
    black_hare "Мне нужны, и тебе. Хоть ты в этом и не признаешься."
    show black_hare regular
    narrator "Брат положил палочки на тарелку, сжал концы, и те стали разлагаться, сливаясь с остатками еды в общую вязкую массу. Затем встал."
    hide black_hare
    stop music2 fadeout 3
    jump scene_6


label scene_6 :
    pause 0.2
    scene audience
    #Аш рассказывает о благородной цели ушей. Появляется Макс у и них происходит конфликт.
    play music1 'music/newman_v4.mp3' fadein 3
    narrator "Недалеко, в другом конце аудитории, туда-обратно ходил парень. "
    narrator "Его однокурсник. Тот, кто побеждал во всех конкурсах."
    hide black_hare
    show maks regular
    narrator "Выглядел он соответствующе: самоуверенно и нахально."
    narrator "Обычно, людей по одежке только встречают. "
    narrator "Но, как только появляется новая информация, она начинает незамедлительно применяться, меняя впечатление о человеке."
    narrator "Про Макса Аш думал, что это — не тот случай. И именно первое мнение оказалось самым верным. "
    narrator "Блондин репетировал выступление."
    show maks regular
    hide maks
    show black_hare regular_angry
    narrator "Аш пытался его не слушать. Время в ожидании Вечны тянулось бесконечно."
    hide black_hare
    show maks regular
    hide black_hare
    maks "Автоматическая система озеленения: дроны, которые самостоятельно решают..."
    maks "...где и какие растения нужно рассадить, в какое время года это лучше делать. "
    maks "Они смогут сами заказывать необходимые семена из банков..."
    maks "...отслеживать процент успешных всходов и, конечно, возвращаться на станцию для зарядки. "
    maks "Во второй версии предусматривается возможность самодиагностики, чтобы в случае необходимости прибыть на станцию техобслуживания."
    maks "Технология актуальна для Земли..."
    hide maks
    show black_hare regular_angry
    narrator "Вечны все не было. Аш злился. "
    show black_hare angry_var
    black_hare "Таких проектов куча! "
    show maks regular
    hide black_hare
    maks "Значит, есть сформированный рынок и спрос. "
    maks "Прикинь, в бизнесе это \"плюс\", а не \"минус\". "
    narrator "Он рассмеялся."
    maks "Нужно искать занятие на будущее, уже на Земле. "
    hide maks
    show black_hare regular_annoyed
    hide maks
    black_hare "Я думал, ты ошиваешься преимущественно в сети."
    hide black_hare
    show maks angry
    narrator "Максим скривил губы и сделал шаг в сторону темноволосого. "
    narrator "Он размахнулся и бросил рулон армированного скотча \"BRUTAL\" Ашу в голову. "
    hide maks
    show black_hare angry_var
    play sound 'audio/caught.mp3'
    narrator "Тот поймал рулон."
    hide black_hare
    show maks angry
    hide black_hare
    maks "Не смей говорить со мной про сеть. Я ее ненавижу."
    narrator "И никаких сомнений в обратном не было..."
    hide maks
    show black_hare angry_var
    hide maks
    black_hare "Что ты как дикарь какой-то? Я это забираю."
    narrator "Парень убрал моток в карман и развернулся."
    black_hare "Все такие нервные."
    hide black_hare
    show maks regular
    narrator "Максим, проговаривая презентацию, сел в первый ряд и положил ноги на стол."
    hide maks
    stop music1 fadeout 3
    jump scene_7


label scene_7:
    pause 0.2
    scene audience
    #Появляется Онка. 
    play music2 'music/newman_gt.mp3' fadein 3
    narrator "В следующий момент, статной походкой в аудиторию зашел броско одетый мужчина, за которым проскользнул рыжий хвост."
    show onka regular
    narrator "Мужчина сел на скамейку, близко-близко к Максиму, практически столкнув его с занятого места."
    narrator "Для зрителей в сети это место скоро облепят бейджами \"Жюри\" и \"Потрясный Илли Онка\". "
    hide onka
    show fox collar_smile
    narrator "Под ногами у человека в фиолетовом разместился лис с белым воротничком на шее. "
    hide fox
    show maks regular
    narrator "Максима никак не задело это вторжение. Он продолжал насмешливо сверлить Аша глазами."
    hide maks
    show onka regular
    narrator "Онка обратил внимание на светящийся в дополненной реальности бейдж выступающего и обратился к Максиму:"
    show onka smile
    onka "Когда Ваш выход?"
    show maks regular
    hide onka
    maks "После первой звезды."
    show onka confused
    hide maks
    onka "Дерзко! Но тут так скучно, что я прощу."
    show maks regular
    hide onka
    maks "Я Вас тоже, так и быть, прощу."
    narrator "Максим презрительно посмотрел на Онку и пошел в другой угол аудитории."
    show onka thinking
    hide maks
    onka "Воспитание у парня хуже, чем его настроение."
    onka "Вас папа манерам не учил?"
    show maks angry
    hide onka
    maks "У меня теперь нет папы."
    hide maks
    show black_hare regular_confused
    narrator "Аш наблюдал за сценой издалека. Это было интересно."
    hide black_hare
    show onka sneaky
    hide black_hare
    onka "Давай осмотримся, раз уж я вышел с Фабрики."
    hide onka
    show fox collar_smile
    narrator "Лис в голубом неоновом ошейнике держался рядом с хозяином, словно на привязи."
    hide fox
    show onka sneaky
    hide fox
    onka "Вы молодцы, что успели доделать бесконтактный ошейник не за три года, а за три месяца."
    hide onka
    show fox collar_smile
    narrator "Взгляд лиса забегал, он наклонил свою голову и начал вылизывать пятно на груди."
    hide fox
    show onka sneaky
    hide fox
    onka "Как долго будут идти презентации?"
    show fox collar_smile
    hide onka
    fox "Пару часов. Желающих идти к Вам на суд оказалось, как ни странно, много."
    show onka sneaky
    hide fox
    onka "А ты из какой касты?"
    show fox collar_angry
    hide onka
    fox "Из низшей."
    show onka smile
    hide fox
    onka "Что думаешь насчет перехода в высшую касту?"
    hide onka
    show fox collar_shock
    narrator "Лис был возбужден и выбежал перед хозяином вперед, на довольно большое расстояние."
    show fox collar_shock
    fox "Огромное спасибо! Я бы очень хотел, очень! "
    hide fox
    show onka sneaky
    narrator "Рыжий провел глазами от себя до лиса, отмечая расстояние, на которое от него убежало животное."
    narrator "Хозяин засмеялся."
    show onka smile
    onka "Вот это технологии! "
    show onka sneaky
    onka "Ошейник не нужно выключать? Или он удерживает на километры, а не на полтора метра?"
    hide onka
    show fox collar_shock
    narrator "Лис кинулся под ноги Онке."
    show fox collar_shock
    fox "Чую, я буду сегодня на ужин."
    hide fox
    show onka thinking
    hide fox
    onka "Я не..."
    narrator "Онка закатил глаза и терпеливо продолжил."
    show onka smile
    onka "Я не скармливаю вас друг другу. Хватит читать бред в сети. "
    show onka sneaky
    onka "Вы и сами неплохо грызетесь."
    onka "Я схитрил насчет ошейника, знал, что это фикция. Лучше сними его."
    onka "А то потом объясняйся в СМИ, когда это выйдет на рынок."
    show fox shock
    hide onka
    fox "С ошейником так вышло. "
    fox "Высшие лисы сказали, он должен быть, но проект не закончен!"
    hide fox
    show black_hare regular_happy1
    narrator "Ашу показалось это забавным. Было очевидно, \"кто\" и \"что\" перед ним. "
    narrator "Он на миг забыл о сестре, глядя на пушистую морду."
    show black_hare regular_happy1
    black_hare "Добрый день!"
    show onka smile
    hide black_hare
    onka "О! Земное приветствие! Я уже давно путаюсь, когда день, а когда ночь."
    hide onka
    show black_hare regular_happy2
    narrator "Аш с азартом рассматривал Лиса, нагнувшись, чтобы заглянуть ему в мордочку."
    show black_hare regular_happy2
    black_hare "Моя сестра такого хотела. Любит всех пушистых. "
    show black_hare sad_var
    black_hare "Но черт знает, где ее сейчас носит..."
    show fox angry
    hide black_hare
    fox "Некрасиво перебивать! "
    fox "Я, между прочим, объяснялся с хозяином Фабрики Чипов, с Самим..."
    hide fox
    show onka danger
    narrator "Онка отодвинул Лиса от себя, посмотрев на него так, что тот снова поверил, будто Илли действительно скармливает лисам лис…"
    show onka regular
    onka "Прошу прощения. Он взбалмошный... И презентует меня излишне пафосно."
    show black_hare regular_happy2
    hide onka
    black_hare "Мне кажется, в нем все прекрасно."
    show fox smile
    hide black_hare
    fox "Благодарю!"
    hide fox
    show black_hare regular_confused
    hide fox
    black_hare "Но я не видел подобных моделей в продаже. Те не говорят!"
    hide black_hare
    show fox angry
    narrator "Лис вышел вперед."
    show fox angry
    fox "Личность не продается. Стоит рассказать вам поучительную историю..."
    hide fox
    show onka sneaky
    hide fox
    onka "Очень разумных мы не продаем. "
    show onka smile
    onka "А этого забирай бесплатно."
    hide onka
    show fox shock
    hide onka
    fox "!"
    hide fox
    show onka smile
    hide fox
    onka "Фокус группа показала, что люди хотят иметь молчаливых друзей."
    show onka sneaky
    onka "А не как в том древнем меме с собакой, которая делает больно по-другому."
    #(Прозвенел старт.)
    onka "Мне пора в жюри. Судить, разумеется."
    hide onka
    show black_hare regular
    hide onka
    black_hare "А мне, похоже, пора быть судимым."
    black_hare "Приятно было познакомиться."
    narrator "Аш шел ближе к сцене, обдумывая, что хорошие отношения с жюри — это плюс балл к его выступлению."
    show black_hare sad_var
    black_hare "И все-таки, где Вечна?"
    hide black_hare
    show onka sneaky
    narrator "В это время Онка посмотрел вслед Ашу."
    show onka sneaky
    onka "Все-таки странный аксессуар у него на голове. Да? Тем не менее, для продаж в этом только плюсы, ха."
    show fox angry
    hide onka
    fox "Лучше бы лисьи Уши сделал."
    hide fox
    show onka smile
    narrator "Онка засмеялся."
    show fox smile
    hide onka
    fox "Нам пора начинать судить."
    hide fox
    show onka smile
    hide fox
    onka "Мне пора, не нам."
    hide onka
    show fox smile
    narrator "Но лис молча улыбался, идя в ногу рядом с самим Илли Онкой, и витая в своих лисьих рыжих облаках..."
    hide fox
    pause
    narrator "В следующий момент на сцену вышел Макс."
    stop music2 fadeout 3
    jump scene_8


label scene_8:
    pause 0.2
    scene audience
    #Аш рассказывает о своем изобретении. Появляется Максим. Показываем, что вечна не приходит.
    play music1 'music/rt.mp3' fadein 3
    narrator "Несколько часов презентаций тянулись бесконечно."
    show onka sad
    narrator "Онка оживился лишь во время выступления Макса. "
    show onka sneaky
    narrator "Да и то — ради того, чтоб завалить его вопросами. "
    narrator "Пришла очередь Аша. В аудитории погас свет."
    show onka smile
    onka "Веселье выходит в плюс!"
    narrator "Илли подался вперед, уперев локти в стол и столкнув пустой стакан."
    hide onka
    show black_hare regular
    narrator "Свет от камер падал на Аша, находящегося в центре сцены."
    hide black_hare
    show onka sneaky
    hide black_hare
    onka "Смотри, еще один наш знакомый!"
    hide onka
    show fox smile
    narrator "Лис, в качестве ответа хозяину, довольно вывалил язык."
    hide fox
    show black_hare regular
    pause
    call angry_sad
    show black_hare mood
    narrator "Аш пытался найти глазами Вечну, хотя никто этого и не видел. "
    narrator "Аш пытался сосредоточиться: \"Важный момент. Соберись…\""
    show black_hare regular
    black_hare "Спасибо, что дождались последнего выступления."
    hide black_hare
    show maks regular
    narrator "В ответ Максим ухмыльнулся."
    hide maks
    show onka sneaky
    narrator "А Онка мило усмехнулся. "
    hide onka
    show black_hare regular
    hide onka
    black_hare "Всем привет! Меня зовут Аш Хом. Я студент первого курса биопротезирования."
    show black_hare regular_happy1
    black_hare "Сегодня я расскажу об инструменте, который позволяет интерпретировать чужие чувства."
    black_hare "И демонстрировать ваши."
    show black_hare regular
    black_hare "Люди верят, будто эмоции у всех одинаковые. Но так ли это?"
    show black_hare regular_happy1
    black_hare "Пол Экман нашел подтверждение теории, что базовые эмоции универсальны для всех."
    black_hare "Страх, радость, удивление, отвращение, злость и грусть."
    show black_hare regular_happy2
    black_hare "Человеческие общества, не связанные единой культурой и развивающиеся параллельно..."
    black_hare "...будут выражать базовые эмоции одинаково. "
    show black_hare regular
    black_hare "Но есть смешанные эмоции. Их испытывают чаще других, и это вызывает сложности."
    black_hare "Потому что интерпретация смешанных эмоций в разных культурах отличается. "
    black_hare "Мы не всегда даже можем понять, что чувствуем сами. "
    show black_hare regular_confused
    black_hare "А выразить свои чувства для других — вообще отдельная задача."
    show black_hare regular_happy1
    black_hare "Я разрабатываю универсальный язык эмоций. "
    black_hare "Который сможет интуитивно понятным, визуальным языком показать ваши чувства другим."
    black_hare "На данный момент Искусственный Интеллект Ушей учится узнавать и отображать базовые эмоции. "
    black_hare "Но, получая все больше данных, он сможет интерпретировать и интенсивность эмоций, и мета-эмоции."
    show black_hare regular_sad
    black_hare "Например, смесь гнева с отчаянием, или — любви с ненавистью."
    narrator "Он сделал драматическую паузу и встретился с Онкой взглядом."
    hide black_hare
    show onka regular
    narrator "Илли внимательно смотрел и слушал Аша, при этом еле сдерживаясь, чтобы не прокомментировать проект."
    hide onka
    show maks fight
    narrator "Насмешливый взгляд Максима демотивировал, поэтому Аш старался на него не смотреть."
    hide maks
    show black_hare regular_sad
    hide maks
    black_hare "Почему людям так важно понимать друг друга? "
    black_hare "Сложность интерпретации чужих эмоций приводит к конфликтам на Земле."
    show black_hare regular_confused
    black_hare "А ведь люди уже на Луне. "
    show black_hare regular
    black_hare "Что же мы принесем новым мирам, когда займем их? Войны?"
    narrator "Он вышел ближе к зрителям, замолчал, и медленно обвел их взглядом, нагнетая атмосферу."
    narrator "Он знал, в сети их — сотни. И они его слышат. Каждый. "
    show black_hare regular_happy1
    black_hare "Или мы принесем мир? "
    black_hare "Достигнутый за счет универсального визуального языка?"
    narrator "В зале послышался шепот. Это были Илли и Лис."
    hide black_hare
    show onka victory
    hide black_hare
    onka "Как же я люблю, когда говорят про космос!"
    hide onka
    show maks regular
    narrator "Макс строго посмотрел на рыжего."
    hide maks
    show onka sad
    narrator "Онка, словно школьник, виновато замолчал и обратил взгляд на сцену. "
    hide onka
    show black_hare regular
    narrator "Выступающий в это время сделал паузу, которой и воспользовался член жюри."
    hide black_hare
    show onka thinking
    hide black_hare
    onka "Есть вопрос! Общения в реальности действительно мало. "
    onka "Импланты в виде Ушей Зайца ведь предназначены для неё?"
    show black_hare regular
    hide onka
    black_hare "Живое общение — это стресс."
    show black_hare regular_happy1
    black_hare "Есть даже слово, означающее пресыщение людьми — \"аумбук\"."
    show onka thinking
    hide black_hare
    onka "Логично, большую часть истории Homo Sapiens жили в небольших группах, а не в городах-миллионниках."
    show black_hare regular_happy1
    hide onka
    black_hare "Именно поэтому общению тоже нужно учиться. "
    black_hare "Это не врожденный навык."
    show black_hare regular
    black_hare "Но мы не думаем об этом."
    black_hare "Мы не прикладываем усилий для того, чтобы понимать других и себя."
    black_hare "Я вижу, что проблема недопонимания является комплексной. "
    black_hare "Импланты, выражающие эмоции, — это неплохой проект для популяризации данной идеи."
    black_hare "Глядя на человека с имплантами, мы будем помнить, как его нужно понять."
    show black_hare regular_happy2
    black_hare "Его можно понять."
    hide black_hare
    show maks regular
    narrator "Максим поджал губы. На его особенном языке это означало грусть."
    hide maks
    show black_hare regular
    narrator "Аш смотрел на публику, она — на него. "
    narrator "Неловкие секунды отстучали с десяток раз. Все молчали."
    hide black_hare
    show onka victory
    hide black_hare
    onka "Я в восторге!"
    onka "Бредово, но при этом — все так и есть."
    show onka regular
    onka "Довольно интересно узнать, как работает устройство?"
    show black_hare regular_happy2
    hide onka
    black_hare "Конечно, стоит поблагодарить Вас за то, что чип, выпускаемой вашей Фабрикой Чипов, стал открытым."
    show black_hare regular
    black_hare "Запустив на нем свой код ИИ, я смог задать параметры, по которым программа учится различать и отслеживать эмоции в мозгу. "
    black_hare "И когда распознает эмоцию (с разной степенью уверенности), то отображает ее на дисплее."
    black_hare "Чем менее четкое изображение на имплантах, тем меньше ИИ уверен, что верно определил эмоцию."
    hide black_hare
    show onka sneaky
    narrator "Онка хотел задать целый каскад вопросов, но его перебили."
    hide onka
    show maks fight
    hide onka
    maks "Тенденция к увеличению сетевого дня говорит о том, что ты провалишься."
    narrator "Это было сказано хладнокровно и уверенно."
    maks "Кто будет это покупать? Частные инвесторы не станут вкладывать в это деньги."
    show black_hare regular_angry
    hide maks
    black_hare "Возможность распознавать эмоции работает и в сети."
    black_hare "В чем разница, на какое средство вывода информации передавать данные с чипа? "
    black_hare "Что импланты, что аватар в сети. Устройство универсально."
    show black_hare regular
    black_hare "И это не важно. "
    black_hare "Важно то, что с момента появления жилых станций на Луне прошло двести лет."
    black_hare "И мы идем дальше."
    black_hare "Скорее всего, основная коммуникация будет строиться в Вашей, Илли Онка, Чудесной сети."
    black_hare "Мы там работаем, развлекаемся, учимся и получаем новую информацию."
    black_hare "Скоро войну в соседней галактике сможет обеспечить одна строчка кода, выпустившая ракету."
    show black_hare angry_var
    black_hare "Нет разницы, где мы общаемся. Важно, — как мы это делаем."
    narrator "На последних словах он сделал особенно яркий акцент."
    hide black_hare
    show maks angry
    hide black_hare
    maks "В итоге, ты стимулируешь людей к увеличению сетевого дня. "
    maks "Ведь в реале никто не захочет ставить себе импланты."
    hide maks
    voice_from_net "Время на вопросы вышло."
    pause
    narrator "Вскоре, в смешанной реальности, одна за другой гасли отметки об онлайн-зрителях."
    stop music1 fadeout 3
    jump scene_9


label scene_9:
    pause 0.2
    scene home
    #Аш видит, что девушка хакнула мозг без его ведома и злиться.
    play music2 'music/newman_v4.mp3' fadein 3
    narrator "Аш был возмущен итогом презентации."
    #(Девушка сидела за столом, волосы обрезаны, на лице написано блаженство. Она не слушала брата.)
    show black_hare angry_var
    black_hare "Почему всегда побеждает Максим?"
    hide black_hare
    show vechna smile2
    narrator "Сестра слушала брата, улыбаясь."
    hide vechna
    show black_hare angry_var
    hide vechna
    black_hare "Все эти графики, финансовые показатели..."
    show black_hare regular
    black_hare "Хотя кому я вру? С точки зрения бизнеса, идея у меня — так себе."
    show black_hare sad_var
    black_hare "Это все равно что физикам выбивать деньги на фундаментальные исследования..."
    black_hare "...которые, может быть, пригодятся только лет через триста."
    show vechna smile1
    hide black_hare
    vechna "Да, тяжелый вышел день! Но неплохой."
    hide vechna
    show vechna sad
    narrator "Она продолжала улыбаться, но быстро вспомнила про брата и сделала сочувствующее лицо."
    show vechna smile2
    vechna "Но у меня радость! "
    vechna "Всего четыре часа и сотня мелких задач — и я смогла удачно хакнуть мозг!"
    hide vechna
    show black_hare regular_surprised
    call angry_sad
    show black_hare mood
    show black_hare mood
    black_hare "Как? В смысле? Ты изменила свой мозг?"
    narrator "Он произнес это резко, чувствуя приближение проблем."
    hide black_hare
    show vechna thinking
    hide black_hare
    vechna "Как бы я ни любила свою работу — мне тоже лень, и я устаю."
    show vechna smile2
    vechna "Но нашлось изящное решение."
    narrator "Ей не терпелось поделиться своим открытием."
    show vechna thinking
    vechna "Нейрохакинг. Ты забыл? "
    vechna "Я провела первый тест! "
    show vechna smile1
    vechna "Я знаю, ты был против, но все ок! Задача выполнена! Это прорыв!"
    show black_hare sad_var
    hide vechna
    black_hare "Значит, ты этим занималась, пока я так отчаянно тебя ждал?"
    show black_hare regular
    black_hare "Я же ненавижу сцену, ты была мне так нужна!"
    show vechna smile1
    hide black_hare
    vechna "Но..."
    show black_hare angry_var
    hide vechna
    black_hare "И ты обещала посмотреть код, а не экспериментировать над собой!"
    show vechna thinking
    hide black_hare
    vechna "Насчет эксперимента... "
    vechna "Все же хорошо, все прошло успешно!"
    show vechna angry
    vechna "А от слива презентации я бы тебя не спасла."
    show black_hare angry_var
    hide vechna
    black_hare "Значит, это я виноват?"
    show vechna angry
    hide black_hare
    vechna "Не знаю, но я точно не виновата в том, что твоя работа не \"зашла\" на конкурсе. "
    show vechna thinking
    vechna "Там же был супер-пупер Макс."
    show vechna smile2
    vechna "Но только послушай! "
    vechna "Моей целью было выкроить себе еще часика четыре для работы. "
    vechna "Собрала статистику, чтобы посмотреть, на что я трачу время в реальности, и вышло..."
    show vechna thinking
    vechna "...что больше всего времени уходит на сон, а все остальное, по мелочи, занимает час-два."
    show black_hare angry_var
    hide vechna
    black_hare "Я тебе про одно, а ты совсем о другом..."
    show vechna thinking
    hide black_hare
    vechna "Сон я урезать уже не могу, хватило галлюцинаций в прошлом месяце."
    show black_hare angry_var
    hide vechna
    black_hare "Как разумно."
    show vechna smile1
    hide black_hare
    vechna "У меня была идея зафиксировать в мозгу связи, отвечающие за любовь к еде, сериалам и прочей ерунде."
    vechna "Но! Чтобы изменить три параметра в мозгу, нужно их определить."
    show vechna thinking
    vechna "А это в три раза больше времени, чем определять связи для чего-то одного. "
    vechna "Но, главное — когда меняешь много связей в мозгу, то возрастает вероятность ошибок. "
    show vechna smile2
    vechna "Все-таки, я думаю о своем здоровье!"
    show black_hare regular_confused
    hide vechna
    black_hare "Даже не знаю, что тут сказать. Разве что... это странно!"
    show vechna smile1
    hide black_hare
    vechna "И тогда в голову пришла такая крутая мысль! "
    show vechna smile2
    vechna "Не нужно уменьшать любовь к чему-то, когда я могу увеличить любовь к выполнению задач!"
    vechna "В итоге, сейчас я получаю огромное удовольствие, когда закрываю задачу!"
    show black_hare regular_surprised
    hide vechna
    black_hare "Я даже не знаю, поздравлять тебя или ругать. "
    black_hare "Тоесть теперь, кроме работы тебе вообще ничего не интересно?"
    show vechna smile2
    hide black_hare
    vechna "Очень на это надеюсь!"
    show black_hare sad_var
    hide vechna
    black_hare "Я хочу уйти. "
    black_hare "Испытываю очень смешанные чувства, в том числе злость и обиду."
    black_hare "Поэтому я просто пойду пройдусь."
    show vechna smile2
    hide black_hare
    vechna "Окей, а я буду работать!"
    show vechna thinking
    vechna "И, прошу, не трогай мои вещи."
    vechna "Доставка с Земли — это очень дорого!"
    hide vechna
    narrator "Девушка легла на пол и закрыла глаза. "
    narrator "Ее уже не было в этой комнате, она превращала набор 0 и 1, переданные ровером с далекой планеты..."
    narrator "...в симуляцию, позволяющую пройтись каждому по неизведанному миру."
    show black_hare angry_var
    narrator "Аш встал из-за стола. "
    narrator "Взял охапку игрушек Вечны, немного подумал, и вернул на место ее любимую коалу."
    hide black_hare
    narrator "И затем вышел из жилого отсека, располагающегося в лавовом тоннеле, под поверхностью лунного кратера."
    pause 0.2
    scene station_corridor
    narrator "И направился в свое любимое место."
    stop music2 fadeout 3
    jump scene_10


label scene_10 :
    pause 0.2
    scene lake
    #Аш надеется, что присутствие на конкурсе объединит их с сестрой.
    play music1 'music/newman_gt.mp3' fadein 3
    narrator "Рядом с берегом, о который ударялись невысокие волны Лунной реки, состоящей из миллиардов наноботов, Илли Онка думал вслух."
    show onka sad
    onka "Что создал я? Чип? Нет."
    onka "Его создал дед. Сеть? Ее создал отец. "
    show onka angry
    onka "А что сделал я? "
    show onka sad
    onka "Я просто неудачник, который не может заселить космос."
    narrator "Онка поднял голову вверх. Горький ком застрял в горле, когда его взгляд уткнулся в темный потолок."
    onka "Как велик соблазн жалости к себе, и как я хочу дойти до конца."
    onka "Но ничего не получается. Для моих целей не хватает вычислительных мощностей..."
    onka "У меня нет столько ресурсов, чтобы заселять планеты. "
    onka "Ни у кого их нет."
    play sound 'audio/hit.mp3'
    narrator "Он стукнул по металлической поверхности пола и вскрикнул от боли."
    show onka sad
    narrator "В этот момент ему в голову прилетела игрушка. "
    hide onka
    show black_hare angry_var
    narrator "Аш и так бесился, а тут еще этот нытик. И где? В его любимом месте!"
    show black_hare regular_happy1
    black_hare "Не хотел попасть, честно."
    hide black_hare
    show onka angry
    narrator "Онка молча смотрел на парня, держа в руках прилетевшую в голову плюшевую игрушку."
    hide onka
    show black_hare regular
    hide onka
    black_hare "Шутка. Не слишком больно?"
    show onka sneaky
    hide black_hare
    onka "Не больнее, чем критика твоего проекта."
    onka "Это твое место силы? Думаю, стоит ли искать новое?"
    show black_hare regular
    hide onka
    black_hare "Прихожу выбрасывать вещи, когда совсем уж погано."
    show onka sneaky
    hide black_hare
    onka "Древний фен-шуй? Выкинь вещи, и освободи свою жизнь?"
    show black_hare regular_happy1
    hide onka
    black_hare "Это не мои вещи."
    show onka smile
    hide black_hare
    onka "Тогда понимаю."
    show black_hare regular_happy2
    hide onka
    black_hare "У тебя, значит, депрессия? "
    black_hare "Нет идей для изобретений?"
    show onka sad
    hide black_hare
    onka "У меня нет идей? "
    show onka thinking
    onka "У меня может не быть лишь нескольких решений, но со временем и они находятся."
    show black_hare regular_happy1
    hide onka
    black_hare "Если не знаешь, что делать, — найди тех, кто знает. "
    show black_hare regular_happy2
    black_hare "У кого есть хорошие решения."
    narrator "Он как бы невзначай провел рукой по Ушкам. Онка следил за его движениями."
    hide black_hare
    show onka danger
    hide black_hare
    onka "А ты прав! Все это время, решение было на виду."
    narrator "В его взгляде показалось нечто зловещее, но тут же погасло."
    hide onka
    show onka thinking
    onka "Хотя, разве бывает иначе?"
    show onka sneaky
    onka "Ты мне очень пригодился, молодой человек!"
    show black_hare regular_happy2
    hide onka
    black_hare "Я еще не начинал искать инвестиции, но если речь идет о..."
    hide black_hare
    show onka regular
    narrator "Онка приложил палец к губам и обшарил свои карманы."
    hide onka
    show onka thinking
    narrator "Не найдя то, что искал, он принялся прощупывать и карманы Аша."
    hide onka
    show black_hare regular_confused
    narrator "Первая реакция — замереть! "
    narrator "Не потому, что Заяц, а потому, что непонятно: что миллиардер может искать в твоих карманах?"
    hide black_hare
    show onka confused
    hide black_hare
    onka "Пожалуйста, скажи, у тебя есть камера? "
    onka "Это чертова река — единственное место, не утыканное ими. "
    show onka thinking
    onka "Самое обидное, я сам об этом попросил. "
    show onka angry
    onka "Мне необходимо сделать трансляцию!"
    hide onka
    show black_hare regular_confused
    narrator "Аш растерялся, и, находясь в недоумении, отдал ему планшет, который достал из кармана."
    hide black_hare
    show onka confused
    hide black_hare
    onka "Ого! Ты что, воспитывался общественниками в приюте?"
    show black_hare angry_var
    hide onka
    black_hare "Представь себе. "
    black_hare "И не все хотят каждый раз отрубаться на полу, чтобы войти в сеть."
    hide black_hare
    show onka thinking
    narrator "Онка молча на него посмотрел. Было непонятно, что ему еще нужно."
    hide onka
    show black_hare angry_var
    hide onka
    black_hare "Бери раз спрашивал!"
    show onka thinking
    hide black_hare
    onka "Нет."
    show black_hare angry_var
    hide onka
    black_hare "Что значит — нет?"
    show onka thinking
    hide black_hare
    onka "Ты снимай! Я зашел в свой мунтер."
    onka "Социальные сети — лучший выход, когда что-то нужно."
    show black_hare angry_var
    hide onka
    black_hare "Ты взломал мой акк?"
    show onka smile
    hide black_hare
    onka "Это лисы."
    onka "Твой пароль — четыре одинаковые цифры, два слова и символ."
    show onka sneaky
    onka "Слишком простой, я бы даже постеснялся предъявлять претензии."
    show black_hare angry_var
    hide onka
    black_hare "Значит, желтая пресса про тебя не врет?"
    show onka sneaky
    hide black_hare
    onka "Конечно, врет! Транслируй!"
    hide onka
    show onka victory
    narrator "Илли сел на периллы и вскинул руки к потолку лавового тоннеля."
    hide onka
    show onka smile
    onka "Фабрика Чипов создана ради воплощения и внедрения в нашу жизнь великих инновационных идей."
    onka "И сегодня я ищу проекты, которые должны увидеть свет. "
    show onka victory
    onka "Объявляю хакатон!"
    show onka smile
    onka "Обязательное условие — использование в проекте чипа с Фабрики Чипов как ключевого составляющего элемента."
    show black_hare regular_confused
    hide onka
    black_hare "А мне подходит!"
    show onka smile
    hide black_hare
    onka "Не упустите свой шанс! Подробности — сами знаете где."
    narrator "Онка пару секунд натужно улыбался, пока темноволосый догадался выключить камеру."
    hide onka
    show black_hare regular_surprised
    hide onka
    black_hare "Конкурс?"
    show onka smile
    hide black_hare
    onka "Да, там я и найду хорошие проекты."
    show black_hare regular_confused
    hide onka
    black_hare "Я могу на него пройти?"
    show onka smile
    hide black_hare
    onka "Конечно, ты же навел меня на мысль."
    onka "Но попасть туда можно только через тест. "
    show onka sneaky
    onka "Очень сложный!"
    show black_hare angry_var
    hide onka
    black_hare "Если бы я не открыл рот, тест, похоже, был бы проще?"
    show onka sneaky
    hide black_hare
    onka "Кто же знает?"
    narrator "Владелец фабрики бросил это, практически скрывшись за поворотом к выходу."
    hide onka
    show black_hare angry_var
    hide onka
    black_hare "Ты!"
    narrator "Оставшись один, он с досадой бросил вещи Вечны в самую красивую реку по переработке мусора."
    hide black_hare
    show black_hare sad_var
    black_hare "Как глупо думать, что он в меня инвестирует."
    black_hare "Хотя, ради конкурса, Вечна может вылезти из сети."
    play sound 'audio/notification1.mp3'
    narrator "Он вызвал девушку с планшета. "
    narrator "Перед ним высветилось сообщение: \"Готовлюсь к экзамену на Конкурс Фабрики\", и куча эмодзи: шок, истерика, счастье."
    black_hare "Ну естественно, это ведь не к брату прийти."
    hide black_hare
    narrator "Грустно вздохнув, парень зашел в мунтер Илли Онки."
    jump scene_11


label scene_11 :
    pause 0.2
    scene audience
    #Аш и Вечна знакомятся с Лисом. Аш помогает Лису. Вечна завидует высокому баллу брата. Тот говорит что отдал бы ей жетон, но это бесполезно. Там они снова встречают Макса. Тот негативно настроен на лиса (из-за отца винит фабрику) Аш спрашивает для чего тот туда пошел, но Макс не говорит... это Макс устроил пожар в лаборатории
    narrator "Большая часть подростков сидели по домам. В аудитории с Ашем находилось лишь несколько человек."
    narrator "Блондинка и рыжая девушка сидели с двух сторон от него, с интересом поглядывая на его импланты. "
    narrator "Все чувствовали дискомфорт — редко на Луне встретишь больше пары человек в одном месте."
    show maks regular
    narrator "В конце аудитории Аш разглядел знакомый костюм и крашеные волосы Макса."
    hide maks
    show black_hare regular
    call angry_sad
    show black_hare mood
    show black_hare mood
    black_hare "Ну конечно, куда же без тебя!"
    narrator "Он нащупал в кармане моток армированной изоленты BRUTAL, которую в него бросил Максим в этой же аудитории..."
    narrator " ...и еле сдержался, чтобы не \"вернуть\" ее назад, в голову Максима."
    narrator "Аш закатал рукава мантии, и щелкнул сигнал сети. "
    narrator "В смешанной реальности заговорил голос, подаваемый чипом прямо в мозг. "
    hide black_hare
    pause 0.2
    scene black_background
    narrator "Перед глазами появился владелец Фабрики."
    show onka smile
    hide black_hare
    onka "Фабрика чипов приветствует юных изобретателей! "
    show onka victory
    onka "Сегодня мы объявляем итоги отбора!"
    onka "Решим же, кто достоин вступить на территорию инноваций и успеха! "
    show onka smile
    onka "Территорию, где изобретатель сможет потягаться за приз — ресурсы для развития своего изобретения!"
    narrator "Знакомый голос затих. "
    onka "Сейчас вы получите жетоны, решающие судьбу. "
    show onka sneaky
    onka "Синий жетон. Через годы напомнит вам о неудаче. "
    show onka smile
    onka "Зеленый напомнит о шансе, а возможно... о победе! Фабрика желает вам удачи!"
    hide onka
    pause 0.2
    scene audience
    narrator "Владелец Фабрики так и не сказал, что же им делать. Все сидели в ожидании."
    narrator "В аудиторию забежали лисы с жетонами в зубах. Большинство бежало на четырех лапах."
    show fox angry
    narrator "К Ашу же, торжественной походкой, крепко стоя на задних лапах, подошел лис без жетона."
    narrator "Парень внимательно осмотрел зверя. Они друг друга узнали."
    hide fox
    show black_hare regular_happy2
    hide fox
    black_hare "Приятно снова увидеться."
    narrator "Он улыбнулся серьезному зверю. Тот продолжал молчать."
    hide black_hare
    show fox angry
    hide fox
    show black_hare regular_confused
    hide fox
    black_hare "Мне нужно что-то сделать, чтобы получить результат?"
    narrator "Парень осмотрелся по сторонам, глядя, что делают остальные."
    narrator "С одной стороны рыжая девочка держала в руках синий жетон и плакала."
    narrator "С другой стороны блондинка повесила на шею зеленый, но тоже заливалась слезами."
    narrator "Аш вопросительно посмотрел на своего лиса. "
    hide black_hare
    show fox angry
    narrator "Тот отвел морду."
    hide fox
    show black_hare regular_happy1
    hide fox
    black_hare "Если я попаду на конкурс с сестрой, у нас будут отличные каникулы. "
    black_hare "Не лишайте меня их."
    hide black_hare
    show fox angry
    narrator "Лис сердито молчал."
    hide fox
    show maks regular
    narrator "Мимо прошел Максим, размахивая зеленым жетоном."
    hide maks
    show black_hare angry_var
    narrator "Темноволосый повернулся к рыжему зверю."
    show black_hare angry_var
    black_hare "Я ведь все равно узнаю результат."
    hide black_hare
    show fox angry
    narrator "Животное смягчило выражение мордочки."
    hide fox
    show fox smile
    fox "По ужасному стечению обстоятельств, ваш жетон недоступен."
    show black_hare regular_surprised
    hide fox
    black_hare "?"
    show fox smile
    hide black_hare
    fox "Он оказался в моем желудке."
    hide fox
    show black_hare angry_var
    narrator "В ответ парень лишь молча помахал руками в воздухе..."
    narrator "...будто с его языка хотело сорваться возмущенное: \"Что ты несешь? Как такое возможно?\""
    narrator "Но, видя грустное лицо лиса, который даже опустился на четыре лапы, Аш не стал его ругать."
    hide black_hare
    show black_hare regular
    black_hare "Хорошо, какие у нас варианты?"
    hide black_hare
    show fox smile
    narrator "Зверь повеселел."
    show fox smile
    fox "Начало конкурса завтра, до этого времени все само собой решится."
    show black_hare regular
    hide fox
    black_hare "Удобно всем, кроме меня."
    show black_hare regular_annoyed
    black_hare "Я не могу ждать, пока ты сделаешь свои непотребства в аудитории университета. "
    show black_hare regular_confused
    black_hare "Попрошу заменить жетон. Так ведь можно?"
    narrator "Лис вжался в пол."
    show fox shock
    hide black_hare
    fox "Так будет проще для Вас, справедливо."
    show black_hare regular_confused
    hide fox
    black_hare "Но?"
    black_hare "Почему ты сразу не предложил этот вариант?"
    hide black_hare
    show fox shock
    narrator "Лис дернулся от \"ТЫ\", но его внимание переключилось на вопрос студента."
    show fox angry
    fox "Хозяин спишет меня как брак. "
    fox "У нас говорят: \"Ты не создан совершать ошибки\"."
    show black_hare angry_var
    hide fox
    black_hare "Это очень, очень жестоко. "
    show black_hare regular_fear
    black_hare "Надеюсь, конкурсантам ничего не угрожает?"
    narrator "Лис посмотрел в пол. В помещении оставались лишь они вдвоем, остальные уже разошлись."
    show fox angry
    hide black_hare
    fox "Только удача."
    show black_hare regular_fear
    hide fox
    black_hare "Ладно, ждать так ждать. Но мне нужно найти кое-кого."
    show black_hare regular_surprised
    black_hare "Она ведь только что была тут?"
    narrator "Он развернулся, чуть не столкнувшись лицом с сестрой. "
    narrator "На ее лице была широченная улыбка, совсем как у Чеширского кота."
    show vechna smile2
    hide black_hare
    vechna "Я прошла! Целых сто восемьдесят шесть баллов! "
    vechna "У остальных, кто прошел меньше!"
    vechna "Я спросила почти у всех! Я выиграю и буду работать на фабрике!"
    show black_hare regular_happy1
    hide vechna
    black_hare "Поздравляю тебя! Повидалась с друзьями?"
    show vechna thinking
    hide black_hare
    vechna "Да, все такие же скучные, как и год назад."
    show black_hare regular_happy1
    hide vechna
    black_hare "Наверно, тебе нужны новые друзья."
    show vechna thinking
    hide black_hare
    vechna "Сколько ты набрал?"
    show black_hare regular_happy1
    hide vechna
    black_hare "У меня проблемы с лисьим пищеварением — жетон пока недоступен."
    show fox angry
    hide black_hare
    fox "Это неловкий инцидент! Не нужно всем рассказывать."
    show vechna smile1
    hide fox
    vechna "Оооо, ты говоришь!!! А погавкаешь, погавкаешь?"
    show fox angry
    hide vechna
    fox "Попрошу побольше уважения!"
    show black_hare regular_annoyed
    hide fox
    black_hare "Пришла бы на мое выступление, он бы там и погавкал."
    hide black_hare
    show vechna smile2
    narrator "По глазам Вечны стало видно, что она ничего не понимает."
    show black_hare regular_annoyed
    hide vechna
    black_hare "Мы познакомились там, куда тебе было сложно прийти."
    show vechna smile2
    hide black_hare
    vechna "Лис, что ты любишь? Расскажи мне о себе!"
    hide vechna
    show fox angry
    hide vechna
    fox "РасскажиТЕ!"
    show vechna smile2
    hide fox
    vechna "Ой, прошу прощения. Где мои манеры."
    hide vechna
    show fox smile
    narrator "Лис смущенно махнул лапкой. "
    hide fox
    show vechna smile2
    narrator "А Вечна бросила взгляд в сторону брата..."
    show vechna smile1
    narrator "...и незаметно для лиса покрутила пальцем у виска, корча смешное лицо."
    hide vechna
    show black_hare regular_happy1
    hide black_hare
    show fox smile
    hide black_hare
    fox "Что же я люблю?"
    narrator "Он расплылся в улыбке."
    fox "Например, я люблю коал. Они..."
    show black_hare regular_happy1
    hide fox
    black_hare "Они вымерли."
    hide black_hare
    show vechna smile1
    narrator "Вечна протянула руки в сторону лиса, намереваясь обнять и потискать."
    show vechna smile1
    vechna "О! Это мои любимые животные. Я обязана обнять тебя!"
    vechna "Ой! Обнять Вас!"
    hide vechna
    show fox angry
    narrator "Лис ловко перекатился от Вечны где-то на метр."
    hide fox
    show black_hare regular_happy1
    narrator "Аш закатил глаза, но тут ему пришла в голову одна мысль."
    show black_hare regular_disgust
    black_hare "Коалы! Это же врожденно гадкие животные."
    show fox angry
    hide black_hare
    fox "Несправедливо!"
    narrator "Лис манерно махнул хвостом."
    show black_hare regular_happy1
    hide fox
    black_hare "Тогда давайте, достопочтенный господин, посмотрим зарисовки из жизни этих благородных животных."
    narrator "Парень передразнивал манеру речи лиса."
    narrator "Он снова достал свой старенький планшет, весь усыпанный затершимися от времени наклейками."
    black_hare "В первую очередь, хочу посмотреть, как они заботились о потомстве."
    black_hare "Видите ли, чтобы передать детенышам полезные бактерии, им приходилось..."
    hide black_hare
    show fox smile
    hide black_hare
    fox "Кормить их молоком?"
    show black_hare regular_disgust
    hide fox
    black_hare "Не совсем. Они кормили их гов.., прошу прощения, – продуктами жизнедеятельности."
    narrator "Аш показал видеозапись лису."
    show vechna thinking
    hide black_hare
    vechna "Мерзость, вот так, сразу в рот своему ребенку..."
    hide vechna
    show fox shock
    narrator "Лис был в шоке, а затем его ожидаемо стошнило."
    pause
    show black_hare regular_happy2
    hide fox
    black_hare "И ждать не пришлось! На Земле я бы взял палочку, но на Луне её нет."
    show fox angry
    hide black_hare
    fox "Может вашим Ухом подцепить жетон?"
    show black_hare regular_happy2
    hide fox
    black_hare "Очень остроумно. "
    show black_hare regular_disgust
    black_hare "Но доставать, многоуважаемый сударь, придется Вам."
    hide black_hare
    show fox angry
    narrator "Лис брезгливо поднял жетон. Достал из-за воротничка салфетку."
    hide fox
    show black_hare regular_disgust
    narrator "Аш немного отодвинулся, желая держаться подальше от предмета."
    show black_hare regular_confused
    black_hare "Он ведь должен быть синий или зеленый?"
    show fox angry
    hide black_hare
    fox "Красный — значит самые высокие баллы за входной тест."
    show black_hare regular_surprised
    hide fox
    black_hare "И что это значит?"
    show vechna sad
    hide black_hare
    vechna "Значит, что у тебя баллов больше, чем у меня."
    narrator "Расстроилась Вечна."
    show black_hare regular_happy2
    hide vechna
    black_hare "Завтра утром мы будем на Фабрике, там ты сможешь отыграться."
    show fox smile
    hide black_hare
    fox "Благодарю, что решили вопрос без привлечения администрации."
    show black_hare regular_happy2
    hide fox
    black_hare "Я бы не смог спать, зная, что тебя списали."
    show vechna thinking
    hide black_hare
    vechna "Его — что?"
    show black_hare regular_happy2
    hide vechna
    black_hare "Потом расскажу."
    hide black_hare
    jump scene_12


label scene_12 :
    pause 0.2
    scene chip_factory_territory
    #Ребята ждут старта конкурса
    narrator "Перед двумя десятками испытуемых и кучей дронов находился двор Фабрики Чипов."
    show vechna smile1
    vechna "Диснейленд! Микки Маус меня дери!"
    show black_hare regular_disgust
    hide vechna
    black_hare "Твои формулировки — это нечто."
    hide black_hare
    show vechna smile2
    narrator "Она остановилась, жадно изучая глазами обстановку."
    hide vecnha
    narrator "Дроны разлетелись по территории. "
    narrator "Компании на Земле и Луне давно выглядели как этажи автоматизированных лабораторий, сборочных цехов, серверов — царства тишины и темноты. "
    narrator "Ведь роботам не нужен свет."
    narrator "Но что же скрывала Фабрика Чипов, дающая пожизненный пропуск в Чудесную сеть каждому, кто желает подключиться к ней?"
    narrator "Вечна трепетала и подпрыгивала. Кроме них, здесь было двадцать детей и множество дронов, транслирующих все в сеть."
    show vechna smile2
    vechna "Я так завидую, что ты уже знаешь Онку! "
    vechna "Вселенная тебя просто облизывает."
    show black_hare regular_confused
    hide vechna
    black_hare "Ага, перед тем, как съесть."
    #Онка говорит пару слов о своих сотрудниках и о том, что много денег заработал на разумных домашних животных.
    hide black_hare
    narrator "Всюду стояли геометрические статуи. "
    narrator "Сквозь них проникали лучи подсветки, добавляя яркости."
    narrator "Отовсюду доносились звуки жизни. "
    narrator "Летали плавно, или, наоборот, как безумные, птицы: живые и механические, с протезами и имплантами."
    narrator "Под странной фигурой у входа в Фабрику сидела группа хорьков. "
    show hight_fox smile
    narrator "На лавках обедали или читали лисы. Вечна уставилась на одного из них, с ланчбоксом."
    show hight_fox angry
    narrator "Заметив это, лис раздраженно поднялся на задние лапы и зашагал в сторону здания."
    show vechna smile1
    hide hight_fox
    vechna "Где бы мне взять такую походку!"
    hide vechna
    show onka regular
    narrator "К гостям вышел Онка. "
    narrator "Некоторое время он снисходительно смотрел, как дроны снимают все происходящее, а участники не обращают на него внимания. "
    narrator "Кроме Аша, который специально отошел, чтобы не попадать в его поле зрения и лишний раз не общаться."
    show onka smile
    onka "Добро пожаловать на Конкурс Фабрики Чипов! "
    onka "Именно здесь может ожить ваш проект."
    show onka sneaky
    onka "А может и не ожить, а может ожить и сразу умереть..."
    show onka smile
    onka "Ну да ладно. Мы отвлеклись."
    onka "По правилам конкурса, вы должны пробыть на Фабрике два дня."
    onka "Если готовы, идите за мной."
    narrator "Он развернулся. И сразу повернулся обратно, отчего его шея хрустнула."
    onka "Ах, да! Все свои вещи оставляйте у входа. "
    show onka thinking
    onka "Хорьки с ними ничего не сделают, их последнее время интересует одна архитектура."
    hide onka
    show black_hare regular
    narrator "Все пошли за ним. Аш посмотрел на сестру."
    show black_hare regular_disgust
    black_hare "Вытри слюни, ну серьезно."
    show vechna smile1
    hide black_hare
    vechna "Мысль, что его симуляцию можно сделать в сети, не дает мне покоя."
    show black_hare regular_disgust
    hide vechna
    black_hare "Я не хочу знать этого, никогда."
    hide black_hare
    show black_hare regular
    narrator "Он пошел вперед, обгоняя сестру."
    hide black_hare
    show onka regular
    narrator "Перед входом в здание, Онка развернулся к присутствующим и сообщил:"
    show onka sneaky
    onka "Отправляя заявку на участие, вы подписали договор о неразглашении того, что увидите и услышите внутри. "
    onka "Это значит, что при нарушении договора вы станете бессильны."
    narrator "Он сочувственно пожал плечами, словно не сам придумал такие правила."
    hide onka
    jump scene_13


label scene_13 :
    pause 0.2
    scene chip_factory_corridor1
    #Рассказываем условия конкурса. Наташа устраивает Ашу проблему с проектом, так как считает его главным конкурентом. Проект Макса и Наташи тоже должен быть на основе чипа или онка ее потом за это сольет
    narrator "Внутри Фабрика не выглядела, как сказочные декорации из фильма."
    show black_hare regular_surprised
    narrator "Обычный космический корабль, как на любой вывеске в сети."
    hide black_hare
    show onka sneaky
    narrator "Илли заметил пораженный отсутствием удивительного взгляд Аша."
    narrator "Хозяин заправил волосы за ухо и пожал плечами:"
    show onka thinking
    onka "Думаете, я не смотрел Чарли и Шоколадную Фабрику?"
    show onka sneaky
    onka "Приходя сюда, все ожидают увидеть что-то подобное."
    show onka victory
    show onka victory
    onka "Но у меня намного круче! В миллион раз!"
    hide onka
    show black_hare regular
    narrator "У Аша появилось желание повесить жетон на шею, чтобы Онка обратил внимание на количество баллов. "
    hide black_hare
    show black_hare regular_disgust
    narrator "Но воспоминания о том, где этот жетон побывал, остановили его."
    show black_hare angry_var
    black_hare "Не удивлены, что я тут?"
    show onka sneaky
    hide black_hare
    onka "Удивлен? Конечно, нет. "
    onka "Я же делал тест, исходя из того, какими сильными будут конкурсанты."
    show onka danger
    narrator "Потом он широко улыбнулся, показывая зубы."
    hide onka
    show onka regular
    narrator "Они пошли по коридору. Хозяин Фабрики остановился у одной из дверей."
    show onka thinking
    onka "Еще раз про договор. "
    onka "Никто, никогда не должен рассказывать о том, что тут произошло. "
    show onka smile
    onka "Помещения Фабрики в вашем распоряжении! "
    onka "О назначении всего, что вас заинтересует, расскажут лисы."
    show onka danger
    onka "Есть места ОПАСНЫЕ, боюсь, есть риск некоторых увечий. "
    show onka sneaky
    onka "Прошу заметить, это не покрывается страховкой по документу, который вы подписали."
    pause 0.2
    scene chip_factory_corridor2
    play sound 'audio/door.mp3'
    narrator "Онка закончил фразу, на ходу пропуская конкурсантов в одну из дверей."
    pause 0.2
    scene chip_factory_audience
    narrator "Все вошли в огромную аудиторию."
    show onka smile
    onka "В ходе конкурса вы должны создать или улучшить свое изобретение."
    show onka sneaky
    onka "Конкурс субъективный. "
    onka "Цель фабрики — найти потенциально коммерчески успешный проект на основе чипа, выпускаемого моей компанией."
    show onka smile
    onka "Не важно, идея у вас или прототип. Важно, как сильно вы сможете меня впечатлить."
    narrator "Вечна смотрела на Онку влюбленными глазами."
    hide onka
    show black_hare regular_disgust
    hide onka
    black_hare "Не могу рядом с тобой стоять."
    show vechna smile1
    hide black_hare
    vechna "У него есть отдел космоса!"
    show black_hare regular
    hide vechna
    black_hare "C каким проектом ты пришла? "
    show vechna smile2
    hide black_hare
    vechna "Я же не просто так просила доступ к использованию твоего патента."
    show black_hare regular_happy2
    hide vechna
    black_hare "Ты получишь поддержку фабрики!"
    show vechna sad
    hide black_hare
    vechna "Мое изобретение сделано на основе твоего."
    show black_hare regular_happy1
    hide vechna
    black_hare "Есть куча способов запустить проект без Онки."
    stop music1 fadeout 3
    play music2 'music/12.mp3' fadein 3
    hide black_hare
    show natasha regular
    play sound 'audio/door.mp3'
    narrator "Дверь зала открылась с характерным звуком, и в помещение вошла девушка с длинными волосами и гордо поднятой головой."
    narrator "По яркости ее образ мог бы посоперничать с самим Илли Онкой."
    narrator "Вечна открыла информацию о девушке в смешанной реальности: Наташа Ром. "
    narrator "Факультет микробиологии, второй курс. Восемнадцать лет."
    narrator "Статус: сто девяносто девять баллов на Конкурсе Илли Онки. "
    narrator "Иду побеждать! Подписывайтесь и следите за мной в мунтере!"
    hide natasha
    show vechna thinking
    hide natasha
    vechna "А ты, может, и подружишься с ней. Тоже ботанка."
    hide vechna
    show black_hare angry_var
    narrator " Аш бросил взгляд на Онку, тот помахал ему рукой."
    hide black_hare
    show onka smile
    hide black_hare
    onka "..."
    hide onka
    show black_hare angry_var
    hide onka
    black_hare "Он точно врал, когда говорил, что поверил в меня. "
    black_hare "Такая интонация была, знаешь..."
    hide black_hare
    pause
    show natasha smile
    narrator "Новенькая раскручивала на пальце жетон с цепочкой, на котором было выгравировано количество баллов за входной тест. "
    narrator "Она настолько ловко пропускала цепочку между пальцами, что эти движения можно было сравнить с совершенным владением неким древним оружием."
    hide natasha
    show vechna thinking
    hide natasha
    vechna "Она же не могла научиться заранее так крутить! "
    vechna "Неужели успела за ночь? Как ты думаешь?"
    hide vechna
    show natasha regular
    narrator "Девушка с длинными волосами остановилась и оглядела присутствующих презрительным взглядом."
    show natasha regular
    natasha "Здравствуйте, меня зовут Наташа, и я собираю команду для конкурса."
    show natasha smile
    natasha "Мой проходной балл – сто девяносто девять. "
    natasha "Что подтверждает особенный, красный жетон."
    narrator "Она несколько раз повертела его на пальце."
    natasha "Буду рада приветствовать в своей команде сильных конкурсантов."
    natasha "Подробный чек-лист, как попасть в нее, вы можете посмотреть в моем блоге."
    narrator "Девушка опустила руки и сомкнула за спиной в замок."
    natasha "У кого из вас самые высокие баллы после меня?"
    hide natasha
    show black_hare angry_var
    narrator "Теперь Аш обратил на нее внимание."
    show black_hare angry_var
    black_hare "А если в последнем туре тебе придется сражаться с участником твоей команды, который сильнее тебя?"
    show natasha smile
    hide black_hare
    natasha "Это ты что, намекаешь на себя?"
    hide natasha
    show black_hare regular
    pause
    call angry_sad
    show black_hare mood
    narrator "Аш ничего ей не ответил, он повернулся к остальным участникам."
    narrator "Все наблюдали за неофициальным поединком. Поэтому каждый услышал:"
    show black_hare regular_happy1
    black_hare "Я приглашаю к себе в команду трех человек с самым низким проходным баллом. "
    black_hare "Кстати, мой балл - двести."
    show natasha angry
    hide black_hare
    natasha "Вау! Двести! Разница целый один балл. "
    natasha "Все очень эпично, но моя цель - победить."
    hide natasha
    show onka regular
    narrator "Онка, все это время молча наблюдавший, наконец подошел к участникам."
    show onka regular
    onka "Для тех, кто пропустил инструктаж: узнаете подробности у других конкурсантов."
    narrator "Он перевел взгляд на Наташу."
    show onka thinking
    onka "Конечно, если они захотят вам что-то рассказывать."
    hide onka
    show maks regular
    narrator "Максим, прогуливающийся по периферии аудитории и внимательно осматривающий ее, засмеялся."
    hide maks
    show natasha sad
    narrator "Наташа повернула голову в его сторону, на лице читалась обида."
    show natasha regular
    narrator "Девушка сделала вид, что ничего не заметила. "
    hide natasha
    show onka smile
    narrator "К присутствующим обратился владелец фабрики."
    show onka smile
    onka "Я рад, что вы столь инициативны и успели разделиться на команды. "
    show onka sneaky
    onka "Хотя, еще час, — и были бы жертвы."
    show onka thinking
    onka "Но вы играете каждый за себя."
    onka "Сейчас у нас будет питч проектов — за минуту вам нужно рассказать о том, что вы создаете, и что собираетесь делать на конкурсе. "
    narrator "Все молча смотрели на Онку. Он в ответ молча смотрел на конкурсантов."
    hide onka
    show natasha regular
    hide onka
    natasha "Я первая!"
    hide natasha
    show onka sneaky
    narrator "Илли Онка ехидно улыбнулся поднимавшейся на сцену девушке."
    hide onka
    show natasha smile
    narrator "Остановившись в центре, она развернулась на небольших острых каблучках лицом к публике."
    show natasha smile
    natasha "В наше мирное и спокойное время, когда ресурсов для живых организмов может быть в избытке..."
    natasha "...люди сталкиваются с необходимостью сокращения или истребления некоторых видов животных."
    show natasha regular
    natasha "Например, на нашей любимой Земле нужен более эффективный способ сокращения количества медуз."
    natasha "Несмотря на увеличение популяций их естественных хищников..."
    natasha "...потепление Мирового океана и кормовая база, создает благоприятную среду для медуз. "
    natasha "Они парализуют электростанции, попадая в системы охлаждения, в которых используется морская вода."
    show natasha sad
    natasha "Оставляя города без энергии. "
    natasha "Мы боремся с ними почти двести лет."
    show natasha regular
    natasha "В качестве решения, я предлагаю программируемые вирусы. "
    show natasha smile
    natasha "Они могут внедряться в клетку и быть неактивными до того момента, пока не поступит триггер. "
    natasha "Вот и все."
    natasha "Презентацию можно скачать в моем мунтере. "
    natasha "Он, разумеется, открыт, как и мое сердечко."
    hide natasha
    show onka sneaky
    narrator "Онка жевал саранчу, покрытую разноцветной карамелью."
    show onka smile
    onka "Давайте похлопаем первому конкурсанту!"
    hide onka
    show natasha smile
    narrator "Наташа чувствовала себя свободно, она улыбнулась и поклонилась аплодирующим."
    hide natasha
    show onka thinking
    hide natasha
    onka "Крайне интересный доклад. Но остаются вопросы. Какой же триггер?"
    show natasha smile
    hide onka
    natasha "Для каждого организма — разный."
    natasha "Когда происходит триггер, вирус сокращает популяцию."
    natasha "Хотите знать, как это связано с чипом Фабрики?"
    show onka smile
    hide natasha
    onka "Вы читаете мои мысли!"
    show natasha smile
    hide onka
    natasha "Триггером для запуска умерщвления может являться импульс от чипа."
    natasha "Один чипированный организм может получить импульс для активации вируса и запустить цепную реакцию внутри своей популяции. "
    natasha "Можно сказать, они будут заражать друг друга."
    show onka danger
    hide natasha
    onka "Очень жизнеутверждающий проект!"
    hide onka
    show fox shock
    narrator "Лис рядом поперхнулся."
    hide fox
    show onka danger
    hide fox
    onka "Кто следующий?"
    hide onka
    show vechna smile1
    play sound 'audio/gum.mp3'
    narrator "Хлопнув большой пузырь жвачки, который переливался всеми цветами нефти, на сцену поднялась Вечна."
    show vechna smile2
    vechna "Всем привет, меня зовут Вечна Хом и я заканчиваю факультет обработки данных космических объектов."
    vechna "Несмотря на мою основную специальность... "
    vechna "...недавно я опубликовала исследование о технологии нейрохакинга мозга."
    vechna "Возможности изменения связей между нейронами. "
    show vechna smile1
    vechna "Да, такое уже есть, но у меня лучше."
    show vechna smile2
    vechna "Отмечу, что мозг работает по принципу: какие связи сильнее, по ним и пойдет импульс, и, соответственно, такое решение вы примите."
    vechna "Все наши хорошие и плохие привычки — это определенные, закрепленные связи в мозге."
    show vechna smile1
    vechna "Но чип... спасибо Илли Онке! "
    vechna "Вы, кстати, сегодня отлично выглядите!"
    narrator "Она улыбнулась и покраснела."
    hide vechna
    show black_hare regular_disgust
    hide vechna
    black_hare "..."
    hide black_hare
    show vechna smile2
    hide black_hare
    vechna "Значит, на основе Чипа можно изменить \"мощность\" связей в мозге."
    vechna "Можно стать любым человеком, приобрести страхи или же избавиться от них. "
    vechna "На данном конкурсе я хочу подтвердить работоспособность технологии. "
    vechna "Я покажу, что связи в мозге действительно можно изменить при помощи чипа, а вслед за ними, — и поведение!"
    narrator "Она осмотрела зал, ожидая вопросы. Все хлопали глазами."
    vechna "Всем спасибо за внимание!"
    narrator "Она бросила взгляд на Онку. "
    hide vechna
    show onka thinking
    narrator "Он смотрел прямо на нее, но в то же время как бы сквозь."
    hide onka
    show fox smile
    narrator "Рядом с ним крутился лис."
    hide fox
    show onka confused
    hide fox
    onka "Это сестра Аша?"
    show fox smile
    hide onka
    fox "Определенно."
    fox "Опережая Ваш вопрос, в исследовании она писала..."
    fox "...что определяет связи в мозгу то же программное обеспечение, которое определяет и эмоции у его имплантов."
    show onka danger
    hide fox
    onka "Очень ценная информация!"
    hide onka
    show vechna smile2
    narrator "Девушка спустилась со сцены. Только Наташа, стоявшая в первом ряду, расслышала тихое:"
    show vechna smile1
    vechna "Задачка выполнена! Какой же кайф!"
    narrator "К ней сразу же подошел брат."
    hide vechna
    show black_hare regular_happy2
    hide vechna
    black_hare "Думаю, у тебя мало конкурентов. "
    show vechna smile1
    hide black_hare
    vechna "Спасибо! Я об этом подозревала!"
    hide vechna
    narrator "Вскоре и остальные участники закончили свои презентации."
    show onka victory
    narrator "Хозяин Фабрики, активно жестикулируя, разговаривал с конкурсантами."
    show onka victory
    onka "Я очень впечатлен вашими проектами. "
    onka "Это талантливые и оригинальные применения чипа! "
    show onka smile
    onka "Но у нас остался последний участник."
    show onka sneaky
    onka "Питч обязателен. Надеюсь, это Ваша скромность, а не страх?"
    show black_hare regular_happy2
    hide onka
    black_hare "А может, мой способ привлечь внимание?"
    narrator "Сегодня Аш был не в настроении выступать. "
    narrator "Но что делать, он сам заварил эту кашу. В прямом смысле. Конкурсант медленно поднялся на сцену. Выдохнул."
    show black_hare regular
    black_hare "Аш — первый курс биопротезирования."
    black_hare "Использую технологические возможности чипа, чтобы решить проблему отсутствия взаимопонимания между людьми."
    narrator "По залу разнеслись звуки непонимания. "
    narrator "Он на автомате пересказывал свою недавнюю презентацию, следя за Вечной."
    black_hare "Мой ИИ позволяет обучить чип распознавать эмоции и чувства, и выдавать на них специфическую реакцию."
    show black_hare regular_angry
    narrator "Он посмотрел на сестру, та с кем-то увлеченно болтала, не глядя в его сторону."
    show black_hare angry_var
    black_hare "На конкурсе я обучу какую-нибудь эмоцию. Надеюсь, не ярость."
    black_hare "Конец."
    show onka victory
    hide black_hare
    onka "Будем очень ждать!"
    show onka confused
    onka "И мне кажется, кого-то здесь не хватает..."
    show onka thinking
    onka "Вы видели парня в костюме с галстуком?"
    narrator "Он повернулся лицом ко всем."
    onka "Ладно. Дальше."
    show onka regular
    onka "Я объявляю старт Конкурса! До 18:00 найдите на Фабрике все необходимое для представления и разработки своей технологии."
    onka "Напоминаю, что лисы вам помогут."
    hide onka
    stop music2 fadeout 3
    jump scene_14


label scene_14:
    pause 0.2
    scene chip_factory_audience
    #Показываем лиса, который не справляется  работой и Онку
    play music1 'music/newman_music.mp3' fadein 3
    narrator "В 18:00 участники конкурса стояли в аудитории."
    show onka regular
    onka "Я рад, после выдачи первого задания, появилось столько вопросов. "
    show onka sneaky
    onka "Я уж было испугался, что вам все понятно."
    onka "Вашей задачей была подготовка материалов для работы над проектами."
    onka "Что вы нашли для себя на Фабрике?"
    hide onka
    show natasha regular
    narrator "Наташа сделала шаг вперед и уже хотела говорить."
    hide natasha
    show vechna smile2
    narrator "Но ее перебила Вечна, которая поднималась на сцену."
    narrator "Взгляд девушки перемещался из стороны в сторону. "
    narrator "Она читала текст в смешанной реальности, не видимый никому, кроме нее."
    show vechna smile2
    vechna "Мне потребуются сорок лис и один фиолетовый мячик. "
    narrator "Она повертела мячик в руках."
    show vechna thinking
    vechna "Я хотела бы сохранить предполагаемые итоги эксперимента в тайне."
    narrator "Девушка кинула мячик вниз, в руки брата."
    vechna "Ты — следующий. А я — работать."
    hide vechna
    show black_hare regular_surprised
    play sound 'audio/ball.mp3'
    narrator "Он поймал мяч! И занял её место на сцене."
    show black_hare regular_confused
    black_hare "Неудобно говорить..."
    show fox shock
    hide black_hare
    fox "Неужели Вы не подготовились?"
    narrator "У лиса начали подкашиваться лапки. Конкурсант продолжал:"
    hide fox
    show black_hare regular_confused
    hide fox
    black_hare "Мне нужны были деньги, поэтому я продал часть оборудования Фабрики."
    hide black_hare
    show onka confused
    hide black_hare
    onka "А так можно было?"
    show fox smile
    hide onka
    fox "Это не запрещено правилами. "
    fox "Конкурсантам было позволено использовать оборудование Фабрики."
    show onka angry
    hide fox
    onka "Как можно было так составлять документы? Может, он и Фабрику продал? А?"
    hide onka
    show fox shock
    narrator "Лис подался назад, скрываясь от гнева хозяина."
    hide fox
    show onka confused
    narrator "Онка посмотрел на Аша, гадая: издевается он над ним, или нет?"
    show onka thinking
    onka "Один-ноль в Вашу пользу. Могу я узнать, чего именно лишилась Фабрика Чипов?"
    show black_hare regular
    hide onka
    black_hare "Это было оборудование, требующее переработки. "
    black_hare "Нашлись места, где нужны подобные материалы."
    show black_hare regular_surprised
    black_hare "Так что считайте, что я просто вынес мусор."
    show black_hare regular_happy1
    black_hare "Деньги требуются для добровольцев."
    black_hare "Распознавать эмоции в полукибернетическом мозгу лис — "
    black_hare "...это не то же самое, что распознавать человеческий мозг."
    show onka sneaky
    hide black_hare
    onka "Что мы увидим в итоге, Аш?"
    narrator "Он обвел руками аудиторию с конкурсантами. "
    hide onka
    show black_hare regular_happy1
    hide onka
    black_hare "Я планирую обучить Уши удивлению или отвращению..."
    black_hare "...и научить распознавать эмоцию хотя бы три раза из десяти."
    black_hare "Уверен, на Фабрике найдется то, что сможет удивить меня. Или наоборот."
    hide black_hare
    show natasha smile
    narrator "В стороне стояла Наташа. "
    narrator "Она ехидно смотрела на Аша, и, когда он закончил, медленно похлопала в ладоши."
    show natasha regular
    natasha "Ты хочешь выйти за пределы Фабрики и попросить людей зафиксировать активность мозга твоим софтом?"
    natasha "Хочу тебя расстроить. Очень хочу!"
    narrator "Девушка смотрела снизу вверх, сложив руки за идеально ровной спиной."
    narrator "Она остановилась перед сценой, наслаждаясь своим торжеством."
    narrator "Ей нравилось, что это — торжество ниже стоящего над тем, кто стоит выше."
    show natasha smile
    natasha "Это против правил."
    hide natasha
    show black_hare regular_confused
    pause
    call angry_sad
    show black_hare mood
    show black_hare mood
    black_hare "Правда?"
    hide black_hare
    show onka confused
    narrator "Онка вопросительно посмотрел на лиса. "
    hide onka
    show fox smile
    narrator "Тот одобрительно кивнул головой."
    hide fox
    show onka thinking
    hide fox
    onka "Как можно было так составлять документы?"
    show black_hare regular_confused
    hide onka
    black_hare "Мне кажется, Вы тоже удивлены!"
    show onka confused
    hide black_hare
    onka "Есть ли другие варианты обучения эмоций на людях?"
    show black_hare angry_var
    hide onka
    black_hare "Если другие конкурсанты не захотят быть моими подопытными всю ночь, то — нет."
    narrator "Он злился, но, пожалуй, больше — на самого себя. "
    narrator "Потому что думал о таком развитии событий, но надеялся, что ему повезет. "
    show black_hare sad_var
    narrator "В голове мелькнула мысль: \"Слово \"обойдется\" — точно не про тебя\"."
    show black_hare sad_var
    black_hare "Соберу всю информацию на себе самом."
    show black_hare regular
    black_hare "А что? Устрою марафон удивления или другой эмоции. Как пойдет."
    show black_hare angry_var
    black_hare "А может, научиться не удивлению, а радости? "
    black_hare "Для этого придется проверить, сколько человек я смогу убить за время конкурса."
    hide black_hare
    show onka danger
    narrator "Онка залился смехом. В тишине это звучало довольно странно. "
    narrator "Другие присутствовавшие не оценили юмор."
    hide onka
    show natasha sad
    narrator "Наташа округлила глаза. Трудно было не принять шутку на свой счет."
    hide natasha
    show maks regular
    play sound 'audio/door.mp3'
    narrator "В аудиторию проскользнул Макс, и девушка переключила внимание на него."
    hide maks
    show natasha sad
    narrator "Она не замечала рядом с собой парня, который пытался незаметно понюхать ее волосы."
    narrator "А Максим даже не скользнул по ней взглядом."
    hide natasha
    show onka regular
    narrator "Онка, наконец, отсмеялся и глубоко задышал, стараясь успокоиться."
    narrator "Лис принес ему воду."
    show onka regular
    onka "Мне нравится настрой! Но, во избежание жертв, могу помочь с удивлением."
    show onka sad
    narrator "Настроение Онки изменилось. Он сел на пол."
    show onka sad
    onka "Что-то мне нехорошо."
    narrator "Он взял воду у лиса и через пару минут пришел в себя."
    show onka thinking
    onka "Все участники получили необходимую информацию о точках проживания, питания и прочие нужные сведения? "
    narrator "Ему никто не ответил."
    onka "Прекрасно. Завтра, в 18:00, подводим итоги."
    narrator "Хозяин обратился к подопечному."
    show onka regular
    onka "Зафиксируй требования остальных участников."
    show onka thinking
    onka "И не совершай ошибок."
    hide onka
    show fox angry
    narrator "Лис кивнул головой, выпрямил спину и серьезно посмотрел на конкурсантов."
    hide fox
    narrator "Вскоре все покинули аудиторию. "
    narrator "Аш искал глазами сестру, но, нигде не увидев ее, вышел в коридор."
    stop music1 fadeout 3
    jump scene_15


label scene_15:
    pause 0.2
    scene chip_factory_corridor2
    #Аш получает возможность узнать о лисьих кастах
    play music2 'music/newman_classic.mp3' fadein 3
    narrator "Пройдя пару метров, Аш почувствовал чью-то ладонь на своей руке. "
    show onka smile
    narrator "Нос уловил слабый запах манго. Это Илли тянул Аша за собой, в другую сторону."
    hide onka
    show black_hare regular
    pause
    call surprised_disgust
    show black_hare mood
    show black_hare mood
    black_hare "Эм... Проводить тебя ко врачу? Он, кстати, тоже лис?"
    show onka sad
    hide black_hare
    onka "Я в норме, физические проблемы меня не остановят."
    show black_hare surprised_var
    hide onka
    black_hare "Я хотел сестру найти. Куда она ушла после выступления?"
    narrator "Илли резко остановился."
    show onka confused
    hide black_hare
    onka "Разве ты пришел не за шансом для своего изобретения?"
    hide onka
    show black_hare regular
    narrator "Аш смотрел вглубь длинного коридора, стараясь разглядеть удаляющуюся Вечну."
    show onka confused
    hide black_hare
    onka "Ты можешь выбрать любое направление работы Фабрики. "
    onka "Я покажу тебе, как это устроено."
    show black_hare surprised_var
    hide onka
    black_hare "А, да..."
    black_hare "Я все равно не знаю, куда мне нужно."
    show onka confused
    hide black_hare
    onka "Почему ты не стараешься ради своего изобретения?"
    show black_hare sad_var
    hide onka
    black_hare "У тебя высокие требования. "
    black_hare "Это все, на что я способен."
    show onka confused
    hide black_hare
    onka "Ты же понимаешь, что читать эмоции — это практически то же самое, что и читать мысли?"
    show black_hare sad_var
    hide onka
    black_hare "Я всего лишь хотел, чтобы у людей был шанс понять меня. "
    black_hare "Думаешь, чтение мыслей сделает мир лучше?"
    show onka sneaky
    hide black_hare
    onka "Смотря как использовать. "
    onka "Сейчас Чудесная сеть настолько эффективна, что вредит людям."
    onka "Они должны меньше в ней сидеть."
    show onka thinking
    onka "Сеть — это не место для жизни, а инструмент для осуществления действительно великих проектов."
    hide onka
    show black_hare surprised_var
    narrator "Аш посмотрел на Илли другими глазами."
    show black_hare surprised_var
    black_hare "Сложно это говорить, но я с тобой согласен."
    black_hare "И еще. Почему, находясь наедине, мы говорим друг с другом на “ты”?"
    show onka sad
    hide black_hare
    onka "Иногда мне нужен хотя бы один такой человек. "
    show onka confused
    onka "Хотя, достаточно того, что ты — человек, а не лис."
    show black_hare sad_var
    hide onka
    black_hare "Это, должно быть, грустно?"
    show onka smile
    hide black_hare
    onka "Разнообразие необходимо. Мозг всегда требует новую информацию."
    show onka thinking
    onka "Но он такой глупый! Для него насыщенная жизнь — то же самое, что и видеоряд в сети. "
    show onka smile
    onka "Поэтому, я не переживаю из-за того, что мой мозг заставляет меня чувствовать. "
    show onka sad
    onka "Чувства — это иллюзия."
    show black_hare sad_var
    hide onka
    black_hare "Очень хорошо, что у тебя получается игнорировать чувства."
    black_hare "Только простые смертные — такие, как я — не могут их игнорировать. "
    show black_hare regular
    black_hare "Поэтому мне приходится их учитывать. Я живу не среди лис."
    show onka sneaky
    hide black_hare
    onka "Очень остроумно. Нужно внести в правила запрет на шуточки."
    onka "Куда мы пойдем?"
    show black_hare angry_var
    hide onka
    black_hare "Я уже говорил, что не знаю, куда мне нужно идти. "
    black_hare "Я ищу сестру."
    show onka smile
    hide black_hare
    onka "Эх! Дай ей спокойно поработать."
    onka "Если человек хочет хакнуть свои мозги, то его уже не остановить."
    onka "А ты — идешь со мной."
    show black_hare regular_disgust
    hide onka
    black_hare "Вот внеси это в правила, тогда и посмотрим."
    show onka sneaky
    hide black_hare
    onka "Ты хочешь узнать, как живут мои кибернетические лисы? "
    narrator "Гость Фабрики оживился."
    show black_hare regular_happy2
    hide onka
    black_hare "Сложно отказаться от такого!"
    hide black_hare
    narrator "Хозяин Фабрики и Аш продолжали петлять по коридорам."
    stop music2 fadeout 3
    jump scene_16


label scene_16:
    pause 0.2
    scene chip_factory_corridor3
    #Здесь показываем, что Облачный пытается обмануть Онку и он не так-то прост. Хотя как потом покажут, он все равно улизнул и вернулся только что бы помочь Ашу в битве с Максом
    play music1 'music/newman_gt.mp3' fadein 3
    play sound 'audio/door.mp3'
    narrator "Спустя десять минут они вошли в одну из дверей. В новом помещении было темно."
    pause 0.2
    scene black_background
    show onka sneaky
    onka "Это — самая скучная часть."
    show black_hare surprised_var
    hide onka
    black_hare "Почему так темно?"
    show onka sneaky
    hide black_hare
    onka "Скажи, для чего тратить энергию на помещения, где живут те, кто видит в темноте?"
    show black_hare surprised_var
    hide onka
    black_hare "А я много увижу? В темноте?"
    show onka sneaky
    hide black_hare
    onka "Света нет только в служебных помещениях, не беспокойся."
    show onka smile
    onka "На Фабрике обычно тоже темно."
    show black_hare regular
    hide onka
    black_hare "К твоему приходу здесь не готовятся?"
    show onka smile
    hide black_hare
    onka "Нет."
    show black_hare surprised_var
    hide onka
    black_hare "Разве не от тебя зависит их судьба?"
    narrator "Хозяин Фабрики рассмеялся."
    show onka smile
    hide black_hare
    onka "Нет, что ты. Жизнь — да. Судьба — совершенно нет."
    show black_hare disgust_var
    hide onka
    black_hare "Сказал тот, кто разделил их на касты!"
    show onka confused
    hide black_hare
    onka "Может, тебе не нужно туда? Смотрю, ты и так все знаешь."
    show black_hare disgust_var
    hide onka
    black_hare "Ты спрашивал об этом лиса на презентации."
    show onka sad
    hide black_hare
    onka "Лисы появились очень давно. Задолго до меня."
    onka "Фабрика Чипов — это же технологическая династия."
    show onka thinking
    onka "У лис есть культура, связанная с Фабрикой. "
    onka "Ты должен понимать, что те, кто варится в изоляции, живут по очень причудливым правилам."
    show black_hare disgust_var
    hide onka
    black_hare "Разве ты не можешь взять и отменить касты?"
    show onka thinking
    hide black_hare
    onka "От меня зависит лишь то, станет ли лис из Низшей касты представителем Высшей."
    narrator "Аш обрадовался, что он смог донести мысль."
    show black_hare regular_happy1
    hide onka
    black_hare "Об этом я и говорю: ты же можешь лис повышать или понижать!"
    show onka regular
    hide black_hare
    onka "Только Высших и Низших. Третья и вторая — неразумные. "
    narrator "Илли остановился и посмотрел на Аша."
    onka "Другие лисы даже не назвали те касты. Они — другие. Увидишь. Просто три и два."
    hide onka
    pause 0.2
    scene chip_factory_foxs
    narrator "Они вошли в кубическое помещение. "
    narrator "Все его стенки были увиты лестницами и ячейками."
    narrator "С разных сторон шли туннели куда-то глубже."
    narrator "А в самом центре стоял удивительно блестящий, словно новенький, робот в желтой накидке."
    show black_hare surprised_var
    hide onka
    black_hare "Целый лисий улей!"
    black_hare "Но я себе все не так представлял. Они же такие важные, с ланчбоксами."
    show onka sneaky
    hide black_hare
    onka "О! Тут есть кухня и прачечные. Куда ж без этого. "
    show onka smile
    onka "Шучу, все автоматизировано."
    hide onka
    narrator "Вокруг было шумно, лисы бегали по лестницам, носили что-то в руках и зубах, шумно обсуждали новости на скамейках."
    show onka confused
    onka "Ты захотел на Фабрике посмотреть не самое интересное, но, однако, попал на один из весьма любопытных моментов."
    show black_hare regular
    hide onka
    black_hare "Ты сам предложил."
    show black_hare regular_happy2
    narrator "Аш пытался ухватить окруживших его лис за хвосты."
    narrator "В стенах собственного дома лисы походили на обычных зверей, которых он видел в детстве, еще на Земле."
    show black_hare surprised_var
    black_hare "Это и есть третья и вторая касты?"
    narrator "Лисы поблизости презрительно на него фыркнули и сразу ушли."
    show onka confused
    hide black_hare
    onka "Вот и урок местной культуры. Их обижает такое сравнение."
    show black_hare disgust_var
    hide onka
    black_hare "Что с ними не так?"
    hide black_hare
    play sound 'audio/gong.mp3'
    narrator "Зазвучал громкий звук, и лисы посыпались из нор. "
    narrator "Илли отошел вместе с Ашем к стене."
    show black_hare surprised_var
    narrator "Аш наблюдал, как, спускаясь с лестниц, словно стекая вниз волной, лисы смешивались в кишащей оранжевой толпе."
    narrator "Аш оглянулся вокруг. Что-то казалось ему непривычным, странным."
    play sound 'audio/gong.mp3'
    narrator "Раздался еще один удар, и движущаяся масса пушистых зверей замерла вокруг робота в желтой накидке. "
    narrator "Робот, находящийся в центре зала, шевельнулся."
    narrator "Аш повернул голову в сторону Илли. "
    hide black_hare
    show onka smile
    narrator "Тот широко улыбался, с любовью глядя на зверей."
    hide onka
    stop music1 fadeout 3
    play music2 'music/e.mp3' fadein 3
    narrator "Шум и гам сменились тишиной. В воздухе запахло благовониями."
    narrator "Как сильно ни пытался гость понять, где они находятся, но так и не смог этого сделать. "
    show black_hare regular_confused
    narrator "Робот сложил ладони перед грудью. "
    narrator "Сидящие вокруг него лисы наклонили головы, и в воздухе зазвучала буддийская сутра."
    show black_hare surprised_var
    narrator "Про себя Аш решил, что это был правильный выбор места, чтобы по-настоящему удивиться."
    show black_hare surprised_var
    black_hare "Что происходит?"
    show onka smile
    hide black_hare
    onka "Они молятся, что же еще?"
    hide onka
    show black_hare regular
    pause
    call surprised_disgust
    show black_hare mood
    show black_hare mood
    black_hare "Что-что?"
    narrator "Он уже не смотрел на лис, а пытался понять по глазам Онки, смеется тот или нет. "
    narrator "Хотя, зрелище подтверждало истинность его слов."
    hide black_hare
    show onka smile
    hide black_hare
    onka "Религия, или другая фантазия, дает им что-то общее, чтобы они друг друга не убивали."
    show black_hare disgust_var
    hide onka
    black_hare "Почему не дать им что-то более адекватное?"
    show onka confused
    hide black_hare
    onka "Веру в Фабрику? Это ведь тоже фантазия. "
    show onka thinking
    onka "Убери из Фабрики всех лис — разве при этом она закроется? "
    onka "Убери все здания — Фабрика при этом юридически все равно будет существовать. "
    onka "А юридическое существование — просто фантазия, о которой люди договорились между собой. "
    show onka sneaky
    onka "Если подпишем бумаги, то будем в них верить."
    onka "Религия и компании основаны на вере. Это коллективные фантазии."
    show black_hare surprised_var
    hide onka
    black_hare "Но почему — буддизм?"
    show onka smile
    hide black_hare
    onka "Искусственный интеллект Фабрики считает это оптимальным вариантом. "
    onka "Кстати, это именно Фабрика управляет судьбой лис в момент рождения."
    onka "Судьбой, а значит, и кастами."
    show black_hare surprised_var
    hide onka
    black_hare "А здесь какие?"
    show onka confused
    hide black_hare
    onka "Высшие и Низшие."
    show black_hare surprised_var
    hide onka
    black_hare "Они живут вместе?"
    show onka smile
    hide black_hare
    onka "И растут вместе. "
    show black_hare surprised_var
    hide onka
    black_hare "В чем между ними разница?"
    show onka smile
    hide black_hare
    onka "Их разница — в уровне образования."
    onka "Любой Низший может стать Высшим."
    onka "Лисятами они растут вместе, получая базовое воспитание."
    onka "Затем получают имплант развитого неокортекса и специализацию."
    onka "Высшие специализируются на научных дисциплинах. "
    onka "Низшие — на обслуживании Фабрики."
    onka "Хотя, там тоже куча инженерии."
    onka "Те из Низших, кто хочет попасть в Высшую касту — сдают экзамен, если находят для этого время."
    show black_hare regular_confused
    hide onka
    black_hare "А почему этот не здесь?"
    narrator "Он показал рукой на лиса, выскользнувшего из одного туннеля и направившегося ко входу в следующий. "
    narrator "Лис был ему знаком."
    hide black_hare
    stop music2 fadeout 3
    play music1 'music/w.mp3' fadein 3
    show onka thinking
    hide black_hare
    onka "Это же Облачный! Быстрее!"
    narrator "Хозяин Фабрики взял Аша за руку и повел за животным."
    hide onka
    show black_hare surprised_var
    narrator "Они окликнули зверя, но тот старательно пытался скрыться из виду."
    show black_hare surprised_var
    black_hare "Что случилось?"
    hide black_hare
    show onka confused
    narrator "Илли выждал десять секунд, затем выглянул в коридор и тихо пошел за лисом, держа гостя за руку. "
    hide onka
    pause 0.2
    scene black_background
    narrator "Аш двигался за Онкой практически в кромешной тьме."
    hide black_hare
    show onka confused
    play sound 'audio/door.mp3'
    narrator "Вскоре, тот открыл одну из дверей. "
    show onka thinking
    narrator "Снова досчитав до десяти, Илли дал Ашу знак идти за ним."
    narrator "Потом вспомнил, что спутник ничего не видит. "
    show onka thinking
    onka "Плохо тебе, без лисьего зрения!"
    narrator "Хозяин Фабрики потянул парня за собой."
    hide onka
    jump scene_17


label scene_17:
    pause 0.2
    scene chip_factory_foxs_3_2
    #Макс говорит, что Онка зло поскольку создает животных для обсчета данных на них. Выдвигает гипотезу, что может быть и скопированных он использует также? Онка выгоняет его.
    narrator "В слабом освещении герой разглядел длинное помещение с высокими потолками."
    narrator "В конце комнаты был огромный алый экран."
    show black_hare regular
    black_hare "Ты модифицированный? С лисьим зрением?"
    show onka angry
    hide black_hare
    onka "..."
    onka "Где Облачный?"
    narrator "В нос ударил сильный запах. Пахло паленой плотью, тлеющей шерстью и дымом. "
    show black_hare regular_fear
    hide onka
    black_hare "У экрана? Ты чувствуешь запах дыма?"
    narrator "Хозяин Фабрики снова вел парня вперед."
    show black_hare disgust_var
    black_hare "Здесь я и сам вижу."
    hide black_hare
    show onka thinking
    narrator "Онке не было смешно или любопытно. Он насторожился. Послышался лай нескольких лис."
    hide onka
    show black_hare regular_fear
    narrator "Приблизившись, Аш понял, что ошибся насчет экрана. Это было окно в другое помещение. "
    narrator "Рядом с ним располагалась дверь."
    narrator "Парень замер на месте, вглядываясь в происходящее за стеклом."
    hide black_hare
    narrator "Внутри полыхало пламя, а в нем — что-то хаотично металось и перемещалось резкими скачками. "
    play sound 'audio/colb.mp3'
    narrator "С треском лопнула колба, из которой вывалился кто-то живой, но без сознания."
    show black_hare angry_var
    black_hare "Это лисы! Отключите подачу кислорода! Ну же!"
    narrator "Он повернулся к Онке и лисам, которые молча наблюдали за происходящим."
    narrator "Один из них что-то жевал. Парень стал искать Облачного, но среди лис его не было."
    hide black_hare
    show hight_fox smile
    hide black_hare
    hight_fox "Само потухнет."
    narrator "Аш подошел к двери, ведущей внутрь."
    show hight_fox shock
    hight_fox "Я благоразумно рекомендую не трогать..."
    hide hight_fox
    show black_hare angry_var
    narrator "Но Аш уже открыл дверь. "
    play sound 'audio/fire.mp3'
    narrator "И этого хватило, чтобы огонь ворвался в общее помещение. "
    show black_hare regular_fear
    narrator "Конечно, парень сразу же пожалел о своем эмоциональном порыве — одежда на нем загорелась."
    hide black_hare
    show hight_fox angry
    narrator "Легкие обожгло. Но рядом появился лис, закрывший лапами дверь."
    narrator "Лисы тут же повалили Аша на пол и принялись топтаться и тушить прожженную в нескольких местах мантию."
    narrator "Повреждения были почти не видны."
    hide black_hare
    show black_hare sad_var
    hide hight_fox
    black_hare "Да что же это?!"
    show onka thinking
    hide black_hare
    onka "Похоже, произошла авария в блоке Третьей и Второй каст. "
    onka "Но Фабрика все починит."
    onka "Вопрос — в причине аварии."
    show black_hare angry_var
    hide onka
    black_hare "В смысле — в причине?"
    show hight_fox smile
    hide black_hare
    hight_fox "Это же Третьи и Вторые! Расходный материал. "
    hight_fox "Вот оборудование действительно жаль, оно дорогое."
    hide hight_fox
    show black_hare regular
    pause
    call surprised_disgust
    show black_hare mood
    show black_hare mood
    black_hare "Вы совсем дикие?"
    show hight_fox angry
    hide black_hare
    hight_fox "Молодой человек, следите за словами!"
    show black_hare angry_var
    hide hight_fox
    black_hare "Разве это не ваши сородичи?"
    narrator "Лисы рядом засмеялись."
    hide black_hare
    show hight_fox smile
    hide black_hare
    hight_fox "Да они на Фабрику выходят из-за стекла только года в четыре — хуже роботов!"
    show hight_fox angry
    hight_fox "Годятся только для экспериментов над ними, да для расчетов."
    hight_fox "Когда запретили есть их мозги, они стали совсем бесполезными."
    show black_hare disgust_var
    hide hight_fox
    black_hare "Вы дикие!"
    hide black_hare
    show hight_fox shock
    narrator "Он бросился на лиса и стал его трясти."
    hide hight_fox
    show maks angry
    narrator "Из темного угла помещения вышел Максим."
    show maks angry
    maks "А что ты удивляешься?"
    maks "Я знаю, что он их использует, как живые компьютеры."
    show black_hare surprised_var
    hide maks
    black_hare "Это ты сделал?"
    show black_hare angry_var
    black_hare "Сжег бы лучше Онку, идиот!"
    hide black_hare
    show maks angry
    narrator "Спустя секунду, Максим ударил Аша под колени, и, схватив его за Уши, рванул их изо всех сил вверх."
    hide maks
    show black_hare regular_blood
    play sound 'audio/ears.mp3'
    narrator "Раздался жуткий хруст, и из места крепления имплантов по лицу Аша потекла кровь. "
    narrator "Он закричал."
    show black_hare regular_blood
    black_hare "Ты меня убьешь!"
    black_hare "Идиот! Они же вживлены в голову!"
    narrator "Кровь продолжала стекать по лицу, а Максим все тянул Уши вверх."
    hide black_hare
    show maks angry
    hide black_hare
    maks "А ты уже, смотрю, подружился с этим террористом?"
    hide maks
    show onka confused
    narrator "Онка молча наблюдал за сценой, дав лисам сигнал не вмешиваться."
    show onka thinking
    onka "Я вижу, ты многое узнал, пока тут шастал. "
    show onka angry
    onka "Сжег бы тут все, чего мелочиться. Даже — всю лунную станцию."
    onka "А то ведь сколько тут зла, наверное, творится!"
    hide onka
    show black_hare regular_blood
    narrator "Максим не давал Ашу подняться. В его глазах сверкала жестокость."
    hide black_hare
    show maks angry
    hide black_hare
    maks "Твоя сеть..."
    maks "Почему в ней пропадают копии людей, а?"
    maks "Почему мой отец скопировался в нее и пропал, не подскажешь?"
    show black_hare regular_blood
    hide maks
    black_hare "Может, он просто свалил от такого маньяка, как ты?"
    hide black_hare
    show maks angry
    narrator "Максим отпустил свою жертву, и пнул Аша ногой."
    show maks angry
    maks "Все, кто поддерживают рыжего ублюдка, сгорят! "
    maks "И, да! Может, и вся станция!"
    narrator "Максим хотел броситься на Онку, но Аш сбил его с ног."
    hide maks
    show black_hare regular_blood
    hide maks
    black_hare "Нафига жечь лис?"
    narrator "Аш обездвижил соперника, усевшись сверху и заломив ему руки за спину."
    narrator "Затем достал из кармана моток армированного скотча \"Brutal\"!"
    play sound 'audio/brutal.mp3' 
    narrator "До ушей Максима донесся резкий скрип."
    narrator "Он пытался сопротивляться, но Аш уже накрепко залепил ему рот... "
    narrator "...и всё сильнее обматывал голову скотчем, перекрывая доступ к кислороду."
    narrator "А когда ты живешь на лунной станции, задохнуться — твой самый большой страх."
    black_hare "Помнишь свой подарок мне на презентации? Пригодился!"
    show onka confused
    hide black_hare
    onka "Ого! У меня будут из-за этого проблемы?"
    narrator "Он задал этот вопрос Облачному, но забыл, что того нет рядом. И вызвал его в сети."
    show onka thinking
    onka "Наверняка, будут."
    onka "Оттащите парня."
    hide onka
    show black_hare regular_blood
    narrator "В порыве ярости Аш продолжал заматывать голову Максима клейкой лентой, пока не почувствовал на руке крепкие челюсти."
    hide black_hare
    show hight_fox angry
    narrator "Из-под клыков Лиса брызнула кровь."
    hide hight_fox
    show onka angry
    hide hight_fox
    onka "Хватит! И так тошно последнюю неделю."
    narrator "Он сам отбросил Аша в сторону."
    hide onka
    show black_hare regular_blood
    hide onka
    black_hare "Что ты делаешь? Он жег твоих лис!"
    show onka angry
    hide black_hare
    onka "Ничего страшного! "
    hide onka
    show hight_fox angry
    narrator "Лис разорвал зубами скотч на лице Макса и невинно отметил:"
    show hight_fox smile
    hight_fox "Третьи и Вторые не разумны, я же сообщил."
    show black_hare regular_blood
    hide hight_fox
    black_hare "Но ведь маленькие лисы Высшей и Низшей касты тоже неразумные! "
    black_hare "Разве нет? Но о них вы заботитесь!"
    show hight_fox smile
    hide black_hare
    hight_fox "Производство Третьих и Вторых автоматизировано. "
    hight_fox "Они, пока не достигнут взрослого состояния, растут в аквариумах."
    hight_fox "Логично, что мы к ним не привязываемся."
    hide hight_fox
    show black_hare regular_blood
    narrator "Аш посмотрел на Онку."
    show black_hare regular_blood
    black_hare "Ты собираешься спасать лис? Ты же отвечаешь за их безопасность!"
    narrator "Тот удивленно на него посмотрел."
    hide black_hare
    show onka angry
    hide black_hare
    onka "Я думал ты про это забыл, пока бил белобрысого."
    show onka thinking
    onka "Но это подпольное лисье развлечение. "
    onka "Они сами иногда специально так делают."
    show onka angry
    onka "Именно поэтому данному “недоразумению” удалось попасть только сюда."
    narrator "Он указал рукой на Макса, который сидел на полу. Тот уже не выглядел таким самоуверенным."
    onka "Из преступлений — только нерациональная трата ресурсов. "
    show onka thinking
    onka "Этих лис все-таки и кормили, и поили."
    hide onka
    show black_hare regular_blood
    narrator "Аш молчал, пытаясь понять, среди кого он оказался."
    show onka thinking
    hide black_hare
    onka "А ты…"
    narrator "Он повернулся к Максу."
    onka "Исключен из конкурса. "
    show onka danger
    onka "И, поверь, лучше тебе молчать о том, что здесь произошло."
    hide onka
    show fox angry
    narrator "В помещении появился Облачный лис."
    hide fox
    show onka thinking
    hide fox
    onka "Где ты был?"
    hide onka
    show fox shock
    narrator "Лис хотел что-то сказать."
    narrator "В этот момент в воздухе раздался крик Илли Онки."
    show onka angry
    hide fox
    onka "Кто? Кто находится в зале с моими лианами?!"
    onka "Почему сработала система безопасности? "
    onka "Там кто-то без лис! Без присмотра!"
    narrator "Лисы подпрыгнули на месте и разбежались в разные стороны. Облачный остался на месте."
    hide onka
    show fox angry
    hide onka
    fox "Что случилась?"
    show onka angry
    hide fox
    onka "Очевидно, решили разрушить всю мою Фабрику!"
    hide onka
    show black_hare regular_blood
    narrator "Он помог подняться Ашу на ноги и снова повел за собой."
    hide black_hare
    play sound 'audio/fire2.mp3'
    narrator "Аш не отрывал взгляда от горящих заживо лис. "
    narrator "Не мог поверить, что лисы так поступают друг с другом: считают мертвыми тех, кто еще живы."
    hide black_hare
    show fox angry
    hide black_hare
    fox "Третья каста — просто лабораторные животные, а Вторая — живые компьютеры. "
    fox "Они даже не говорят."
    show black_hare regular_blood
    hide fox
    black_hare "Некоторые люди тоже не говорят..."
    show fox angry
    hide black_hare
    fox "Фабрика вырастит новых, у нас регулярно какие-то аварии. "
    fox "Это же Луна."
    narrator "Успокаивал его Облачный."
    show onka angry
    hide fox
    onka "Пойдешь с нами, пушистый."
    onka "И еще расскажешь, где ты был!"
    onka "И этого тоже, бери с собой!"
    narrator "Он с презрением посмотрел на потрепанного Максима, на лицо которого уже вернулась ухмылка."
    hide onka
    stop music1 fadeout 3
    jump scene_18


label scene_18 :
    pause 0.2
    scene chip_factory_corridor1
    #Показываем, что Онке его мечта о заселении планет важнее, чем живые лисы на Луне. Он рассказывает о своем деле жизни
    play music2 'music/newman_classic.mp3' fadein 3
    narrator "Они вышли с территории лис. "
    show black_hare regular_blood
    narrator "Петляя по коридорам, Аш давно потерял ориентацию, даже не глядя на освещение. "
    narrator "Кровь перестала течь и уже местами запеклась. "
    narrator "По всей видимости, повреждения оказались не слишком серьезными..."
    narrator "...и парень просто оттер ее с лица рукавом мантии. "
    show black_hare sad_var
    narrator "Аш посматривал на Максима."
    show black_hare regular
    black_hare "Что с твоим отцом?"
    show maks angry
    hide black_hare
    maks "Я же сказал — он пропал."
    show black_hare surprised_var
    hide maks
    black_hare "Причем тут Онка?"
    show maks angry
    hide black_hare
    maks "Ты дурак? Да! "
    maks "Он сделал сеть и чип открытыми, но ядро ведь принадлежит ему!"
    maks "Непонятно, чем он здесь занимается."
    maks "Одна из пятидесяти копий пропадает! И никаких следов!"
    show black_hare disgust_var
    hide maks
    black_hare "Очень надуманно."
    black_hare "Ты же не можешь узнать, пропали они или нет, на сто процентов."
    black_hare "Могли специально скрыться от семьи."
    show maks regular
    hide black_hare
    maks "Мой отец не мог. "
    maks "Он и ушел туда, чтобы закрыть все \"хотелки\" этой..."
    narrator "Парень остановил себя и сменил тему."
    maks "А могли копии, как и лисы, стать функциями? Нет?"
    narrator "Онка остановился у одной из дверей."
    show onka thinking
    hide maks
    onka "Лис, отвечаешь за белобрысого головой. "
    onka "Стойте оба здесь."
    hide onka
    stop music2 fadeout 3
    play music1 'music/w.mp3' fadein 3
    play sound 'audio/door.mp3'
    narrator "Онка вошел внутрь. "
    pause 0.2
    scene chip_factory_vines2
    show onka confused
    narrator "Помещение освещалось бледно-голубым светом растений. Оно напоминало жуткий ботанический сад."
    show onka thinking
    onka "Смотри под ноги!"
    show black_hare surprised_var
    hide onka
    black_hare "Ого!"
    narrator "Он споткнулся о лиану, испачкавшись чем-то липким и теплым."
    show black_hare disgust_var
    black_hare "Фэ!"
    hide black_hare
    narrator "Свет ламп отражался от корнеобразных растений, стелющихся высоким ковром по большому залу."
    narrator "Илли крепко взял парня за руку."
    show onka thinking
    hide black_hare
    onka "Для равновесия."
    narrator "И они двинулись в центр."
    hide onka
    show black_hare disgust_var
    narrator "Скоро Аш все-таки потерял равновесие и схватился рукой за одну из лиан. "
    narrator "Скользкая, толщиной с руку, она была на ощупь похожа на червя. "
    narrator "Казалось, что она — живая и пульсирует."
    show black_hare disgust_var
    black_hare "Чем оно покрыто? Что это?"
    show onka angry
    hide black_hare
    onka "Тихо!"
    hide onka
    narrator "В центре помещения виднелся чей-то силуэт."
    pause
    show onka thinking
    narrator "Они медленно пробирались всё ближе, преодолевая стелющийся лес долгих несколько минут. "
    narrator "Раздался знакомый голос."
    hide onka
    show natasha smile
    hide onka
    natasha "Приготовьтесь удивляться!"
    show black_hare surprised_var
    hide natasha
    black_hare "Это Наташа!"
    show onka thinking
    hide black_hare
    onka "Я уже понял."
    hide onka
    show natasha regular
    narrator "Лица девушки не было видно. "
    narrator "Лианы подсвечивали бледно-голубым цветом ее тонкие ноги."
    narrator "Она взяла светящуюся лиану левой рукой, затем поднялась и наступила каблуком на ее середину."
    narrator "Снова наклонилась, взяв два конца лианы в свободную руку. "
    narrator "Накрутила их вокруг кистей, натянула, и..."
    show onka angry
    hide natasha
    onka "Стой! Твою...!"
    hide onka
    show natasha smile
    narrator "Но она уже резко дернула концы вверх."
    play sound 'audio/tearing.mp3' 
    narrator "От рывка лиана разорвалась. "
    narrator "Из-под ног девушки, в месте разрыва, красиво разлетелся светящийся сок, рассыпавшись на множество капель."
    narrator "Наташа опустила руки и села на колени. "
    narrator "Лианы из центра сада начали меняться — они угасали."
    show natasha regular
    narrator "Девушка казалась настоящим центром смерти."
    hide natasha
    show black_hare regular
    narrator "В голове Аша была пустота. Он наблюдал за тотальным уничтожением растений. "
    hide black_hare
    show onka angry
    narrator "Онка же просто упал на колени, не в силах произнести даже двух слов."
    hide onka
    show natasha smile
    narrator "Наташа шла, улыбаясь, по границе между темными (мертвыми) и светящимися (живыми) голубыми лианами."
    narrator "Словно каждый ее шаг убивал растения."
    hide natasha
    pause 0.2
    scene chip_factory_vines
    narrator "Растения же тихо угасали."
    show natasha smile
    narrator "В навалившейся тьме светились лишь глаза девушки. "
    narrator "Наташа заметила Онку и Аша. И ярко улыбнулась, забыв в порыве радости об их отношениях."
    show natasha smile
    natasha "У меня получилось! Все прекрасно сработало! "
    natasha "Думаю, ролик будет эффектный!"
    hide natasha
    show onka angry
    narrator "Онка молчал. Его глаз задергался. "
    narrator "Он пытался что-то сказать, но губы не слушались."
    hide onka
    show natasha smile
    hide onka
    natasha "Конечно, в качестве триггера на самоубийство, я взяла сильное разрушение. "
    natasha "Оно все и запустило! Это отличная демонстрация моей концепции."
    show onka angry
    hide natasha
    onka "Это было единственное растение, которое смогло жить хоть сколько-то на RDF-13!"
    show onka thinking
    onka "А ты его убила из-за ролика?!"
    narrator "Он схватился за волосы."
    show onka sad
    onka "Это кошмар. Кто допустил Вас до этого помещения?"
    onka "Мне и так постоянно плохо, еще Вы!"
    hide onka
    show natasha sad
    narrator "Уверенность девушки испарилась."
    hide natasha
    show onka angry
    hide natasha
    onka "Я исключаю вас."
    show natasha angry
    hide onka
    natasha "Что? Нет! Вы не можете просто так взять и нарушить правила."
    show onka thinking
    hide natasha
    onka "О! Раз я не могу их нарушить, то, может быть, млечный сок лиан это сделает? "
    show onka danger
    onka "В нем хватит яда на десять Лун. Надеюсь, что-то попало Вам в рот!"
    onka "А если не попало, я помогу!"
    narrator "Аш понял, что дело плохо."
    hide onka
    show black_hare angry_var
    hide onka
    black_hare "Она — не лисы!"
    hide black_hare
    show natasha sad
    narrator "Девушка стояла, как вкопанная."
    hide natasha
    show black_hare angry_var
    hide natasha
    black_hare "Ты не можешь причинить вред конкурсантам на своем же конкурсе."
    hide black_hare
    show onka danger
    narrator "Онка взглянул на Аша."
    hide onka
    show onka thinking
    onka "Могу."
    show onka sad
    onka "Я даже подумать не мог, что у кого-то рука поднимется на такое..."
    show black_hare angry_var
    hide onka
    black_hare "Это же твои собственные правила!"
    black_hare "Как говорится, выбирая игру, ты выбираешь правила."
    hide black_hare
    show onka angry
    narrator "Онка снял цилиндр и понес его в руках, постоянно приглаживая волосы назад."
    hide onka
    show natasha sad
    hide onka
    natasha "Не выгоняйте меня! Это же все было по правилам!"
    natasha "Я спросила у лис, где и что может умереть по цепной реакции..."
    natasha "Сказали..."
    narrator "Ее остановил новый друг."
    hide natasha
    show black_hare regular
    hide natasha
    black_hare "Не нужно. Не продолжай."
    hide black_hare
    show onka sad
    narrator "Быстрым шагом, с потухшими глазами, Онка пробирался сквозь лианы обратно."
    narrator "Аш с Наташей шли за ним."
    hide onka
    show natasha sad
    hide onka
    natasha "Он угрожал мне?"
    show black_hare regular
    hide natasha
    black_hare "Он просто зол."
    show natasha sad
    hide black_hare
    natasha "Спасибо, что заступился. Я ему точно не нравлюсь."
    show black_hare regular
    hide natasha
    black_hare "Нет, дело действительно в лианах, а не в тебе. "
    show black_hare sad_var
    black_hare "Похоже, ими он дорожит больше, чем другими подопечными."
    narrator "Он снова зацепился за растение, но теперь уже не теплая, а холодная жижа стекала по его ноге."
    show black_hare disgust_var
    black_hare "Как же мерзко! Как же мерзко!"
    show natasha regular
    hide black_hare
    natasha "Аккуратней! Там же яд!"
    hide natasha
    show black_hare regular_happy1
    narrator "Аш обрадовался свету, когда вышел из зала."
    hide black_hare
    pause 0.2
    scene chip_factory_corridor1
    show onka angry
    narrator "Онка давал указания лису на счет Макса. "
    hide onka
    show maks fight
    narrator "Тот скользнул презрительным взглядом по девушке. "
    hide maks
    show natasha sad
    narrator "В ее глазах появились слезы, и она потянула Аша прочь от остальных."
    pause
    show natasha smile
    natasha "Тебе нужна одежда!"
    hide natasha
    show black_hare disgust_var
    narrator "Аш был перепачкан."
    show black_hare disgust_var
    black_hare "Я чувствую, как по ноге что-то течет!"
    hide black_hare
    stop music1 fadeout 3
    jump scene_19


label scene_19 :
    pause 0.2
    scene chip_factory_corridor3
    #Аш рассказывает про Макса, Наташа жалеет парня так как проецирует свои отношения с братом на их. Но Ната еще не говорит, что Макс ее брат
    play music2 'music/3333.mp3' fadein 3
    narrator "Ребята разговаривали, двигаясь по коридору."
    show black_hare sad_var
    black_hare "Этот придурок сжег сегодня лис..."
    show black_hare angry_var
    black_hare "Главное, для Онки это — нормально!"
    show natasha regular
    hide black_hare
    natasha "А для лис?"
    show black_hare disgust_var
    hide natasha
    black_hare "Для них, кажется, тоже."
    show natasha sad
    hide black_hare
    natasha "Многое бы отдала за интервью с одним из них для блога..."
    natasha "Только они не особо хотят со мной говорить."
    show black_hare disgust_var
    hide natasha
    black_hare "У них очень закрытое сообщество. "
    black_hare "И далеко не все понравится широкой общественности."
    show black_hare regular_confused
    black_hare "Не могу даже понять, хорошие они или нет..."
    black_hare "А еще, я видел, как Макс на тебя посмотрел. "
    black_hare "Что между вами?"
    show natasha sad
    hide black_hare
    natasha "Похоже, что мы с ним знакомы?"
    show black_hare surprised_var
    hide natasha
    black_hare "Да не особо."
    hide black_hare
    show natasha smile
    narrator "Она засмеялась."
    hide natasha
    show black_hare regular_happy1
    narrator "Аш улыбнулся в ответ."
    hide black_hare
    show natasha smile
    hide black_hare
    natasha "Лучше поспешить сменить твою одежду."
    hide natasha
    narrator "Они шли незнакомыми коридорами. Вокруг никого не было."
    show natasha sad
    natasha "Прости за ненормальное поведение вчера. "
    natasha "И за то, что сорвала твои планы."
    natasha "Насчет обучения ИИ на людях... "
    natasha "Ради Которого ты продал оборудование Фабрики."
    show black_hare regular_happy2
    hide natasha
    black_hare "Я уже забыл."
    show natasha sad
    hide black_hare
    natasha "Просто у меня проблемы. "
    show natasha angry
    natasha "Еще этот Онка, который вечно критикует."
    show black_hare regular_happy1
    hide natasha
    black_hare "Не переживай, это не связано с тем, что твой проект плохой."
    show black_hare regular
    black_hare "Людям тяжело говорить о смерти, о возможности использования средств массового убийства. "
    black_hare "И о том, что это может быть полезно."
    show natasha smile
    hide black_hare
    natasha "Да! Знаешь, как много можно заработать, выключив половину медуз?"
    natasha "Электростанции и очистные сооружения, бассейны — все забивается медузами."
    hide natasha
    show black_hare regular_happy2
    narrator "Она взяла его за руку, и Аш почувствовал, что ему нравится это прикосновение. "
    narrator "В отличие от прикосновений странного Хозяина Фабрики, который вечно пахнет манго."
    hide black_hare
    show natasha regular
    stop music2 fadeout 3
    play music1 'music/ayay1.mp3' fadein 3
    narrator "Проходя мимо одной из дверей, они услышали шорохи. Наташа остановила Аша."
    hide natasha
    show black_hare disgust_var
    hide natasha
    black_hare "Мне нужна новая одежда."
    hide black_hare
    show natasha regular
    narrator "Подруга закрыла ему рот."
    show natasha regular
    natasha "Там кто-то из наших! В смысле — это точно человек!"
    hide natasha
    narrator "Аш замолк, и они заглянули за приоткрытую дверь."
    pause 0.2
    scene chip_factory_room
    narrator "В комнате с имитацией окна на голом полу стояла клетка. "
    show wild_fox regular
    narrator "А в ней сидел лис из третьей касты. "
    hide wild_fox
    show vechna thinking
    narrator "Напротив клетки, на мягком пуфике, сидела Вечна и делала в смешанной реальности заметки, невидимые другим."
    pause 0.2
    scene chip_factory_corridor3
    narrator "От удивления Наташа замерла."
    show natasha regular
    hide vechna
    natasha "Эта выскочка — это же твоя сестра?"
    hide natasha
    show black_hare angry_var
    narrator "Парень посмотрел на Наташу с упреком. В ответ она виновато пожала плечами."
    hide black_hare
    show natasha sad
    hide natasha
    pause 0.2
    scene chip_factory_room
    narrator "В комнате происходили странные вещи."
    show wild_fox regular
    narrator "Сестра обратила внимание на лиса в клетке: тот махал хвостом из стороны в сторону. "
    hide wild_fox
    show vechna smile1
    narrator "Его взгляд не отрывался от сидящей девушки. Он был просто поглощен ею."
    narrator "Ребята увидели, как Вечна достала из-за спины мячик. Обычный фиолетовый мяч. "
    narrator "Такой же она бросила в руки Ашу, приглашая его на сцену."
    narrator "Покрутила игрушкой перед своим лицом."
    hide vechna
    show wild_fox regular
    narrator "Лис высунул язык и часто задышал, но не сдвинулся с места. Зеленоглазая обратилась к нему:"
    hide wild_fox
    show vechna smile2
    hide wild_fox
    vechna "Насколько сильно ты его хочешь? Посчитай от одного до десяти. "
    vechna "Тебе ведь поставили имплант для речи?"
    hide vechna
    show wild_fox crazy
    narrator "Зрачки лиса расширились. Изо рта потекла слюна."
    show wild_fox crazy
    wild_fox "Дддддд! Аааа!"
    hide wild_fox
    show vechna smile1
    narrator "Животные пыталось выдавить из себя хоть что-нибудь, напоминающее человеческую речь."
    narrator "Девушка несколько раз аппетитно помяла мяч в руке. Потом потянула его в рот."
    hide vechna
    show wild_fox crazy
    play sound 'audio/cell.mp3'
    narrator "Лис сорвался с места и так накинулся на прутья клетки, что та качнулась."
    show wild_fox crazy
    wild_fox "Рррр!"
    show vechna thinking
    hide wild_fox
    vechna "Жаль, что речь так скудна... "
    vechna "Скажи, как сильно хочешь его — по шкале от одного до десяти!"
    narrator "В ответ лис зарычал и начал грызть клетку."
    show vechna angry
    vechna "Я же говорила правила: без команды \"встать\" двигаться нельзя."
    hide vechna
    show wild_fox crazy
    play sound 'audio/wild_fox.mp3'
    narrator "Зверь бесился."
    hide wild_fox
    show vechna thinking
    narrator "Вечна смотрела на лиса с досадой."
    show vechna thinking
    vechna "Значит, нужно сделать синоптические связи слабее... "
    vechna "Хмм… В два раза?"
    vechna "Дели или умножай на два: так хоть будет ясно, меняется что-то или нет."
    narrator "Сказала она самой себе. Сестра подошла к клетке и снова аппетитно помяла мячик."
    hide vechna
    show fox angry
    narrator "Из-за ее спины показался Облачный лис. Он неодобрительно посмотрел в клетку."
    hide fox
    show wild_fox crazy
    narrator "Лис громко рычал."
    hide wild_fox
    show vechna angry
    hide wild_fox
    vechna "Долго пришлось тебя ждать."
    show fox angry
    hide vechna
    fox "Пришел, как только смог. И можно на “Вы”?"
    hide fox
    show vechna thinking
    narrator "Девушка сделала недовольное лицо. "
    play sound 'audio/cell2.mp3'
    hide vechna
    show wild_fox crazy
    narrator "Внутри клетки бесновался лис."
    show wild_fox crazy
    wild_fox "Ддддд! Ppppp!"
    show vechna thinking
    hide wild_fox
    vechna "Можно научить его говорить лучше?"
    show fox shock
    hide vechna
    fox "На это нужна хотя бы неделя. "
    show fox angry
    fox "Мы не можем поставить ему более развитый неокортекс, как, например, у меня или у Высших. "
    fox "Только имплант для речи."
    show vechna sad
    hide fox
    vechna "Печаль..."
    show fox angry
    hide vechna
    fox "Но совершенно очевидно, что желание играть с мячом у него ненормально сильное..."
    hide fox
    show vechna thinking
    narrator "Вечна повернулась в сторону лиса в клетке и снова показала ему мяч. "
    hide vechna
    show wild_fox regular
    narrator "Тот замер, сел на пол, как это было еще минуту назад."
    hide wild_fox
    show vechna smile2
    hide wild_fox
    vechna "Слушаешься? "
    hide vechna
    show wild_fox regular
    narrator "Животное замолкло."
    hide wild_fox
    show vechna thinking
    hide wild_fox
    vechna "Не дам мяч. Он мой."
    hide vechna
    show wild_fox crazy
    narrator "Она даже не успела закончить слова, как лис бросился на прутья."
    play sound 'audio/cell.mp3' 
    narrator "Клетка покачнулась. Он пытался пролезть сквозь решетку."
    narrator " "
    narrator "А затем... стал грызть свою лапу."
    hide wild_fox
    show vechna thinking
    narrator "Девушка наблюдала минуту, скептически глядя на зверя."
    narrator "А затем сделала заметки, проговаривая вслух:"
    show vechna thinking
    vechna "Образец №7 демонстрирует сильную психологическую зависимость. "
    vechna "Надо изучить данные более подробно."
    vechna "Важно! Нужно собрать информацию, чтобы такое больше не повторялось. "
    vechna "А чтобы изучить, требуется повторить."
    show vechna angry
    vechna "Что же делать?"
    show fox angry
    hide vechna
    fox "Не знаю. Но, по приказу нашего Хозяина, мы выполним любые Ваши указания."
    narrator "Тихо произнес Облачный."
    hide fox
    show vechna thinking
    hide fox
    vechna "Пойду разбираться. Он меня пугает."
    show fox angry
    hide vechna
    fox "Можно его забрать?"
    show vechna thinking
    hide fox
    vechna "Да, конечно. К сожалению, с ним не вышло."
    vechna "Мне нужен подопытный с навыками речи."
    narrator "Она на секунду остановилась."
    vechna "Будешь следующим?"
    hide vechna
    show fox shock
    hide vechna
    fox "!"
    pause 0.2
    scene chip_factory_corridor3
    narrator "Из помещения доносились грызущие, чавкающие звуки."
    show natasha sad
    narrator "Наташа с сочувствием посмотрела на Аша и потянула его скорее прочь."
    show natasha sad
    natasha "Что за жесть!"
    show black_hare sad_var
    hide natasha
    black_hare "Это был лис из Второй или Третьей касты, не говорящий..."
    call surprised_disgust
    show black_hare mood
    show black_hare mood
    black_hare "Пока Вечна не попросила."
    narrator "Аш молчал. Из-за двери еще слышались поскуливания. "
    narrator "Он вспоминал, как в детстве сестра спасла его и кроликов во время аварии."
    show black_hare sad_var
    pause
    narrator "Парень задумался. "
    narrator "Что же она тогда делала: спасала животных или убивала людей, которые могли бы занять их место?"
    narrator "Девушка всегда готова кем-то жертвовать. "
    narrator "Тогда — жизнью людей ради него и кроликов."
    narrator "А сейчас — жизнью лис. Но ради чего?"
    narrator "Он решил, что главное — быть для сестры важнее, чем все эти открытия и сеть."
    narrator "Они шли по коридору. Яд на одежде парня высох."
    hide black_hare
    show natasha sad
    hide black_hare
    natasha "Я знаю, каково это, когда твои близкие отдаляются. "
    natasha "С моим братом — похожая история."
    show black_hare sad_var
    hide natasha
    black_hare "Сочувствую. Но у меня все не так плохо. "
    black_hare "Я для нее важнее всего."
    narrator "Наташа обняла его."
    show natasha sad
    hide black_hare
    natasha "Я тоже очень на это надеюсь."
    natasha "Но думаю... "
    natasha "Что о сумасшедшем лисе никто не позаботится..."
    hide natasha
    stop music1 fadeout 3
    jump scene_20


label scene_20:
    pause 0.2
    scene chip_factory_audience
    #Аш видит изменения Вечны, и чувствует свою вину - не нужно было давать ей код. Наташа его поддерживает (может за руку берет), а он поддерживает ее - Онка сливает девушку за несоответствие теме конкурса. Аш побеждает, но отдает победу Вечне. Предварительно спрашивая, позволяют ли это правила.
    play music2 'music/newman_v4.mp3' fadein 3
    narrator "Последний день на конкурсе."
    pause
    show black_hare sad_var
    black_hare "Можно?"
    show vechna thinking
    hide black_hare
    vechna "Почему ты спрашиваешь о таком?"
    show black_hare sad_var
    hide vechna
    black_hare "Надеюсь, что на остальные вопросы ты будешь отвечать охотнее."
    narrator "От вчерашних воспоминаний на душе скребли кошки. \"Бедные лисы\", — подумал он про себя."
    show black_hare angry_var
    black_hare "Всех лис \"починила\"?"
    show vechna thinking
    hide black_hare
    vechna "Ты это о чем?"
    narrator "Аш вспомнил, что вчера он лишь подсматривал, но в комнате с Вечной не находился."
    vechna "Ты слишком часто психуешь. Даже шутить об этом не хочется."
    show black_hare sad_var
    hide vechna
    black_hare "Хотел узнать, сколько лис ушло в утиль."
    hide black_hare
    show vechna smile2
    narrator "Вечна пожала плечами, потом задумалась."
    show vechna smile2
    vechna "Двадцать три лисы, пока я не поняла, в чем проблема."
    show vechna smile1
    vechna "Ты был прав, — мне повезло не спалить свой мозг!"
    hide vechna
    show black_hare sad_var
    narrator "В глубине души Аш был уверен, что Вечна вправит мозги всем лисам. "
    hide black_hare
    show vechna smile1
    narrator "Сестра продолжала говорить."
    show vechna smile1
    vechna "Я достигла прогресса в изменении мозга. "
    show vechna smile2
    vechna "Теперь можно менять в нем все, что хочешь."
    show vechna thinking
    vechna "Естественно, как всегда, самое долгое — это обучение. "
    vechna "Найти именно те связи, которые нужно усилить."
    vechna "Но кое-что вышло. "
    show vechna smile2
    vechna "И все — благодаря тебе!"
    show black_hare disgust_var
    hide vechna
    black_hare "Класс, я очень горжусь, что лисы свихнулись благодаря мне. "
    show black_hare regular_annoyed
    black_hare "И ты тоже свихнулась."
    show vechna smile2
    hide black_hare
    vechna "Я?"
    show black_hare angry_var
    hide vechna
    black_hare "Еще недавно ты бы никогда так не поступила с животными. "
    black_hare "Если бы не твоя радость от выполнения задач, достигнутая за счет нейрохакинга."
    show vechna thinking
    hide black_hare
    vechna "С Облачным все прошло ок."
    narrator "Девушка задумалась и пожала плечами."
    show vechna angry
    vechna "Может, я, наконец, именно та, кем и хотела быть? "
    vechna "А может, я такой и была?"
    hide vechna
    show black_hare regular
    narrator "Аш хотел что-то сказать, но девушка дала знак молчать."
    narrator "Её отвлек звук шагов. Это Онка поднялся на сцену."
    hide black_hare
    show onka angry
    hide black_hare
    onka "Сегодня мы выслушаем итоговые презентации, и я выберу победителя."
    show onka confused
    onka "Конечно, не сразу. После выступлений лисы разберут ваши данные по проектам."
    hide onka
    show natasha smile
    narrator "Наташа поднялась с места. Она лучезарно улыбнулась Онке."
    hide natasha
    show black_hare regular
    narrator "Аш сочувственно подумал: \"Думаю, это тебе уже не поможет\". "
    show black_hare surprised_var
    narrator "Его мысли сразу же перескочили на собственный проект: готов ли он сам к тому, чтобы участники видели его эмоции? "
    narrator "Почему он об этом волнуется? Да потому, что пусть он и не сблизится с сестрой, но хотя бы продвинется по работе."
    hide black_hare
    show natasha smile
    hide black_hare
    natasha "Вы не против, если я начну?"
    show onka sneaky
    hide natasha
    onka "Разве Вас кто-то сможет остановить?"
    hide onka
    show natasha regular
    narrator "Наташа проигнорировала сарказм Онки. "
    narrator "Что еще она могла сделать? Девушка поднялась на сцену."
    show natasha smile
    natasha "Прошу всех подключиться к сети. Я начну трансляцию презентации в смешанной реальности."
    narrator "Перед аудиторией появилось окно с презентацией. "
    narrator "В самом конце, она открыла видео. "
    hide natasha
    show black_hare surprised_var
    narrator "Аш замотал головой: \"Надеюсь ты не покажешь Онке, как убила его лианы, выживающие даже на астероидах?\". "
    hide black_hare
    show natasha smile
    narrator "Но у нее хватило ума так не делать."
    show natasha smile
    natasha "Внутри Фабрики я еще раз протестировала распространение вируса, но не для животных, а для ландышей. "
    show natasha regular
    natasha "Триггером запуска цепной реакции, назовем это самоуничтожением, являлся холод."
    show natasha smile
    natasha "Пришлось напечатать базовый прототип моего вируса за ночь, но я успела!"
    narrator "Девушка указала рукой на невидимую для нечипированных презентацию, в которой открылось видео. "
    hide natasha
    show onka thinking
    narrator "Онка молчал, вертя в пальцах крупную засахаренную саранчу, которую взял из вазы со снеками."
    show onka thinking
    onka "Сама концепция биологического оружия противоречит нашим ценностям открытия и создания новых возможностей для жизни."
    show natasha angry
    hide onka
    natasha "Я не веду речи о полном истреблении. Речь о регуляции численности."
    hide natasha
    show onka angry
    play sound 'audio/crunch.mp3'
    narrator "Хозяин Фабрики положил в рот хрустящее насекомое."
    hide onka
    show natasha regular
    narrator "Девушка твердо смотрела перед собой. Аш чувствовал себя неловко, он боялся, что подруга заплачет."
    hide natasha
    show onka sneaky
    hide natasha
    onka "Спасибо за выход. Не обижайтесь, конкурс субъективный. "
    narrator "К Илли снова вернулся интерес."
    show onka smile
    onka "Кто выступает следующим?"
    hide onka
    show natasha sad
    narrator "Наташа в расстроенных чувствах спустилась со сцены. Аш ждал у лестницы."
    hide natasha
    show black_hare surprised_var
    hide natasha
    black_hare "Меня тоже недавно Онка слил."
    show natasha sad
    hide black_hare
    natasha "Все из-за вчерашнего..."
    narrator "На глазах Наташи наворачивались слезы."
    natasha "Хотя бы в одной сфере жизни было так, как хочется! "
    show natasha angry
    natasha "И я все транслировала в сеть! Вот позор!"
    show black_hare surprised_var
    hide natasha
    black_hare "Ничего страшного нет, даже если это кто-то и увидит."
    show black_hare regular_happy1
    black_hare "Наоборот, больше шансов найти инвестора. "
    black_hare "Глядишь, какой-нибудь Онка-ненавистник решит дать тебе денег, чтобы насолить ему."
    hide black_hare
    show natasha angry
    narrator "Наташа подняла глаза на сцену. Там стояла Вечна."
    hide natasha
    show black_hare regular
    narrator "Аш не отрывал взгляд от сестры. Подруга это заметила."
    hide black_hare
    show natasha angry
    hide black_hare
    natasha "Останься с сестрой, мне нужно побыть одной."
    show natasha sad
    narrator "На глаза девушки опять навернулись слезы, она старалась глубоко дышать. "
    hide natasha
    show black_hare regular
    narrator "Только Аш не обращал на нее внимания."
    hide black_hare
    show vechna smile2
    narrator "Вечна стояла на сцене в сопровождении Облачного лиса."
    show vechna smile2
    vechna "Рада вас приветствовать!"
    narrator "Перед глазами конкурсантов появился полупрозрачный слой с презентацией. Оратор стояла прямо перед ним."
    vechna "На снимках можно видеть активность мозга при любви к фиолетовым мячам."
    narrator "Показывает новый кадр."
    vechna "Перед вами — мозг моего ассистента-лиса."
    show fox angry
    hide fox
    vechna "Если кратко, то за одну ночь я смогла научить мозг лиса любить неодушевленный предмет до дрожи. "
    vechna "Очень сильно любить. "
    vechna "Конечно, есть данные \"до\" и \"после\"."
    vechna "Они хранятся в открытом доступе..."
    vechna "...поэтому вы можете ознакомиться с уровнем активности мозга до нейрохакинга и после него."
    vechna "Перспективы применения данной разработки огромные, вплоть до изменения психики. "
    show vechna thinking
    vechna "Конечно, первые применения спорных технологий, — это всегда медицина."
    narrator "Она обратилась к Илли."
    vechna "Исследование монетизации и рынка для подобных инноваций требует больше времени, чем было доступно."
    show vechna smile2
    vechna "Но я верю, что сфера применения нейрохакинга огромна, и это может действительно изменить мир."
    hide vechna
    show onka victory
    narrator "Онка аплодировал стоя."
    hide onka
    pause
    show black_hare sad_var
    narrator "С момента ухода Наташи Аш смотрел лишь в одну точку на сцене и думал про свою сестру. "
    narrator "Краем глаза он заметил, что Вечна движется к выходу, и пошел за ней. "
    hide black_hare
    show fox angry
    narrator "Его под руку поймал Облачный."
    show fox angry
    fox "Ай, ай, ай! Сейчас Ваш выход, молодой человек!"
    show black_hare surprised_var
    hide fox
    black_hare "Я пропускаю вперед кого-нибудь."
    show fox angry
    hide black_hare
    fox "Вы же последний! Как всегда!"
    narrator "С этими словами он взял его зубами за рукав и повел за собой."
    hide fox
    show black_hare disgust_var
    hide fox
    black_hare "А как же манеры?"
    narrator "Лис выпустил рукав из пасти."
    show fox angry
    hide black_hare
    fox "Что Вы знаете о нашей культуре?"
    hide fox
    show black_hare sad_var
    narrator "Парень вздохнул и попробовал собраться с мыслями."
    hide black_hare
    pause 0.2
    scene chip_factory_room
    show wild_fox crazy
    narrator "Перед глазами был только лис в клетке."
    pause 0.2
    scene chip_factory_audience
    narrator "Из головы не выходил безумный взгляд животного. Что она с ним сделала?"
    show black_hare regular
    hide wild_fox
    black_hare "После таких открытий, как у Наташи или Вечны, моя работа не выглядит такой революционной."
    black_hare "Конечно, можно найти полезное применение нейрохакингу, но я хочу разобраться с проблемами наших чувств. "
    black_hare "За эту ночь я смог немного обучить ИИ распознавать удивление и отвращение."
    black_hare "Кроме этого, внедрил автогенерацию дизайна: с помощью сторонней программы Уши ищут изображения, которые максимально ассоциируются с эмоцией и выводят их на себя."
    black_hare "Технически они представляют собой интерфейс, подключенный к чипу, находящемуся в голове. Дисплеи — сами Уши."
    black_hare "Из-за автогенерации изображений, Уши сами, без моего участия, создают визуальный язык."
    hide black_hare
    show onka confused
    narrator "Илли слушал не отрываясь."
    show onka confused
    onka "Ваша теория заключается в том, что одни люди, наблюдая эмоции других людей, будут менять свое отношение к ним?"
    show black_hare regular
    hide onka
    black_hare "Да, это позволит человеку быть более открытым с самим собой и с другими людьми. "
    black_hare "Часто мы сами не хотим признаваться себе в собственных чувствах."
    show onka sneaky
    hide black_hare
    onka "Если все будут видеть мои эмоции, это приведет к серьезному изменению образа жизни. "
    onka "Я тогда с Фабрики носа не покажу."
    show black_hare angry_var
    hide onka
    black_hare "Это изменение культуры. "
    black_hare "Как мы знаем, минимальный шаг значимых культурных изменений — одно поколение."
    show fox angry
    hide black_hare
    fox "Почему именно Уши зайца? Не лис... Не кошачьи, например?"
    show black_hare angry_var
    hide fox
    black_hare "Это решение необоснованно технически. "
    black_hare "Можно сделать дисплеи в форме разных Ушей. Дело вкуса."
    hide black_hare
    show fox smile
    narrator "Скрестив руки на груди и чувствуя себя неимоверно важным, Облачный внимательно выслушал ответ..."
    narrator "...и утвердительно покачал головой, говоря самому себе, что так он и думал."
    hide fox
    show onka sneaky
    hide fox
    onka "И значит, у Вас есть патент на софт?"
    show black_hare angry_var
    hide onka
    black_hare "Да, я дал его в безвозмездное пользование сестре."
    black_hare "Думаю, Вы и так все уже знаете."
    hide black_hare
    show onka regular
    narrator "Онка повернулся к другим участникам."
    show onka smile
    onka "Через два часа отдел контроля проверит данные ваших проектов и сообщит результаты. "
    onka "Победитель сможет присоединиться к любой исследовательской группе на Фабрике. "
    hide onka
    show black_hare surprised_var
    narrator "Через пару часов все были поражены тем, что выиграл Аш. "
    hide black_hare
    pause
    show vechna sad
    narrator "Второе место принадлежало Вечне. "
    show vechna angry
    narrator "От досады она рвала на голове волосы."
    hide vechna
    show black_hare regular_happy1
    hide vechna
    black_hare "Я отказываюсь от победы. И я прочел правила — так можно."
    show onka sneaky
    hide black_hare
    onka "Ожидаемо... Но не расстраивайся!"
    onka "Занявший второе место получит утешительный приз — ужин с самым выдающимся инноватором нашего поколения – ..."
    show black_hare angry_var
    hide onka
    black_hare "...Со мной."
    narrator "Договорил за него Аш и закатил глаза."
    hide black_hare
    show vechna smile1
    narrator "Вечна сидела, не шевелясь, красная, как помидор, от приливающей к лицу крови."
    show vechna smile1
    vechna "Я победила! Задача выполнена!"
    hide vechna
    narrator "Проигравшие не смотрели на нее с завистью: все они с непониманием провожали взглядом парня в черной мантии до колен."
    stop music2 fadeout 3
    jump scene_21


label scene_21:
    pause 0.2
    scene home
    #Девушка продолжает нейрохакинг. Аш отговаривает его, напоминая, сколько лис она убила ради этого на конкурсе...
    play music1 'music/newman_stars.mp3' fadein 3
    narrator "Прошел месяц."
    pause
    show black_hare regular
    #(Черный экран. Появляется кнопка с текстом.)
    show black_hare regular
    black_hare "Соединить с Вечной."
    hide black_hare
    pause 0.2
    scene planet
    narrator "Мир вокруг изменился."
    show black_hare surprised_var
    narrator "Парень стоял на планете, чувствуя резкий запах кислот. Они обжигали легкие. "
    play sound 'audio/grom.mp3'
    narrator "Звучали свист и раскаты грома. "
    narrator "Руку резко прибило к земле. Аш понял — что-то падает с неба."
    narrator "\"Кристаллы\", — мелькнуло в голове. И снова боль пробила руку."
    narrator "Оглядевшись, он начал двигаться в сторону невысокой пещеры."
    narrator "Дойдя до нее, Аш попробовал вытащить один из кристаллов."
    narrator "Никак не получалось нащупать его конец, чтобы подцепить и вытащить из руки."
    narrator "На глаза ему попались рубины, лежащие у входа в укрытие, они были сантиметров пять в длину и острые, как иглы."
    show black_hare regular_fear
    black_hare "Ааа, я такие длинные не вытащу!"
    narrator "Из-под рубинов, застрявших в руке, стали выделяться капли крови."
    show black_hare disgust_var
    black_hare "Что за жесть! "
    narrator "\"Красиво\", — успел подумать парень, пока рука не онемела. Ему казалось, что пробиты даже кости."
    narrator "Вытащить из себя пятигранные кристаллы казалось невозможным. "
    show black_hare angry_var
    black_hare "Вечна! Фак! Выключи это все нафиг!"
    narrator "Но никто не ответил."
    black_hare "Все, я тогда пас! Выйти из сети."
    voice_cartoon "Пожалуйста, закончите симуляцию."
    show black_hare surprised_var
    hide voice_cartoon
    black_hare "Что?"
    voice_cartoon "Вход в симуляцию подразумевает подписание пользовательского соглашения."
    play sound 'audio/notification1.mp3'
    narrator "Перед Ашем появилось соглашение."
    show black_hare angry_var
    hide voice_cartoon
    black_hare "Так не пойдет. Я присоединился не к симуляции, а к пользователю."
    voice_cartoon "Для минимизации получения нежелательного опыта в сети рекомендуется перед переходом ознакомиться с локацией."
    narrator "Аш злился на себя за то, что всегда пропускал этот шаг, настроив мгновенный переход после одобрения запроса."
    hide voice_cartoon
    black_hare "Ладно, как закончить игру?"
    play sound 'audio/notification1.mp3'
    narrator "Перед ним высветились правила."
    narrator "\"Наблюдай за Нихалом и найди новое открытие — свое серендипити\"."
    call surprised_disgust
    show black_hare mood
    show black_hare mood
    black_hare "О, то, что нужно для человека с раздробленной рукой! "
    black_hare "Самое оно, мать вашу."
    narrator "Рука заныла."
    show black_hare surprised_var
    black_hare "А если я умру?"
    voice_cartoon "Симуляция закончится."
    hide voice_cartoon
    black_hare "Выбор очевиден. Кристаллы еще сыплются с неба?"
    narrator "Он посмотрел на небо — дождь из рубинов закончился."
    show black_hare angry_var
    black_hare "И как мне выпилиться?"
    show black_hare regular
    narrator "Спустя десять минут он сидел в позе лотоса у входа в пещеру и глубоко дышал, наблюдая за ландшафтом."
    hide black_hare
    show vechna smile2
    narrator "Появилась Вечна."
    show vechna smile2
    vechna "Прости, я только-только включила уведомления. Не знала, что ты тут."
    show black_hare angry_var
    hide vechna
    black_hare "Я тут такой боли натерпелся!"
    narrator "Он хотел выругаться, что из симуляции просто так не выйти, но вспомнил, что, будь он сам внимательнее, мог бы этого избежать."
    narrator "Она бы точно на это указала."
    hide black_hare
    show vechna smile1
    hide black_hare
    vechna "Прости! Планета с атмосферой из синильной кислоты и дождями из драгоценных камней..."
    vechna "...может показаться неприветливой в первое время."
    show black_hare disgust_var
    hide vechna
    black_hare "То-то я чувствую, что легких уже нет. Почему я жив?"
    show vechna smile1
    hide black_hare
    vechna "Если я все буду включать на полную катушку, то не продержусь тут и пары минут. "
    vechna "Поэтому, обычно, то, что разрабатываю сейчас, — включаю полностью, а остальные внешние факторы — приглушаю."
    show black_hare surprised_var
    hide vechna
    black_hare "Что за фишка с серендипити?"
    show vechna smile1
    hide black_hare
    vechna "Ааа, ну это мое упражнение, перед выходом из симуляции."
    vechna "Я наблюдаю за миром вокруг и записываю какое-то потенциальное открытие."
    vechna "Я понимаю под серендипити глубокий вывод из случайных наблюдений."
    hide vechna
    show black_hare regular
    narrator "Девушка сделала несколько манипуляций рукой, и Аш облегченно вздохнул. "
    narrator "Боль пропала, но чувствовался холод рубинов, когда дотрагиваешься пальцами."
    hide black_hare
    show vechna thinking
    hide black_hare
    vechna "У тебя какое-то дело? А то у меня..."
    show black_hare sad_var
    hide vechna
    black_hare "...Еще столько задач незакрытых есть."
    show vechna thinking
    hide black_hare
    vechna "Именно."
    show black_hare regular_fear
    hide vechna
    black_hare "Ты что, все это сейчас на себе тестишь?"
    show black_hare surprised_var
    black_hare "Почему не на модели? Ты вон вся какая драная."
    show vechna angry
    hide black_hare
    vechna "Сам ты \"драная\"! Я подвожу итоги."
    show vechna thinking
    vechna "Когда поставлена задача — сделать дожди, как на других планетах..."
    vechna "...то удар камня по голове может обрадовать тебя больше, чем рождество!"
    show black_hare disgust_var
    hide vechna
    black_hare "Это нездорОво и не ЗдОрово."
    show vechna thinking
    hide black_hare
    vechna "Я делаю великие вещи."
    hide vechna
    show black_hare regular_confused
    narrator "Аш пристально на нее посмотрел. Одна рука девушки была выбита из плеча. На теле виднелись ожоги."
    show vechna angry
    hide black_hare
    vechna "Это не вредит мне!"
    show black_hare angry_var
    hide vechna
    black_hare "А не вредит ли? Пусть тело это не проживает, но зато проживает мозг."
    hide black_hare
    show vechna thinking
    narrator "Девушка была недовольна непредвиденным конфликтом на пустом месте."
    show vechna thinking
    vechna "Для меня это просто инструмент, понимаешь? "
    vechna "Может быть, странный, но это новая культура. "
    vechna "Хоть умри, с этим уже ничего не сделаешь. "
    vechna "Оглянись, мы на другой планете. "
    vechna "Где люди даже жить не могут. "
    show vechna angry
    vechna "Остальное — е-рун-да. Я бы за это сотни раз умирала без притупления чувств."
    hide vechna
    play sound 'audio/grom.mp3'
    narrator "С неба снова сыпались кристаллы."
    narrator "Сестра показала рукой на выход из пещеры. "
    narrator "Над дождем из кристаллов садилась звезда — местное Солнце."
    narrator "Сквозь минералы преломлялись лучи, на секунду зажигая камни яркими вспышками."
    narrator "Словно блестящие звезды падают с неба."
    narrator "В такие моменты все кажется неважным, никчемным, в сравнении с вселенной и её чудесами. И грусть отпускает."
    show black_hare sad_var
    narrator "А позже, от осознания этой никчемности, становится еще хуже."
    show black_hare sad_var
    black_hare "Ты делаешь великие вещи."
    black_hare "Но ты постоянно лежишь, подключившись к Фабрике, работаешь по семнадцать часов."
    show vechna thinking
    hide black_hare
    vechna "Ты сюда подключился просто так? На мозг мне капать?"
    show black_hare sad_var
    hide vechna
    black_hare "Пообщаться, узнать как дела."
    show vechna thinking
    hide black_hare
    vechna "Отлично дела! Были!"
    vechna "Я работаю в месте своей мечты. "
    vechna "Мне теперь платят за моделирование других планет. "
    vechna "Счастливое везение, что Онка просто помешан на космосе."
    show vechna angry
    vechna "И, опережая твои комментарии, я очень благодарна, что ты отдал мне победу!"
    show vechna sad
    vechna "Пойми, у меня правда загруженный период. Потом будет проще."
    vechna "Я использую нейрохакинг. И буду успевать то же, что и сейчас, часов за тринадцать-четырнадцать."
    show black_hare sad_var
    hide vechna
    black_hare "Только не говори, что подключишь себя к системе жизнеобеспечения."
    show black_hare angry_var
    black_hare "Тогда и на зрение ресурсы мозга не тратятся, и легкие от аппарата смогут работать!"
    hide black_hare
    show vechna smile2
    narrator "Вечна засмеялась."
    show vechna smile2
    vechna "Я хочу повысить производительность мозга, убрать какую-нибудь внешнюю информацию, которую ему требуется обрабатывать. "
    show vechna thinking
    vechna "Я не отключу свои легкие."
    show black_hare regular_confused
    hide vechna
    black_hare "Если честно, звучит плохо."
    show vechna thinking
    hide black_hare
    vechna "Ты доверяешь мне?"
    show black_hare sad_var
    hide vechna
    black_hare "Опять этот вопрос..."
    hide black_hare
    stop music1 fadeout 3
    jump scene_22


label scene_22:
    pause 0.2
    scene lake
    #Он приглашает к ней знакомого лиса, для скандального интервью, лис просит анонимности, чтоб ему не влетело
    play music2 'music/noname.mp3' fadein 3
    narrator "Друзья сидели на берегу реки для переработки мусора. "
    narrator "Возле самой красивой свалки в мире. "
    narrator "Зеркальная масса наноботов отражала в себе цветную подсветку с потолка."
    show black_hare regular_happy1
    narrator "Аш что-то читал вслух Наташе. "
    hide black_hare
    show natasha regular
    narrator "Она слушала невнимательно и всем своим видом показывала, как ей скучно."
    hide natasha
    show black_hare regular_happy1
    hide natasha
    black_hare "Ты должна разбираться не только в микробиологии, но и в других смежных дисциплинах, быть в тренде."
    narrator "Они сидели на застеленном пледом полу, где были разложены печенье в чашечки. "
    narrator "У них был настоящий пикник. "
    show black_hare regular_happy2
    black_hare "Нельзя так долго грустить из-за проекта. "
    black_hare "Ты все равно хорошо шаришь в микробиологии. "
    black_hare "Чем занимаются у тебя в семье?"
    show natasha angry
    hide black_hare
    natasha "Что ты все время спрашиваешь про семью?"
    natasha "Я думала, что воспитанных обществом это не интересует."
    show black_hare regular_happy2
    hide natasha
    black_hare "У меня есть семья, просто в ней не было родителей. "
    black_hare "И я вижу, что моя психика вышла более устойчивой."
    show natasha angry
    hide black_hare
    natasha "Ну да, ищешь, с кем бы пообщаться, пока твоя сестра пожинает плоды победы, обрабатывая данные Онки в режиме 24/7."
    show black_hare sad_var
    hide natasha
    black_hare "Только 17/7."
    black_hare "И это было очень грубо."
    show natasha sad
    hide black_hare
    natasha "Да. Прости. "
    natasha "Просто я со своей традиционной семьей общаюсь еще хуже."
    narrator "Она поджала под себя колени, длинные волосы свесились цветными волнами на лицо."
    hide natasha
    show black_hare regular_happy1
    hide natasha
    black_hare "Тебе все равно нужно решить, чем ты хочешь заниматься. "
    black_hare "Какие у тебя баллы на учебе?"
    show natasha sad
    hide black_hare
    natasha "Мы с тобой познакомились на конкурсе для ботанов. Догадайся."
    show black_hare regular_confused
    hide natasha
    black_hare "Что тебе еще интересно?"
    show natasha sad
    hide black_hare
    natasha "Вот новость для тебя:"
    show natasha angry
    natasha "Я учусь, как и большинство, не потому, что хочу собирать звезды, а чтобы выдержать всю эту бешеную конкуренцию! "
    show natasha sad
    natasha "Иногда кажется, эта гонка словно... "
    natasha "Словно, чем сложнее тебе двигаться, тем быстрее приходится это делать, чтобы не выбыть из игры. "
    show natasha angry
    natasha "Безумие, но даже дело моей жизни пришло не изнутри, а извне."
    natasha "Сказали: \"Наташ, факультет оки-доки\". А мне ни оки это и ни доки."
    natasha "Я не знаю, чем мне заниматься. "
    show natasha sad
    natasha "Где, блин, моя кьюти-марка??? Я хочу быть пони..."
    narrator "Наташа схватилась за голову."
    hide natasha
    show black_hare regular_happy1
    hide natasha
    black_hare "У тебя есть блог. Кажется, тебе реально интересно им заниматься."
    show natasha sad
    hide black_hare
    natasha "Интересно. Но это же не так круто, как наука."
    narrator "Она мило вытерла носик."
    hide natasha
    show black_hare regular_happy1
    hide natasha
    black_hare "У тебя действительно проблема с чужим мнением."
    black_hare "Есть сюрприз: сейчас придет лис — он готов рассказать про самые внутренности Фабрики! "
    black_hare "Но без видео, анонимно."
    hide black_hare
    show natasha smile
    narrator "Наташа сложила руки перед лицом, словно сейчас прочитает Ашу молитву. "
    narrator "Девушка подползла к нему на коленях, и по ее взгляду было не понятно, заплачет она сейчас или упадет в обморок."
    hide black_hare
    show natasha smile
    natasha "Спасибо! Я не верю, что кто-то что-то сделал для меня!"
    hide natasha
    show fox angry
    narrator "За их спиной кто-то прочистил горло со всей возможной важностью."
    show fox angry
    fox "Кхм-кхм… Простите, я не знал, что у вас время молитвы. "
    show fox smile
    fox "Какую религию вы исповедуете?"
    hide fox
    show black_hare regular_happy2
    narrator "Аш засмеялся и подал Нате руку."
    hide black_hare
    show natasha angry
    hide black_hare
    natasha "Мы не молимся! Это жуткая глупость."
    hide natasha
    show fox angry
    hide natasha
    fox "Неверное, нахальное утверждение!"
    fox "Это полезно для нервов."
    hide fox
    show natasha smile
    narrator "Наташа жестом пригласила Облачного сесть рядом. "
    narrator "Она уже не выглядела вялой и апатичной. "
    narrator "Громко хлопнула в ладоши. От неожиданности ее друг вздрогнул. "
    hide natasha
    show black_hare regular_fear
    narrator "Аш вспомнил, что сестра всегда хлопала в ладоши, когда радовалась."
    hide black_hare
    show fox angry
    hide black_hare
    fox "Можем поскорее начать?"
    show natasha smile
    hide fox
    natasha "Конечно. Только мне нужно придумать вопросы. "
    show natasha angry
    natasha "Буду импровизировать."
    narrator "Про себя она ругала Аша, которого больше волновал \"вау\" эффект сюрприза, чем ее подготовка к интервью."
    hide natasha
    show fox angry
    hide natasha
    fox "Заранее оговариваю: никто не должен знать источник. "
    fox "Я возвращаю старый долг."
    show black_hare regular_happy2
    hide fox
    black_hare "Лис имеет в виду, что съел входной жетон на конкурс, а я не стал жаловаться и подождал, когда он из него выйдет."
    narrator "Лис смешался и поправил воротник."
    hide black_hare
    show fox angry
    hide black_hare
    fox "\"Выйдет\", — это очень грубо звучит, можно подумать..."
    show black_hare disgust_var
    hide fox
    black_hare "Тут ничего эстетичного все равно не подумаешь."
    hide black_hare
    show natasha angry
    narrator "Наташа заметила, что гость чувствует себя некомфортно."
    show natasha smile
    natasha "Мы очень признательны, что Вы тут."
    natasha "Скажите, Вы — разумный лис, потому что имеете имплант неокортекса? "
    natasha "Как ваше имя?"
    narrator "Девушка попыталась опустить ноги в массу нанороботов, но Аш успел привлечь ее внимание. "
    narrator "Наташа очень не хотела бы остаться без ногтей. Мертвые ткани наноботы расщепляют быстро."
    hide natasha
    show fox angry
    hide natasha
    fox "Я предпочитаю скрыть свое имя."
    narrator "Сердито ответил лис."
    show fox smile
    fox "Щенками мы проходим процедуру имплантации."
    show natasha smile
    hide fox
    natasha "Вы знаете, как работает имплант?"
    show fox shock
    hide natasha
    fox "Не знаю. Если б я был распределен в касту Высших, может знал бы."
    show natasha smile
    hide fox
    natasha "Как вы говорите?"
    show fox angry
    hide natasha
    fox "С помощью имплантов. "
    fox "После установки неокортекса, Высшие и Низшие получают возможность говорить."
    hide fox
    show black_hare regular
    narrator "Аш все это знал, поэтому сидел молча и старался не мешать."
    hide black_hare
    show natasha smile
    hide black_hare
    natasha "Можно ли сменить касту?"
    show fox angry
    hide natasha
    fox "Очень редко лисы могут переходить между кастами."
    narrator "Лис выглядел очень гордым собой."
    show natasha smile
    hide fox
    natasha "Вы говорите о себе?"
    show fox angry
    hide natasha
    fox "Стараюсь, очень стараюсь."
    narrator "Наташа отправила в реку помятое печенье, и зеркальные капли попали на воротник лиса."
    show fox shock
    fox "Аккуратнее! Никто не должен знать, что я тут был!"
    show fox angry
    fox "Это Вам не кожа, а фабричная ткань! Ее разъест!"
    narrator "Лис судорожно счищал капли наноботов с воротника, но в некоторых местах всё же остались маленькие дырочки."
    narrator "Наташа кивнула головой на реку."
    hide natasha
    show natasha smile
    hide fox
    natasha "Наноботы Онки тоже имеют касты?"
    show fox angry
    hide natasha
    fox "Что за глупость?"
    narrator "В ответ она пожала плечами."
    show natasha regular
    hide fox
    natasha "Значит, Вы правда молитесь? "
    show fox angry
    hide natasha
    fox "Да, мы молимся, нас так воспитала Фабрика. "
    show natasha regular
    hide fox
    natasha "Почему одни лисы ходят на задних лапах, а другие — нет?"
    show fox smile
    hide natasha
    fox "Часто Высшие лисы могут ходить на задних лапах. "
    show fox angry
    fox "Но это — не ограничение, а привычка. Поэтому Низшие тоже ходят на задних."
    pause
    fox "Мне пора. "
    hide fox
    show natasha angry
    narrator "Наташа толкнула парня в бок, привлекая его внимание."
    hide natasha
    show fox angry
    hide natasha
    fox "В моей касте заведено так: сколько часов за день ты отработал, плюс шесть часов на сон — столько времени ты проживешь."
    hide fox
    show natasha angry
    narrator "Наташа одним прыжком встала на ноги. Даже Аш вернулся из своих мыслей."
    show natasha angry
    natasha "Вы зарабатываете часы жизни?"
    show fox shock
    hide natasha
    fox "Все справедливо. "
    fox "Содержание каждого лиса требует ресурсов."
    show fox angry
    fox "Как будто люди содержат детей, чтобы те потом ушли на все четыре стороны, и ничего им не дали."
    narrator "Лис встал и стал внимательно себя оглядывать."
    hide fox
    show natasha sad
    hide fox
    natasha "Уходите?"
    show fox angry
    hide natasha
    fox "Завтра я проживу десять часов, плюс шесть часов на сон. "
    fox "А я не хочу, чтобы мой день длился одиннадцать часов! Имейте совесть."
    hide fox
    show natasha regular
    narrator "Наташа не нашлась, что ответить. Лис уже удалялся. Девушка обняла Аша со спины."
    show natasha smile
    natasha "А этот Онка — чистое зло!"
    show natasha sad
    natasha "Теперь я не удивляюсь, почему он позволил Вечне ставить эксперименты на лисах."
    hide natasha
    show black_hare sad_var
    narrator "Аш отвернул голову, ему было стыдно за сестру."
    hide black_hare
    show natasha angry
    hide black_hare
    natasha "Сделал на заводе свою собственную страну, где он — Бог!"
    narrator "Она встала и начала собирать свои вещи: баночку для воды, чашки."
    hide natasha
    show black_hare surprised_var
    hide natasha
    black_hare " Ты уходишь?"
    show natasha angry
    hide black_hare
    natasha "Мы же договорились встретиться вечером?"
    show black_hare sad_var
    hide natasha
    black_hare "Хорошо."
    hide black_hare
    narrator "Но вечером девушка была занята."
    stop music2 fadeout 3
    jump scene_23


label scene_23:
    pause 0.2
    scene home
    #Парень поддерживает как может, рассказываем, что он вырос без родителей
    play music1 'music/newman_stars.mp3' fadein 3
    narrator "Темноволосый точно знал, какую эмоцию он может научить распознавать ИИ сегодня. Только в очереди ее нет."
    show black_hare regular
    narrator "С самого утра он испытывал тревогу."
    show black_hare surprised_var
    narrator "Его мысли прервал поток сообщений с одинаковым содержанием: \"Ты не идешь на учебу, ты идешь со мной к реке.\""
    hide black_hare
    pause 0.2
    scene station_corridor
    narrator "Парень вышел из жилого отсека."
    show black_hare regular_fear
    narrator "Ему потребовалось время, чтобы убедить себя, что поводов для тревоги нет."
    hide black_hare
    pause 0.2
    scene lake
    narrator "Наташа сидела на пледе там же, где и в прошлый раз."
    show natasha sad
    hide black_hare
    natasha "Она умерла. Она убила себя."
    show black_hare surprised_var
    hide natasha
    black_hare "О ком ты говоришь? "
    black_hare "Ты рассказывала про семью: отца, брата, мать..."
    hide black_hare
    show natasha sad
    narrator "По щекам Наташи потекли слезы."
    hide natasha
    show black_hare regular
    narrator "Аш догадался."
    show black_hare regular
    black_hare "Прости. У меня не было родителей, никогда."
    narrator "Ему было очень стыдно, что он не испытывает жалости к родителям, только — к Наташе."
    narrator "Хотя знал, что это нормально. У него же не было традиционной модели семьи."
    narrator "Множество взрослых, и — сестра. Но его беспокоило, что Наташа видит, что ему не жаль."
    narrator "Уши молчали. Был бы на Ушах стыд — она хотя бы знала, что у него есть совесть."
    black_hare "Я бы хотел разделить с тобой, но..."
    show natasha sad
    hide black_hare
    natasha "Ничего, я понимаю. "
    show black_hare regular
    hide natasha
    black_hare "Хочешь поговорить? Это твоя мать убила себя?"
    hide black_hare
    show natasha sad
    narrator "Наташа сильнее заплакала."
    hide natasha
    show black_hare regular
    hide natasha
    black_hare "А где твой отец, брат?"
    hide black_hare
    show natasha sad
    narrator "Девушка зарыдала и начала задыхаться."
    hide natasha
    show black_hare sad_var
    narrator "Он решил ничего не спрашивать. "
    narrator "Аш вспомнил, что такое \"паническая атака\". Вспомнил про термос в рюкзаке."
    narrator "Аш обнял ее так, что она не видела ничего, и уткнулась лицом ему в плечо."
    hide black_hare
    show natasha sad
    narrator "Спустя несколько минут Наташа перестала реветь и начала говорить."
    show natasha sad
    natasha "Отца тоже нет, уже год. После копирования в сеть он пропал."
    show black_hare surprised_var
    hide natasha
    black_hare "А оригинал?"
    show natasha sad
    hide black_hare
    natasha "Ты делаешь копию в сеть — и убиваешь тело, чтобы решить парадокс двойников."
    natasha "Потому что мы верим, что человек должен быть индивидуален. "
    natasha "Он должен быть единственным."
    show black_hare angry_var
    hide natasha
    black_hare "Но оригинал же — главный!"
    show natasha angry
    hide black_hare
    natasha "Если он при жизни отдаст права на личность копии, то нет."
    hide natasha
    show natasha sad
    narrator "Она вытирала лицо салфетками, слезы так и текли из глаз, но девушка стала спокойней. "
    hide natasha
    show black_hare angry_var
    narrator "Внутри Аша все перевернулось. Он сделал глубокий вход."
    show black_hare regular
    black_hare "Нужно выпить что-нибудь сладкое."
    narrator "Наташа смотрела в пол."
    black_hare "А где твой брат? Вы нужны друг другу."
    show natasha sad
    hide black_hare
    natasha "Мы не общаемся с тех пор, как отец пропал."
    show black_hare regular
    hide natasha
    black_hare "Наверное, ему нужно время."
    narrator "Девушка одобрительно качнула головой и вытерла нос."
    hide black_hare
    pause 0.2
    scene station_corridor
    narrator "Парень повел девушку за собой, стараясь больше не задавать вопросов — не делать подруге больно."
    show natasha sad
    hide black_hare
    natasha "Куда мы идем?"
    show black_hare regular
    hide natasha
    black_hare "В кафе рядом с универом, если его можно так назвать. "
    show black_hare regular_happy2
    black_hare "Выпьем густой горячий шоколад. Это, конечно, яд, но помогает."
    hide black_hare
    show natasha sad
    narrator "Наташа взяла его за руку и шла, тихо плача себе под нос."
    narrator "Еще издалека была заметна какая-то шумиха рядом с аудиторией университета. "
    hide natasha
    show black_hare regular
    narrator "Аш хотел уйти."
    show black_hare surprised_var
    black_hare "На станции так просто толпы не собираются. "
    black_hare "Пойдем другим путем."
    hide black_hare
    show natasha angry
    narrator "Но Наташа, как дикая, побежала в сторону скопления роботов и нескольких человек, все еще держа его за руку."
    play sound 'audio/door.mp3'
    narrator "Они вошли внутрь."
    hide natasha
    pause 0.2
    scene audience
    narrator "Сердце Аша колотилось, тело ослабло – теперь ему не хватило бы сил увести девушку, пожелай он это сделать."
    show black_hare regular_fear
    narrator "Наташа сбавила шаг, и Аш заметил кровь среди людей и устройств. "
    hide black_hare
    show natasha sad
    narrator "Подруга отпустила его руку и медленно подошла поближе."
    narrator "Почему-то ему захотелось остановить ее. Но он не решился, просто шел вслед."
    show natasha angry
    narrator "Совсем рядом кто-то сказал ей, чтобы она ушла, но девушка оттолкнула человека."
    show natasha sad
    narrator "На скамейке лежало что-то, накрытое черной тканью. "
    narrator "Если вы думаете, что на темной ткани не видно кровь — вы ошибаетесь."
    narrator "В стороне лежал галстук. Инстинктивно, девушка все поняла. "
    narrator "Кто-то до последнего отказывается верить в происходящее, но она была не тем человеком. "
    narrator "Несчастная выросла среди людей — которые верят в худшее."
    show natasha sad
    natasha "Зачем?! Теперь я совсем одна!"
    hide natasha
    show black_hare sad_var
    narrator "Аш вспомнил слова Макса: \"У меня отец пропал в сети...\"."
    show black_hare surprised_var
    narrator "Как же он раньше не догадался?"
    pause
    narrator "Наташу, бьющуюся в истерике, увели. "
    show black_hare sad_var
    narrator "Ему не позволили пойти с ней."
    show black_hare angry_var
    narrator "Аш уже был готов идти следом, в Медцентр. "
    narrator "Он же, при необходимости, выполнял функции Центра Копирования во время переноса в сеть."
    show black_hare regular
    show black_hare surprised_var
    play sound 'audio/notification1.mp3'
    narrator "Но ему пришло уведомление. Тот же Медцентр, комната №33."
    hide black_hare
    stop music1 fadeout 3
    jump scene_24


label scene_24:
    pause 0.2
    scene helpcentre
    #Аш пытается дозвониться до Вечны, но выясняется, что та в больнице из-за неудачного теста с нейрохакингом. Девушка заходит все дальше. Оставаясь в тишине она думает, что сегодня могла лишиться всего (тела). И она готова, готова оставить брату оригинал. Она отправляет Онке запрос, можно ли так сделать
    play music2 'music/r.mp3' fadein 3
    narrator "В палате №33 без сознания лежала Вечна."
    show black_hare sad_var
    narrator "Он хотел спрятаться от зрелища, которое все равно будет преследовать его всю жизнь."
    narrator "В смешанной реальности появился автоматический помощник — мобильная камера."
    mobile_camera "Состояние пациента удовлетворительное. "
    mobile_camera "Диагноз: отключение сигналов с рецепторов и скелетной мускулатуры. "
    mobile_camera "Последствия: возможно, чувствительность и активность мышц не восстановятся. "
    mobile_camera "Лечение: нет. "
    mobile_camera "Профилактика: прекращение неквалифицированного вмешательства в мозг."
    narrator "Парень схватился за волосы."
    show black_hare surprised_var
    hide mobile_camera
    black_hare "Как она могла отключить свою кожу и скелетные мышцы? Как?"
    mobile_camera "Могу найти информацию в сети. Отправить запрос?"
    show black_hare regular_fear
    hide mobile_camera
    black_hare "Нет. Она в коме?"
    narrator "Он стал быстро ходить туда-сюда."
    mobile_camera "По текущим прогнозам, пациент придет в сознание через несколько часов."
    show black_hare sad_var
    narrator "Аш начал вытирать слезы трясущимися руками."
    show black_hare sad_var
    black_hare "Как она поступила к вам?"
    mobile_camera "Она отправила запрос из сети."
    stop music2 fadeout 3
    play music1 'music/newman_stars.mp3' fadein 3
    narrator "Парень развернулся к кровати сестры, пытаясь осознать ситуацию."
    show black_hare angry_var
    hide mobile_camera
    black_hare "Думала, что все контролируешь?"
    narrator "У него появился порыв дернуть сестру за руку, сбросить с кушетки, разбудить."
    narrator "Вместо этого, он почувствовал холодную ладонь сестры и одернул свою. "
    narrator "На секунду перестав дышать, он постарался отогнать страшную мысль."
    narrator "В голове загудело. Сердце стало биться громче, адреналин выплескивал ярость, разжигая кровь."
    show black_hare regular
    black_hare "Как у тебя хватило смелости сделать все это?"
    call surprised_disgust
    show black_hare mood
    show black_hare mood
    black_hare "Как у тебя хватило совести?"
    narrator "Он игнорировал ответы на свои вопросы: \"Что тут такого? Врачи бы приехали, в сети я в сознании...\"."
    show black_hare angry_var
    black_hare "Почему? Почему из всего, что есть в этом мире, ты выбираешь различные способы покончить с собой?"
    narrator "У него появилось желание поступить с ней так же, как и она с ним. "
    narrator "Взять шприц, взять нож: \"Интересно, тут есть чем убить себя?\""
    black_hare "Хай, Алиса, чем себя можно убить в радиусе двух метров?"
    alise "Острый угол тумбы. Рекомендуется удариться виском с расстояния десяти шагов от нее."
    hide alise
    black_hare "Совсем не то."
    alise "Вы можете придавить паховую область ножкой кушетки и умереть от болевого шока."
    narrator "Парня передернуло."
    alise "Вариант №3. Вы можете съесть плед и умереть."
    show black_hare regular_happy1
    narrator "Ашу стало смешно. Он решил про себя: \"Понятно, почему разработчикам разрешили ввести такую функцию\"."
    play sound 'audio/bed.mp3'
    narrator "Он услышал шелест ткани. Вечна очнулась. "
    show black_hare sad_var
    narrator "Ему было сложно сдержаться и не обнять сестру, но она зашла слишком далеко."
    narrator "Он думал, что не должен поощрять такие действия."
    narrator "Руки еще дрожали, ноги стали подкашиваться, и он сел на пол рядом с кушеткой. Посмотрел на нее снизу вверх."
    black_hare "Ты просто не знаешь меру. "
    black_hare "Может, все же, подключиться к аппарату жизнеобеспечения? "
    black_hare "Например, можно выключить легкие, или сердце. "
    black_hare "Интересно, как это повлияет на твою производительность?"
    hide black_hare
    show vechna thinking
    narrator "Вечна задумалась. Осторожно села на постели."
    show black_hare angry_var
    hide vechna
    black_hare "Хорошо, что можешь двигаться. "
    black_hare "Но это уже глупо. Если хочешь уйти в сеть — уходи."
    black_hare "Только какая тебе от этого польза?"
    black_hare "Жизнью в сети будет наслаждаться копия."
    show vechna thinking
    hide black_hare
    narrator "Вечна молча смотрела на брата. Она словно выжидала: сказать или нет? Брат продолжал."
    show black_hare angry_var
    hide vechna
    black_hare "Удел настоящих людей — жизнь в реальности. "
    black_hare "И если что-то нельзя сделать в ней — делать в сети."
    show vechna thinking
    hide black_hare
    vechna "Ты не против моего копирования в сеть?"
    narrator "Парень закатил глаза."
    show black_hare disgust_var
    hide vechna
    black_hare "Не судьба тебе оптимизироваться на сто процентов, или даже на девяносто пять."
    black_hare "Копия — это уже не жизнь. "
    black_hare "Что это вообще? Ее симуляция?"
    show vechna thinking
    hide black_hare
    vechna "Симуляция как раз полностью ее повторяет. "
    vechna "То, что похоже на жизнь, называется \"эмуляция\"."
    show black_hare surprised_var
    hide vechna
    black_hare "?"
    show vechna thinking
    hide black_hare
    vechna "Сеть — это жизнь, просто ты ее не узнаешь в новой форме."
    show black_hare sad_var
    hide vechna
    black_hare "Все плохо закончится."
    black_hare "Как ты смогла отключить импульсы от кожи и мышц? "
    show black_hare angry_var
    black_hare "Там же столько расчетов! Даже начни ты это до конкурса — не успела бы!"
    show vechna thinking
    hide black_hare
    vechna "Я же на Фабрике работаю."
    show black_hare angry_var
    hide vechna
    black_hare "Начинаю понимать Макса..."
    black_hare "Парень из университета, оказывается, брат Наташи. "
    black_hare "И он умер. "
    black_hare "К слову, после конфликта на Фабрике."
    show vechna angry
    hide black_hare
    vechna "Оставь свои домыслы. "
    vechna "Если я и покорю дальний космос, то только за ресурсы Онки."
    show black_hare angry_var
    hide vechna
    black_hare "Одно другому не мешает."
    narrator "Он поднялся на ноги."
    show black_hare regular
    black_hare "Я подожду, пока ты оденешься."
    show vechna thinking
    hide black_hare
    vechna "Вообще-то... Мне кажется, я еще не оправилась и мне стоит провести здесь еще день."
    narrator "Брат разозлился."
    show black_hare angry_var
    hide vechna
    black_hare "Очень удобно — никто не помешает побыть в сети еще часиков двадцать."
    show vechna angry
    hide black_hare
    vechna "Хватит."
    show black_hare angry_var
    hide vechna
    black_hare "Ты чуть не убила себя! Понимаешь, каково мне?"
    show vechna angry
    hide black_hare
    vechna "А ты понимаешь, каково мне?"
    play sound 'audio/bed.mp3'
    narrator "Она приподнялась на кушетке. Руки дрожали, но злость придавала сил."
    vechna "Я делаю то, что считаю верным!"
    mobile_camera "Не рекомендуется вставать с кровати в ближайшие три-пять часов."
    show vechna thinking
    hide mobile_camera
    vechna "Вот видишь? Все решилось само. Я остаюсь."
    narrator "Голос парня дрожал."
    show black_hare angry_var
    hide vechna
    black_hare "Ты считаешь, что у тебя все нормально? "
    black_hare "Ты можешь не восстановить чувствительность многих мышц и рецепторов."
    show vechna thinking
    hide black_hare
    vechna "А оно мне надо?"
    show black_hare angry_var
    hide vechna
    black_hare "Ты чуть не умерла!"
    show vechna angry
    hide black_hare
    vechna "Это побочный эффект!"
    hide vechna
    show black_hare angry_var
    narrator "Зубы Аша скрипели друг о друга."
    play sound 'audio/kick.mp3'
    narrator "Он пнул кушетку. Аппаратура для измерения показателей жизнеобеспечения затряслась. Вечна испугалась."
    mobile_camera "Законные разрушения невозможны в медицинском учреждении."
    narrator "Парень не обращал внимание на автоматического помощника. Вечна кричала."
    hide black_hare
    show vechna angry
    hide mobile_camera
    vechna "Что ты делаешь? Успокойся!"
    narrator "Он стал задыхаться, злость отступала. Но нарастала в его сестре."
    narrator "Она снова приподнялась на постели."
    vechna "Ты лицемер. Ты сам..."
    narrator "В ее голосе слышалась желчь."
    vechna "Ты цифровизируешь чувства. Твои Уши..."
    vechna "Ты запрещаешь мне жить так, как я хочу! Где я хочу!"
    show black_hare angry_var
    hide vechna
    black_hare "Потому что ты выбрала самый короткий путь в могилу!"
    black_hare "Ты просто не доживешь до отлета на Землю! "
    black_hare "А, Вечна? Ты не вечна! Очнись уже!"
    show vechna smile2
    hide black_hare
    vechna "Пока не вечна."
    show black_hare angry_var
    hide vechna
    black_hare "Хочешь, делай копию в сеть."
    black_hare "Все равно, как только ты поймешь, что копия лучше тебя — ты ее удалишь."
    black_hare "Больше открытий! Ты, похоже, любишь только свое эго!"
    show black_hare angry_var
    narrator "Он вылетел в коридор. "
    hide black_hare
    show vechna sad
    narrator "Сестра долго смотрела в стену, она и забыла, что ее сознание не живет в сети, оно лишь заходит в нее."
    show vechna smile2
    play sound 'audio/notification1.mp3'
    narrator "Ей пришло уведомление. Прочитав, девушка улыбнулась."
    show vechna smile1
    narrator "Она смотрела в потолок и шептала сама себе: \"Скоро, задача будет выполнена\"."
    hide vechna
    stop music1 fadeout 3
    jump scene_25


label scene_25 :
    pause 0.2
    scene lake
    #Раскрываются карты, что Макс ее брат. Он винит в своей смерти Онку и Аша (чисто из вредности. А еще, саму Наташу в смерти отца, это ей нужны были ресурсы. Из-за этого, он пропал в сети
    play music2 'music/noname.mp3' fadeout 3
    narrator "Со стороны Аш выглядел, как сумасшедший. Наташа сидела на пледе, скрестив ноги."
    show black_hare angry_var
    show black_hare angry_var
    black_hare "Куда ты? Луна маленькая."
    show natasha angry
    hide black_hare
    natasha "Я не могу и не хочу тут находиться."
    natasha "Мой брат вынес себе мозги в университете. "
    show natasha sad
    natasha "Как мне тут жить?"
    show black_hare angry_var
    hide natasha
    black_hare "Это пройдет."
    show natasha angry
    hide black_hare
    natasha "Что, прости, пройдет? "
    natasha "Люди стали оживать? О, как-то я пропустила эту новость!"
    natasha "Ты действительно не можешь поставить себя на мое место?"
    show black_hare angry_var
    hide natasha
    black_hare "Знаешь, я более, чем на твоем месте."
    show black_hare regular
    black_hare "Разве мы должны ругаться, а не поддержать друг друга?"
    black_hare "Разве я — не твой родной человек?"
    show natasha angry
    hide black_hare
    natasha "Кто тебе родной? Для общественников родной — любой, с кем знаком месяц."
    hide natasha
    show black_hare regular
    narrator "Аш сделал шаг вперед. Наташа подалась назад."
    show black_hare sad_var
    black_hare "Почему ты не рассказала про свои проблемы?"
    show natasha sad
    hide black_hare
    natasha "Для чего?"
    natasha "Расскажи я, что отец пропал во время копирования в сеть, а свое тело при этом сам умертвил... "
    show natasha angry
    natasha "Что бы ты делал? "
    natasha "Ходил бы за своей сестрой! А мне тоже нужна забота!"
    show natasha sad
    natasha "Расскажи я, что мать, которая при попытке удалить воспоминания экспериментальным нейрохакингом..."
    show natasha angry
    natasha "...Спалила себе мозг, что бы ты сделал?"
    hide natasha
    show black_hare angry_var
    narrator "Аш молчал. Никогда он не чувствовал такого разочарования."
    show black_hare angry_var
    black_hare "Почему ты не сказала про Максима?"
    show natasha angry
    hide black_hare
    natasha "Он во всем винил меня! "
    show natasha sad
    natasha "Что я требовала себе и факультет получше, и вещи, и вообще..."
    narrator "По ее щекам снова покатились слезы. "
    hide natasha
    show black_hare angry_var
    narrator "Аш стоял напротив. За ним серебрилась река по переработке. "
    narrator "Девушка стояла и смотрела в глаза Аша."
    show black_hare angry_var
    black_hare "Теперь ты точно одна."
    hide black_hare
    show natasha regular
    narrator "Плечи девушки на секунду опустились, но автоматически вытянулись в струну. Она вздернула подбородок."
    show natasha angry
    natasha "Ты хоть иногда думаешь о том, каково другим? "
    natasha "Не о том, что сделают тебе, и как ты будешь себя чувствовать, а о том, что будут испытывать другие?"
    show black_hare disgust_var
    hide natasha
    black_hare "Ты неадекватная. "
    black_hare "Ты, как и все, кто пережил подростковый возраст под лунным куполом — психованная."
    show black_hare angry_var
    black_hare "Ведь ты молчала, зная, что светит Вечне от самопального нейрохакинга!"
    black_hare "Не пытайся выставить меня виноватым."
    show black_hare regular_fear
    play sound 'audio/push.mp3'
    narrator "Темноволосый почувствовал толчок в грудь. Он понял, что стоит на краю. "
    hide black_hare
    show natasha angry
    narrator "Наташа прижалась к нему. Он испугался, что она его столкнет."
    show natasha angry
    natasha "Стоило бы сбросить тебя. "
    natasha "Оставить с повреждениями мозга от переработанного протеза."
    show black_hare regular
    hide natasha
    black_hare "Имплантов."
    black_hare "И я даже не против."
    hide black_hare
    show natasha angry
    narrator "Она говорила сквозь зубы. Четко произнося каждый звук. "
    show natasha angry
    natasha "Пусть ты и твои идеи будут никому не нужны."
    show black_hare sad_var
    hide natasha
    black_hare "Это и есть, моя текущая ситуация."
    hide black_hare
    show natasha angry
    narrator "Наташа держала парня за футболку, потом резко дернула на себя, заставив сделать несколько шагов вперед."
    show natasha angry
    natasha "Еще объяснительные писать."
    show natasha regular
    natasha "И без моей помощи сгниешь."
    hide natasha
    show black_hare regular
    pause
    call surprised_disgust
    show black_hare mood
    show black_hare mood
    black_hare "Кто бы мог подумать, что вместо трогательных прощаний, я познакомлюсь с тобой настоящей."
    hide black_hare
    show natasha regular
    narrator "Девушка сложила плед, собрала влажные от слез платки и бросила в реку."
    show natasha regular
    natasha "Не пытайся всех контролировать! Я – не твоя сестра!"
    show natasha angry
    narrator "Уходя, она не подняла глаза на Аша. "
    hide natasha
    show black_hare sad_var
    narrator "Он повернулся лицом к массе наноботов, подался вперед, словно намереваясь броситься вниз."
    show black_hare sad_var
    black_hare "Живого они меня не переработают, но Уши в голове расщепят."
    black_hare "Смысл оставаться овощем и радовать Наташу?"
    show black_hare surprised_var
    play sound 'audio/notification1.mp3'
    narrator "Он получил уведомление, и, подумал было, что это Онка вспомнил про \"утешительный приз — ужин\"."
    show black_hare regular
    narrator "Темноволосый поставил ногу, нависшую над субстанцией, назад на берег."
    show black_hare regular_sad
    narrator "Открыв сообщение — он пришел в ужас и со всех ног помчался в Медцентр, выполняющий функцию Центра Копирования."
    hide black_hare
    pause 0.2
    scene station_corridor
    narrator "В голове стучал быстрый пульс и звучали слова: \"Твоя сестра в Центре Копирования... Говорят, копии пропадают\"."
    #Показываем полную сцену копирования Вечны. Она не хотела убивать оригинал, но что-то пошло не так. Почему-то рядом с Ашем оказался Лис. После этого, лиса повысит онка
    show black_hare regular_fear
    narrator "Аш чувствовал, что плохой конец ближе, чем он думал."
    hide black_hare
    jump scene_26


label scene_26:
    pause 0.2
    scene helpcenter
    narrator "Спустя 30 минут."
    pause
    show vechna sad
    narrator "Вечна повернула голову к Ашу, лицо брата искажалось сквозь стекло. Он бился лбом и руками. Зря."
    show vechna angry
    vechna "Это все он... !"
    show vechna sad
    narrator "Ее заглушил голос станции:"
    robotic_voice "Автоматическая подача газа запущена."
    narrator "Вскоре фиксирующие браслеты, удерживавшие девушку на кушетке, перестали натягиваться."
    hide vechna
    stop music2 fadeout 3
    jump scene_27


label scene_27:
    pause 0.2
    scene blood_room
    play music1 'music/w.mp3' fadein 3
    narrator "Настоящее время."
    pause
    show black_hare sad_var
    black_hare "Это все я? Неужели, она так думала? "
    black_hare "Что это я во всем виноват?"
    show black_hare angry_var
    black_hare "Как я жалею, что дал код Ушей..."
    black_hare "Не только сестра должна платить. Я — тоже."
    show black_hare regular
    black_hare "Здесь и закончу. "
    pause
    narrator "Раздается мужской голос."
    man "Ну ты, парень, и удумал."
    hide man
    black_hare "Мне бы хотелось быстрее начать."
    show black_hare regular_fear
    narrator "Аш не может ничего разглядеть. Но, через минуту, глаза привыкают к темноте. "
    show black_hare regular
    play sound 'audio/dog.mp3'
    narrator "Вскоре раздался звук открывающейся двери, и по полу застучали когти."
    play sound 'audio/ryichanie.mp3'
    narrator "Дверь сразу закрывается. Он слышит рычание. "
    show black_hare regular_sad
    narrator "Тело парализует страх, но в следующий момент его охватывает адреналиновая эйфория, и он чувствует отчаяние и злость."
    narrator "На него бросаются три собаки."
    call mad_fear
    show black_hare mood
    show black_hare mood
    black_hare "Не только я виноват! Ты меня бросила!"
    show black_hare mad_var
    narrator "Он сам не понимает, как под зубами оказывается пульсирующая шея пса."
    narrator "Все происходит быстро, у него во рту словно лопается помидорка черри, забрызгав своим соком-кровью все вокруг."
    narrator "Вцепившаяся мертвой хваткой в руку собака остается без глаза, еще одна спешно убегает в соседний угол и начинает скулить."
    narrator "Аша качает, он чувствует тошноту."
    narrator "Открывается дверь."
    narrator "Вбегает мужчина с аптечкой в руке. "
    narrator "Он бросается к псам, обрабатывает рану одному из них и пытается остановить кровь."
    man "Ты ему артерию перегрыз!"
    man "Не по договору! Сиди! Надолго здесь останешься!"
    man "Решил сдохнуть — так бы и делал!"
    narrator "Пес, оставшийся без глаза, жалобно скулит. "
    narrator "Мужчина, чуть не плача, осматривает голову животного, с любовью гладя его по морде."
    show black_hare regular
    narrator "Аш начинает приходить в себя. "
    show black_hare fear_var
    narrator "Руки стали трястись только сейчас."
    narrator "Мужчина держит голову собаки и гладит."
    man "Помощь скоро будет."
    man "Псы не должны были пострадать. Ты же сам заплатил, чтобы тебя съели!"
    show black_hare sad_var
    narrator "Аш молчит. Что здесь можно сказать?"
    hide black_hare
    pause 0.2
    scene chip_factory_laboratory
    narrator "В лаборатории Онки: он и лисы смотрят на экран. Видят на нем Аша в крови и мужчину, бинтующего псов."
    show onka danger
    hide black_hare
    onka "А вы так можете?"
    show fox shock
    hide onka
    fox "Мы в двадцать втором веке."
    show onka sneaky
    hide fox
    onka "Ну, чисто теоретически: что вы думаете о боях?"
    hide onka
    show fox angry
    narrator "Лис показывает всем своим видом, что он не будет это обсуждать."
    show onka thinking
    hide fox
    onka "Ладно. Пора провести обещанный ужин. "
    show onka sneaky
    onka "Он же все-таки выиграл утешительный приз."
    hide onka
    stop music1 fadeout 3
    jump scene_28


label scene_28:
    #Онка связывается с Ашем. Рассказывая, как с помощью кода ушей можно жить вечно. Аш задачется вопросом, почему сейчас тот говорит ему это все? Но соглашается - ведь это способ вернуть сестру. Но ему кое-что нужно (тело)
    pause 0.2
    scene blood_room
    play music2 'music/newman_v4.mp3' fadein 3
    narrator "На полу постепенно темнеют следы крови."
    show black_hare sad_var
    narrator "Сидя в изоляции от окружающих, Аш проваливается в сон. "
    play sound 'audio/notification1.mp3'
    narrator "Заключенный получает приглашение — в сети. "
    narrator "Забыв, где и по каким обстоятельствам находится, он автоматически принимает вызов и заходит в сеть."
    hide black_hare
    pause 0.2
    scene planet
    narrator "Виртуальный мир и понимание происходящего захлестывают его с головой."
    show black_hare surprised_var
    black_hare "Что мы тут делаем? Как ты получил доступ?"
    show onka sneaky
    hide black_hare
    onka "Это работа моей сотрудницы. Почему бы не зайти?"
    show black_hare angry_var
    hide onka
    black_hare "Что тебе нужно? Все это чертовски странно. "
    black_hare "Мне же должны были заблокировать сеть."
    show onka smile
    hide black_hare
    onka "Я, что — зря в ней главный? Код, может, и открытый, а ядро — мое."
    onka "Это очень серьезно, если нельзя связаться с человеком в сети."
    show onka sneaky
    onka "Поэтому я сразу принялся тебя искать."
    onka "Решил, здесь тебе будет уютно. "
    show onka smile
    onka "Не бойся, разрушающие факторы окружающего мира отключены."
    show black_hare angry_var
    hide onka
    black_hare "Я принял все наказания, которые мне дали."
    show onka smile
    hide black_hare
    onka "Да, охранник сообщил, что ты даже не пытался торговаться по праву субъективной оценки для личностей со здоровыми моральными ценностями."
    show black_hare disgust_var
    hide onka
    black_hare "Я в это число не попадаю."
    show onka danger
    hide black_hare
    onka "У нас здоровые моральные ценности! "
    show onka smile
    onka "Мое и твое понимание хорошего и плохого совпадает с пониманием большей части людей."
    hide onka
    show black_hare regular_happy1
    narrator "Аш смеется."
    show black_hare regular_happy1
    black_hare "Что, если наоборот? Мы все — больные?"
    show onka smile
    hide black_hare
    onka "Думал, и считаю маловероятным, что сумасшедшие — почти девяносто пять процентов всех жителей Луны и Земли."
    onka "Тебе нравится космос?"
    show black_hare angry_var
    hide onka
    black_hare "Земля мне нравится больше."
    show onka thinking
    hide black_hare
    onka "Это был риторический вопрос."
    show black_hare angry_var
    hide onka
    black_hare "Что тебе нужно? Можно покороче? Мне здесь тяжело."
    narrator "Аш смотрит на кристаллы под ногами и невольно думает про сестру."
    show onka thinking
    hide black_hare
    onka "Мои предки видели в чипе лишь способ заработка, с помощью которого они финансировали борьбу с голодом и покорение Луны. "
    show onka angry
    onka "Ерунду, одним словом."
    show black_hare angry_var
    hide onka
    black_hare "Поскольку, с недавних пор, мне наплевать на манеры... К чему ты ведешь?"
    show onka angry
    hide black_hare
    onka "Я вижу в чипе большее."
    show onka victory
    onka "Кое-что сумасшедшее — возможность жить вечно."
    hide onka
    show black_hare surprised_var
    narrator "Аш не находит, что сказать. Он изо всех сил пытается понять, что говорит Илли."
    hide black_hare
    show onka smile
    hide black_hare
    onka "Чип — это то, что фиксирует карту активности мозга, вплоть до мощности сигналов в нем. "
    onka "И может передавать эти сигналы обратно в мозг."
    onka "Теоретически, цифровую копию можно использовать, как прослойку, — между переносом из одного тела в другое."
    show onka danger
    onka "Сейчас люди могут уйти в сеть, но не вернуться в реальность."
    hide onka
    show black_hare surprised_var
    hide onka
    black_hare "Ты предлагаешь это исправить?"
    narrator "Аша прошибает пот."
    hide black_hare
    show onka sneaky
    narrator "Онка еле сдерживается, чтобы не похвалить себя."
    show onka sneaky
    onka "Но мне нужен кто-то, кто готов заниматься проектом. "
    onka "Раз ты уже знаком с чипом, и написал для него прекрасный ИИ..."
    show black_hare angry_var
    hide onka
    black_hare "Какая-то слабая причина..."
    show onka thinking
    hide black_hare
    onka "Ладно. Ты знаешь, в душе я — монополист, и занимаюсь дальним космосом."
    onka "Мне нравится концепция универсального языка: она может объединить людей из разных галактик лет через триста-пятьсот."
    show black_hare surprised_var
    hide onka
    black_hare "За работу над проектом по возвращению копий из сети, ты просто хочешь ИИ ушей? Он же простой."
    show onka thinking
    hide black_hare
    onka "Он работает, и это главное. Считай, такая прихоть."
    onka "Конечно, всегда можно остаться в одиночке."
    narrator "Он выжидающе смотрит на парня."
    show onka sneaky
    onka "Мы сделаем тебя очень популярным. Имплантируем Уши детям, вместе с чипом. А?"
    onka "Права — мне, а популярность — тебе."
    show black_hare regular_confused
    hide onka
    black_hare "Неплохо."
    show black_hare fear_var
    black_hare "Но с возвращением копии в тело столько технических моментов... И экспериментов..."
    hide black_hare
    show onka danger
    narrator "Улыбка Илли становится все шире. Он поднимает руки и поправляет цилиндр."
    show onka danger
    onka "Сложный проект, но благой. Возможно, ты решишь за счет него некоторые проблемы..."
    onka "Ради вечной жизни в теле, а не в сети, стоит попробовать."
    onka "Ведь разве это жизнь? В цифре?"
    show black_hare regular
    hide onka
    black_hare "Ты прав..."
    narrator "Ему кажется, что что-то тут не так, но возможность вернуть сестру заглушает все остальное."
    narrator "Он вспоминает ее последние слова: \"Это все он...\"."
    narrator "Сердце Аша снова сжимается, а тело охватывает невыносимая боль."
    pause
    call mad_fear
    show black_hare mood
    show black_hare mood
    black_hare "Я виноват."
    show onka danger
    hide black_hare
    onka "Что?"
    show black_hare mood
    hide onka
    black_hare "Хорошо, Уши Зайца станут твоей дочерней компанией."
    show black_hare mad_var
    black_hare "Но ты должен дать мне кучу ресурсов для возвращения..."
    narrator "Он оборвал себя."
    black_hare "Для загрузки копий в живое тело."
    show onka danger
    hide black_hare
    onka "Я так и хотел! "
    show onka confused
    onka "Придумаем тебе крутой псевдоним."
    show onka danger
    onka "Уже придумал! Черный Заяц! А как тебе?"
    $ash_name="Черный Заяц"
    show black_hare mad_var
    hide onka
    black_hare "Публичный псевдоним?"
    narrator "Аш смеется, вспоминая пасти псов."
    hide black_hare
    show onka sneaky
    hide black_hare
    onka "Кстати, Черного Зайца отпустят, как только он выйдет из сети."
    onka "Сразу иди на Фабрику Чипов. "
    show onka danger
    onka "Жду не дождусь подписания документов."
    hide onka
    stop music2 fadeout 3
    jump scene_29


label scene_29:
    pause 0.2
    scene chip_factory_laboratory
    play music1 'music/newman_classic.mp3' fadein 3
    narrator "Войдя в помещение на Фабрике Чипов, им не приходится зажигать свет. Все вокруг светится причудливым образом. "
    narrator "Помещение представляет собой лабиринт, разделенный панелями с жидкостью — плоскими аквариумами с разноцветными сгустками слизи. "
    narrator "Каждый аквариум уникален по цвету, подсветке и наполнению."
    show onka victory
    narrator "Глаза владельца Фабрики горят."
    show onka victory
    onka "Добро пожаловать домой!"
    show black_hare fear_var
    hide onka
    black_hare "Это не мой дом."
    show onka sneaky
    hide black_hare
    onka "Зря ты так... Привыкнешь."
    show black_hare disgust_var
    hide onka
    black_hare "Что это за аквариумы с плесенью?"
    show onka sneaky
    hide black_hare
    onka "Это колонии бактерий! Созданы заселять космические объекты. Считай — Боги."
    show black_hare surprised_var
    hide onka
    black_hare "Это же гигантские чашечки Петри?"
    show onka confused
    hide black_hare
    onka "Что это?"
    show black_hare regular_happy2
    hide onka
    black_hare "Я думал, ты шаришь в биотехнологиях, ну, или в школьной программе."
    show onka thinking
    hide black_hare
    onka "Лисы из Высшей касты знают. А я — это космос, деньги и видение развития компании."
    onka "Я верю, что только эти бактерии способны стать космосу родными."
    show black_hare regular_happy2
    hide onka
    black_hare "Или умереть."
    show onka thinking
    hide black_hare
    onka "Если есть вычислительные мощности и время — нет нерешаемых задач."
    narrator "Илли Онка стоит посреди дела всей-всей своей жизни."
    hide onka
    show black_hare regular_happy2
    hide onka
    black_hare "Исследуя Фабрику на конкурсе, я не нашел тут сухих лабораторий. Ну, таких, чтобы кто-то мог выйти в сеть и обработать там данные."
    show onka thinking
    hide black_hare
    onka "Все вычисления делегированы копиям в сети и касте №2."
    show black_hare regular_happy2
    hide onka
    black_hare "Все это, конечно, мило, но давай ближе к делу."
    show black_hare fear_var
    black_hare "Ты сам понимаешь что нужно для создания технологии копирования из сети в тело?"
    show onka danger
    hide black_hare
    onka "Я хочу узнать твое видение."
    hide onka
    show black_hare fear_var
    narrator "Аш обводит взглядом помещение и продолжает шепотом:"
    show black_hare fear_var
    black_hare "Где взять живого человека, который согласится, чтобы в его тело посадили чужое сознание? "
    black_hare "Это же нелегально... И смертельно!"
    black_hare "Копировать в лис? На первой стадии — ок, но нужен и человек."
    narrator "Онка наклоняется к Ашу. Тот чувствует запах манго."
    hide black_hare
    show onka sneaky
    hide black_hare
    onka "А что — тело смертельно больного мужчины может не подойти?"
    show onka danger
    onka "Или нужна молодая девушка?"
    hide onka
    show black_hare regular_confused
    narrator "Аш серьезно смотрит на Онку. "
    narrator "Тот точно знает, зачем он согласился на эту работу. Смысл кривить душой?"
    call mad_fear
    show black_hare mood
    show black_hare mood
    black_hare "Раз так, то — да. Лет восемнадцати. Когда поймем, что все точно работает."
    black_hare "До финального теста на роль испытуемого сойдет даже дед."
    show onka danger
    hide black_hare
    onka "Придумай эксперимент, все его стадии, а там — подумаем."
    narrator "Илли хищно улыбается, и у Аша мелькает в голове мысль, что у Онки зубов больше, чем у Пеннивайза."
    hide onka
    show black_hare mad_var
    narrator "Но ради сестры он готов на любую сделку."
    hide black_hare
    stop music1 fadeout 3
    jump scene_30


label scene_30:
    pause 0.2
    scene lake
    play music2 'music/r.mp3' fadein 3
    play sound 'audio/heart.mp3'
    narrator "Пульс стучит в голове, заглушая мысли."
    show black_hare regular
    narrator "Парень чувствует невыносимое желание начинать действовать, не откладывая, двигаться к цели. Но, как же все сложно..."
    narrator "Аш смотрит на свое отражение в зеркальной поверхности реки из наноботов."
    narrator "Он смотрит в отражение своих глаз и понимает, каким был его взгляд, когда он решил убить собак. "
    narrator "Автоматически, бессознательно, глупо..."
    narrator "Когда он выбирал — жить или умереть, да или нет, один или ноль — Аш первый раз почувствовал тот животный страх."
    show black_hare regular
    black_hare "Это всегда во мне было?"
    call mad_fear
    show black_hare mood
    show black_hare mood
    black_hare "Вечнуть Вечну... "
    narrator "Он вспоминает, как она любила каламбуры. Пока не захакала свой мозг до неузнаваемости."
    black_hare "Дьявол в деталях. И этих деталей тысячи..."
    black_hare "Для того, чтобы понять, возвращается копия в тело или нет..."
    black_hare "...нужно провести эксперимент статистически достоверное количество раз."
    black_hare "А это — сотни, в идеале — тысячи раз."
    black_hare "Тысячи, мать его, людей!"
    show black_hare angry_var
    black_hare "Понятно, почему Онка не хочет брать это на себя."
    black_hare "Он точно знает о Вечне. "
    black_hare "Как-никак она у него работала. Поэтому и пришел ко мне."
    show black_hare sad_var
    black_hare "Очевидно, без его помощи я ничего не смогу..."
    narrator "Человек, который может позволить себе самую большую роскошь..."
    narrator "...возможность собственным умом и ресурсами реализовывать свои дикие идеи и добиться успеха."
    show black_hare regular
    narrator "Парень смотрит вверх: взгляд всегда упирается в далекие, но вездесущие стенки купола или потолки лавовых тоннелей под ним."
    narrator "Мысли в голове Аша в который раз бегут по кругу."
    narrator "Он представляет себе мягкие кресла корабля, рядом сидит сестра, разглядывает маленьких собачек и пушистых ящериц на руках у пассажиров поблизости. "
    narrator "Приятный голос сообщает, что корабль отправляется, и скоро они вернутся на Землю."
    stop music2 fadeout 3
    play music1 'music/newman_music.mp3' fadein 3
    narrator "Из мечтаний его вырывает рычание лиса. Перед парнем — Облачный, он выглядит обеспокоенным."
    hide black_hare
    show fox angry
    hide black_hare
    fox "Мне конец! Видео с интервью попало в сеть."
    fox "За мной и так есть другие грехи."
    show black_hare disgust_var
    hide fox
    black_hare "Успокойся, не убить же ты его пытался."
    hide black_hare
    show fox angry
    narrator "Лис рассердился."
    show black_hare fear_var
    hide fox
    black_hare "Или пытался?"
    show black_hare regular_confused
    black_hare "Расскажи, что за видео?"
    narrator "Ответ сразу приходит ему в голову. Лис ложится на пол и закрывает лапами голову."
    show black_hare fear_var
    black_hare "Она не могла так поступить! Покажи."
    narrator "Да. Это действительно был тот замечательный день, когда Наташа брала у Лиса интервью."
    show black_hare surprised_var
    black_hare "Как может быть настолько на всех наплевать?"
    show fox shock
    hide black_hare
    fox "Еще как может быть! Я же ей помог, показал лианы..."
    show black_hare regular_happy1
    hide fox
    black_hare "Месть уже в ее стиле..."
    black_hare "А ты словно ненавидишь Онку! Раз показал ей его сокровища!"
    show fox angry
    hide black_hare
    fox "Не важно, мой путь — на переработку."
    narrator "Зверь обреченно смотрит на реку с расщепляющими наноботами."
    fox "Вам, скорее всего, тоже."
    show black_hare angry_var
    hide fox
    black_hare "До сих пор не верю. После всего того, что произошло с ее семьей, с моей..."
    black_hare "Она должна лучше всех меня понимать, но осознанно делает хуже и хуже!"
    hide black_hare
    show fox angry
    narrator "Лис нервно машет хвостом и оглядывается по сторонам."
    show fox angry
    fox "Все труды насмарку! Я сбегу. Сбегу."
    hide fox
    show black_hare regular
    narrator "Друг опускается на колени рядом с лисом."
    show black_hare regular
    black_hare "Ты напуган, это мешает тебе здраво рассуждать."
    black_hare "Мы на Луне, в сети пещер, а над нами — купол."
    black_hare "За ним — радиация, и нет атмосферы."
    narrator "Аш дотрагивается до Лиса."
    show black_hare regular_happy2
    black_hare "Куда ты хочешь сбежать?"
    hide black_hare
    show fox smile
    narrator "Лис поднимает свою мордочку и рисует носом в воздухе круг."
    show fox smile
    fox "На Землю."
    show black_hare regular_happy2
    hide fox
    black_hare "Ты не сможешь улететь в этом году."
    show fox angry
    hide black_hare
    fox "Я могу пробраться на корабль через месяц."
    show black_hare regular_confused
    hide fox
    black_hare "Как можно не заметить лиса?"
    show black_hare regular_happy1
    black_hare "Но я мог бы взять тебя с собой. Как неразумное домашнее животное."
    show fox angry
    hide black_hare
    fox "Унизительно!"
    hide fox
    show black_hare regular_confused
    narrator "Парень пожимает плечами."
    show black_hare regular
    black_hare "Зато не смертельно!"
    narrator "Лис перестает драматизировать."
    show fox angry
    hide black_hare
    fox "Когда? Когда мы сможем вылететь?"
    show black_hare regular
    hide fox
    black_hare "Через год. Я ручаюсь, что Онка тебя не тронет."
    show fox angry
    hide black_hare
    fox "С чего мне Вам верить? Какая Вам выгода?"
    show black_hare angry_var
    hide fox
    black_hare "Да никакой выгоды! Что вы все..."
    show fox angry
    hide black_hare
    fox "Вы нужны хозяину, только это ничего не значит."
    show black_hare angry_var
    hide fox
    black_hare "Мы закончим свои дела на Луне. Тебе же есть чем заняться?"
    show fox angry
    hide black_hare
    fox "Еще как есть!"
    show black_hare angry_var
    hide fox
    black_hare "Ты же хотел в Высшую касту?"
    black_hare "На счет видео..."
    show fox angry
    hide black_hare
    fox "Оно по всей сети!"
    show black_hare angry_var
    hide fox
    black_hare "Это я тебя попросил об интервью. Сам и решу."
    show fox shock
    hide black_hare
    fox "Как, как вы это решите?"
    show black_hare mad_var
    hide fox
    black_hare "У твоего хозяина, я уверен, рыльце тоже в пушку."
    black_hare "Именно поэтому он, должно быть, сам все решил."
    narrator "Парень подталкивает Лиса в сторону выхода, и тот понуро плетется за ним на Фабрику Чипов."
    hide black_hare
    stop music1 fadeout 3
    jump scene_31


label scene_31:
    pause 0.2
    scene chip_factory_laboratory
    play music2 'music/ayay1.mp3' fadein 3
    narrator "Ученый осматривает лабораторию, не глядя никуда конкретно."
    show black_hare fear_var
    narrator "Он сосредоточен на мыслях."
    show black_hare fear_var
    black_hare "Значит, пункт один: решить, что такое \"сознание\"."
    black_hare "Эксперимент будет успешен, если мы сможем понять: в новом теле — оригинал сознания или химера? "
    show black_hare regular
    black_hare "Значит, мне вообще не обязательно понимать, что такое \"сознание\"."
    show black_hare fear_var
    black_hare "Нужно лишь сравнить оригинал и копию в теле."
    black_hare "Если они будут считать себя одним человеком, тогда сделаем допущение — это успех."
    narrator "Аш водит пальцем по панели со светящимися бактериями. От тепла они меняют цвет на малиновый."
    black_hare "Ладно, значит, с этим разобрались."
    black_hare "Пункт два: провести эксперимент по пересадке сознания. Безумный."
    black_hare "Трудности: нужно пересадить сознание примерно в тысячу людей, чтобы удостовериться, что это работает. "
    black_hare "На тысячу испытуемых, однозначно, будут ошибки. "
    black_hare "Вопрос: один процент или девяносто девять?"
    narrator "Как хороший брат, он бы никогда не стал переселять сознание Вечны в качестве теста в тысячу непонятных тел. "
    narrator "Мне нужна всего одна сестра."
    black_hare "Копии Вечны, наверное, будет плевать, что ее еще раз скопируют в тело."
    show black_hare sad_var
    black_hare "Но что скажет Вечна в новом теле?"
    black_hare "Стоит ли этим заниматься?"
    narrator "Панель с бактериями перед ним становится холодной, движение сгустков бактерий останавливается. На поверхности появляется конденсат."
    show black_hare fear_var
    black_hare "Ценой тысяч испытуемых. Тысяч жертв."
    black_hare "Я действительно — зло?"
    narrator "Аш рисует перед собой единицу. А потом еще, и еще одну."
    narrator "Прошло минут десять, а он, как в трансе, все рисует и рисует. "
    stop music2 fadeout 3
    play music1 'music/newman_gt.mp3' fadein 3
    pause
    narrator "В зале слышатся шаги."
    hide black_hare
    show onka danger
    hide black_hare
    onka "Забыл кое-что!"
    show onka confused
    narrator "Хозяин Фабрики удивленно рассматривает Аша, который отрешенно рисует палочки."
    show onka confused
    onka "Все хорошо?"
    show black_hare sad_var
    hide onka
    black_hare "Хочу прочувствовать. Какую цену придется заплатить за попытку вернуть копию в тело."
    show onka sneaky
    hide black_hare
    onka "Это не стоит победы над смертью?"
    show black_hare fear_var
    hide onka
    black_hare "Если облажаемся, то не стоит..."
    show onka smile
    hide black_hare
    onka "Я забыл предложить закрепить сделку. Устрою обещанный ужин."
    show onka sneaky
    onka "Не знаю как ты, но в таких ситуациях пьют что-то одурманивающее."
    onka "Лучше друг друга узнаем."
    show black_hare surprised_var
    hide onka
    black_hare "Не смогу пропустить такое зрелище. Лисы тоже пьют?"
    show onka thinking
    hide black_hare
    onka "ИИ Фабрики им не позволяет. Они же сотрудники."
    show onka danger
    onka "Я не спросил, как ты предпочитаешь веселиться: алкоголь, галлюциногены, убийства? "
    show onka smile
    onka "Я имею в виду игры, конечно."
    show black_hare surprised_var
    hide onka
    black_hare "Ты так веселишься?"
    show onka smile
    hide black_hare
    onka "Только на мамин день рождения. Почему нет?"
    show black_hare surprised_var
    hide onka
    black_hare "Куда я попал?"
    hide black_hare
    show onka danger
    narrator "Онка отмахивается рукой и наклоняется к парню."
    show onka danger
    onka "Всем регулярно бывает невыносимо — это здоровое состояние человека."
    show onka sneaky
    onka "Особенно в космосе. "
    show onka regular
    onka "Луна никогда не станет такой, как Земля. Разве что — для бактерий."
    show black_hare regular
    hide onka
    black_hare "Надеюсь, у тебя есть другие темы для разговоров."
    show black_hare disgust_var
    narrator "Илли продолжает держаться рядом, и Аш чувствует приторный фруктовый запах."
    hide black_hare
    show onka regular
    hide black_hare
    onka "Самое сложное для меня в реализации научных причуд — делиться ими."
    onka "Например, хочу я розовых крыс — это генетика."
    onka "Хочу, чтобы светились — это системная биология."
    onka "Хочешь, чтобы они играли с тобой в шашки и жгли твое электричество — умей работать с железяками. "
    show onka thinking
    onka "Одному это сделать нереально."
    show black_hare disgust_var
    hide onka
    black_hare "А с лисами — реально?"
    hide black_hare
    show fox smile
    narrator "В дверь заходят лисы с подносами, японским столиком и подушками. Расставляют в центре комнаты."
    narrator "Облачный остается, остальные выходят за дверь."
    hide fox
    show black_hare regular
    narrator "Аш напрягается, ожидая, когда Илли отреагирует на видео в сети."
    hide black_hare
    show onka smile
    narrator "Илли качает головой в сторону подушки рядом со столиком, жестом приглашая Аша сесть."
    show onka smile
    onka "Я с ними рос. Рядом, не среди них. Как я говорил, судьба лис — это Фабрика. "
    onka "ИИ которой заботится о производстве лис. "
    onka "Она выбрала буддизм для одних каст и выращивание в колбах — для других."
    onka "Иначе они хуже будут выполнять свои функции."
    show onka danger
    onka "Ты знал, что не так давно Высшая каста ела мозг Второй и Третьей каст?"
    show black_hare disgust_var
    hide onka
    black_hare "Рад, что это в прошлом."
    show onka sneaky
    hide black_hare
    onka "Надеюсь."
    show black_hare surprised_var
    hide onka
    black_hare "Почему вечеринка в японском стиле?"
    show onka sneaky
    hide black_hare
    onka "Для разнообразия. Дед, который сделал чип массовым, был японцем."
    hide onka
    show black_hare regular_happy2
    narrator "Аш пытается разрядить обстановку, избегая неприятных разговоров, которые могут возникнуть во время паузы."
    play sound 'audio/voda.mp3'
    narrator "Лис наполняет отёко."
    show black_hare regular_happy2
    black_hare "О, ты лучше, чем первая гейся Осаки."
    hide black_hare
    show fox angry
    narrator "Лис недовольно смотрит на парня, он явно нервничает, но старается не подавать виду."
    show fox angry
    fox "Лисята надоели: убегают по ночам к Онке."
    fox "Они могут попасть в беду."
    hide fox
    show onka thinking
    narrator "Онка цыкает на лиса, показывая взглядом, что разговоров достаточно."
    hide onka
    show fox smile
    narrator "Тот дожидается, когда хозяин отвернется, и лакает подогретое саке из его чашечки."
    hide fox
    show black_hare surprised_var
    narrator "Аш удивляется, думая при этом, что со стороны ничего не видно. Но Уши выдают его."
    hide black_hare
    show onka confused
    hide black_hare
    onka "Что такое?"
    show black_hare regular_happy2
    hide onka
    black_hare "Я, знаешь, тоже ребенком спал среди кроликов."
    black_hare "Когда попал на Луну."
    black_hare "Как-то раз это спасло мне жизнь."
    black_hare "Основной купол разгерметизировался, но загоны для животных имеют отдельную систему жизнеобеспечения."
    show onka smile
    hide black_hare
    onka "Помню эту аварию. Я на Луне уже двадцать пять лет."
    show black_hare regular_happy2
    hide onka
    black_hare "И как себя чувствуешь?"
    show onka angry
    hide black_hare
    onka "Последний месяц — ужасно! Думаю, это стресс."
    onka "Еще вопросы?"
    show black_hare regular_confused
    hide onka
    black_hare "Был ли ты влюблен?"
    show onka smile
    hide black_hare
    onka "В человека или явление?"
    narrator "Он обводит взглядом лабораторию со светящимися пластинами."
    show black_hare regular_confused
    hide onka
    black_hare "Думаю, ты ответил на мой вопрос."
    hide black_hare
    show onka confused
    narrator "Хозяин Фабрики пожимает плечами. Раздается лакающий звук — это лис."
    show onka victory
    onka "Этот сад! Он кишит жизнью для разных космических объектов."
    narrator "Илли краснеет и упирается взглядом в один из стендов — с зелеными замерзшими бактериями."
    show black_hare angry_var
    hide onka
    black_hare "Сменим тему..."
    black_hare "Почему от тебя пахнет манго? Ты специально прыскаешься?"
    stop music1 fadeout 3
    play music2 'music/ayay1.mp3' fadein 3
    narrator "Онка медленно отворачивает голову от бактерий, его глаза заметно округляются."
    hide black_hare
    show onka confused
    hide black_hare
    onka "Манго? Ты не путаешь?"
    narrator "Аш утвердительно кивает головой."
    show black_hare surprised_var
    hide onka
    black_hare "Ты сам не чувствуешь?"
    hide black_hare
    show fox angry
    narrator "Лис бросает на гостя горящий недовольством взгляд."
    show fox angry
    fox "..."
    show onka thinking
    hide fox
    onka "Я не чувствую запахи."
    show onka angry
    onka "Но теперь ясно, почему мне все время плохо."
    hide onka
    show black_hare surprised_var
    hide onka
    black_hare "Почему не восстановил обоняние?"
    show onka angry
    hide black_hare
    onka "Не люблю лишнее вмешательство в организм."
    show black_hare surprised_var
    hide onka
    black_hare "А лисье зрение значит не лишнее?"
    show onka smile
    hide black_hare
    onka "Конечно!"
    narrator "Онка встает и начинает снимать с себя одежду. "
    hide onka
    show black_hare surprised_var
    hide onka
    black_hare "Думал, что уже привыкаю к тебе."
    hide black_hare
    show onka angry
    narrator "Стоящему рядом лису Онка бросает:"
    show onka angry
    onka "Проверь мою комнату! "
    onka "Найди на Фабрике манго или эфирные масло, все, что возможно!"
    show onka thinking
    onka "И без интервью, будь добр."
    hide onka
    show fox smile
    narrator "Лис, немного покачиваясь, делает реверанс. Теперь он не так сильно нервничает."
    hide fox
    show black_hare regular_confused
    hide fox
    black_hare "Мне не то чтобы сильно интересно, но для чего ты разделся?"
    show onka thinking
    hide black_hare
    onka "Нашел нам развлечение. Нужно это сжечь. "
    onka "У меня — аллергия!"
    hide onka
    show black_hare regular_happy2
    narrator "Аш хлопает себя по коленке."
    show black_hare regular_happy2
    black_hare "На Фабрике есть возможность жечь?"
    show onka sneaky
    hide black_hare
    onka "Значит, такое веселье подходит?"
    show black_hare regular_happy2
    hide onka
    black_hare "То, что обыденность — на Земле, в закрытом куполе — дорогое удовольствие."
    show onka danger
    hide black_hare
    onka "У меня есть бензин!"
    show black_hare regular_happy1
    hide onka
    black_hare "Это действительно хорошая идея!"
    show black_hare mad_var
    show black_hare mad_var
    black_hare "Для того, кто пару дней назад пытался скормить себя псам."
    hide black_hare
    pause 0.2
    scene black_background
    play sound 'audio/fire.mp3'
    narrator "Спустя несколько часов, Аш вспоминает, как Илли жег свою одежду в костре, и последнее, что они сказали друг другу:"
    show onka danger
    hide black_hare
    onka "Готов начать наш проект?"
    hide onka
    show black_hare regular
    pause
    call mad_fear
    show black_hare mood
    show black_hare mood
    black_hare "Чтобы добиться вечной жизни, нам нужно нарушить все законы."
    show onka danger
    hide black_hare
    onka "С какого начнем?"
    hide onka
    narrator "Аш смотрит в черноту и думает, готов ли взять на себя ответственность за смерть тысячи людей? "
    narrator "А то и больше тысячи?"
    stop music2 fadeout 3
    jump scene_32


label scene_32:
    pause 0.2
    scene chip_factory_laboratory
    #Аш получает триггер заняться разработкой, не только ради сестры, но и ради остальных, кто может прожить не двойную жизнь в сети, а в другом теле
    play music1 'music/newman_stars.mp3' fadein 3
    narrator "Спустя несколько недель."
    show onka thinking
    narrator "Онка вместе с лисом наблюдают за Ашем, который лежит на полу в лаборатории. Он в сети."
    show onka angry
    onka "Я думал, что после того, как получит добро, он начнет эксперимент по копированию в тело."
    show onka thinking
    onka "Но он медлит."
    onka "Когда я смогу получить столько ресурсов для обработки данных, что совершу революцию? "
    show fox angry
    hide onka
    fox "По вашему запросу — насчет пяти-шести тысяч испытуемых. Мы нашли три варианта их получения."
    fox "С разной тяжестью последствий, так как закон не поощряет такие испытания. "
    fox "Тем более, на живых. Даже на добровольцах."
    show onka angry
    hide fox
    onka "Какая разница. Наш Заяц все равно тянет время. "
    show fox smile
    hide onka
    fox "Ему очень сложно жертвовать людьми. И лисами."
    show onka thinking
    hide fox
    onka "Да. Но я до последнего надеялся, что он — самостоятельный мальчик. Зря."
    onka "Поэтому..."
    hide onka
    show fox shock
    narrator "Здание заметно вздрагивает. Лисы тревожно шепчутся. Снова чувствуется толчок."
    show onka danger
    hide fox
    onka "Скоро вернусь."
    hide onka
    show black_hare sad
    narrator "Аш вышел из сети. Первые секунды тело не двигается."
    narrator "Вокруг все трясется. "
    hide black_hare
    pause 0.2
    scene chip_factory_corridor2
    narrator "Парень выбегает в коридор. Лисы спокойно перемещаются по Фабрике, явно зная, что делать."
    show black_hare fear_var
    black_hare "Что происходит?"
    show fox angry
    hide black_hare
    fox "Тоннель под куполом провалился!"
    show black_hare fear_var
    hide fox
    black_hare "Какой именно?"
    show fox angry
    hide black_hare
    fox "На периферии... И он продолжает разрушаться."
    hide fox
    show black_hare fear_var
    narrator "Он вспоминает крики людей, стучавших в отчаянии по куполу, под которым когда-то сидел вместе с кроликами. "
    narrator "Все повторяется."
    show black_hare fear_var
    black_hare "Я должен узнать, что там происходит!"
    hide black_hare
    show fox angry
    narrator "Лис отворачивает мордочку."
    show fox angry
    fox "В аудитории есть окно. "
    fox "Но я боюсь, что зрелище может оказаться не из приятных."
    hide fox
    pause 0.2
    scene chip_factory_audience
    narrator "Аш попадает в знакомое помещение. Лис отключает затемнение стекла."
    show black_hare surprised_var
    play sound 'audio/sirena3.mp3'
    narrator "Черный Заяц не сразу понимает, что произошло. С внешней стороны купола поднимаются клубы пыли. "
    narrator "Острой режущей пыли. Которую не обтачивает ветер. "
    narrator "Она вступит в реакцию с жидкостью в легких и отравит организм токсичными соединениями."
    show black_hare fear_var
    black_hare "Мы должны открыть им!"
    narrator "Воспоминания о ночи с кроликами накрывают его. Воздух застревает в легких, и парень начинает задыхаться. "
    narrator "Он падает на пол, больно ударяясь коленями."
    narrator "Аш чувствует, как нарастает давление в голове. Перед ним, опираясь на одно колено, сидит Илли."
    narrator "Он смотрит Ашу в лицо и что-то говорит, но Аш его не слышит. Парень лишь сжимает кулаки, ощущая под ногтями кровь."
    hide black_hare
    show onka danger
    hide black_hare
    onka "Это паническая атака."
    narrator "Он берет Аша за плечи, когда тот начинает заваливаться вперед. "
    narrator "Холодные-холодные руки Илли приводят Зайца в чувство."
    hide onka
    show black_hare fear_var
    hide onka
    black_hare "Нужно помочь остальным!"
    show onka thinking
    hide black_hare
    onka "Как только возобновят герметичность. Но не сейчас."
    show black_hare fear_var
    hide onka
    black_hare "Мы не можем их оставить."
    show onka thinking
    hide black_hare
    onka "Это лунная станция, тут все знают, что надо делать в такой ситуации."
    onka "Сейчас все должны оставаться в помещениях."
    hide onka
    show black_hare sad_var
    pause
    call mad_fear
    show black_hare mood
    narrator "Аш смотрит в окно, на площадь. Над ней клубится пыль, повисая в воздухе."
    narrator "И он знает точно: когда ее отфильтруют, множество людей уже будут мертвы."
    pause
    show black_hare mad_var
    narrator "Он точно знает, что ему теперь делать."
    hide black_hare
    stop music1 fadeout 3
    jump scene_33


label scene_33:
    pause 0.2
    scene chip_factory_laboratory
    #Онка предлагает как тело – Наташу. и не принимает отговорки, Аш мечется
    play music2 'music/w.mp3' fadein 3
    narrator "На следующий день."
    narrator "Онка лежит в углу, не двигается. Голова безжизненно свешивается вниз."
    show black_hare surprised_var
    narrator "Аш входит вместе с Облачным, но тут же отскакивает назад."
    hide black_hare
    show fox shock
    hide black_hare
    fox "Неужели! Получилось?"
    hide fox
    show black_hare regular
    narrator "Аш стоит, как вкопанный. Только думает: \"Так не вовремя\"!"
    narrator "Илли резко подскакивает и вскрикивает от испуга. Он смотрит на Аша заспанными, непонимающими глазами."
    hide black_hare
    show fox angry
    hide black_hare
    fox "Я решил, Вы мертвы..."
    show black_hare angry_var
    hide fox
    black_hare "Ты прикидывался мертвым?"
    show onka angry
    hide black_hare
    onka "Что? Нет. Я всего лишь долго работал."
    show onka thinking
    onka "Ты не видел спящих людей?"
    show onka smile
    narrator "Онка щурит взгляд и расплывается в широкой улыбке."
    show onka sneaky
    onka "Ты успел испугаться!"
    narrator "Он довольно потягивается."
    hide onka
    show black_hare angry_var
    hide onka
    black_hare "Потому что отдал Фабрике свое изобретение!"
    black_hare "Но я не о том."
    pause
    show black_hare regular
    black_hare "Есть план. "
    black_hare "Нам нужно поместить одну копию в большое количество человек — от девятисот до двух тысяч."
    black_hare "Ты их найдешь?"
    show onka danger
    hide black_hare
    onka "..."
    show black_hare regular
    hide onka
    black_hare "Потом нужен итоговый тест — копию из сети поместить в тело. Да, это..."
    show onka danger
    hide black_hare
    onka "Это того стоит!"
    onka "Помню недавно, ты сомневался."
    show black_hare fear_var
    hide onka
    black_hare "Мы могли бы спасти всех тех, кто умер вчера. У них был бы шанс..."
    hide black_hare
    show onka sneaky
    narrator "Онка подходит к Ашу. Как всегда, неприятно близко, отчего Аш чувствует дискомфорт."
    show onka sneaky
    onka "Что бы ты ни потерял, распространение Ушей..."
    onka "...и возможность пересадить сознание в тело сделают жизнь людей намного лучше."
    onka "Ты сможешь довести дело до конца?"
    show black_hare sad_var
    hide onka
    black_hare "Идя на съедение к собакам, я не имел цели, надежды и желания."
    black_hare "Но сейчас все это — не только для меня."
    narrator "Заяц не хочет говорить Илли обо всем. Он ему не доверяет, слишком все гладко..."
    hide black_hare
    show onka sneaky
    hide black_hare
    onka "На счет итогового теста: я нашел то, что ты просил. "
    show onka danger
    onka "Одинока, доверчива и та еще заноза. "
    onka "Станет испытуемой или умрет."
    onka "Наташа."
    show black_hare surprised_var
    hide onka
    black_hare "!"
    hide black_hare
    pause 0.2
    scene chip_factory_vines2
    narrator "Сочувствующая. Яркая. Эгоистичная и некогда близкая?"
    show natasha smile
    narrator "В голове Аша возникает образ девушки, стоящей в комнате с инопланетными растениями."
    narrator "Аш думает, что у Онки было два повода забрать ее: трансляция с конкурса и интервью с лисом."
    hide natasha
    pause 0.2
    scene chip_factory_laboratory
    narrator "Неужели, он специально, не остановил ее на конкурсе?"
    show black_hare angry_var
    hide natasha
    black_hare "Это как-то связано с видео?"
    black_hare "Не удивительно."
    show onka angry
    hide black_hare
    onka "С каким из них?"
    show black_hare angry_var
    hide onka
    black_hare "Может, ты и с Максимом связан?"
    hide black_hare
    show onka sneaky
    narrator "Илли сжимает губы, плохо сдерживая улыбку, и пожимает плечами."
    show onka sneaky
    onka "Эта информация не нужна для принятия решения. "
    show onka danger
    onka "Или ты отказываешься?"
    narrator "За спиной хозяина Фабрики появляются лисы из Высшей касты, они скалятся."
    onka "А еще я нашел манго."
    narrator "Из толпы лис вырывается Облачный."
    hide onka
    show fox angry
    hide onka
    fox "Это он разрушил туннель!"
    show onka thinking
    hide fox
    onka "Я же не кричу: \"Это он хотел меня отравить\"!"
    show black_hare surprised_var
    hide onka
    black_hare "Что ты сделал?"
    hide black_hare
    show onka danger
    narrator "В ответ Хозяин Фабрики улыбается, показывая острые зубы."
    show onka danger
    onka "Разве это что-то изменит для всех тех людей?"
    hide onka
    show black_hare angry_var
    narrator "\"Кроме того, что они были бы живы\", — сказал Заяц сам себе."
    show black_hare angry_var
    black_hare "От тебя пришло сообщение, что Вечна копируется?"
    hide black_hare
    show onka sneaky
    narrator "Онка молчит."
    hide onka
    show black_hare angry_var
    narrator "Парень вспоминает последние слова сестры. "
    hide black_hare
    pause 0.2
    scene helpcenter
    narrator "Затянувшуюся на несколько секунд тишину разрезал полный бесконечного отчаяния крик девушки:"
    show vechna angry
    hide black_hare
    vechna "Это все он... !"
    hide vechna
    pause 0.2
    scene chip_factory_laboratory
    narrator "В голове сверкает, словно молния: \"Это все Онка\"!"
    play sound 'audio/dog.mp3'
    narrator "Лабораторию наполняют лисы с полными пастями острых зубов."
    narrator "Перемещаясь на четырех лапах, они вызывают истинный животный страх."
    show black_hare regular
    narrator "Аш думает про себя: \"Вот кто помог копии убить оригинал. Вот с кем был договор...\""
    call mad_fear
    show black_hare mood
    show black_hare mood
    black_hare "Хорошо — начали игру, значит, и закончим."
    show onka danger
    hide black_hare
    onka "Доиграть — твой единственный вариант, иначе..."
    hide onka
    show black_hare mad_var
    narrator "Черный Заяц достает из кармана фиолетовый мяч, похожий на тот, из-за которого лис на конкурсе отгрыз себе лапу."
    play sound 'audio/ryichanie.mp3'
    narrator "При взгляде на мяч, глаза Облачного загорелись безумным огнем."
    narrator "Лисы из Высшей касты окружают Аша. "
    narrator "Их глаза горят, а лаборатория погружается во тьму."
    hide black_hare
    pause 0.2
    scene black_background
    stop music2 fadeout 2
    play music1 'music/r.mp3' fadeout 2
    narrator "Самый целеустремленный человек — тот, у которого нет выбора."
    #Здесь мы рассказываем о том, где они живую и что это - опасное место. Где бояться нужно не только природы, но и себя. Аш винит себя, что это он подвел Вечну к копированию. В сцене герой должен быть крут и логичен. Он рассказывает о законе копирования.
    call end_card
