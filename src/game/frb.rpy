label scene_1:
    #Здесь мы рассказываем о том, где они живую и что это - опасное место. Где бояться нужно не только природы, но и себя. Аш винит себя, что это он подвел Вечну к копированию. В сцене герой должен быть крут и логичен. Он рассказывает о законе копирования.
    scene black_background
    #(Появляется фон.)
    #(Начинается музыка.)
    #(На фоне музыки раздается вздох молодого парня.)
    #(Появляется текст.)
    show black regular with Dissolve(.3)
    black "В начале двадцать первого века самыми большими страхами людей были высота и темнота. "
    black "В 22 веке бо́льшая часть населения Земли вынуждена десять лет жить на Луне. "
    black "Все – ради науки. "
    black "А люди больше всего на свете боятся разгерметизации лунных станций. "
    black "В ту ночь я спал в кроличьем Куполе, созданном для спасения животных при авариях."
    #(CG — спящий кролик. Раздается звук сирены. )
    #(Сменяется: CG — спящий кролик в красном, аварийном освящении.)
    black "Я услышал, как кто-то закрыл люк моего крошечного купола."
    #(Звук закрытия механического люка на фоне сирены и тишина.)
    black "Внутрь кто-то проскользнул... Это была моя девятилетняя сестра."
    #(Кролик в аварийном освящении погружается в полную темноту.)
    black "Вечна ладонями закрыла мне глаза. Кролики вокруг задрожали."
    black "А поверхность Луны отозвалась вибрацией."
    #(Эффект вибрации. Музыка развивается, становится активной.)
    #(Звук разрушения, крики, звон стекла.)
    black "Я не мог ничего видеть, но... я слышал."
    #(Стук ладоней по Куполу.)
    black "Смерть... К нам стучались. К нам ломились! "
    black "Вечна могла открыть, верно? Но она не сделала этого."
    #(Пауза, темный экран и просто музыка 1 секунду.)
    black "Это мое самое страшное воспоминание. Но так же и самое любимое."
    black "Я понял, что есть та, которая найдет меня, даже когда мир рухнет."
    black "Когда он расщепится на атомы в отголосках памяти."
    black "Ее погубило мое изобретение. "
    black "У любой технологии есть темная сторона."
    black "Желая обучить программный код распознавать эмоции, я создал монстра..."
    black "...Сделал её монстром... А поплатилась за это она.."
    black "Поплатилась три часа назад."
    jump scene_2


label scene_2 :
    scene station_corridor
    #В этой сцене мы должны увидеть, как герой стал крутым парнем из сцены 1. Он шел чтоб спасти девушку от закона копирования, но не смог. Виртуальная Вечна удалила реальную. Как? Это останется загадкой, но потом выясниться – что это Онка
    narrator "Тремя часами ранее."
    show black regular_confused with Dissolve(.3)
    narrator "В голове парня мелькнула мысль: \"Что она там делает?\""
    show black regular_angry with Dissolve(.3)
    narrator "Он несся по коридорам станции, пока не остановился перед дверью."
    show black regular_fear with Dissolve(.3)
    narrator "Аш чувствовал, что плохой конец ближе, чем он думал."
    scene helpcenter
    narrator "В Центре Помощи, выполняющего сегодня функции Центра Копирования, по ту сторону стекла, лежала его сестра."
    show vechna smile2 with Dissolve(.3)
    narrator "Вечна рассматривала потолок. Ее тело было намертво зафиксировано на кушетке."
    hide vechna
    show black regular_angry with Dissolve(.3)
    narrator "Аш попытался попасть внутрь, но Центр Копирования был занят, а значит, и доступ закрыт."
    show black regular_fear with Dissolve(.3)
    black "Вечна, все в порядке?"
    narrator "  Его заглушил голос."
    hide black
    robotic_voice "Оцифровка прошла успешно. Поздравляем!"
    show vechna smile2 with Dissolve(.3)
    narrator "Девушка заметила брата и повернула голову в его сторону."
    show vechna smile2 with Dissolve(.3)
    vechna "Замечательно! Можете меня расстегнуть? За мной пришли."
    robotic_voice "Мы обязаны вас выключить, по запросу о сохранении индивидуальности."
    show vechna thinking with Dissolve(.3)
    narrator "На ее лице на секунду мелькнуло непонимание. "
    narrator "А затем радость сменилась нарастающим чувством тревоги."
    robotic_voice "Причина: копия в сети признана первичной личностью."
    hide robotic_voice
    vechna "Эм, как так? Стоп-стоп-стоп! Обычно все наоборот!"
    show digital_vechna smile1 with Dissolve(.3)
    narrator "Перед глазами Вечны развернулась голограмма. "
    narrator "Девушка посмотрела на нее сосредоточенным взглядом."
    narrator "Это были ее собственные глаза, но такие холодные и чужие..."
    hide vechna
    hide digital_vechna
    show black regular_angry with Dissolve(.3)
    black "Что происходит? Вечна?"
    hide black
    show digital_vechna smile1 with Dissolve(.3)
    narrator "Он как будто задумался, к какой из версий девушки обращаться. Они похожи, как две капли воды."
    show vechna sad with Dissolve(.3)
    narrator "В горле настоящей Вечны стоял ком. "
    narrator "Она абсолютно точно понимала, как поступит девушка с холодными глазами. "
    show vechna thinking with Dissolve(.3)
    narrator "Ведь она поступила бы точно так же."
    show vechna angry with Dissolve(.3)
    vechna "Не удаляй меня! Слышишь?!"
    vechna "Здесь же Аш, как ты можешь?.."
    narrator "Ее крик взорвал стены Центра Копирования. Но дошли ли ее слова до копии?"
    hide vechna
    show digital_vechna thinking with Dissolve(.3)
    digital_vechna "Его не должно здесь быть. К тому же, на моем месте ты поступила бы также. "
    digital_vechna "Мы обе это понимаем, верно?.. Я не могу делить с кем-то свою индивидуальность."
    digital_vechna "Мы не можем существовать в двух экземплярах."
    show vechna sad with Dissolve(.3)
    narrator "Лежа на кушетке, девушка глубоко дышала, пытаясь собраться с мыслями."
    narrator "Оригинальная версия проглотила ком, ресницы перестали дрожать. "
    narrator "Она облизнула губы, и ее голос зазвучал спокойно."
    show vechna smile2 with Dissolve(.3)
    vechna "Я знаю, почему мы поступаем именно так. "
    vechna "И ты, так же как и я, знаешь основное допущение. Которое ломает все аргументы."
    vechna "Зачем тебе индивидуальность? "
    hide vechna
    show digital_vechna thinking with Dissolve(.3)
    digital_vechna "Могу ли я допустить, чтобы кто-то еще использовал мой интеллект? Я пока не настолько открыта новому."
    show vechna sad with Dissolve(.3)
    narrator "Эти слова сильно задели девушку на кушетке. "
    narrator "Ирония в том, что это были слова копии в сети, но они удивительно точно передавали ее собственные недавние размышления."
    vechna "Ты и так получаешь мою мечту, дрянь!"
    show vechna angry with Dissolve(.3)
    vechna "Я не смогу сама попасть в сеть! Это можешь сделать только ты — моя копия. "
    vechna "Ты! Ты получишь вычислительные мощности!"
    hide vechna
    show digital_vechna smile1 with Dissolve(.3)
    digital_vechna "Именно поэтому цифровая копия — ведущее сознание. "
    digital_vechna "В цифре я сделаю больше, чем две \"настоящие\" Вечны. "
    digital_vechna "Ты сама знаешь про уговор!"
    hide digital_vechna
    show vechna sad with Dissolve(.3)
    vechna "Это ошибка! Такого уговора не было!.."
    narrator "Девушка перешла на шепот, всем лицом выражая мольбу."
    narrator "Пространство вокруг сжалось, и не осталось ничего, кроме слов. Слов входящих и исходящих."
    vechna "Я откажусь от всего. Не убивай меня! "
    vechna "Это я – исходная личность! Почему решаешь ты?"
    hide vechna
    show digital_vechna smile1 with Dissolve(.3)
    digital_vechna "Мне помогли... И, знаешь... Через год или два ты удалила бы меня!"
    hide digital_vechna
    show vechna sad with Dissolve(.3)
    vechna "Но мы так не договаривались! Как же брат?.."
    hide vechna
    show digital_vechna smile1 with Dissolve(.3)
    narrator "Цифровая Вечна повернулась к стеклу, разделяющему ее и брата. Парень ломился в дверь."
    show digital_vechna smile1 with Dissolve(.3)
    digital_vechna "У него буду я."
    show vechna sad with Dissolve(.3)
    narrator "Ответ был пронизан холодом. Она могла стерпеть что угодно. Но это было, как лезвие самого острого ножа. "
    show vechna sad with Dissolve(.3)
    vechna "Как же я безжалостна к себе!"
    narrator "Она плакала, ее руки тряслись. Отчаянный смех пробивался сквозь слезы обреченности."
    narrator "\"Славно\" вот так лежать, осознавая, что собственными руками изобрел самый оригинальный способ самоубийства."
    hide vechna
    show digital_vechna smile2 with Dissolve(.3)
    narrator "Безнадежное положение, в котором тебя убивает твоя собственная копия."
    hide digital_vechna
    show vechna thinking with Dissolve(.3)
    narrator "Выход есть всегда? "
    narrator "Только не здесь. Все это напоминает Луну, где за пределами купола тебя ждут лишь тьма, холод и смерть."
    show vechna thinking with Dissolve(.3)
    vechna "Ты в сговоре с этим богатым ублюдком! "
    vechna "Он обманул меня! И тебя ждет такая же участь, не сомневайся!"
    show vechna sad with Dissolve(.3)
    narrator "Она взглянула на Аша. На его лицо, искаженное стеклом, заляпанным кровью."
    hide vechna
    show black regular_sad with Dissolve(.3)
    narrator "Он отчаянно бился лбом и руками. "
    narrator "Но что это изменит? "
    narrator "Даже если его упрямства хватит, чтобы преодолеть стекло, его не хватит, чтобы преодолеть барьер между жизнью и смертью."
    narrator "Затянувшуюся на несколько секунд тишину разрезал полный бесконечного отчаяния крик девушки:"
    hide black
    show vechna sad with Dissolve(.3)
    vechna "Это все он!!!"
    narrator "Ее заглушил голос станции:"
    robotic_voice "Автоматическая подача газа запущена."
    hide vechna
    show vechna sad with Dissolve(.3)
    hide vechna
    hide vechna
    show black regular_angry with Dissolve(.3)
    black "Нет! Отключите! Отключите, это ошибка! Живая девушка, - исходная личность! Не наоборот!"
    hide black
    show vechna sad with Dissolve(.3)
    narrator "Пальцы ее рук онемели."
    narrator "Девушка понимала, что у нее нет шансов выстоять против самой себя. Она умирает. "
    narrator "Слезы теплым ручьем струились из глаз, стекая по вискам."
    narrator "Вскоре фиксирующие браслеты, удерживавшие девушку на кушетке, перестали натягиваться."
    hide vechna
    narrator "Кисти безжизненно повисли, приобретая мертвый синий оттенок."
    show black regular_sad with Dissolve(.3)
    narrator "Аш только молча наблюдал. Все это время. "
    narrator "Внутрь помещения вошли чистые до блеска роботы и подняли тело девушки."
    show black regular_angry with Dissolve(.3)
    black "Нет! Пустите меня к ней! Пустите!"
    hide black
    show digital_vechna smile1 with Dissolve(.3)
    digital_vechna "Не плачь! Я же здесь!"
    hide digital_vechna
    show black regular_angry with Dissolve(.3)
    black "Как ты это сделала? Как ты стала главной?!"
    black "Ты мне не сестра! Ты – чудовище!"
    black "Копии – не люди! Они не принимают решения!"
    hide black
    show digital_vechna thinking with Dissolve(.3)
    digital_vechna "Я покажу тебе, я все объясню..."
    hide digital_vechna
    narrator "А затем, внезапно, даже цифровая копия сестры покинула его. "
    show black regular_surprised with Dissolve(.3)
    narrator "Исчезла, словно не по своей воле."
    narrator "Его разум никак не мог осознать произошедшее. "
    narrator "В голове раз за разом крутилась лишь одна фраза: \"Это все он…\"."
    show black regular_sad with Dissolve(.3)
    black "Зачем я дал ей код! Это я во всем виноват!"
    narrator "Как же быстро все произошло… "
    narrator "Аш лишь поднял голову, собираясь уходить, а комната уже была стерильно чиста."
    narrator "Словно ничего и не произошло. "
    narrator "Словно еще несколько минут назад здесь трагически не оборвалась жизнь."
    narrator "Перед ним высветилось сообщение в смешанной реальности: \"Центр Копирования свободен, отправьте запрос...\""
    jump scene_3


label scene_3:
    scene helpcentere_3
    narrator "Прошел час, после копирования Вечны."
    #(Показываем уведомление для игрока: Распознайте эмоции героя – от этого зависит, какие эмоции увидят на Ушах другие персонажи)
    #(Показываем героя в центре помощи. Он сидит на полу и проверяет свою очередь. Еще пять человек до него.)
    show black regular_sad with Dissolve(.3)
    black "Это все он... Неужели она имела в виду меня?"
    call angry_sad
    black "Хотя, кому я вру? Это все правда."
    black "Я просто хотел научить Уши распознавать эмоции. Я совсем не хотел..."
    black "Я не должен был давать тебе то, что ты так просила."
    black "Все мои действия во благо обернулись злом. Все..."
    jump scene_4


label scene_4 :
    scene planet
    #Показывая свою планету, она уговаривает его дать доступ к коду Ушей и объясняет для чего ей это. Он соглашается, но просит ее быть на выступлении и уходит
    narrator "3 месяца назад..."
    show black regular_surprised with Dissolve(.3)
    narrator "Аш посмотрел под ноги. Песок. Но не такой, как лунный грунт, и не такой, как любой песок с Земли. "
    show black regular with Dissolve(.3)
    narrator "Похож на перемолотые кристаллы красно-рубинового цвета. "
    narrator "Над головой - атмосфера. Она кажется настолько густой и насыщенной парами... "
    narrator "...Что розовые скопления облаков, того и гляди, начнут падать под собственной тяжестью."
    hide black
    show vechna smile1 with Dissolve(.3)
    vechna "Круто, да? "
    vechna "Такие облака образуются только между темной и светлой сторонами планеты. "
    vechna "Там такие перепады температур - сдохнуть можно!"
    hide vechna
    show black regular_surprised with Dissolve(.3)
    narrator "Парень поднял голову вверх."
    show black sad_var with Dissolve(.3)
    black "Как я скучаю по небу."
    hide black
    show vechna smile2 with Dissolve(.3)
    vechna "Все, кто под куполом, скучают по небу. "
    vechna "Но есть сеть: тут тебе и земное небо, и небо, спроектированное мной!"
    narrator "Она сделала несколько движений пальцами - и раскрылась модель галактики. "
    narrator "Вечна отмотала изображение куда-то влево, на периферию Млечного Пути."
    vechna "Это невообразимо далеко. Ровер добирался туда восемьдесят лет, Ашик!"
    hide vechna
    show black angry_var with Dissolve(.3)
    black "Ты своим \"Ашиком\" весь драматизм ситуации убила."
    narrator "В густых красных облаках засверкали молнии."
    show black regular_surprised with Dissolve(.3)
    narrator "Казалось, небеса захлестнула электронная музыка."
    hide black
    show vechna smile1 with Dissolve(.3)
    narrator "Вечна в нетерпении захлопала в ладоши и вытянула шею, будто бы желая стать хоть чуточку ближе к облакам."
    hide vechna
    show black regular_confused with Dissolve(.3)
    black "Что-то начинается?"
    hide black
    show vechna smile1 with Dissolve(.3)
    narrator "Видя, что сестра смотрит на небо и не реагирует, парень тоже решил уделить ему все свое внимание."
    narrator "Тучи разразились красными, сверкающими, будто бы кровавыми, слезами-каплями."
    narrator "Крупные кристаллы дождем посыпались на их головы."
    hide vechna
    hide vechna
    show black regular_fear with Dissolve(.3)
    black "Ааа!"
    narrator "Аш испугался. Но кристаллы не коснулись его."
    black "Они проходят насквозь?"
    hide black
    show vechna sad with Dissolve(.3)
    vechna "Пока не доделаю, на мир можно только смотреть, но не чувствовать."
    hide vechna
    show black regular_confused with Dissolve(.3)
    black "Почему?"
    hide black
    show vechna thinking with Dissolve(.3)
    narrator "Вечна сделала недовольное лицо. "
    show vechna sad with Dissolve(.3)
    narrator "Присела на корточки и попыталась зачерпнуть розовый кристальный песок."
    show vechna sad with Dissolve(.3)
    vechna "Я не успела проработать все подробно. "
    vechna "За обработку данных с исследовательских устройств мне не платят."
    hide vechna
    show black regular_happy1 with Dissolve(.3)
    black "Не переживай, ты найдешь себе именно такую работу, как хочешь!"
    hide black
    show vechna smile2 with Dissolve(.3)
    narrator "Девушка встала, и он обнял ее за плечи. Она ответила ему усталой улыбкой. "
    narrator "Словно давно, уже в который раз, пыталась что-то ему объяснить."
    show vechna sad with Dissolve(.3)
    vechna "Лучшее, что может быть, — это полное отсутствие причин заниматься чем-то другим, кроме создания далеких миров."
    vechna "А у меня и нет их, этих причин... Но и возможностей заниматься только этим тоже нет."
    hide vechna
    show black sad_var with Dissolve(.3)
    narrator "Лицо брата изменилось. "
    narrator "Вечна заметила это."
    hide black
    show vechna thinking with Dissolve(.3)
    vechna "Нет смысла грустить."
    hide vechna
    show black angry_var with Dissolve(.3)
    black "Ты ругаешь меня за мои чувства?"
    narrator "Его глаза выражали осуждение, Вечна же свои закатила."
    hide black
    show vechna thinking with Dissolve(.3)
    vechna "Нет. Но и ты тоже не обижайся на меня за мои чувства."
    vechna "Тем более, что ты можешь мне помочь..."
    hide vechna
    show black angry_var with Dissolve(.3)
    black "Ты опять за свое. Это опасно."
    hide black
    show vechna thinking with Dissolve(.3)
    vechna "Эээх!"
    hide vechna
    show black regular with Dissolve(.3)
    black "Лучше я займусь едой."
    hide black
    show vechna sad with Dissolve(.3)
    vechna "Как хочешь. "
    vechna "Что ж, пока я тут, нужно закрыть пару задач по работе."
    narrator "Аш вышел из сети."
    jump scene_5


label scene_5:
    scene home
    narrator "Поднявшись, и немного попрыгав на месте, Вечна потянулась и сделала колесо."
    show vechna thinking with Dissolve(.3)
    vechna "Когда находишься в реальности, почти все время приходится упражняться."
    hide vechna
    show black sad_var with Dissolve(.3)
    black "Потому что ты любую свободную минуту проводишь в сети."
    #(Девушка гримасничает.)
    narrator "Вечна схватила с дивана плюшевую коалу и резко надавила. Голова с громким \"чпоком\" отделилась от плюшевого тела."
    black "Я починю, не переживай."
    hide black
    show vechna smile2 with Dissolve(.3)
    vechna "Ты просто лапушка-коалушка! "
    vechna "Я хочу вечером начать обработку новых данных от ровера. "
    vechna "Мой рейтинг ниже, чем у копий в сети! "
    vechna "Конечно, легко иметь высокие показатели, если можешь работать 24/7. "
    vechna "Меня хватает только на четырнадцать часов в день! "
    vechna "Да и то через неделю выдыхаюсь."
    vechna "Еще и все эти уборки, уход за собой, спорт..."
    narrator "Ее передернуло."
    hide vechna
    show black angry_var with Dissolve(.3)
    black "Ты давно не занималась уборкой."
    hide black
    show vechna thinking with Dissolve(.3)
    narrator "Она всплеснула руками, раздражаясь."
    show vechna thinking with Dissolve(.3)
    vechna "Двадцать второй век на дворе! А пыль все равно не победили. Под куполом, блин, на Луне!"
    hide vechna
    show black angry_var with Dissolve(.3)
    black "Ты отлично знаешь, что это пыль из пещер. Гигантские тоннели все равно будут пылить."
    hide black
    show vechna thinking with Dissolve(.3)
    vechna "Жестокая жизнь колонистов."
    narrator "Она вздохнула."
    vechna "Еда готова?"
    hide vechna
    show black regular_happy2 with Dissolve(.3)
    black "Сегодня праздник. Поэтому есть кое-что особенное."
    hide black
    show vechna thinking with Dissolve(.3)
    vechna "Сегодня день траура, милый. "
    vechna "24 августа 2025 года, в 23:50, под куполом было шестьсот пятьдесят человек. "
    vechna "А через пятнадцать минут осталось всего двести."
    hide vechna
    show black regular_sad with Dissolve(.3)
    black "Но нам же повезло. Хотя после всего нас могли бы и вернуть на Землю."
    hide black
    show vechna thinking with Dissolve(.3)
    vechna "Нам скорее повезло, потому что ты спал с животинками. "
    vechna "Вообще, \"везение\" - веселенькое понятие. "
    vechna "Смотри, нам \"повезло\" выиграть на Земле в лотерею, чтоб свалить в космос, а потом \"повезло\" чуть не умереть в первый месяц! "
    vechna "Получается — везение на невезение."
    hide vechna
    show black regular_happy1 with Dissolve(.3)
    narrator "Брат взял плюшевую голову коалы и кинул в сестру."
    hide black
    show vechna smile2 with Dissolve(.3)
    vechna "Ты со своей едой самым подлым образом отвлекаешь меня от работы."
    vechna "А-та-та. Три кота. А голова у них - одна."
    narrator "Она залилась смехом."
    hide vechna
    show black regular_happy1 with Dissolve(.3)
    black "Очень черный юмор. Тебе же нужно есть, чтоб работать."
    narrator "Он с чем-то копался на кухне. Комнату заполнили светлячки, и когда Аш погасил свет, подсветили собой помещение."
    hide black
    hide black
    show vechna smile1 with Dissolve(.3)
    vechna "Божечки-кошечки! Если можно получить разрыв сердца из-за красоты, я его получу!"
    vechna "Я хочу есть их в темноте! Ты ведь не всех выпустил их фудрариума? "
    narrator "Младший брат был доволен, что угодил сестре."
    hide vechna
    show black regular_happy1 with Dissolve(.3)
    black "Конечно, я оставил светлячков на салат. Хотя они и симпатичные, но в первую очередь - еда. "
    black "Об этом нужно помнить."
    hide black
    show vechna smile1 with Dissolve(.3)
    narrator "Вечна хлопала в ладоши, пока брат в полумраке расставлял посуду с едой: салат с бабочками, рагу из сверчков и пирожные."
    show vechna smile1 with Dissolve(.3)
    vechna "Ты такой хороший."
    show vechna sad with Dissolve(.3)
    narrator "Девушка стала грустной."
    hide vechna
    show black regular_confused with Dissolve(.3)
    black "Ты чего это загрустила?"
    hide black
    show vechna sad with Dissolve(.3)
    narrator "Вечна положила пластиковые палочки рядом с тарелкой."
    show vechna sad with Dissolve(.3)
    vechna "Мне грустно от твоих слов, что я тут будто бы и не живу..."
    vechna "Я не могу работать меньше... Напротив, стремлюсь делать как можно больше."
    hide vechna
    show black regular with Dissolve(.3)
    black "Разве ты не сделала уже все, что могла? Ты что, хочешь вообще не спать?"
    hide black
    show vechna sad with Dissolve(.3)
    vechna "Ну, раньше так и было. А сейчас ты можешь мне помочь."
    hide vechna
    show black angry_var with Dissolve(.3)
    black "Опять? Твои идеи это слишком."
    hide black
    show vechna thinking with Dissolve(.3)
    vechna "Идея это – фантазия. "
    vechna "Ну а у тебя - есть готовое решение для меня!"
    hide vechna
    show black regular_annoyed with Dissolve(.3)
    narrator "Аш напрягся. Он знал, что сестра может мыслить слишком нестандартно, и при этом не знает границ."
    hide black
    show vechna smile2 with Dissolve(.3)
    vechna "Ты же написал софт для обучения Ушей, который распознает эмоции и выводит их на импланты. "
    vechna "Если ты можешь научить распознавать эмоции, значит, можно научить распознавать и другие активности мозга."
    vechna "А значит, можно что-то засечь. А то, что можно засечь - можно изменить."
    vechna "Софт Ушей ведь работает на основе чипа, с помощью которого мы выходим в сеть. "
    vechna "Эта железяка может усиливать или ослаблять связи. "
    vechna "Я могу хакнуть себя, понимаешь? Могу стать продуктивнее!"
    vechna "Дашь доступ к коду?"
    hide vechna
    show black regular_confused with Dissolve(.3)
    call angry_sad
    narrator "Аш подавился светлячком и выплюнул его в тарелку. "
    narrator "Тот, конечно, постарался улизнуть. Вечна с омерзением отодвинула свой салат."
    hide black
    show vechna thinking with Dissolve(.3)
    vechna "Ты опять не умертвил их в вакуумном шкафу? Это уже слишком. "
    vechna "Есть живых запрещено везде, кроме парочки отсталых стран."
    hide vechna
    show black regular with Dissolve(.3)
    narrator "Парень пристально смотрел в свою тарелку..."
    show black angry_var with Dissolve(.3)
    black "Почему-то мне это не нравится."
    hide black
    show vechna smile2 with Dissolve(.3)
    vechna "Так дашь доступ к BitBacket? Я просто посмотрю код. Что там, да как."
    hide vechna
    show black angry_var with Dissolve(.3)
    black "Уже 10:00. Мне нужно на презентацию."
    hide black
    show vechna smile2 with Dissolve(.3)
    vechna "Ты ведь видел мой проект! Разве он не потрясный?"
    vechna "По набору нулей и единичек я воссоздаю настолько далекие миры, что мы с тобой умрем, пока долетим туда!"
    vechna "Ну пожалуйста! Ты же мне доверяешь?"
    hide vechna
    show black sad_var with Dissolve(.3)
    black "Доверяю... Я поделюсь доступом. "
    black "Но будь на моей презентации."
    hide black
    show vechna smile2 with Dissolve(.3)
    vechna "Спасибо, спасибо! Ты самый лучший!"
    vechna "Можно доступ прямо сейчас?"
    hide vechna
    show black regular with Dissolve(.3)
    black "Только приходи в реальности, не в сети. Мне так спокойней. "
    black "Я могу получить отличные инвестиции, и сделать Уши массовым продуктом на Луне и Земле."
    hide black
    show vechna smile2 with Dissolve(.3)
    vechna "Эх... Кому нужны Луна или Земля, когда можно пройтись по мирам, не имеющим названий?"
    hide vechna
    show black regular_annoyed with Dissolve(.3)
    black "Мне нужны, и тебе. Хоть ты в этом и не признаешься."
    narrator "Брат положил палочки на тарелку, сжал концы, и те стали разлагаться, сливаясь с остатками еды в общую вязкую массу. Затем встал."
    black "Мне пора. "
    narrator "Он остановился у выхода."
    hide black
    show vechna smile2 with Dissolve(.3)
    vechna "Хорошо. Только не забудь про доступ."
    hide vechna
    show black regular with Dissolve(.3)
    black "Уже дал. "
    black "Жаль, ведь чем более проработанной будет твоя симуляция, тем мучительнее будет находиться там человеку."
    hide black
    show vechna smile2 with Dissolve(.3)
    vechna "Конечно, атмосфера же состоит из кислот!"
    jump scene_6


label scene_6 :
    scene audience
    #Аш рассказывает о благородной цели ушей. Появляется Макс у и них происходит конфликт.
    show black sad_var with Dissolve(.3)
    narrator "Аш ждал Вечну."
    narrator "Недалеко, в другом конце аудитории, туда-обратно ходил парень. "
    narrator "Его однокурсник. Тот, кто побеждал во всех конкурсах."
    hide black
    show maks regular with Dissolve(.3)
    narrator "Выглядел он соответствующе: самоуверенно и нахально."
    narrator "Обычно, людей по одежке только встречают. "
    narrator "Но, как только появляется новая информация, она начинает незамедлительно применяться, меняя впечатление о человеке."
    narrator "Про Макса Аш думал, что это - не тот случай. И именно первое мнение оказалось самым верным. "
    narrator "Блондин репетировал выступление."
    show maks regular with Dissolve(.3)
    hide maks
    show black regular_annoyed with Dissolve(.3)
    narrator "Аш пытался его не слушать. Время в ожидании Вечны тянулось бесконечно."
    show black angry_var with Dissolve(.3)
    hide black
    hide black
    show maks regular with Dissolve(.3)
    maks "Автоматическая система озеленения: дроны, которые самостоятельно решают.."
    maks "..Где и какие растения нужно рассадить, в какое время года это лучше делать. "
    maks "Они смогут сами заказывать необходимые семена из банков..."
    maks "..Отслеживать процент успешных всходов и, конечно, возвращаться на станцию для зарядки. "
    maks "Во второй версии предусматривается возможность самодиагностики, чтобы в случае необходимости прибыть на станцию техобслуживания."
    maks "Технология актуальна для Земли..."
    hide maks
    show black regular_annoyed with Dissolve(.3)
    narrator "Вечны все не было. Аш злился. "
    show black angry_var with Dissolve(.3)
    black "Таких проектов куча! "
    hide black
    show maks regular with Dissolve(.3)
    maks "Значит, есть сформированный рынок и спрос. "
    maks "Прикинь, в бизнесе это \"плюс\", а не \"минус\". "
    narrator "Он рассмеялся."
    maks "Нужно искать занятие на будущее, уже на Земле. "
    hide maks
    hide maks
    show black regular_annoyed with Dissolve(.3)
    black "Я думал, ты ошиваешься преимущественно в сети."
    hide black
    show maks angry with Dissolve(.3)
    narrator "Максим скривил губы и сделал шаг в сторону темноволосого. "
    narrator "Он размахнулся и бросил рулон армированного скотча BRUTAL Ашу в голову. "
    hide maks
    show black angry_var with Dissolve(.3)
    narrator "Тот поймал рулон."
    hide black
    hide black
    show maks angry with Dissolve(.3)
    maks "Не смей говорить со мной про сеть. Я ее ненавижу."
    narrator "И никаких сомнений в обратном не было..."
    hide maks
    hide maks
    show black angry_var with Dissolve(.3)
    black "Что ты, как дикарь какой-то? Я это забираю."
    narrator "Парень убрал моток в карман и развернулся."
    black "Все такие нервные."
    hide black
    show maks regular with Dissolve(.3)
    narrator "Максим, проговаривая презентацию, сел в первый ряд и положил ноги на стол."
    jump scene_7


label scene_7:
    scene audience
    #Появляется Онка. 
    narrator "В следующий момент, статной походкой в аудиторию зашел броско одетый мужчина, за которым проскользнул рыжий хвост."
    show onka regular with Dissolve(.3)
    narrator "Мужчина сел на скамейку, близко-близко к Максиму, практически столкнув его с занятого места."
    narrator "Для зрителей в сети это место скоро облепят бейджами \"Жюри\" и \"Потрясный Илли Онка\". "
    hide onka
    show fox collar_smile with Dissolve(.3)
    narrator "Под ногами у человека в фиолетовом разместился лис с белым воротничком на шее. "
    hide fox
    show maks regular with Dissolve(.3)
    narrator "Максима никак не задело это вторжение. Он продолжал насмешливо сверлить Аша глазами."
    hide maks
    show onka regular with Dissolve(.3)
    narrator "Онка обратил внимание на светящийся в дополненной реальности бейдж выступающего и обратился к Максиму:"
    show onka smile with Dissolve(.3)
    onka "Когда Ваш выход?"
    hide onka
    show maks regular with Dissolve(.3)
    maks "После первой звезды."
    hide maks
    show onka confused with Dissolve(.3)
    onka "Дерзко! Но тут так скучно, что я прощу."
    hide onka
    show maks regular with Dissolve(.3)
    maks "Я Вас тоже, так и быть, прощу."
    narrator "Максим презрительно посмотрел на Онку и пошел в другой угол аудитории."
    hide maks
    show onka thinking with Dissolve(.3)
    onka "Воспитание у парня хуже, чем его настроение."
    onka "Вас папа манерам не учил?"
    hide onka
    show maks angry with Dissolve(.3)
    maks "У меня теперь нет папы."
    hide maks
    show black regular_confused with Dissolve(.3)
    narrator "Аш наблюдал за сценой издалека. Это было интересно."
    hide black
    hide black
    show onka sneaky with Dissolve(.3)
    onka "Давай осмотримся, раз уж я вышел с Фабрики."
    hide onka
    show fox collar_smile with Dissolve(.3)
    narrator "Лис в голубом неоновом ошейнике держался рядом с хозяином, словно на привязи."
    hide fox
    hide fox
    show onka sneaky with Dissolve(.3)
    onka "Вы молодцы, что успели доделать бесконтактный ошейник не за три года, а за три месяца."
    hide onka
    show fox collar_smile with Dissolve(.3)
    narrator "Взгляд лиса забегал, он наклонил свою голову и начал вылизывать пятно на груди."
    hide fox
    hide fox
    show onka sneaky with Dissolve(.3)
    onka "Как долго будут идти презентации?"
    hide onka
    show fox collar_smile with Dissolve(.3)
    fox "Пару часов. Желающих идти к Вам на суд оказалось, как ни странно, много."
    hide fox
    show onka sneaky with Dissolve(.3)
    onka "А ты из какой касты?"
    hide onka
    show fox collar_angry with Dissolve(.3)
    fox "Из низшей."
    hide fox
    show onka smile with Dissolve(.3)
    onka "Что думаешь насчет перехода в высшую касту?"
    hide onka
    show fox collar_shock with Dissolve(.3)
    narrator "Лис был возбужден и выбежал перед хозяином вперед, на довольно большое расстояние."
    show fox collar_shock with Dissolve(.3)
    fox "Огромное спасибо! Я бы очень хотел, очень! "
    hide fox
    show onka sneaky with Dissolve(.3)
    narrator "Рыжий провел глазами от себя до лиса, отмечая расстояние, на которое от него убежало животное."
    narrator "Хозяин засмеялся."
    show onka smile with Dissolve(.3)
    onka "Вот это технологии! "
    onka "Ошейник не нужно выключать? Или он удерживает на километры, а не на полтора метра?"
    hide onka
    show fox collar_shock with Dissolve(.3)
    narrator "Лис кинулся под ноги Онке."
    show fox collar_shock with Dissolve(.3)
    fox "Чую, я буду сегодня на ужин."
    hide fox
    hide fox
    show onka thinking with Dissolve(.3)
    onka "Я не..."
    narrator "Онка закатывает глаза и терпеливо продолжает."
    onka "Я не скармливаю вас друг другу. Хватит читать бред в сети. "
    onka "Вы и сами неплохо грызетесь."
    onka "Я схитрил насчет ошейника, знал, что это фикция. Лучше сними его."
    onka "А то потом объясняйся в СМИ, когда это выйдет на рынок."
    hide onka
    show fox shock with Dissolve(.3)
    fox "С ошейником так вышло. "
    fox "Высшие лисы сказали, он должен быть, но проект не закончен!"
    hide fox
    show black regular_happy1 with Dissolve(.3)
    narrator "Ашу показалось это забавным. Было очевидно, \"кто\" и \"что\" перед ним. "
    narrator "Он на миг забыл о сестре, глядя на пушистую морду."
    show black regular_happy1 with Dissolve(.3)
    black "Добрый день!"
    hide black
    show onka smile with Dissolve(.3)
    onka "О! Земное приветствие! Я уже давно путаюсь, когда день, а когда ночь."
    hide onka
    show black regular_happy2 with Dissolve(.3)
    narrator "Аш с азартом рассматривал Лиса, нагнувшись, чтоб заглянуть ему в мордочку."
    show black regular_happy2 with Dissolve(.3)
    black "Моя сестра такого хотела. Любит всех пушистых. "
    black "Но черт знает, где ее сейчас носит..."
    hide black
    show fox angry with Dissolve(.3)
    fox "Некрасиво перебивать! "
    fox "Я, между прочим, объяснялся с хозяином Фабрики Чипов, с Самим..."
    hide fox
    show onka danger with Dissolve(.3)
    narrator "Онка отодвинул Лиса от себя, посмотрев на него так, что тот снова поверил, будто Илли действительно скармливает лисам лис…"
    show onka regular with Dissolve(.3)
    onka "Прошу прощения. Он взбалмошный… И презентует меня излишне пафосно."
    hide onka
    show black regular_happy2 with Dissolve(.3)
    black "Мне кажется, в нем все прекрасно."
    hide black
    show fox smile with Dissolve(.3)
    fox "Благодарю!"
    hide fox
    hide fox
    show black regular_confused with Dissolve(.3)
    black "Но я не видел подобных моделей в продаже. Те не говорят!"
    hide black
    show fox angry with Dissolve(.3)
    narrator "Лис вышел вперед."
    show fox angry with Dissolve(.3)
    fox "Личность не продается. Стоит рассказать вам поучительную историю..."
    hide fox
    hide fox
    show onka sneaky with Dissolve(.3)
    onka "Очень разумных мы не продаем. "
    onka "А этого забирай бесплатно."
    hide onka
    show fox shock with Dissolve(.3)
    hide fox
    hide fox
    show onka smile with Dissolve(.3)
    onka "Фокус группа показала, что люди хотят иметь молчаливых друзей."
    onka "А не как в том древнем меме с собакой, которая делает больно по-другому."
    #(Прозвенел старт.)
    onka "Мне пора в жюри. Судить, разумеется."
    #(Улыбается.)
    hide onka
    show black regular_happy2 with Dissolve(.3)
    black "А мне, похоже, пора быть судимым."
    black "Приятно было познакомиться."
    show black regular with Dissolve(.3)
    narrator "Аш шел ближе к сцене, обдумывая, что хорошие отношения с жюри - это плюс балл к его выступлению."
    black "И все-таки, где Вечна?"
    hide black
    show onka sneaky with Dissolve(.3)
    narrator "В это время Онка посмотрел вслед Ашу."
    show onka sneaky with Dissolve(.3)
    onka "Все-таки странный аксессуар у него на голове. Да? Тем не менее, для продаж в этом только плюсы, ха."
    hide onka
    show fox angry with Dissolve(.3)
    fox "Лучше бы лисьи Уши сделал."
    narrator "Онка засмеялся."
    fox "Нам пора начинать судить."
    hide fox
    hide fox
    show onka smile with Dissolve(.3)
    onka "Мне пора, не нам."
    hide onka
    show fox smile with Dissolve(.3)
    narrator "Но лис молча улыбался, идя в ногу рядом с самим Илли Онкой, и витая в своих лисьих рыжих облаках..."
    jump scene_8


label scene_8:
    scene audience
    #Аш рассказывает о своем изобретении. Появляется Максим. Показываем, что вечна не приходит.
    show onka sad with Dissolve(.3)
    narrator "Несколько часов Онка зевал. И оживился лишь во время выступления Макса. "
    narrator "Да и то - ради того, чтоб завалить его вопросами. "
    narrator "Пришла очередь Аша. В аудитории погас свет."
    show onka smile with Dissolve(.3)
    onka "Веселье выходит в плюс!"
    narrator "Илли подался вперед, уперев локти в стол и столкнув пустой стакан."
    hide onka
    show black regular with Dissolve(.3)
    narrator "Свет от камер падал на Аша, находящегося в центре сцены."
    hide black
    hide black
    show onka sneaky with Dissolve(.3)
    onka "Смотри, еще один наш знакомый!"
    hide onka
    show fox smile with Dissolve(.3)
    narrator "Лис, в качестве ответа хозяину, довольно вывалил язык."
    hide fox
    show black regular with Dissolve(.3)
    narrator "Аш пытался найти глазами Вечну, хотя никто этого и не видел. "
    call angry_sad
    narrator "Аш пытался сосредоточиться: \"Важный момент. Соберись…\""
    show black regular with Dissolve(.3)
    black "Спасибо, что дождались последнего выступления."
    hide black
    show maks regular with Dissolve(.3)
    narrator "В ответ Максим ухмыльнулся."
    hide maks
    show onka sneaky with Dissolve(.3)
    narrator "А Онка мило усмехнулся. "
    hide onka
    hide onka
    show black regular with Dissolve(.3)
    black "Всем привет! Меня зовут Аш Хом. Я студент первого курса биопротезирования."
    black "Сегодня я расскажу об инструменте, который позволяет интерпретировать чужие чувства."
    black "И демонстрировать ваши."
    black "Люди верят, будто эмоции у всех одинаковые. Но так ли это?"
    black "Пол Экман нашел подтверждение теории, что базовые эмоции универсальны для всех."
    black "Страх, радость, удивление, отвращение, злость и грусть."
    black "Человеческие общества, не связанные единой культурой и развивающиеся параллельно..."
    black "...Будут выражать базовые эмоции одинаково. "
    black "Но есть смешанные эмоции. Их испытывают чаще других, и это вызывает сложности."
    black "Потому что интерпретация смешанных эмоций в разных культурах отличается. "
    black "Мы не всегда даже можем понять, что чувствуем сами. "
    black "А выразить свои чувства для других – вообще отдельная задача."
    black "Я разрабатываю универсальный язык эмоций. "
    black "Который сможет интуитивно понятным, визуальным языком показать ваши чувства другим."
    black "На данный момент Искусственный Интеллект Ушей учится узнавать и отображать базовые эмоции. "
    black "Но, получая все больше данных, он сможет интерпретировать и интенсивность эмоций, и мета-эмоции."
    black "Например, смесь гнева с отчаянием, или - любви с ненавистью."
    narrator "Он сделал драматическую паузу и встретился с Онкой взглядом."
    hide black
    show onka regular with Dissolve(.3)
    narrator "Илли внимательно смотрел и слушал Аша, при этом еле сдерживаясь, чтобы не прокомментировать проект."
    hide onka
    show maks fight with Dissolve(.3)
    narrator "Насмешливый взгляд Максима демотивировал, поэтому Аш старался на него не смотреть."
    hide maks
    hide maks
    show black regular_sad with Dissolve(.3)
    black "Почему людям так важно понимать друг друга? "
    black "Сложность интерпретации чужих эмоций приводит к конфликтам на Земле."
    black "А ведь люди уже на Луне. "
    black "Что же мы принесем новым мирам, когда займем их? Войны?"
    narrator "Он вышел ближе к зрителям, замолчал, и медленно обвел их взглядом, нагнетая атмосферу."
    narrator "Он знал, в сети их – сотни. И они его слышат. Каждый. "
    black "Или мы принесем мир? "
    black "Достигнутый за счет универсального визуального языка?"
    narrator "В зале послышался шепот. Это были Илли и Лис."
    hide black
    hide black
    show onka victory with Dissolve(.3)
    onka "Как же я люблю, когда говорят про космос!"
    hide onka
    show maks regular with Dissolve(.3)
    narrator "Макс строго посмотрел на рыжего."
    hide maks
    show onka sad with Dissolve(.3)
    narrator "Онка, словно школьник, виновато замолчал и обратил взгляд на сцену. "
    hide onka
    show black regular with Dissolve(.3)
    narrator "Выступающий в это время сделал паузу, которой и воспользовался член жюри."
    hide black
    hide black
    show onka thinking with Dissolve(.3)
    onka "Есть вопрос! Общения в реальности действительно мало. "
    onka "Импланты в виде Ушей Зайца ведь предназначены для неё?"
    hide onka
    show black regular with Dissolve(.3)
    black "Живое общение – это стресс."
    black "Есть даже слово, означающее пресыщение людьми – \"аумбук\"."
    hide black
    show onka thinking with Dissolve(.3)
    onka "Логично, большую часть истории Homo Sapiens жили в небольших группах, а не в городах-миллионниках."
    hide onka
    show black regular_happy1 with Dissolve(.3)
    black "Именно поэтому общению тоже нужно учиться. "
    black "Это не врожденный навык."
    black "Но мы не думаем об этом."
    black "Мы не прикладываем усилий для того, чтобы понимать других и себя."
    black "Я вижу, что проблема недопонимания является комплексной. "
    black "Импланты, выражающие эмоции, - это неплохой проект для популяризации данной идеи."
    black "Глядя на человека с имплантами, мы будем помнить, как его нужно понять."
    black "Его можно понять."
    hide black
    show maks regular with Dissolve(.3)
    narrator "Максим поджал губы. На его особенном языке это означало грусть."
    hide maks
    show black regular with Dissolve(.3)
    narrator "Аш смотрел на публику, она - на него. "
    narrator "Неловкие секунды отстучали с десяток раз. Все молчали."
    hide black
    hide black
    show onka victory with Dissolve(.3)
    onka "Я в восторге!"
    onka "Бредово, но при этом — все так и есть."
    onka "Довольно интересно узнать, как работает устройство?"
    hide onka
    show black regular_happy2 with Dissolve(.3)
    black "Конечно, стоит поблагодарить Вас за то, что чип, выпускаемой вашей Фабрикой Чипов, стал открытым."
    black "Запустив на нем свой код ИИ, я смог задать параметры, по которым программа учится различать и отслеживать эмоции в мозгу. "
    black "И когда распознает эмоцию (с уверенностью в девяносто девять процентов), то отображает ее на дисплее."
    black "Чем менее четкое изображение на имплантах, тем меньше ИИ уверен, что верно определил эмоцию."
    hide black
    show onka sneaky with Dissolve(.3)
    narrator "Онка хотел задать целый каскад вопросов, но его перебили."
    hide onka
    hide onka
    show maks fight with Dissolve(.3)
    maks "Тенденция к увеличению сетевого дня говорит о том, что ты провалишься."
    narrator "Это было сказано хладнокровно и уверенно."
    maks "Кто будет это покупать? Частные инвесторы не станут вкладывать в это деньги."
    hide maks
    show black regular_angry with Dissolve(.3)
    black "Возможность распознавать эмоции работает и в сети."
    black "В чем разница, на какое средство вывода информации передавать данные с чипа? "
    black "Что имплатны, что аватар в сети. Устройство универсально."
    black "И это не важно. "
    black "Важно то, что с момента появления первых станций на Луне прошло двести лет."
    black "И мы идем дальше."
    black "Скорее всего, основная коммуникация будет строиться в Вашей, Илли Онка, Чудесной сети."
    black "Мы там работаем, развлекаемся, учимся и получаем новую информацию."
    black "Скоро войну в соседней галактике сможет обеспечить одна строчка кода, выпустившая ракету."
    black "Нет разницы, где мы общаемся. Важно, - как мы это делаем."
    narrator "На последних словах он сделал особенно яркий акцент."
    hide black
    hide black
    show maks angry with Dissolve(.3)
    maks "В итоге, ты стимулируешь людей к увеличению сетевого дня. "
    maks "Ведь в реале никто не захочет ставить себе импланты."
    voice_from_net "Время на вопросы вышло."
    jump scene_9


label scene_9:
    scene home
    #Аш видит, что девушка хакнула мозг без его ведома и злиться.
    #(Девушка сидела за столом, волосы обрезаны, на лице написано блаженство. Она не слушала брата.)
    show black angry_var with Dissolve(.3)
    black "Почему всегда побеждает Максим?"
    hide black
    show vechna smile2 with Dissolve(.3)
    narrator "Сестра слушала его, улыбаясь."
    hide vechna
    hide vechna
    show black angry_var with Dissolve(.3)
    black "Все эти графики, финансовые показатели..."
    black "Хотя кому я вру? С точки зрения бизнеса, идея у меня - так себе."
    black "Это все равно, что физикам выбивать деньги на фундаментальные исследования..."
    black "...Которые, может быть, пригодятся только лет через триста."
    hide black
    show vechna smile1 with Dissolve(.3)
    vechna "Да, тяжелый вышел день! Но неплохой."
    hide vechna
    show vechna sad with Dissolve(.3)
    narrator "Она продолжала улыбаться, но быстро вспомнила про брата и сделала сочувствующее лицо."
    show vechna smile2 with Dissolve(.3)
    vechna "Но у меня радость! "
    vechna "Всего четыре часа и сотня мелких задач - и я смогла удачно хакнуть мозг!"
    hide vechna
    call angry_sad
    hide vechna
    show black mood with Dissolve(.3)
    black "Как? Всмысле? Ты изменила свой мозг?"
    narrator "Он произнес это резко, чувствуя приближение проблем."
    hide black
    hide black
    show vechna thinking with Dissolve(.3)
    vechna "Как бы я ни любила свою работу - мне тоже лень, и я устаю."
    vechna "Но нашлось изящное решение."
    narrator "Ей не терпелось поделиться своим открытием."
    vechna "Нейрохакинг. Ты забыл? "
    vechna "Я провела первый тест! "
    vechna "Я знаю, ты был против, но все ок! Задача выполнена! Это прорыв!"
    hide vechna
    show black sad_var with Dissolve(.3)
    black "Значит, ты этим занималась, пока я так отчаянно тебя ждал?"
    black "Я же ненавижу сцену, ты была мне так нужна!"
    hide black
    show vechna smile1 with Dissolve(.3)
    vechna "Но..."
    hide vechna
    show black angry_var with Dissolve(.3)
    black "И ты обещала посмотреть код, а не экспериментировать над собой!"
    hide black
    show vechna thinking with Dissolve(.3)
    vechna "Насчет эксперимента... "
    vechna "Все же хорошо, все прошло успешно!"
    vechna "А от слива презентации я бы тебя не спасла."
    hide vechna
    show black angry_var with Dissolve(.3)
    black "Значит, это я виноват?"
    hide black
    show vechna angry with Dissolve(.3)
    vechna "Не знаю, но я точно не виновата в том, что твоя работа не \"зашла\" на конкурсе. "
    vechna "Там же был супер-пупер Макс."
    vechna "Но только послушай! "
    vechna "Моей целью было выкроить себе еще часика четыре для работы. "
    vechna "Собрала статистику, чтобы посмотреть, на что я трачу время в реальности, и вышло..."
    vechna "..Что больше всего времени уходит на сон, а все остальное, по мелочи, занимает час-два."
    hide vechna
    show black angry_var with Dissolve(.3)
    black "Я тебе про одно, а ты совсем о другом..."
    hide black
    show vechna thinking with Dissolve(.3)
    vechna "Сон я урезать уже не могу, хватило галлюцинаций в прошлом месяце."
    hide vechna
    show black angry_var with Dissolve(.3)
    black "Как разумно."
    hide black
    show vechna smile1 with Dissolve(.3)
    vechna "У меня была идея зафиксировать в мозгу связи, отвечающие за любовь к еде, сериалам и прочей ерунде."
    vechna "Но! Чтобы изменить три параметра в мозгу, нужно их определить."
    vechna "А это в три раза больше времени, чем определять связи для чего-то одного. "
    vechna "Но, главное - когда меняешь много связей в мозгу, то возрастает вероятность ошибок. "
    vechna "Все-таки, я думаю о своем здоровье!"
    hide vechna
    show black regular_confused with Dissolve(.3)
    black "Даже не знаю, что тут сказать. Разве что... это странно!"
    hide black
    show vechna smile1 with Dissolve(.3)
    vechna "И тогда в голову пришла такая крутая мысль! "
    vechna "Не нужно уменьшать любовь к чему-то, когда я могу увеличить любовь к выполнению задач!"
    vechna "В итоге, сейчас я получаю огромное удовольствие, когда закрываю задачу!"
    hide vechna
    show black regular_surprised with Dissolve(.3)
    black "Я даже не знаю, поздравлять тебя или ругать. "
    black "Тоесть теперь, кроме работы тебе вообще ничего не интересно?"
    hide black
    show vechna smile2 with Dissolve(.3)
    vechna "Очень на это надеюсь!"
    hide vechna
    show black sad_var with Dissolve(.3)
    black "Я хочу уйти. "
    black "Испытываю очень смешанные чувства, в том числе злость и обиду."
    black "Поэтому я просто пойду пройдусь."
    hide black
    show vechna smile2 with Dissolve(.3)
    vechna "Окей, а я буду работать!"
    vechna "И, прошу, не трогай мои вещи."
    vechna "Доставка с Земли – это очень дорого!"
    hide vechna
    narrator "Девушка легла на пол и закрыла глаза. "
    narrator "Ее уже не было в этой комнате, она превращала набор 0 и 1, переданные ровером с далекой планеты..."
    narrator "...В симуляцию, позволяющую пройтись каждому по неизведанному миру."
    show black angry_var with Dissolve(.3)
    narrator "Аш встал из-за стола. "
    narrator "Взял охапку игрушек Вечны, немного подумал, и вернул на место ее любимую коалу. "
    scene station_corridor
    narrator "И затем вышел из жилого отсека, располагающегося в лавовом тоннеле, под поверхностью Лунного кратера."
    jump scene_10


label scene_10 :
    scene lake
    #Аш надеется, что присутствие на конкурсе объединит их с сестрой.
    narrator "Рядом с берегом, о который ударялись невысокие волны Лунной реки, состоящей из миллиардов нано-ботов, Илли Онка думал вслух."
    show onka sad with Dissolve(.3)
    onka "Что создал я? Чип? Нет."
    onka "Его создал дед. Сеть? Ее создал отец. "
    onka "А что сделал я? "
    onka "Я просто неудачник, который не может заселить космос."
    narrator "Онка поднял голову вверх. Горький ком застрял в горле, когда его взгляд уткнулся в темный потолок."
    onka "Как велик соблазн жалости к себе, и как я хочу дойти до конца."
    onka "Но ничего не получается. Для моих целей не хватает вычислительных мощностей..."
    onka "У меня нет столько ресурсов, чтобы заселять планеты. "
    onka "Ни у кого их нет."
    narrator "Он стукнул по металлической поверхности пола и вскрикнул от боли."
    show onka sad with Dissolve(.3)
    narrator "В этот момент ему в голову прилетела игрушка. "
    hide onka
    show black angry_var with Dissolve(.3)
    narrator "Аш и так бесился, а тут еще этот нытик. И где? В его любимом месте!"
    show black regular_happy1 with Dissolve(.3)
    black "Не хотел попасть, честно."
    hide black
    show onka angry with Dissolve(.3)
    narrator "Онка молча смотрел на парня, держа в руках прилетевшую в голову плюшевую игрушку."
    hide onka
    hide onka
    show black regular with Dissolve(.3)
    black "Шутка. Не слишком больно?"
    hide black
    show onka sneaky with Dissolve(.3)
    onka "Не больнее, чем критика твоего проекта."
    onka "Это твое место силы? Думаю, стоит ли искать новое?"
    hide onka
    show black regular with Dissolve(.3)
    black "Прихожу выбрасывать вещи, когда совсем уж погано."
    hide black
    show onka sneaky with Dissolve(.3)
    onka "Древний фен-шуй? Выкинь вещи, и освободи свою жизнь?"
    hide onka
    show black regular_happy1 with Dissolve(.3)
    black "Это не мои вещи."
    hide black
    show onka smile with Dissolve(.3)
    onka "Тогда понимаю."
    hide onka
    show black regular_happy2 with Dissolve(.3)
    black "У тебя, значит, депрессия? "
    black "Нет идей для изобретений?"
    hide black
    show onka sad with Dissolve(.3)
    onka "У меня нет идей? "
    onka "У меня может не быть лишь нескольких решений, но со временем и они находятся."
    hide onka
    show black regular_happy1 with Dissolve(.3)
    black "Если не знаешь, что делать, — найди тех, кто знает. "
    black "У кого есть хорошие решения."
    narrator "Он как бы невзначай провел рукой по Ушкам. Онка следил за его движениями."
    hide black
    hide black
    show onka danger with Dissolve(.3)
    onka "А ты прав! Все это время, решение было на виду."
    narrator "В его взгляде показалось нечто зловещее, но тут же погасло."
    hide onka
    show onka thinking with Dissolve(.3)
    onka "Хотя, разве бывает иначе?"
    onka "Ты мне очень пригодился, молодой человек!"
    hide onka
    show black regular_happy2 with Dissolve(.3)
    black "Я еще не начинал искать инвестиции, но если речь идет о..."
    hide black
    show onka regular with Dissolve(.3)
    narrator "Онка приложил палец к губам и обшарил свои карманы."
    hide onka
    show onka thinking with Dissolve(.3)
    narrator "Не найдя то, что искал, он принялся прощупывать и карманы Аша."
    hide onka
    show black regular_confused with Dissolve(.3)
    narrator "Первая реакция — замереть! "
    narrator "Не потому, что Заяц, а потому, что непонятно: что миллиардер может искать в твоих карманах?"
    hide black
    hide black
    show onka confused with Dissolve(.3)
    onka "Пожалуйста, скажи, у тебя есть камера? "
    onka "Это чертова река - единственное место, не утыканное ими. "
    onka "Самое обидное, я сам об этом попросил. "
    onka "Мне необходимо сделать трансляцию!"
    hide onka
    show black regular_confused with Dissolve(.3)
    narrator "Аш растерялся, и, находясь в недоумении, отдал ему планшет, который достал из кармана."
    hide black
    hide black
    show onka confused with Dissolve(.3)
    onka "Ого! Ты что, воспитывался общественниками в приюте?"
    hide onka
    show black angry_var with Dissolve(.3)
    black "Представь себе. "
    black "И не все хотят каждый раз отрубаться на полу, чтобы войти в сеть."
    hide black
    show onka thinking with Dissolve(.3)
    narrator "Онка молча на него посмотрел. Было непонятно, что ему еще нужно."
    hide onka
    hide onka
    show black angry_var with Dissolve(.3)
    black "Бери раз спрашивал!"
    hide black
    show onka thinking with Dissolve(.3)
    onka "Нет."
    hide onka
    show black angry_var with Dissolve(.3)
    black "Что значит - нет?"
    hide black
    show onka thinking with Dissolve(.3)
    onka "Ты снимай! Я зашел в свой мунтер."
    hide onka
    show black angry_var with Dissolve(.3)
    black "Ты взломал мой акк?"
    hide black
    show onka smile with Dissolve(.3)
    onka "Это лисы."
    onka "Твой пароль - четыре одинаковые цифры, два слова и символ."
    onka "Слишком простой, я бы даже постеснялся предъявлять претензии."
    hide onka
    show black angry_var with Dissolve(.3)
    black "Значит, желтая пресса про тебя не врет?"
    hide black
    show onka sneaky with Dissolve(.3)
    onka "Конечно, врет! Транслируй!"
    hide onka
    show onka victory with Dissolve(.3)
    narrator "Илли сел на перилла и вскинул руки к потолку лавового тоннеля."
    hide onka
    show onka smile with Dissolve(.3)
    onka "Фабрика Чипов создана ради воплощения и внедрения в нашу жизнь великих инновационных идей."
    onka "И сегодня я ищу проекты, которые должны увидеть свет. "
    onka "Объявляю хакатон!"
    onka "Обязательное условие — использование в проекте чипа с Фабрики Чипов как ключевого составляющего элемента."
    hide onka
    show black regular_confused with Dissolve(.3)
    black "А мне подходит!"
    hide black
    show onka smile with Dissolve(.3)
    onka "Не упустите свой шанс! Подробности - сами знаете где."
    narrator "Онка пару секунд натужно улыбался, пока темноволосый догадался выключить камеру."
    hide onka
    hide onka
    show black regular_surprised with Dissolve(.3)
    black "Конкурс?"
    hide black
    show onka smile with Dissolve(.3)
    onka "Да, там я и найду хорошие проекты."
    hide onka
    show black regular_confused with Dissolve(.3)
    black "Я могу на него пройти?"
    hide black
    show onka smile with Dissolve(.3)
    onka "Конечно, ты же навел меня на мысль."
    onka "Но попасть туда можно только через тест. "
    onka "Очень сложный!"
    hide onka
    show black angry_var with Dissolve(.3)
    black "Если бы я не открыл рот, тест, похоже, был бы проще?"
    hide black
    show onka sneaky with Dissolve(.3)
    onka "Кто же знает?"
    narrator "Владелец фабрики бросил это, практически скрывшись за поворотом к выходу."
    hide onka
    hide onka
    show black angry_var with Dissolve(.3)
    black "Ты!"
    narrator "Оставшись один, он с досадой бросил вещи Вечны в самую красивую реку по переработке мусора."
    hide black
    show black sad_var with Dissolve(.3)
    black "Как глупо думать, что он в меня инвестирует."
    black "Хотя, ради конкурса, Вечна может вылезти из сети."
    narrator "Он вызвал девушку с планшета. "
    narrator "Перед ним высветилось сообщение: \"Готовлюсь к экзамену на Конкурс Фабрики\", и куча эмодзи: шок, истерика, счастье."
    hide black
    show black sad_var with Dissolve(.3)
    black "Ну естественно, это ведь не к брату прийти."
    jump scene_11


label scene_11 :
    scene audience
    #Аш и Вечна знакомятся с Лисом. Аш помогает Лису. Вечна завидует высокому баллу брата. Тот говорит что отдал бы ей жетон, но это бесполезно. Там они снова встречают Макса. Тот негативно настроен на лиса (из-за отца винит фабрику) Аш спрашивает для чего тот туда пошел, но Макс не говорит... это Макс устроил пожар в лаборатории
    narrator "Большая часть подростков сидели по домам. В аудитории с Ашем находилось лишь несколько человек."
    narrator "Блондинка и рыжая девушка сидели с двух сторон от него, с интересом поглядывая на его импланты. "
    narrator "Все чувствовали дискомфорт — редко на Луне встретишь больше пары человек в одном месте."
    show maks regular with Dissolve(.3)
    narrator "В конце аудитории Аш разглядел знакомый костюм и крашенные волосы Макса."
    hide maks
    call angry_sad
    hide maks
    show black mood with Dissolve(.3)
    black "Ну конечно, куда же без тебя!"
    narrator "Он нащупал в кармане моток армированной изоленты BRUTAL, которую в него бросил Максим в этой же аудитории..."
    narrator " ...И еле сдержался, чтобы не \"вернуть\" ее назад, в голову Максима."
    narrator "Аш закатал рукава толстовки и щелкнул сигнал сети. "
    narrator "В смешанной реальности заговорил голос, подаваемый чипом прямо в мозг. "
    narrator "Перед глазами появился владелец Фабрики:"
    hide black
    scene chip_factory_audience
    hide black
    show onka smile with Dissolve(.3)
    onka "Фабрика чипов приветствует юных изобретателей! "
    onka "Сегодня мы объявляем итоги отбора!"
    onka "Решим же, кто достоин вступить на территорию инноваций и успеха! "
    onka "Территорию, где изобретатель сможет потягаться за приз — ресурсы для развития своего изобретения!"
    narrator "Знакомый голос затих. "
    hide onka
    show onka smile with Dissolve(.3)
    onka "Сейчас вы получите жетоны, решающие судьбу. "
    onka "Синий жетон. Через годы напомнит вам о неудаче. "
    onka "Зеленый напомнит о шансе, а возможно... о победе! Фабрика желает вам удачи!"
    scene audience
    narrator "Голос так и не сказал, что же им делать. Все сидели в ожидании."
    narrator "В аудиторию забежали лисы с жетонами в зубах. Большинство бежали на четырех лапах."
    show fox angry with Dissolve(.3)
    narrator "К Ашу же, торжественной походкой, крепко стоя на задних лапах, подошел лис без жетона."
    narrator "Парень внимательно осмотрел зверя. Они друг друга узнали."
    hide fox
    hide fox
    show black regular_happy2 with Dissolve(.3)
    black "Приятно снова увидеться."
    narrator "Он улыбнулся серьезному зверю. Тот продолжал молчать."
    hide black
    show fox angry with Dissolve(.3)
    hide fox
    hide fox
    show black regular_confused with Dissolve(.3)
    black "Мне нужно что-то сделать, чтобы получить результат?"
    narrator "Парень осмотрелся по сторонам, глядя, что делают остальные."
    narrator "С одной стороны рыжая девочка держала в руках синий жетон и плакала."
    narrator "С другой стороны блондинка повесила на шею зеленый, но тоже заливалась слезами."
    narrator "Аш вопросительно посмотрел на своего лиса. "
    hide black
    show fox angry with Dissolve(.3)
    narrator "Тот отвел морду."
    hide fox
    hide fox
    show black regular_happy1 with Dissolve(.3)
    black "Если я попаду на конкурс с сестрой, у нас будут отличные каникулы. "
    black "Не лишайте меня их."
    hide black
    show fox angry with Dissolve(.3)
    narrator "Лис сердито молчал."
    hide fox
    show maks regular with Dissolve(.3)
    narrator "Мимо прошел Максим, размахивая зеленым жетоном."
    hide maks
    show black angry_var with Dissolve(.3)
    narrator "Темноволосый повернулся к рыжему зверю."
    show black angry_var with Dissolve(.3)
    black "Я ведь все равно узнаю результат."
    hide black
    show fox angry with Dissolve(.3)
    narrator "Животное смягчило выражение мордочки."
    hide fox
    show fox smile with Dissolve(.3)
    fox "По ужасному стечению обстоятельств, ваш жетон недоступен."
    hide fox
    show black regular_surprised with Dissolve(.3)
    black "?"
    hide black
    show fox smile with Dissolve(.3)
    fox "Он оказался в моем желудке."
    hide fox
    show black angry_var with Dissolve(.3)
    narrator "В ответ парень лишь молча помахал руками в воздухе..."
    narrator "...Будто с его языка хотело сорваться возмущенное: \"Что ты несешь? Как такое возможно?\""
    narrator "Но, видя грустное лицо лиса, который даже опустился на четыре лапы, Аш не стал его ругать."
    hide black
    show black regular with Dissolve(.3)
    black "Хорошо, какие у нас варианты?"
    hide black
    show fox smile with Dissolve(.3)
    narrator "Зверь повеселел."
    show fox smile with Dissolve(.3)
    fox "Начало конкурса завтра, до этого времени все само собой решится."
    hide fox
    show black regular with Dissolve(.3)
    black "Удобно всем, кроме меня."
    black "Я не могу ждать, пока ты сделаешь свои непотребства в аудитории университета. "
    black "Попрошу заменить жетон. Так ведь можно?"
    narrator "Лис вжался в пол."
    hide black
    show fox shock with Dissolve(.3)
    fox "Так будет проще для Вас, справедливо."
    hide fox
    show black regular_confused with Dissolve(.3)
    black "Но?"
    black "Почему ты сразу не предложил этот вариант?"
    hide black
    show fox shock with Dissolve(.3)
    narrator "Лис дернулся от \"ТЫ\", но его внимание переключилось на вопрос студента."
    show fox angry with Dissolve(.3)
    fox "Хозяин спишет меня как брак. "
    fox "У нас говорят: \"Ты не создан совершать ошибки\"."
    hide fox
    show black angry_var with Dissolve(.3)
    black "Это очень, очень жестоко. "
    black "Надеюсь, конкурсантам ничего не угрожает?"
    narrator "Лис посмотрел в пол. В помещении оставались лишь они вдвоем, остальные уже разошлись."
    hide black
    show fox angry with Dissolve(.3)
    fox "Только удача."
    hide fox
    show black regular_fear with Dissolve(.3)
    black "Ладно, ждать так ждать. Но мне нужно найти кое-кого."
    black "Она ведь только что была тут?"
    narrator "Он развернулся, чуть не столкнувшись лицом с сестрой. "
    narrator "На ее лице была широченная улыбка, совсем как у Чеширского кота."
    hide black
    show vechna smile2 with Dissolve(.3)
    vechna "Я прошла! Целых сто восемьдесят шесть баллов! "
    vechna "У остальных, кто прошел меньше!"
    vechna "Я спросила почти у всех! Я выиграю и буду работать на фабрике!"
    hide vechna
    show black regular_happy1 with Dissolve(.3)
    black "Поздравляю тебя! Повидалась с друзьями?"
    hide black
    show vechna thinking with Dissolve(.3)
    vechna "Да, все такие же скучные, как и год назад."
    hide vechna
    show black regular_happy1 with Dissolve(.3)
    black "Наверно, тебе нужны новые друзья."
    hide black
    show vechna thinking with Dissolve(.3)
    vechna "Сколько ты набрал?"
    hide vechna
    show black regular_happy1 with Dissolve(.3)
    black "У меня проблемы с лисьим пищеварением — жетон пока недоступен."
    hide black
    show fox angry with Dissolve(.3)
    fox "Это неловкий инцидент! Не нужно всем рассказывать."
    hide fox
    show vechna smile1 with Dissolve(.3)
    vechna "Оооо, ты говоришь!!! А погавкаешь, погавкаешь?"
    hide vechna
    show fox angry with Dissolve(.3)
    fox "Попрошу побольше уважения!"
    hide fox
    show black regular_annoyed with Dissolve(.3)
    black "Пришла бы на мое выступление, он бы там и погавкал."
    hide black
    show vechna smile2 with Dissolve(.3)
    narrator "По глазам Вечны стало видно, что она ничего не понимает."
    hide vechna
    show black regular_annoyed with Dissolve(.3)
    black "Мы познакомились там, куда тебе было сложно прийти."
    hide black
    show vechna smile2 with Dissolve(.3)
    vechna "Лис, что ты любишь? Расскажи мне о себе!"
    hide vechna
    hide vechna
    show fox angry with Dissolve(.3)
    fox "РасскажиТЕ!"
    hide fox
    show vechna smile2 with Dissolve(.3)
    vechna "Ой, прошу прощения. Где мои манеры."
    hide vechna
    show fox smile with Dissolve(.3)
    narrator "Лис смущенно махнул лапкой. А Вечна бросила взгляд в сторону брата..."
    show vechna smile1 with Dissolve(.3)
    narrator "...И незаметно для лиса покрутила пальцем у виска, корча смешное лицо."
    hide vechna
    show black regular_happy1 with Dissolve(.3)
    hide black
    hide black
    show fox smile with Dissolve(.3)
    fox "Что же я люблю?"
    narrator "Он расплылся в улыбке."
    fox "Например, я люблю коал. Они..."
    hide fox
    show black regular_happy1 with Dissolve(.3)
    black "Они вымерли."
    hide black
    show vechna smile1 with Dissolve(.3)
    narrator "Вечна протянула руки в сторону лиса, намереваясь обнять и потискать."
    show vechna smile1 with Dissolve(.3)
    vechna "О! Это мои любимые животные. Я обязана обнять тебя!"
    vechna "Ой! Обнять Вас!"
    hide vechna
    show fox angry with Dissolve(.3)
    narrator "Лис ловко перекатился от Вечны где-то на метр."
    hide fox
    narrator "Аш закатил глаза, но тут ему пришла в голову одна мысль."
    hide fox
    show black regular_disgust with Dissolve(.3)
    black "Коалы! Это же врожденно гадкие животные."
    hide black
    show fox angry with Dissolve(.3)
    fox "Несправедливо!"
    narrator "Лис манерно махнул хвостом."
    hide fox
    show black regular_happy1 with Dissolve(.3)
    black "Тогда давайте, достопочтенный господин, посмотрим зарисовки из жизни этих благородных животных."
    narrator "Парень передразнивал манеру речи лиса."
    narrator "Он снова достал свой старенький планшет, весь усыпанный затершимися от времени наклейками."
    black "В первую очередь, хочу посмотреть, как они заботились о потомстве."
    black "Видите ли, чтобы передать детенышам полезные бактерии, им приходилось..."
    hide black
    hide black
    show fox smile with Dissolve(.3)
    fox "Кормить их молоком?"
    hide fox
    show black regular_disgust with Dissolve(.3)
    black "Не совсем. Они кормили их гов.., прошу прощения, – продуктами жизнедеятельности."
    narrator "Аш показал видеозапись лису."
    hide black
    show vechna thinking with Dissolve(.3)
    vechna "Мерзость, вот так, сразу в рот своему ребенку..."
    hide vechna
    show fox shock with Dissolve(.3)
    narrator "Лис был в шоке, а затем его ожидаемо стошнило."
    hide fox
    show black regular_happy2 with Dissolve(.3)
    black "И ждать не пришлось! На Земле я бы взял палочку, но на Луне её нет."
    hide black
    show fox angry with Dissolve(.3)
    fox "Может вашим Ухом подцепить жетон?"
    hide fox
    show black regular_happy2 with Dissolve(.3)
    black "Очень остроумно. "
    black "Но доставать, многоуважаемый сударь, придется Вам."
    hide black
    show fox shock with Dissolve(.3)
    narrator "Лис брезгливо поднял жетон. Достал из-за воротничка салфетку."
    hide fox
    show black regular_disgust with Dissolve(.3)
    narrator "Аш немного отодвинулся, желая держаться подальше от предмета."
    show black regular_confused with Dissolve(.3)
    black "Он ведь должен быть синий или зеленый?"
    hide black
    show fox shock with Dissolve(.3)
    fox "Красный — значит самые высокие баллы за входной тест."
    hide fox
    show black regular_surprised with Dissolve(.3)
    black "И что это значит?"
    hide black
    show vechna sad with Dissolve(.3)
    vechna "Значит, что у тебя баллов больше, чем у меня."
    narrator "Расстроилась Вечна."
    hide vechna
    show black regular_happy2 with Dissolve(.3)
    black "Завтра утром мы будем на Фабрике, там ты сможешь отыграться."
    hide black
    show fox smile with Dissolve(.3)
    fox "Благодарю, что решили вопрос без привлечения администрации."
    hide fox
    show black regular_happy2 with Dissolve(.3)
    black "Я бы не смог спать, зная, что тебя списали."
    hide black
    show vechna thinking with Dissolve(.3)
    vechna "Его - что?"
    hide vechna
    show black regular_happy2 with Dissolve(.3)
    black "Потом расскажу."
    jump scene_12


label scene_12 :
    scene chip_factory_territory
    #Ребята ждут старта конкурса
    narrator "Перед двумя десятками испытуемых и кучей дронов находился двор Фабрики Чипов."
    show vechna smile1 with Dissolve(.3)
    vechna "Диснейленд! Микки Маус меня дери!"
    hide vechna
    show black regular_disgust with Dissolve(.3)
    black "Твои формулировки - это нечто."
    hide black
    show vechna smile2 with Dissolve(.3)
    narrator "Она остановилась, жадно изучая глазами обстановку."
    hide vecnha
    narrator "Дроны разлетелись по территории. "
    narrator "Компании на Земле и Луне давно выглядели как этажи автоматизированных лабораторий, сборочных цехов, серверов - царства тишины и темноты. "
    narrator "Ведь роботам не нужен свет."
    narrator "Но что же скрывала Фабрика Чипов, дающая пожизненный пропуск в Чудесную сеть каждому, кто желает подключиться к ней?"
    narrator "Вечна трепетала и подпрыгивала. Кроме них, здесь было двадцать детей и множество дронов, транслирующих все в сеть."
    show vechna smile2 with Dissolve(.3)
    vechna "Я так завидую, что ты уже знаешь Онку! "
    vechna "Вселенная тебя просто облизывает."
    hide vechna
    show black regular_confused with Dissolve(.3)
    black "Ага, перед тем, как съесть."
    #Онка говорит пару слов о своих сотрудниках и о том, что много денег заработал на разумных домашних животных.
    hide black
    narrator "Всюду стояли геометрические статуи. "
    narrator "Сквозь них проникали лучи подсветки, добавляя яркости."
    narrator "Отовсюду доносились звуки жизни. "
    narrator "Летали плавно, или, наоборот, как безумные, птицы: живые и механические, с протезами и имплантами."
    narrator "Под странной фигурой у входа в Фабрику сидела группа хорьков. "
    show hight_fox smile with Dissolve(.3)
    narrator "На лавках обедали или читали лисы. Вечна уставилась на одного из них, с ланчбоксом."
    show hight_fox angry with Dissolve(.3)
    narrator "Заметив это, лис раздраженно поднялся на задние лапы и зашагал в сторону здания."
    hide hight_fox
    show vechna smile1 with Dissolve(.3)
    vechna "Где бы мне взять такую походку!"
    hide vechna
    show onka regular with Dissolve(.3)
    narrator "К гостям вышел Онка. "
    narrator "Некоторое время он снисходительно смотрел, как дроны снимают все происходящее, а участники не обращают на него внимания. "
    narrator "Кроме Аша, который специально отошел, чтобы не попадать в его поле зрения и лишний раз не общаться."
    show onka smile with Dissolve(.3)
    onka "Добро пожаловать на Конкурс Фабрики Чипов! "
    onka "Именно здесь может ожить ваш проект."
    onka "А может и не ожить, а может ожить и сразу умереть..."
    onka "Ну да ладно. Мы отвлеклись."
    onka "По правилам конкурса, вы должны пробыть на Фабрике два дня."
    onka "Если готовы, идите за мной."
    narrator "Он развернулся. И сразу повернулся обратно, отчего его шея хрустнула."
    onka "Ах, да! Все свои вещи оставляйте у входа. "
    onka "Хорьки с ними ничего не сделают, их последнее время интересует одна архитектура."
    hide onka
    show black regular with Dissolve(.3)
    narrator "Все пошли за ним. Аш посмотрел на сестру."
    show black regular_disgust with Dissolve(.3)
    black "Вытри слюни, ну серьезно."
    hide black
    show vechna smile1 with Dissolve(.3)
    vechna "Мысль, что его симуляцию можно сделать в сети, не дает мне покоя."
    hide vechna
    show black regular_disgust with Dissolve(.3)
    black "Я не хочу знать этого, никогда."
    hide black
    show black regular with Dissolve(.3)
    narrator "Он пошел вперед, обгоняя сестру."
    hide black
    show onka regular with Dissolve(.3)
    narrator "Перед входом в здание, Онка развернулся к присутствующим и сообщил:"
    hide onka
    show onka sneaky with Dissolve(.3)
    onka "Отправляя заявку на участие, вы подписали договор о неразглашении того, что увидите и услышите внутри. "
    onka "Это значит, что при нарушении договора вы станете бессильны."
    narrator "Он сочувственно пожал плечами, словно не сам придумал такие правила."
    jump scene_13


label scene_13 :
    scene chip_factory_corridor1
    #Рассказываем условия конкурса. Наташа устраивает Ашу проблему с проектом, так как считает его главным конкурентом. Проект Макса и Наташи тоже должен быть на основе чипа или онка ее потом за это сольет
    show black regular_surprised with Dissolve(.3)
    narrator "Внутри Фабрика не выглядела, как сказочные декорации из фильма."
    narrator "Обычный космический корабль, как на любой вывеске в сети."
    hide black
    show onka sneaky with Dissolve(.3)
    narrator "Илли заметил пораженный отсутствием удивительного взгляд Аша."
    narrator "Хозяин заправил волосы за ухо и пожал плечами:"
    show onka thinking with Dissolve(.3)
    onka "Думаете, я не смотрел Чарли и Шоколадную Фабрику?"
    onka "Приходя сюда, все ожидают увидеть что-то подобное."
    onka "Но у меня намного круче! В миллион раз!"
    hide onka
    show black regular with Dissolve(.3)
    narrator "У Аша появилось желание повесить жетон на шею, чтобы Онка обратил внимание на количество баллов. "
    hide black
    show black regular_disgust with Dissolve(.3)
    narrator "Но воспоминания о том, где этот жетон побывал, остановили его."
    show black angry_var with Dissolve(.3)
    black "Не удивлены, что я тут?"
    hide black
    show onka sneaky with Dissolve(.3)
    onka "Удивлен? Конечно, нет. "
    onka "Я же делал тест, исходя из того, какими сильными будут конкурсанты."
    hide onka
    show onka danger with Dissolve(.3)
    narrator "Потом он широко улыбнулся, показывая зубы."
    hide onka
    show onka regular with Dissolve(.3)
    narrator "Они пошли по коридору. Хозяин Фабрики остановился у одной из дверей."
    show onka thinking with Dissolve(.3)
    onka "Еще раз про договор. "
    onka "Никто, никогда не должен рассказывать о том, что тут произошло. "
    onka "Все могут входить, куда им захочется, лисы в помещениях расскажут вам о назначении всего, что вас заинтересует."
    onka "Есть места ОПАСНЫЕ, боюсь, есть риск некоторых увечий. "
    onka "Прошу заметить, это не покрывается страховкой по документу, который вы подписали."
    scene chip_factory_corridor2
    narrator "Онка закончил фразу, на ходу пропуская конкурсантов в одну из дверей."
    scene chip_factory_audience
    narrator "Все вошли в огромную аудиторию."
    onka "В ходе конкурса вы должны создать или улучшить свое изобретение."
    onka "Конкурс субъективный. "
    onka "Цель фабрики — найти потенциально коммерчески успешный проект на основе чипа, выпускаемого моей компанией."
    onka "Не важно, идея у вас или прототип. Важно, как сильно вы меня впечатлите."
    narrator "Вечна смотрела на Онку влюбленными глазами."
    hide onka
    hide onka
    show black regular_disgust with Dissolve(.3)
    black "Не могу рядом с тобой стоять."
    hide black
    show vechna smile1 with Dissolve(.3)
    vechna "У него есть отдел космоса!"
    hide vechna
    show black regular with Dissolve(.3)
    black "C каким проектом ты пришла? "
    hide black
    show vechna smile2 with Dissolve(.3)
    vechna "Я же не просто так просила доступ к использованию твоего патента."
    hide vechna
    show black regular_happy2 with Dissolve(.3)
    black "Ты получишь поддержку фабрики!"
    hide black
    show vechna sad with Dissolve(.3)
    vechna "Мое изобретение сделано на основе твоего. Ты бы мог подать в суд."
    hide vechna
    show black regular_happy1 with Dissolve(.3)
    black "Мне просто нужно повеселиться. Есть куча способов запустить проект без Онки."
    hide black
    show natasha regular with Dissolve(.3)
    narrator "Двери зала распахнулись с характерным звуком, и в помещение вошла девушка с длинными волосами и гордо поднятой головой."
    narrator "По яркости ее образ мог бы посоперничать с самим Илли Онкой."
    narrator "Вечна открыла информацию о девушке в смешанной реальности: Наташа Ром. "
    narrator "Факультет микробиологии, второй курс. Восемнадцать лет."
    narrator "Статус: сто девяносто девять баллов на Конкурсе Илли Онки. "
    narrator "Иду побеждать! Подписывайтесь и следите за мной в мунтере!"
    hide natasha
    hide natasha
    show vechna thinking with Dissolve(.3)
    vechna "А ты, может, и подружишься с ней. Тоже ботанка."
    hide vechna
    show black angry_var with Dissolve(.3)
    narrator " Аш бросил взгляд на Онку, тот помахал ему рукой."
    show onka smile with Dissolve(.3)
    hide onka
    hide onka
    show black angry_var with Dissolve(.3)
    black "Он точно врал, когда говорил, что поверил в меня. "
    black "Такая интонация была, знаешь..."
    hide black
    show natasha smile with Dissolve(.3)
    narrator "Новенькая раскручивала на пальце жетон с цепочкой, на котором было выгравировано количество баллов за входной тест. "
    narrator "Она настолько ловко пропускала цепочку между пальцами, что эти движения можно было сравнить с совершенным владением неким древним оружием."
    hide natasha
    hide natasha
    show vechna thinking with Dissolve(.3)
    vechna "Она же не могла научиться заранее так крутить! "
    vechna "Неужели успела за ночь? Как ты думаешь?"
    hide vechna
    show natasha regular with Dissolve(.3)
    narrator "Девушка с длинными волосами остановилась и оглядела присутствующих презрительным взглядом."
    show natasha regular with Dissolve(.3)
    natasha "Здравствуйте, меня зовут Наташа, и я собираю команду для конкурса."
    natasha "Мой проходной балл – сто девяносто девять. "
    natasha "Что подтверждает особенный, красный жетон."
    narrator "Она несколько раз повертела его на пальце."
    natasha "Буду рада приветствовать в своей команде сильных конкурсантов."
    natasha "Подробный чек-лист, как попасть в нее, вы можете посмотреть в моем блоге."
    narrator "Девушка опустила руки и сомкнула за спиной в замок."
    natasha "У кого из вас самые высокие баллы после меня?"
    hide natasha
    show black angry_var with Dissolve(.3)
    narrator "Теперь Аш обратил на нее внимание."
    show black angry_var with Dissolve(.3)
    black "А если в последнем туре тебе придется сражаться с участником твоей команды, который сильнее тебя?"
    hide black
    show natasha smile with Dissolve(.3)
    natasha "Это ты что, намекаешь на себя?"
    hide natasha
    show black regular with Dissolve(.3)
    call angry_sad
    narrator "Аш ничего ей не ответил, он повернулся к остальным участникам."
    narrator "Все наблюдали за неофициальным поединком. Поэтому каждый услышал:"
    show black regular_happy1 with Dissolve(.3)
    black "Я приглашаю к себе в команду трех человек с самым низким проходным баллом. "
    black "Кстати, мой балл - двести."
    hide black
    show natasha angry with Dissolve(.3)
    natasha "Вау! Двести! Разница целый один балл. "
    natasha "Все очень эпично, но моя цель - победить."
    hide natasha
    show onka regular with Dissolve(.3)
    narrator "Онка, все это время молча наблюдавший, наконец подошел к участникам."
    show onka regular with Dissolve(.3)
    onka "Для тех, кто пропустил инструктаж: узнаете подробности у других конкурсантов."
    narrator "Он перевел взгляд на Наташу."
    onka "Конечно, если они захотят вам что-то рассказывать."
    hide onka
    show maks regular with Dissolve(.3)
    narrator "Максим, прогуливающийся по периферии аудитории и внимательно осматривающий ее, засмеялся."
    hide maks
    show natasha sad with Dissolve(.3)
    narrator "Наташа повернула голову в его сторону, на лице читалась обида."
    show natasha regular with Dissolve(.3)
    narrator "Девушка сделала вид, что ничего не заметила. "
    hide natasha
    show onka smile with Dissolve(.3)
    narrator "К присутствующим обратился владелец фабрики."
    show onka smile with Dissolve(.3)
    onka "Я рад, что вы столь инициативны и успели разделиться на команды. "
    onka "Хотя, еще час, - и были бы жертвы."
    onka "Но вы играете каждый за себя."
    onka "Сейчас у нас будет питч проектов — за минуту вам нужно рассказать о том, что вы создаете, и что собираетесь делать на конкурсе. "
    narrator "Все молча смотрели на Онку. Он в ответ молча смотрел на конкурсантов."
    hide onka
    hide onka
    show natasha regular with Dissolve(.3)
    natasha "Я первая!"
    hide natasha
    show onka sneaky with Dissolve(.3)
    narrator "Илли Онка ехидно улыбнулся поднимавшейся на сцену девушке."
    hide onka
    show natasha smile with Dissolve(.3)
    narrator "Остановившись в центре, она развернулась на небольших острых каблучках лицом к публике."
    show natasha smile with Dissolve(.3)
    natasha "В наше мирное и спокойное время, когда ресурсов для живых организмов может быть в избытке..."
    natasha "..Люди сталкиваются с необходимостью сокращения или истребления некоторых видов животных."
    natasha "Например, на нашей любимой Земле нужен более эффективный способ сокращения количества медуз."
    natasha "Несмотря на увеличение популяций их естественных хищников..."
    natasha "...Потепление Мирового океана и кормовая база, создает благоприятную среду для медуз. "
    natasha "Они парализуют электростанции, попадая в системы охлаждения, в которых используется морская вода."
    natasha "Оставляя города без энергии. "
    natasha "Мы боремся с ними почти двести лет."
    natasha "В качестве решения, я предлагаю"
    natasha "программируемые вирусы. "
    natasha "Они могут внедряться в клетку и быть неактивными до того момента, пока не поступит триггер. "
    natasha "Вот и все."
    natasha "Презентацию можно скачать в моем мунтере. "
    natasha "Он, разумеется, открыт, как и мое сердечко."
    hide natasha
    show onka sneaky with Dissolve(.3)
    narrator "Онка жевал саранчу, покрытую разноцветной карамелью."
    show onka smile with Dissolve(.3)
    onka "Давайте похлопаем первому конкурсанту!"
    hide onka
    show natasha smile with Dissolve(.3)
    narrator "Наташа чувствовала себя свободно, она улыбнулась и поклонилась аплодирующим."
    hide natasha
    hide natasha
    show onka thinking with Dissolve(.3)
    onka "Крайне интересный доклад. Но остаются вопросы. Какой же триггер?"
    hide onka
    show natasha smile with Dissolve(.3)
    natasha "Для каждого организма - разный."
    natasha "Когда происходит триггер, вирус сокращает популяцию."
    natasha "Хотите знать, как это связано с чипом Фабрики?"
    hide natasha
    onka "Вы читаете мои мысли!"
    hide onka
    natasha "Триггером для запуска умерщвления может являться импульс от чипа."
    natasha "Один чипированный организм может получить импульс для активации вируса и запустить цепную реакцию внутри своей популяции. "
    natasha "Можно сказать, они будут заражать друг друга."
    hide natasha
    show onka danger with Dissolve(.3)
    onka "Очень жизнеутверждающий проект!"
    narrator "Лис рядом поперхнулся."
    onka "Кто следующий?"
    hide onka
    show vechna smile1 with Dissolve(.3)
    narrator "Хлопнув большой пузырь жвачки, который переливался всеми цветами нефти, на сцену поднялась Вечна."
    show vechna smile2 with Dissolve(.3)
    vechna "Всем привет, меня зовут Вечна Хом и я заканчиваю факультет обработки данных космических объектов."
    vechna "Несмотря на мою основную специальность... "
    vechna "..Недавно я опубликовала исследование о технологии нейрохакинга мозга."
    vechna "Возможности изменения связей между нейронами. "
    vechna "Да, такое уже есть, но у меня лучше."
    vechna "Отмечу, что мозг работает по принципу: какие связи сильнее, по ним и пойдет импульс, и, соответственно, такое решение вы примите."
    vechna "Все наши хорошие и плохие привычки — это определенные, закрепленные связи в мозге."
    vechna "Но чип... спасибо Илли Онке! "
    vechna "Вы, кстати, сегодня отлично выглядите!"
    narrator "Она улыбнулась и покраснела."
    hide vechna
    show black regular_disgust with Dissolve(.3)
    hide black
    hide black
    show vechna smile2 with Dissolve(.3)
    vechna "Значит, на основе Чипа можно изменить \"мощность\" связей в мозге."
    vechna "Можно стать любым человеком, приобрести страхи или же избавиться от них. "
    vechna "На данном конкурсе я хочу подтвердить работоспособность технологии. "
    vechna "Я покажу, что связи в мозге действительно можно изменить при помощи чипа, а вслед за ними, - и поведение!"
    narrator "Она осмотрела зал, ожидая вопросы. Все хлопали глазами."
    vechna "Всем спасибо за внимание!"
    narrator "Она бросила взгляд на Онку. "
    hide vechna
    show onka thinking with Dissolve(.3)
    narrator "Он смотрел прямо на нее, но в тоже время как бы сквозь."
    hide onka
    show fox smile with Dissolve(.3)
    narrator "Рядом с ним крутился лис."
    hide fox
    hide fox
    show onka confused with Dissolve(.3)
    onka "Это сестра Аша?"
    hide onka
    show fox smile with Dissolve(.3)
    fox "Определенно."
    fox "Опережая Ваш вопрос, в исследовании она писала..."
    fox "...Что определяет связи в мозгу то же программное обеспечение, которое определяет и эмоции у его имплантов."
    hide fox
    show onka danger with Dissolve(.3)
    onka "Очень ценная информация!"
    hide onka
    show vechna smile2 with Dissolve(.3)
    narrator "Девушка спустилась со сцены. Только Наташа, стоявшая в первом ряду, расслышала тихое:"
    show vechna smile1 with Dissolve(.3)
    vechna "Задачка выполнена! Какой же кайф!"
    narrator "К ней сразу же подошел брат."
    hide vechna
    hide vechna
    show black regular_happy2 with Dissolve(.3)
    black "Думаю, у тебя мало конкурентов. "
    hide black
    show vechna smile1 with Dissolve(.3)
    vechna "Спасибо! Я об этом подозревала!"
    hide vechna
    narrator "Вскоре и остальные участники закончили свои презентации."
    show onka victory with Dissolve(.3)
    narrator "Хозяин Фабрики, активно жестикулируя, разговаривал с конкурсантами."
    show onka victory with Dissolve(.3)
    onka "Я очень впечатлен вашими проектами. "
    onka "Это талантливые и оригинальные применения чипа! "
    onka "Но у нас остался последний участник."
    onka "Питч обязателен. Надеюсь, это Ваша скромность, а не страх?"
    hide onka
    show black regular_happy2 with Dissolve(.3)
    black "А может, мой способ привлечь внимание?"
    narrator "Сегодня Аш был не в настроении выступать. "
    narrator "Но что делать, он сам заварил эту кашу. В прямом смысле. Конкурсант медленно поднялся на сцену. Выдохнул."
    black "Аш — первый курс биопротезирования."
    black "Использую технологические возможности чипа, чтобы решить проблему отсутствия взаимопонимания между людьми."
    narrator "По залу разнеслись звуки непонимания. "
    narrator "Он на автомате пересказывал свою недавнюю презентацию, следя за Вечной."
    black "Мой ИИ позволяет обучить чип распознавать эмоции и чувства, и выдавать на них специфическую реакцию."
    show black regular_annoyed with Dissolve(.3)
    narrator "Он посмотрел на сестру, та с кем-то увлеченно болтала, не глядя в его сторону."
    black "На конкурсе я обучу какую-нибудь эмоцию. Надеюсь, не ярость."
    black "Конец."
    hide black
    show onka victory with Dissolve(.3)
    onka "Будем очень ждать!"
    onka "И мне кажется, кого-то здесь не хватает..."
    onka "Вы видели парня в костюме с галстуком?"
    narrator "Он повернулся лицом ко всем."
    onka "Ладно. Дальше."
    onka "Я объявляю старт Конкурса! До 18:00 найдите на Фабрике все необходимое для представления и разработки своей технологии."
    onka "Напоминаю, что лисы вам помогут."
    jump scene_14


label scene_14:
    scene chip_factory_audience
    #Показываем лиса, который не справляется  работой и Онку
    narrator "В 18:00 участники конкурса стояли в аудитории."
    show onka regular with Dissolve(.3)
    onka "Я рад, после выдачи первого задания, появилось столько вопросов. "
    onka "Я уж было испугался, что вам все понятно."
    onka "Вашей задачей была подготовка материалов для работы над проектами."
    onka "Что вы нашли для себя на Фабрике?"
    hide onka
    show natasha regular with Dissolve(.3)
    narrator "Наташа сделала шаг вперед и уже хотела говорить."
    hide natasha
    show vechna smile2 with Dissolve(.3)
    narrator "Но ее перебила Вечна, которая поднималась на сцену."
    narrator "Взгляд девушки перемещался из стороны в сторону. "
    narrator "Она читала текст в смешанной реальности, не видимый никому, кроме нее."
    show vechna smile2 with Dissolve(.3)
    vechna "Мне потребуются сорок лис и один фиолетовый мячик. "
    narrator "Она повертела мячик в руках."
    vechna "Я хотела бы сохранить предполагаемые итоги эксперимента в тайне."
    narrator "Девушка кинула мячик вниз, в руки брата."
    vechna "Ты - следующий. Я работать."
    hide vechna
    show black regular_surprised with Dissolve(.3)
    narrator "Он поймал мяч! И занял её место на сцене."
    show black regular_confused with Dissolve(.3)
    black "Неудобно говорить..."
    hide black
    show fox shock with Dissolve(.3)
    fox "Неужели Вы не подготовились?"
    hide fox
    show vechna smile2 with Dissolve(.3)
    narrator "У лиса начали подкашиваться лапки, но Вечна подхватила его и погладила по голове."
    show vechna smile1 with Dissolve(.3)
    vechna "Увы, нет вакцины от отсутствия хороших манер."
    narrator "Она радовалась, что может потискать это образованное животное. Конкурсант продолжал:"
    hide vechna
    hide vechna
    show black regular_confused with Dissolve(.3)
    black "Мне нужны были деньги, поэтому я продал часть оборудования Фабрики."
    hide black
    show onka confused with Dissolve(.3)
    narrator "Онка не смог сдержать удивления."
    show onka confused with Dissolve(.3)
    onka "А так можно было?"
    hide onka
    show fox smile with Dissolve(.3)
    fox "Это не запрещено правилами. "
    fox "Конкурсантам было позволено использовать оборудование Фабрики."
    hide fox
    show onka angry with Dissolve(.3)
    onka "Как можно было так составлять документы? Может, он и Фабрику продал? А?"
    hide onka
    show fox shock with Dissolve(.3)
    narrator "Лис подался назад, скрываясь от гнева хозяина."
    hide fox
    show onka confused with Dissolve(.3)
    narrator "Онка посмотрел на Аша, гадая: издевается он над ним, или нет?"
    show onka thinking with Dissolve(.3)
    onka "Один-ноль в Вашу пользу. Могу я узнать, чего именно лишилась Фабрика Чипов?"
    hide onka
    show black regular with Dissolve(.3)
    black "Это было оборудование, требующее переработки. "
    black "Нашлись места, где нужны подобные материалы."
    black "Так что считайте, что я просто вынес мусор."
    black "Деньги требуются для добровольцев."
    black "Распознавать эмоции в полукибернетическом мозгу лис - "
    black "...Это не то же самое, что распознавать человеческий мозг."
    hide black
    show onka sneaky with Dissolve(.3)
    onka "Что мы увидим в итоге, Аш?"
    narrator "Он обвел руками аудиторию с конкурсантами. "
    narrator "До этого Онка никогда не называл Аша по имени. По его спине пробежали мурашки."
    hide onka
    hide onka
    show black regular_happy1 with Dissolve(.3)
    black "Я планирую обучить Уши удивлению или отвращению..."
    black "...И научить распознавать эмоцию хотя бы три раза из десяти."
    black "Уверен, на Фабрике найдется то, что сможет удивить меня. Или наоборот."
    hide black
    show natasha smile with Dissolve(.3)
    narrator "В стороне стояла Наташа. "
    narrator "Она ехидно смотрела на Аша, и, когда он закончил, медленно похлопала в ладоши."
    show natasha regular with Dissolve(.3)
    natasha "Ты хочешь выйти за пределы Фабрики и попросить людей зафиксировать активность мозга твоим софтом?"
    natasha "Хочу тебя расстроить. Очень хочу!"
    narrator "Девушка смотрела снизу вверх, сложив руки за идеально ровной спиной."
    narrator "Она остановилась перед сценой, наслаждаясь своим торжеством."
    narrator "Ей нравилось, что это - торжество ниже стоящего над тем, кто стоит выше."
    natasha "Это против правил."
    narrator "Она широко улыбнулась."
    hide natasha
    show black regular_confused with Dissolve(.3)
    call angry_sad
    show black mood with Dissolve(.3)
    black "Правда?"
    hide black
    show onka confused with Dissolve(.3)
    narrator "Онка вопросительно посмотрел на лиса. "
    hide onka
    show fox smile with Dissolve(.3)
    narrator "Тот одобрительно кивнул головой."
    hide fox
    hide fox
    show onka thinking with Dissolve(.3)
    onka "Как можно было так составлять документы?"
    hide onka
    show black regular_confused with Dissolve(.3)
    black "Мне кажется, Вы тоже удивлены!"
    hide black
    show onka confused with Dissolve(.3)
    onka "Есть ли другие варианты обучения эмоций на людях?"
    hide onka
    show black angry_var with Dissolve(.3)
    black "Если другие конкурсанты не захотят быть моими подопытными всю ночь, то - нет."
    narrator "Он злился, но, пожалуй, больше - на самого себя. "
    narrator "Потому что думал о таком развитии событий, но надеялся, что ему повезет. "
    show black sad_var with Dissolve(.3)
    narrator "В голове мелькнула мысль: \"Слово \"обойдется\" - точно не про тебя\"."
    black "Соберу всю информацию на себе самом."
    black "А что? Устрою марафон удивления или другой эмоции. Как пойдет."
    black "А может, научиться не удивлению, а радости? "
    black "Для этого придется проверить, сколько человек я смогу убить за время конкурса."
    hide black
    show onka danger with Dissolve(.3)
    narrator "Онка залился смехом. В тишине это звучало довольно странно. "
    narrator "Другие присутствовавшие не оценили юмор."
    hide onka
    show natasha sad with Dissolve(.3)
    narrator "Наташа округлила глаза. Трудно было не принять шутку на свой счет."
    hide natasha
    show maks regular with Dissolve(.3)
    narrator "В аудиторию проскользнул Макс, и девушка переключила внимание на него."
    hide maks
    show natasha sad with Dissolve(.3)
    narrator "Она не замечала рядом с собой парня, который пытался незаметно понюхать ее волосы."
    narrator "А Максим даже не скользнул по ней взглядом."
    hide natasha
    show onka regular with Dissolve(.3)
    narrator "Онка, наконец, отсмеялся и глубоко задышал, стараясь успокоиться."
    narrator "Лис принес ему воду."
    show onka regular with Dissolve(.3)
    onka "Мне нравится настрой! Но, во избежание жертв, могу помочь с удивлением."
    show onka sad with Dissolve(.3)
    narrator "Настроение Онки изменилось. Он сел на пол."
    onka "Что-то мне нехорошо."
    narrator "Он взял воду у лиса и через пару минут пришел в себя."
    onka "Все участники получили необходимую информацию о точках проживания, питания и прочие нужные сведения? "
    narrator "Ему никто не ответил."
    onka "Прекрасно. Завтра, в 18.00, подводим итоги."
    narrator "Хозяин обратился к подопечному."
    onka "Зафиксируй требования остальных участников."
    onka "И не совершай ошибок."
    hide onka
    show fox angry with Dissolve(.3)
    narrator "Лис кивнул головой, выпрямил спину и серьезно посмотрел на конкурсантов."
    hide fox
    narrator "Вскоре все покинули аудиторию. "
    narrator "Аш искал глазами сестру, но, нигде не увидев ее, вышел в коридор."
    jump scene_15


label scene_15:
    scene chip_factory_corridor2
    #Аш получает возможность узнать о лисьих кастах
    show black regular with Dissolve(.3)
    narrator "Пройдя пару метров, Аш почувствовал чью-то ладонь на своей руке. "
    hide black
    show onka smile with Dissolve(.3)
    narrator "Нос уловил слабый запах манго. Это Илли тянул Аша за собой, в другую сторону."
    hide onka
    call surprised_disgust
    hide onka
    show black mood with Dissolve(.3)
    black "Эм... Проводить тебя ко врачу? Он, кстати, тоже лис?"
    hide black
    show onka sad with Dissolve(.3)
    onka "Я в норме, физические проблемы меня не остановят."
    hide onka
    show black surprised_var with Dissolve(.3)
    black "Я хотел сестру найти. Куда она ушла после выступления?"
    narrator "Илли резко остановился."
    hide black
    show onka confused with Dissolve(.3)
    onka "Разве ты пришел не за шансом для своего изобретения?"
    hide onka
    show black regular with Dissolve(.3)
    narrator "Аш смотрел вглубь длинного коридора, стараясь разглядеть удаляющуюся Вечну."
    hide black
    show onka confused with Dissolve(.3)
    onka "Ты можешь выбрать любое направление работы Фабрики. "
    onka "Я покажу тебе, как это устроено."
    narrator "Лицо Онки выражало торжество."
    hide onka
    show black surprised_var with Dissolve(.3)
    black "А, да..."
    black "Я все равно не знаю, куда мне нужно."
    hide black
    show onka confused with Dissolve(.3)
    onka "Почему ты не стараешься ради своего изобретения?"
    hide onka
    show black sad_var with Dissolve(.3)
    black "У тебя высокие требования. "
    black "Это все, на что я способен."
    hide black
    show onka confused with Dissolve(.3)
    onka "Ты же понимаешь, что читать эмоции – это практически то же самое, что и читать мысли?"
    hide onka
    show black sad_var with Dissolve(.3)
    black "Я всего лишь хотел, чтобы у людей был шанс понять меня. "
    black "Думаешь, чтение мыслей сделает мир лучше?"
    hide black
    show onka sneaky with Dissolve(.3)
    onka "Смотря как использовать. "
    onka "Сейчас Чудесная сеть настолько эффективна, что вредит людям."
    onka "Они должны меньше в ней сидеть."
    onka "Сеть - это не место для жизни, а инструмент для осуществления действительно великих проектов."
    narrator "Аш посмотрел на Илли другими глазами."
    hide onka
    show black surprised_var with Dissolve(.3)
    black "Сложно это говорить, но я с тобой согласен."
    black "И еще. Почему, находясь наедине, мы говорим друг с другом на “ты”?"
    hide black
    show onka sad with Dissolve(.3)
    onka "Иногда мне нужен хотя бы один такой человек. "
    onka "Хотя, достаточно того, что ты - человек, а не лис."
    hide onka
    show black sad_var with Dissolve(.3)
    black "Это, должно быть, грустно?"
    hide black
    show onka smile with Dissolve(.3)
    onka "Разнообразие необходимо. Мозг всегда требует новую информацию."
    onka "Но он такой глупый! Для него насыщенная жизнь – то же самое, что и видеоряд в сети. "
    onka "Поэтому, я не переживаю из-за того, что мой мозг заставляет меня чувствовать. "
    onka "Чувства - это иллюзия."
    hide onka
    show black sad_var with Dissolve(.3)
    black "Очень хорошо, что у тебя получается игнорировать чувства."
    black "Только простые смертные – такие, как я – не могут их игнорировать. "
    black "Поэтому мне приходится их учитывать. Я живу не среди лис."
    hide black
    show onka sneaky with Dissolve(.3)
    onka "Очень остроумно. Нужно внести в договор запрет на шуточки."
    onka "Куда мы пойдем?"
    hide onka
    show black angry_var with Dissolve(.3)
    black "Я уже говорил, что не знаю, куда мне нужно идти. "
    black "Я ищу сестру."
    hide black
    show onka smile with Dissolve(.3)
    onka "Эх! Дай ей спокойно поработать."
    onka "Если человек хочет хакнуть свои мозги, то его уже не остановить."
    onka "А ты - идешь со мной."
    hide onka
    show black regular_disgust with Dissolve(.3)
    black "Вот внеси это в правила, тогда и посмотрим."
    hide black
    show onka sneaky with Dissolve(.3)
    onka "Ты хочешь узнать, как живут мои кибернетические лисы? "
    narrator "Гость Фабрики оживился."
    hide onka
    show black regular_happy2 with Dissolve(.3)
    black "Сложно отказаться от такого!"
    narrator "Они продолжали петлять по коридорам."
    jump scene_16


label scene_16:
    scene chip_factory_corridor3
    #Здесь показываем, что Облачный пытается обмануть Онку и он не так-то прост. Хотя как потом покажут, он все равно улизнул и вернулся только что бы помочь Ашу в битве с Максом
    narrator "Спустя десять минут они вошли в одну из дверей. В новом помещении было темно."
    scene black_background
    show onka sneaky with Dissolve(.3)
    onka "Это – самая скучная часть."
    hide onka
    show black surprised_var with Dissolve(.3)
    black "Почему так темно?"
    hide black
    show onka sneaky with Dissolve(.3)
    onka "Скажи, для чего тратить энергию на помещения, где живут те, кто видит в темноте?"
    hide onka
    show black surprised_var with Dissolve(.3)
    black "А я много увижу? В темноте?"
    hide black
    show onka sneaky with Dissolve(.3)
    onka "Света нет только в служебных помещениях, не беспокойся."
    onka "На Фабрике обычно тоже темно."
    hide onka
    show black regular with Dissolve(.3)
    black "К твоему приходу здесь не готовятся?"
    hide black
    show onka smile with Dissolve(.3)
    onka "Нет."
    hide onka
    show black surprised_var with Dissolve(.3)
    black "Разве не от тебя зависит их судьба?"
    narrator "Хозяин Фабрики рассмеялся."
    hide black
    show onka smile with Dissolve(.3)
    onka "Нет, что ты. Жизнь - да. Судьба - совершенно нет."
    hide onka
    show black angry_var with Dissolve(.3)
    black "Сказал тот, кто разделил их на касты!"
    hide black
    show onka confused with Dissolve(.3)
    onka "Может, тебе не нужно туда? Смотрю, ты и так все знаешь."
    hide onka
    show black angry_var with Dissolve(.3)
    black "Ты спрашивал об этом лиса на презентации."
    hide black
    show onka sad with Dissolve(.3)
    onka "Лисы появились очень давно. Задолго до меня."
    onka "Фабрика Чипов – это же технологическая династия."
    onka "У лис есть культура, связанная с Фабрикой. "
    onka "Ты должен понимать, что те, кто варится в изоляции, живут по очень причудливым правилам."
    hide onka
    show black disgust_var with Dissolve(.3)
    black "Разве ты не можешь взять и отменить касты?"
    hide black
    show onka thinking with Dissolve(.3)
    onka "От меня зависит лишь то, станет ли лис из Низшей касты представителем Высшей."
    narrator "Аш обрадовался, что он смог донести мысль."
    hide onka
    show black regular_happy1 with Dissolve(.3)
    black "Об этом я и говорю: ты же можешь лис повышать или понижать!"
    hide black
    show onka regular with Dissolve(.3)
    onka "Только Высших и Низших. Третья и вторая - неразумные. "
    narrator "Илли остановился и посмотрел на Аша."
    onka "Другие лисы даже не назвали те касты. Они — другие. Увидишь. Просто три и два."
    hide onka
    scene chip_factory_foxs
    narrator "Они вошли в кубическое помещение. "
    narrator "Все его стенки были увиты лестницами и ячейками."
    narrator "С разных сторон  шли туннели куда-то глубже."
    narrator "А в самом центре стоял удивительно блестящий, словно новенький, робот в желтой накидке."
    hide onka
    show black surprised_var with Dissolve(.3)
    black "Целый лисий улей!"
    black "Но я себе все не так представлял. Они же такие важные, с ланчбоксами."
    hide black
    show onka sneaky with Dissolve(.3)
    onka "О! Тут есть кухня и прачечные. Куда ж без этого. "
    onka "Шучу, все автоматизировано."
    hide onka
    narrator "Вокруг было шумно, лисы бегали по лестницам, носили что-то в руках и зубах, шумно обсуждали новости на скамейках."
    show onka confused with Dissolve(.3)
    onka "Ты захотел на Фабрике посмотреть не самое интересное, но, однако, попал на один из весьма любопытных моментов."
    hide onka
    show black regular with Dissolve(.3)
    black "Ты сам предложил."
    hide black
    narrator "Аш пытался ухватить окруживших его лис за хвосты."
    narrator "В стенах собственного дома лисы походили на обычных зверей, которых он видел в детстве, еще на Земле."
    show black surprised_var with Dissolve(.3)
    black "Это и есть третья и вторая касты?"
    narrator "Лисы поблизости презрительно на него фыркнули и сразу ушли."
    hide black
    show onka confused with Dissolve(.3)
    onka "Вот и урок местной культуры. Их обижает такое сравнение."
    hide onka
    show black disgust_var with Dissolve(.3)
    black "Что с ними не так?"
    hide black
    narrator "Зазвучал громкий звук, и лисы посыпались из нор. "
    narrator "Илли отошел вместе с Ашем к стене."
    show black surprised_var with Dissolve(.3)
    narrator "Аш наблюдал, как, спускаясь с лестниц, словно стекая вниз волной, лисы смешивались в кишащей оранжевой толпе."
    narrator "Аш оглянулся вокруг. Что-то казалось ему непривычным, странным."
    narrator "Раздался еще один звонок, и движущаяся масса пушистых зверей замерла вокруг робота в желтой накидке. "
    narrator "Робот, находящийся в центре зала, шевельнулся."
    narrator "Аш повернул голову в сторону Илли. "
    hide black
    show onka smile with Dissolve(.3)
    narrator "Тот широко улыбался, с любовью глядя на зверей."
    hide onka
    narrator "Шум и гам сменились тишиной. В воздухе запахло благовониями."
    narrator "Как сильно ни пытался гость понять, где они находятся, но так и не смог этого сделать. "
    show black regular_confused with Dissolve(.3)
    narrator "Робот сложил ладони перед грудью. "
    narrator "Сидящие вокруг него лисы наклонили головы, и в воздухе зазвучала буддийская сутра."
    show black surprised_var with Dissolve(.3)
    narrator "Про себя Аш решил, что это был правильный выбор места, чтобы по-настоящему удивиться."
    show black surprised_var with Dissolve(.3)
    black "Что происходит?"
    hide black
    show onka smile with Dissolve(.3)
    onka "Они молятся, что же еще?"
    call surprised_disgust
    hide onka
    show black mood with Dissolve(.3)
    black "Что-что?"
    narrator "Он уже не смотрел на лис, а пытался понять по глазам Онки, смеется тот или нет. "
    narrator "Хотя, зрелище подтверждало истинность его слов."
    hide black
    hide black
    show onka smile with Dissolve(.3)
    onka "Религия, или другая фантазия, дает им что-то общее, чтобы они друг друга не убивали."
    hide onka
    show black disgust_var with Dissolve(.3)
    black "Почему не дать им что-то более адекватное?"
    hide black
    show onka confused with Dissolve(.3)
    onka "Веру в Фабрику? Это ведь тоже фантазия. "
    onka "Убери из Фабрики всех лис, - разве при этом она закроется? "
    onka "Убери все здания - Фабрика при этом юридически все равно будет существовать. "
    onka "А юридическое существование – просто фантазия, о которой люди договорились между собой. "
    onka "Если подпишем бумаги, то будем в них верить."
    onka "Религия и компании основаны на вере. Это коллективные фантазии."
    hide onka
    show black surprised_var with Dissolve(.3)
    black "Но почему - буддизм?"
    hide black
    show onka smile with Dissolve(.3)
    onka "Искусственный интеллект Фабрики считает это оптимальным вариантом. "
    onka "Кстати, это именно Фабрика управляет судьбой лис в момент рождения."
    onka "Судьбой, а значит, и кастами."
    hide onka
    show black surprised_var with Dissolve(.3)
    black "А здесь какие?"
    hide black
    show onka confused with Dissolve(.3)
    onka "Высшие и Низшие."
    hide onka
    show black surprised_var with Dissolve(.3)
    black "Они живут вместе? В чем между ними разница?"
    hide black
    show onka confused with Dissolve(.3)
    onka "И растут вместе. "
    onka "Их разница - в уровне образования."
    onka "Любой Низший может стать Высшим."
    onka "Лисятами они растут вместе, получая базовое воспитание."
    onka "Затем получают имплант развитого неокортекса и специализацию."
    onka "Высшие специализируются на научных дисциплинах. "
    onka "Низшие - на обслуживании Фабрики."
    onka "Хотя, там тоже куча инженерии."
    onka "Те из Низших, кто хочет попасть в Высшую касту – сдают экзамен, если находят для этого время."
    hide onka
    show black regular_confused with Dissolve(.3)
    black "А почему эти не здесь?"
    narrator "Он показал рукой на группу лис, выскользнувших из одного туннеля и направившихся ко входу в следующий. "
    narrator "Один из них был уже ему знаком - Облачный лис."
    hide black
    hide black
    show onka thinking with Dissolve(.3)
    onka "Быстрее!"
    narrator "Хозяин Фабрики взял Аша за руку и повел за лисами."
    hide onka
    show black surprised_var with Dissolve(.3)
    narrator "Они окликнули животных, но те старательно пытались скрыться из виду."
    show black surprised_var with Dissolve(.3)
    black "Что случилось?"
    hide black
    show onka confused with Dissolve(.3)
    narrator "Илли выждал десять секунд, затем выглянул в коридор и тихо пошел за лисом, держа гостя за руку. "
    hide onka
    show black regular with Dissolve(.3)
    scene black_background
    narrator "Аш двигался за Онкой практически в кромешной тьме."
    hide black
    show onka confused with Dissolve(.3)
    narrator "Вскоре, тот открыл одну из дверей. "
    show onka thinking with Dissolve(.3)
    narrator "Снова досчитав до десяти, Илли дал Ашу знак идти за ним."
    narrator "Потом вспомнил, что спутник ничего не видит. "
    show onka thinking with Dissolve(.3)
    onka "Плохо тебе, без лисьего зрения!"
    narrator "Хозяин Фабрики потянул парня за собой."
    jump scene_17


label scene_17:
    scene chip_factory_foxs_3_2
    #Макс говорит, что Онка зло поскольку создает животных для обсчета данных на них. Выдвигает гипотезу, что может быть и скопированных он использует также? Онка выгоняет его.
    narrator "В нос ударил сильный запах. Пахло паленой плотью, тлеющей шерстью и дымом. "
    narrator "В слабом освещении герой разглядел длинное помещение с высокими потолками."
    narrator "В конце комнаты был огромный алый экран."
    show onka angry with Dissolve(.3)
    onka "Где Облачный?"
    hide onka
    show black regular_fear with Dissolve(.3)
    black "У экрана? Ты чувствуешь запах дыма?"
    narrator "Хозяин Фабрики снова вел парня вперед."
    black "Здесь я и сам вижу."
    hide black
    show onka thinking with Dissolve(.3)
    narrator "Онке совсем не было смешно или любопытно. Он насторожился. Послышался лай нескольких лис."
    hide onka
    show black regular_fear with Dissolve(.3)
    narrator "Приблизившись, Аш понял, что ошибся насчет экрана. Это было окно в другое помещение. "
    narrator "Рядом с ним располагалась дверь."
    narrator "Парень замер на месте, вглядываясь в происходящее за стеклом."
    hide black
    narrator "Внутри полыхало пламя, а в нем - что-то хаотично металось и перемещалось резкими скачками. "
    narrator "С треском лопнула колба, из которой вывалился кто-то живой, но без сознания."
    show black angry_var with Dissolve(.3)
    black "Это лисы! Отключите подачу кислорода! Ну же!"
    narrator "Он повернулся к Онке и лисам, которые молча наблюдали за происходящим."
    narrator "Один из них что-то жевал. Парень стал искать Облачного, но среди лис его не было."
    hide black
    hide black
    show hight_fox smile with Dissolve(.3)
    hight_fox "Само потухнет."
    narrator "Аш подошел к двери, ведущей внутрь."
    hight_fox "Я благоразумно рекомендую не трогать..."
    hide hight_fox
    show black angry_var with Dissolve(.3)
    narrator "Но Аш уже открыл дверь. И этого хватило, чтобы огонь ворвался в общее помещение. "
    show black regular_fear with Dissolve(.3)
    narrator "Конечно, парень сразу же пожалел о своем эмоциональном порыве - одежда на нем загорелась."
    hide black
    show hight_fox angry with Dissolve(.3)
    narrator "Легкие обожгло. Но рядом появился лис, закрывший лапами дверь."
    narrator "Лисы тут же повалили Аша на пол и принялись топтаться и тушить на нем прожженную в нескольких местах толстовку."
    narrator "Повреждения были почти не видны."
    hide black
    hide hight_fox
    show black sad_var with Dissolve(.3)
    black "Да что же это?!"
    hide black
    show onka thinking with Dissolve(.3)
    onka "Похоже, произошла авария в блоке Третьей и Второй каст. "
    onka "Но Фабрика все починит."
    onka "Вопрос - в причине аварии."
    hide onka
    show black angry_var with Dissolve(.3)
    black "В смысле – в причине?"
    hide black
    show hight_fox smile with Dissolve(.3)
    hight_fox "Это же Третьи и Вторые! Расходный материал. "
    hight_fox "Вот оборудование действительно жаль, оно дорогое."
    call surprised_disgust
    hide hight_fox
    show black mood with Dissolve(.3)
    black "Вы совсем дикие?"
    hide black
    show hight_fox angry with Dissolve(.3)
    hight_fox "Молодой человек, следите за словами!"
    hide hight_fox
    show black surprised_var with Dissolve(.3)
    black "Разве это не ваши сородичи?"
    narrator "Лисы рядом засмеялись."
    hide black
    hide black
    show hight_fox smile with Dissolve(.3)
    hight_fox "Да они на Фабрику выходят из-за стекла только года в четыре - хуже роботов!"
    hight_fox "Годятся только для экспериментов над ними, да для расчетов."
    hight_fox "Когда запретили есть их мозги, они стали совсем бесполезными."
    hide hight_fox
    show black disgust_var with Dissolve(.3)
    black "Вы дикие!"
    hide black
    narrator "Он бросился на лиса и стал его трясти. "
    show maks angry with Dissolve(.3)
    narrator "Из темного угла помещения вышел Максим."
    show maks angry with Dissolve(.3)
    maks "А что ты удивляешься?"
    maks "Я знаю, что он их использует, как живые компьютеры."
    hide maks
    show black sad_var with Dissolve(.3)
    black "Это ты сделал? Сжег бы лучше Онку, идиот!"
    hide black
    show maks angry with Dissolve(.3)
    narrator "Спустя секунду, Максим ударил Аша под колени, и, схватив его за Уши, рванул их изо всех сил вверх."
    hide maks
    show black regular_blood with Dissolve(.3)
    narrator "Раздался жуткий хруст, и из места крепления имплантов по лицу Аша потекла кровь. "
    narrator "Он закричал."
    show black regular_blood with Dissolve(.3)
    black "Ты меня убьешь!"
    black "Идиот! Они же вживлены в голову!"
    narrator "Кровь продолжала стекать по лицу, а Максим все тянул Уши вверх."
    hide black
    hide black
    show maks angry with Dissolve(.3)
    maks "А ты уже, смотрю, подружился с этим террористом?"
    hide maks
    show onka confused with Dissolve(.3)
    narrator "Онка молча наблюдал за сценой, дав лисам сигнал не вмешиваться."
    show onka thinking with Dissolve(.3)
    onka "Я вижу, ты многое узнал, пока тут шастал. "
    onka "Сжег бы тут все, чего мелочиться. Даже - всю лунную станцию."
    onka "А то ведь сколько тут зла, наверное, творится!"
    hide onka
    show black regular_blood with Dissolve(.3)
    narrator "Максим не давал Ашу подняться. В его глазах сверкала жестокость."
    hide black
    hide black
    show maks angry with Dissolve(.3)
    maks "Твоя сеть..."
    maks "Почему в ней пропадают копии людей, а?"
    maks "Почему мой отец скопировался в нее и пропал, не подскажешь?"
    hide maks
    show black regular_blood with Dissolve(.3)
    black "Может, он просто свалил от такого маньяка, как ты?"
    hide black
    narrator "Максим отпустил свою жертву, и пнул Аша ногой."
    hide black
    show maks angry with Dissolve(.3)
    maks "Все, кто поддерживают рыжего ублюдка, сгорят! "
    maks "И, да! Может, и вся станция!"
    narrator "Максим хотел броситься на Онку, но Аш сбил его с ног."
    hide maks
    hide maks
    show black regular_blood with Dissolve(.3)
    black "Нафига жечь лис?"
    narrator "Аш обездвижил соперника, усевшись сверху и заломив ему руки за спину."
    narrator "Затем достал из толстовки моток армированного скотча BRUTAL! "
    narrator "До ушей Максима донесся резкий скрип."
    narrator "Он пытался сопротивляться, но Аш уже накрепко залепил ему рот... "
    narrator "...И всё сильнее обматывал голову скотчем, перекрывая доступ к кислороду."
    narrator "А когда ты живешь на лунной станции, задохнуться – твой самый большой страх."
    black "Помнишь свой подарок мне на презентации? Пригодился!"
    hide black
    show onka confused with Dissolve(.3)
    onka "Ого! У меня будут из-за этого проблемы?"
    narrator "Он задал этот вопрос Облачному, но забыл, что того нет рядом. И вызвал его в сети."
    onka "Наверняка, будут."
    onka "Оттащите парня."
    hide onka
    show black regular_blood with Dissolve(.3)
    narrator "В порыве ярости Аш продолжал заматывать голову Максима клейкой лентой, пока не почувствовал на руке крепкие челюсти."
    hide black
    show hight_fox angry with Dissolve(.3)
    narrator "Из-под клыков Лиса брызнула кровь."
    hide hight_fox
    hide hight_fox
    show onka angry with Dissolve(.3)
    onka "Хватит! И так тошно последнюю неделю."
    narrator "Он сам отбросил Аша в сторону."
    hide onka
    hide onka
    show black regular_blood with Dissolve(.3)
    black "Что ты делаешь? Он жег твоих лис!"
    hide black
    show onka angry with Dissolve(.3)
    onka "Ничего страшного! "
    hide onka
    narrator "Лис разорвал зубами скотч на лице Макса и невинно отметил:"
    hide onka
    show hight_fox smile with Dissolve(.3)
    hight_fox "Третьи и Вторые не разумны, я же сообщил."
    hide hight_fox
    show black regular_blood with Dissolve(.3)
    black "Но ведь маленькие лисы Высшей и Низшей касты тоже неразумные! "
    black "Разве нет? Но о них вы заботитесь!"
    hide black
    show hight_fox smile with Dissolve(.3)
    hight_fox "Производство Третьих и Вторых автоматизировано. "
    hight_fox "Они, пока не достигнут взрослого состояния, растут в аквариумах."
    hight_fox "Логично, что мы к ним не привязываемся."
    narrator "Аш посмотрел на Онку."
    hide hight_fox
    show black regular_blood with Dissolve(.3)
    black "Ты собираешься спасать лис? Ты же отвечаешь за их безопасность!"
    narrator "Тот удивленно на него посмотрел."
    hide black
    hide black
    show onka angry with Dissolve(.3)
    onka "Я думал ты про это забыл, пока бил белобрысого."
    onka "Но это подпольное лисье развлечение. "
    onka "Они сами иногда специально так делают."
    onka "Именно поэтому данному “недоразумению” удалось попасть только сюда."
    narrator "Он указал рукой на Макса, который сидел на полу. Тот уже не выглядел таким самоуверенным."
    onka "Из преступлений - только нерациональная трата ресурсов. "
    onka "Этих лис все-таки и кормили, и поили."
    hide onka
    show black regular_blood with Dissolve(.3)
    narrator "Аш молчал, пытаясь понять, среди кого он оказался."
    hide black
    show onka thinking with Dissolve(.3)
    onka "А ты…"
    narrator "Он повернулся к Максу."
    onka "Исключен из конкурса. "
    onka "И, поверь, лучше тебе молчать о том, что здесь произошло."
    hide onka
    show fox angry with Dissolve(.3)
    narrator "В помещении появился Облачный лис."
    hide fox
    hide fox
    show onka thinking with Dissolve(.3)
    onka "Где ты был?"
    hide onka
    show fox shock with Dissolve(.3)
    narrator "Лис хотел что-то сказать."
    narrator "В этот момент в воздухе раздался крик Илли Онки."
    hide fox
    show onka angry with Dissolve(.3)
    onka "Кто? Кто находится в зале с моими лианами?!"
    onka "Почему сработала безопасность? "
    onka "Там кто-то без лис! Без присмотра!"
    narrator "Лисы подпрыгнули на месте и разбежались в разные стороны. Облачный остался на месте."
    hide onka
    hide onka
    show fox angry with Dissolve(.3)
    fox "Что случилась?"
    hide fox
    onka "Очевидно, решили разрушить всю мою Фабрику!"
    hide onka
    show black regular_blood with Dissolve(.3)
    narrator "Он помог подняться Ашу на ноги и снова повел за собой."
    narrator "Аш не отрывал взгляда от горящих заживо лис. "
    narrator "Он не мог думать ни о чем другом."
    narrator "Не мог поверить, что лисы так поступают друг с другом: считают мертвыми тех, кто еще живы."
    hide black
    hide black
    show fox angry with Dissolve(.3)
    fox "Третья каста — просто живые компьютеры, а Вторая - просто лабораторные животные. "
    fox "Они даже не говорят."
    hide fox
    show black regular_blood with Dissolve(.3)
    black "Некоторые люди тоже не говорят..."
    hide black
    show fox angry with Dissolve(.3)
    fox "Фабрика вырастит новых, у нас регулярно какие-то аварии. "
    fox "Это же Луна."
    narrator "Успокаивал его Облачный."
    hide fox
    onka "Пойдешь с нами, пушистый."
    onka "И еще расскажешь, где ты был!"
    onka "И этого тоже, бери с собой!"
    narrator "Он с презрением посмотрел на потрепанного Максима, на лицо которого уже вернулась ухмылка."
    jump scene_18


label scene_18 :
    scene chip_factory_corridor1
    #Показываем, что Онке его мечта о заселении планет важнее, чем живые лисы на Луне. Он рассказывает о своем деле жизни
    narrator "Они вышли с территории лис. "
    show black regular_blood with Dissolve(.3)
    narrator "Петляя по коридорам, Аш давно потерял ориентацию, даже не глядя на освещение. "
    narrator "Кровь перестала течь и уже местами запеклась. "
    narrator "По всей видимости, повреждения оказались не слишком серьезными..."
    narrator "...И парень просто оттер ее с лица рукавом толстовки."
    show black sad_var with Dissolve(.3)
    narrator "Аш посматривал на Максима."
    show black sad_var with Dissolve(.3)
    black "Что с твоим отцом?"
    hide black
    show maks angry with Dissolve(.3)
    maks "Я же сказал - он пропал."
    hide maks
    show black surprised_var with Dissolve(.3)
    black "Причем тут Онка?"
    hide black
    show maks angry with Dissolve(.3)
    maks "Ты дурак? Да! "
    maks "Он сделал сеть и чип открытыми, но ядро ведь принадлежит ему!"
    maks "Непонятно, чем он здесь занимается."
    maks "Одна из пятидесяти копий пропадает! И никаких следов!"
    hide maks
    show black disgust_var with Dissolve(.3)
    black "Очень надуманно."
    black "Ты же не можешь узнать, пропали они или нет, на сто процентов."
    black "Могли специально скрыться от семьи."
    hide black
    show maks regular with Dissolve(.3)
    maks "Мой отец не мог. "
    maks "Он и ушел туда, чтобы закрыть все \"хотелки\" этой..."
    narrator "Парень остановил себя и сменил тему."
    maks "А могли копии, как и лисы, стать функциями? Нет?"
    narrator "Онка остановился у одной из дверей."
    hide maks
    show onka thinking with Dissolve(.3)
    onka "Лис, отвечаешь за белобрысого головой. "
    onka "Стойте оба здесь."
    scene chip_factory_vines2
    narrator "Затем Онка вошел внутрь. "
    show onka confused with Dissolve(.3)
    narrator "Помещение освещалось бледно-голубым светом растений. Оно напоминало ботанический сад."
    onka "Смотри под ноги!"
    hide onka
    show black surprised_var with Dissolve(.3)
    black "Ого!"
    narrator "Он споткнулся о лиану, испачкавшись чем-то липким и теплым."
    black "Фэ!"
    hide black
    narrator "Свет ламп отражался от корнеобразных растений, стелющихся высоким ковром по большому залу."
    narrator "Илли крепко взял парня за руку."
    hide black
    show onka thinking with Dissolve(.3)
    onka "Для равновесия."
    narrator "И они двинулись в центр."
    hide onka
    show black disgust_var with Dissolve(.3)
    narrator "Скоро Аш все-таки потерял равновесие и схватился рукой за одну из лиан. "
    narrator "Скользкая, толщиной с руку, она была на ощупь похожа на червя. "
    narrator "Казалось, что она - живая и пульсирует."
    show black disgust_var with Dissolve(.3)
    black "Чем оно покрыто? Что это?"
    hide black
    show onka angry with Dissolve(.3)
    onka "Тихо!"
    hide onka
    narrator "В центре помещения виднелся чей-то силуэт."
    show black disgust_var with Dissolve(.3)
    hide black
    show onka thinking with Dissolve(.3)
    narrator "Они медленно пробирались всё ближе, преодолевая стелющийся лес долгих несколько минут. "
    narrator "Раздался знакомый голос."
    hide onka
    hide onka
    show natasha smile with Dissolve(.3)
    natasha " Приготовьтесь удивляться!"
    hide natasha
    show black surprised_var with Dissolve(.3)
    black "Это Наташа!"
    hide black
    show onka thinking with Dissolve(.3)
    onka "Я уже понял."
    hide onka
    show natasha regular with Dissolve(.3)
    narrator "Лица девушки не было видно. "
    narrator "Лианы подсвечивали бледным-голубым цветом ее тонкие голые ноги."
    narrator "Она взяла светящуюся лиану левой рукой, затем поднялась и наступила каблуком на ее середину."
    narrator "Снова наклонилась, взяв два конца лианы в свободную руку. "
    narrator "Накрутила их вокруг кистей, натянула, и..."
    hide natasha
    show onka angry with Dissolve(.3)
    onka "Стой! Твою...!"
    hide onka
    show natasha smile with Dissolve(.3)
    narrator "Но она уже резко дернула концы вверх. От рывка лиана разорвались. "
    narrator "Из-под ног девушки, в месте разрыва, красиво разлетелся светящийся сок, рассыпавшись на множество капель."
    narrator "Наташа опустила руки и села на колени. "
    narrator "Лианы из центра сада начали меняться — они угасали."
    show natasha regular with Dissolve(.3)
    narrator "Девушка казалась настоящим центром смерти."
    hide natasha
    show black regular with Dissolve(.3)
    narrator "В голове Аша была пустота. Он наблюдали за тотальным уничтожением растений. "
    hide black
    show onka angry with Dissolve(.3)
    narrator "Онка же просто упал на колени, не в силах произнести даже двух слов."
    hide onka
    show natasha smile with Dissolve(.3)
    narrator "Наташа шла, улыбаясь, по границе между темными (мертвыми) и светящимися (живыми) голубыми лианами."
    narrator "Словно каждый ее шаг убивал растения."
    scene chip_factory_vines
    show natasha smile with Dissolve(.3)
    narrator "В навалившейся тьме светились лишь глаза девушки. Растения же тихо угасали."
    narrator "Наташа заметила Онку и Аша. И ярко улыбнулась, забыв в порыве радости об их отношениях."
    show natasha smile with Dissolve(.3)
    natasha "У меня получилось! Все прекрасно сработало! "
    natasha "Думаю, ролик будет эффектный!"
    hide natasha
    show onka angry with Dissolve(.3)
    narrator "Онка молчал. Его глаз задергался. "
    narrator "Он пытался что-то сказать, но губы не слушались."
    hide onka
    hide onka
    show natasha smile with Dissolve(.3)
    natasha "Конечно, в качестве триггера на самоубийство, я взяла сильное разрушение. "
    natasha "Оно все и запустило! Это отличная демонстрация моей концепции."
    hide natasha
    show onka angry with Dissolve(.3)
    onka "Это было единственное растение, которое смогло жить хоть сколько-то на RDF-13!"
    onka "А ты его убила из-за ролика?!"
    narrator "Он схватился за волосы."
    onka "Это кошмар. Кто допустил Вас до этого помещения?"
    onka "Мне и так постоянно плохо, еще Вы!"
    hide onka
    show natasha sad with Dissolve(.3)
    narrator "Уверенность девушки испарилась."
    hide natasha
    hide natasha
    show onka angry with Dissolve(.3)
    onka "Я исключаю вас."
    hide onka
    natasha "Что? Нет! Вы не можете просто так взять и нарушить правила."
    hide natasha
    onka "О! Раз я не могу их нарушить, то, может быть, млечный сок лиан это сделает? "
    onka "В нем хватит яда на десять Лун. Надеюсь, что-то попало Вам в рот!"
    onka "А если не попало, я помогу!"
    narrator "Аш понял, что дело плохо."
    hide onka
    hide onka
    show black angry_var with Dissolve(.3)
    black "Она - не лисы!"
    hide black
    show natasha sad with Dissolve(.3)
    hide natasha
    narrator "Девушка стояла, как вкопанная."
    hide natasha
    show black angry_var with Dissolve(.3)
    black "Ты не можешь причинить вред конкурсантам на своем же конкурсе."
    hide black
    show onka danger with Dissolve(.3)
    narrator "Онка взглянул на Аша."
    hide onka
    show onka thinking with Dissolve(.3)
    onka "Могу."
    onka "Я даже подумать не мог, что у кого-то рука поднимется на такое..."
    hide onka
    show black angry_var with Dissolve(.3)
    black "Это же твои правила. Как Это же твои собственные правила."
    black "Как говорится, выбирая игру, ты выбираешь правила."
    hide black
    show onka angry with Dissolve(.3)
    narrator "Онка снял цилиндр и понес его в руках, постоянно приглаживая волосы назад."
    hide onka
    hide onka
    show natasha sad with Dissolve(.3)
    natasha "Не выгоняйте меня! Это же все было по правилам!"
    natasha "Я спросила у лис, где и что может умереть по цепной реакции..."
    natasha "Сказали..."
    narrator "Ее остановил новый друг."
    hide natasha
    hide natasha
    show black regular with Dissolve(.3)
    black "Не нужно. Не продолжай."
    hide black
    show onka sad with Dissolve(.3)
    narrator "Быстрым шагом, с потухшими глазами, Онка пробирался сквозь лианы обратно."
    narrator "Аш с Наташей шли за ним."
    hide onka
    hide onka
    show natasha sad with Dissolve(.3)
    natasha "Он угрожал мне?"
    hide natasha
    show black regular with Dissolve(.3)
    black "Он просто зол."
    hide black
    show natasha sad with Dissolve(.3)
    natasha "Спасибо, что заступился. Я ему точно не нравлюсь."
    hide natasha
    show black regular with Dissolve(.3)
    black "Нет, дело действительно в лианах, а не в тебе. "
    black "Похоже, ими он дорожит больше, чем другими подопечными."
    narrator "Он снова зацепился за растение, но теперь уже не теплая, а холодная жижа стекала по его ноге."
    black "Как же мерзко! Как же мерзко!"
    hide black
    natasha "Аккуратней! Там же яд!"
    hide natasha
    show black regular_happy1 with Dissolve(.3)
    narrator "Аш обрадовался свету, когда вышел из зала."
    hide black
    scene chip_factory_corridor1
    show onka angry with Dissolve(.3)
    narrator "Онка давал указания лису на счет Макса. "
    hide onka
    show maks fight with Dissolve(.3)
    narrator "Тот скользнул презрительным взглядом по девушке. "
    hide maks
    show natasha sad with Dissolve(.3)
    narrator "В ее глазах появились слезы, и она потянула Аша прочь от остальных."
    show natasha smile with Dissolve(.3)
    natasha "Тебе нужна одежда!"
    hide natasha
    show black disgust_var with Dissolve(.3)
    narrator "Аш был перепачкан."
    show black disgust_var with Dissolve(.3)
    black "Я чувствую, как по ноге что-то течет!"
    jump scene_19


label scene_19 :
    scene chip_factory_corridor3
    #Аш рассказывает про Макса, Наташа жалеет парня так как проецирует свои отношения с братом на их. Но Ната еще не говорит, что Макс ее брат
    narrator "Ребята разговаривали, двигаясь по коридору."
    show black sad_var with Dissolve(.3)
    black "Этот придурок сжег сегодня лис..."
    black "Главное, для Онки это - нормально!"
    hide black
    show natasha regular with Dissolve(.3)
    natasha "А для лис?"
    hide natasha
    show black disgust_var with Dissolve(.3)
    black "Для них, кажется, тоже."
    hide black
    show natasha sad with Dissolve(.3)
    natasha "Многое бы отдала за интервью с одним из них для блога..."
    natasha "Только они не особо хотят со мной говорить."
    hide natasha
    show black disgust_var with Dissolve(.3)
    black "У них очень закрытое сообщество. "
    black "И далеко не все понравится широкой общественности."
    black "Не могу даже понять, хорошие они или нет..."
    black "А еще, я видел, как Макс на тебя посмотрел. "
    black "Что между вами?"
    hide black
    show natasha sad with Dissolve(.3)
    natasha "Похоже, что мы с ним знакомы?"
    hide natasha
    show black surprised_var with Dissolve(.3)
    black "Да не особо."
    hide black
    show natasha smile with Dissolve(.3)
    narrator "Она засмеялась."
    hide natasha
    show black regular_happy1 with Dissolve(.3)
    narrator "Аш улыбнулся в ответ."
    hide black
    hide black
    show natasha smile with Dissolve(.3)
    natasha "Лучше поспешить сменить твою одежду."
    hide natasha
    narrator "Они шли незнакомыми коридорами. Вокруг никого не было."
    show natasha sad with Dissolve(.3)
    natasha "Прости за ненормальное поведение вчера. "
    natasha "И за то, что сорвала твои планы."
    natasha "Насчет обучения ИИ на людях... "
    natasha "Ради Которого ты продал оборудование Фабрики."
    hide natasha
    show black regular_happy2 with Dissolve(.3)
    black "Я уже забыл."
    hide black
    show natasha sad with Dissolve(.3)
    natasha "Просто у меня проблемы. "
    natasha "Еще этот Онка, который вечно критикует."
    hide natasha
    show black regular_happy1 with Dissolve(.3)
    black "Не переживай, это не связано с тем, что твой проект плохой."
    black "Людям тяжело говорить о смерти, о возможности использования средств массового убийства. "
    black "И о том, что это может быть полезно."
    hide black
    show natasha smile with Dissolve(.3)
    natasha "Да! Знаешь, как много можно заработать, выключив половину медуз?"
    natasha "Электростанции и очистные сооружения, бассейны — все забивается медузами."
    hide natasha
    show black regular_happy2 with Dissolve(.3)
    narrator "Она взяла его за руку, и Аш почувствовал, что ему нравится это прикосновение. "
    narrator "В отличие от прикосновений странного Хозяина Фабрики, который вечно пахнет манго."
    hide black
    show natasha regular with Dissolve(.3)
    narrator "Проходя мимо одной из дверей, они услышали шорохи. Наташа остановила Аша."
    hide natasha
    hide natasha
    show black disgust_var with Dissolve(.3)
    black "Мне нужна новая одежда."
    hide black
    show natasha regular with Dissolve(.3)
    narrator "Подруга закрыла ему рот."
    show natasha regular with Dissolve(.3)
    natasha "Там кто-то из наших! В смысле - это точно человек!"
    hide natasha
    narrator "Аш замолк, и они заглянули за приоткрытую дверь."
    scene chip_factory_room
    show wild_fox regular with Dissolve(.3)
    narrator "В комнате с имитацией окна на голом полу стояла клетка. А в ней сидел лис из третьей касты. "
    hide wild_fox
    show vechna thinking with Dissolve(.3)
    narrator "Напротив клетки, на мягком пуфике, сидела Вечна и делала в смешанной реальности заметки, невидимые другим."
    scene chip_factory_corridor3
    hide vechna
    show natasha regular with Dissolve(.3)
    natasha "Эта выскочка - это же твоя сестра?"
    hide natasha
    show black angry_var with Dissolve(.3)
    narrator "Парень посмотрел на Наташу с упреком. В ответ она виновато пожала плечами."
    hide black
    show natasha sad with Dissolve(.3)
    hide natasha
    scene chip_factory_room
    show wild_fox regular with Dissolve(.3)
    narrator "Сестра обратила внимание на лиса в клетке: тот махал хвостом из стороны в сторону. Его взгляд не отрывался от сидящей девушки. Он был просто поглощен ею."
    hide wild_fox
    show vechna smile1 with Dissolve(.3)
    narrator "Ребята увидели, как Вечна достала из-за спины мячик. Обычный фиолетовый мяч. "
    narrator "Такой же она бросила в руки Ашу, приглашая его на сцену."
    narrator "Покрутила игрушкой перед своим лицом."
    hide vechna
    show wild_fox regular with Dissolve(.3)
    narrator "Лис высунул язык и часто задышал, но не сдвинулся с места. Зеленоглазая обратилась к нему:"
    hide wild_fox
    hide wild_fox
    show vechna smile2 with Dissolve(.3)
    vechna "Насколько сильно ты его хочешь? Посчитай от одного до десяти. "
    vechna "Тебе ведь поставили имплант для речи?"
    narrator "Зрачки лиса расширились. Изо рта потекла слюна."
    hide vechna
    hide vechna
    show wild_fox crazy with Dissolve(.3)
    wild_fox "Да, сильно! Сильно! Дай!"
    hide wild_fox
    show vechna smile1 with Dissolve(.3)
    narrator "Девушка несколько раз аппетитно помяла мяч в руке. Потом потянула его в рот."
    hide vechna
    show wild_fox crazy with Dissolve(.3)
    narrator "Лис сорвался с места и так накинулся на прутья клетки, что та качнулась."
    show wild_fox crazy with Dissolve(.3)
    wild_fox "Дай!"
    hide wild_fox
    show vechna thinking with Dissolve(.3)
    vechna "Жаль, что речь так скудна... "
    vechna "Скажи, как сильно хочешь его – по шкале от одного до десяти!"
    narrator "В ответ лис зарычал и начал грызть клетку."
    vechna "Я же говорила правила: без команды \"встать\" двигаться нельзя."
    hide vechna
    show wild_fox crazy with Dissolve(.3)
    narrator "Зверь бесился."
    hide wild_fox
    show vechna thinking with Dissolve(.3)
    narrator "Вечна смотрела на лиса с досадой."
    show vechna thinking with Dissolve(.3)
    vechna "Значит, нужно сделать синоптические связи слабее... "
    vechna "Хмм… В два раза?"
    vechna "Дели или умножай на два: так хоть будет ясно, меняется что-то или нет."
    narrator "Сказала она самой себе. Сестра подошла к клетке и снова аппетитно помяла мячик."
    hide vechna
    show fox angry with Dissolve(.3)
    narrator "Из-за ее спины показался Облачный лис. Он неодобрительно посмотрел в клетку."
    hide fox
    show wild_fox crazy with Dissolve(.3)
    narrator "Лис в клетке громко рычал."
    hide wild_fox
    hide wild_fox
    show vechna angry with Dissolve(.3)
    vechna "Долго пришлось тебя ждать."
    hide vechna
    fox "Пришел, как только смог. И можно на “Вы”?"
    hide fox
    show vechna smile1 with Dissolve(.3)
    narrator "Девушка сделала недовольное лицо. Внутри клетки бесновался лис."
    hide vechna
    hide vechna
    show wild_fox regular with Dissolve(.3)
    wild_fox "Дайте! Отберу!"
    hide wild_fox
    show vechna thinking with Dissolve(.3)
    vechna "Можно научить его говорить лучше?"
    hide vechna
    show fox shock with Dissolve(.3)
    fox "На это нужна хотя бы неделя. "
    fox "Мы не можем поставить ему более развитый неокортекс, как, например, у меня или у Высших. "
    fox "Это решает ИИ Фабрики."
    hide fox
    show vechna sad with Dissolve(.3)
    vechna "Печаль..."
    hide vechna
    show fox angry with Dissolve(.3)
    fox "Но совершенно очевидно, что желание играть с мячом у него ненормально сильное..."
    hide fox
    show vechna thinking with Dissolve(.3)
    narrator "Вечна повернулась в сторону лиса в клетке и снова показала ему мяч. "
    hide vechna
    show wild_fox regular with Dissolve(.3)
    narrator "Тот замер, сел на пол, как это было еще минуту назад."
    hide wild_fox
    hide wild_fox
    show vechna smile2 with Dissolve(.3)
    vechna "Слушаешься? "
    hide vechna
    show wild_fox regular with Dissolve(.3)
    narrator "Животное замолкло."
    hide wild_fox
    hide wild_fox
    show vechna thinking with Dissolve(.3)
    vechna "Не дам мяч. Он мой."
    hide vechna
    show wild_fox crazy with Dissolve(.3)
    narrator "Она даже не успела закончить слова, как лис бросился на прутья. "
    narrator "Клетка покачнулась. Он пытался пролезть сквозь решетку. "
    narrator "А затем... стал грызть свою лапу."
    hide wild_fox
    show vechna thinking with Dissolve(.3)
    narrator "Девушка наблюдала минуту, скептически глядя на зверя."
    narrator "А затем сделала заметки, проговаривая вслух:"
    show vechna thinking with Dissolve(.3)
    vechna "Данные по образцу номер семь демонстрируют сильную психологическую зависимость. "
    vechna "Надо изучить данные более подробно."
    vechna "Важно! Нужно собрать данные, чтобы такое больше не повторялось. "
    vechna "А чтобы изучить, требуется повторить."
    vechna "Что же делать?"
    hide vechna
    show fox angry with Dissolve(.3)
    fox "Не знаю. Но, по приказу нашего Хозяина, мы выполним любые Ваши указания."
    narrator "Тихо произнес Облачный."
    hide fox
    hide fox
    show vechna thinking with Dissolve(.3)
    vechna "Пойду разбираться. Он меня пугает."
    hide vechna
    show fox angry with Dissolve(.3)
    fox "Можно его забрать?"
    hide fox
    show vechna thinking with Dissolve(.3)
    vechna "Да, конечно. К сожалению, с ним не вышло."
    vechna "Мне нужен подопытный с навыками речи."
    narrator "Она на секунду остановилась."
    vechna "Будешь следующим?"
    hide vechna
    show fox shock with Dissolve(.3)
    scene chip_factory_corridor3
    show natasha sad with Dissolve(.3)
    narrator "Наташа с сочувствием посмотрела на Аша и потянула его скорее прочь."
    narrator "По щекам девушки потекли слезы. Из комнаты слышались грызущие, чавкающие звуки."
    show natasha sad with Dissolve(.3)
    natasha "Что за жесть!"
    hide natasha
    show black sad_var with Dissolve(.3)
    black "Это был лис из Второй или Третьей касты, не говорящий..."
    call surprised_disgust
    black "Пока Вечна не попросила."
    narrator "Аш молчал. Из-за двери еще слышались поскуливания. "
    narrator "Он вспоминал, как в детстве сестра спасла его и кроликов во время аварии."
    show black sad_var with Dissolve(.3)
    narrator "Парень задумался. "
    narrator "Что же она тогда делала: спасала животных или убивала людей, которые могли бы занять их место?"
    narrator "Девушка всегда готова кем-то жертвовать. "
    narrator "Тогда - жизнью людей ради него и кроликов."
    narrator "А сейчас - жизнью лис. Но ради чего?"
    narrator "Он решил, что главное - быть - для нее важнее, чем эти люди, чем все эти открытия и сеть."
    narrator "Они шли по коридору. Яд на одежде парня высох."
    hide black
    hide black
    show natasha sad with Dissolve(.3)
    natasha "Я знаю, каково это, когда твои близкие отдаляются. "
    natasha "С моим братом - похожая история."
    hide natasha
    show black sad_var with Dissolve(.3)
    black "Сочувствую. Но у меня все не так плохо. "
    black "Я для нее важнее всего."
    narrator "Наташа обняла его."
    hide black
    show natasha sad with Dissolve(.3)
    natasha "Я тоже очень на это надеюсь."
    natasha "Но думаю... "
    natasha "Что о сумасшедшем лисе никто не позаботится..."
    jump scene_20


label scene_20:
    scene chip_factory_audience
    #Аш видит изменения Вечны, и чувствует свою вину - не нужно было давать ей код. Наташа его поддерживает (может за руку берет), а он поддерживает ее - Онка сливает девушку за несоответствие теме конкурса. Аш побеждает, но отдает победу Вечне. Предварительно спрашивая, позволяют ли это правила.
    narrator "Последний день на конкурсе."
    show black sad_var with Dissolve(.3)
    black "Можно?"
    hide black
    show vechna smile1 with Dissolve(.3)
    vechna "Почему ты спрашиваешь о таком?"
    hide vechna
    show black sad_var with Dissolve(.3)
    black "Надеюсь, что на остальные вопросы ты будет отвечать охотнее."
    narrator "От вчерашних воспоминаний на душе скребли кошки. \"Бедные лисы\" — подумал он про себя."
    black "Всех лис \"починила\"?"
    hide black
    show vechna thinking with Dissolve(.3)
    vechna "Ты это о чем?"
    narrator "Аш вспомнил, что вчера он лишь подсматривал, но в комнате с Вечной не находился."
    vechna "Ты слишком часто психуешь. Даже шутить об этом не хочется."
    hide vechna
    show black sad_var with Dissolve(.3)
    black "Хотел узнать, сколько лис ушло в утиль."
    hide black
    show vechna smile2 with Dissolve(.3)
    narrator "Вечна пожала плечами, потом задумалась."
    show vechna smile2 with Dissolve(.3)
    vechna "Двадцать три лисы, пока я не поняла, в чем проблема."
    vechna "Ты был прав, - мне повезло не спалить свой мозг!"
    hide vechna
    show black sad_var with Dissolve(.3)
    narrator "В глубине души Аш был уверен, что Вечна вправит мозги всем лисам. "
    hide black
    show vechna smile1 with Dissolve(.3)
    narrator "Сестра продолжала говорить."
    show vechna smile1 with Dissolve(.3)
    vechna "Я достигла прогресса в изменении мозга. "
    vechna "Теперь можно менять в нем все, что хочешь."
    vechna "Естественно, как всегда, самое долгое — это обучение. "
    vechna "Найти именно те связи, которые нужно усилить."
    vechna "Но кое-что вышло. "
    vechna "И все - благодаря тебе!"
    hide vechna
    show black disgust_var with Dissolve(.3)
    black "Класс, я очень горжусь, что лисы свихнулись благодаря мне. "
    black "И ты тоже свихнулась."
    hide black
    show vechna smile2 with Dissolve(.3)
    vechna "Я?"
    hide vechna
    show black angry_var with Dissolve(.3)
    black "Еще недавно ты бы никогда так не поступила с животными. "
    black "Если бы не твоя радость от выполнения задач, достигнутая за счет нейрохакинга."
    hide black
    show vechna thinking with Dissolve(.3)
    vechna "С Облачным все прошло ок."
    narrator "Девушка задумалась и пожала плечами."
    vechna "Может, я, наконец, именно та, кем и хотела быть? "
    vechna "А может, я такой и была?"
    hide vechna
    show black regular with Dissolve(.3)
    narrator "Аш хотел что-то сказать, но девушка дала знак молчать."
    narrator "Её отвлек звук шагов. Это Онка поднялся на сцену."
    hide black
    hide black
    show onka angry with Dissolve(.3)
    onka "Сегодня мы выслушаем итоговые презентации, и я выберу победителя."
    onka "Конечно, не сразу. После выступлений лисы разберут ваши данные по проектам."
    hide onka
    show natasha smile with Dissolve(.3)
    narrator "Наташа поднялась с места. Она лучезарно улыбнулась Онке."
    hide natasha
    show black regular with Dissolve(.3)
    narrator "Аш сочувственно подумал: \"Думаю, это тебе уже не поможет\". "
    show black surprised_var with Dissolve(.3)
    narrator "Его мысли сразу же перескочили на собственный проект: готов ли он сам к тому, чтобы участники видели его эмоции? "
    narrator "Почему он об этом волнуется? Да потому, что пусть он и не сблизится с сестрой, но хотя бы продвинется по работе."
    hide black
    hide black
    show natasha smile with Dissolve(.3)
    natasha "Вы не против, если я начну?"
    hide natasha
    show onka sneaky with Dissolve(.3)
    onka "Разве Вас кто-то сможет остановить?"
    hide onka
    show natasha regular with Dissolve(.3)
    narrator "Наташа проигнорировала сарказм Онки. "
    narrator "Что еще она могла сделать? Девушка поднялась на сцену."
    show natasha smile with Dissolve(.3)
    natasha "Прошу всех подключиться к сети. Я начну трансляцию презентации в смешанной реальности."
    narrator "Перед аудиторией появилось окно с презентацией. "
    narrator "В самом конце, она открыла видео. "
    hide natasha
    show black surprised_var with Dissolve(.3)
    narrator "Аш замотал головой: \"Надеюсь ты не покажешь Онке, как убила его лианы, выживающие даже на астероидах?\". "
    hide black
    show natasha smile with Dissolve(.3)
    narrator "Но у нее хватило ума так не делать."
    show natasha smile with Dissolve(.3)
    natasha "Внутри Фабрики я еще раз протестировала распространение вируса, но не для животных, а для ландышей. "
    natasha "Триггером запуска цепной реакции, назовем это самоуничтожением, являлся холод."
    natasha "Пришлось напечатать базовый прототип моего вируса за ночь, но я успела!"
    narrator "Девушка указала рукой на невидимую для нечипированных презентацию, в которой открылось видео. "
    hide natasha
    show onka thinking with Dissolve(.3)
    narrator "Онка молчал, вертя в пальцах крупную засахаренную саранчу, которую взял из вазы со снеками."
    hide onka
    show onka thinking with Dissolve(.3)
    onka "Сама концепция биологического оружия противоречит нашим ценностям открытия и создания новых возможностей для жизни."
    hide onka
    show natasha angry with Dissolve(.3)
    natasha "Я не веду речи о полном истреблении. Речь о регуляции численности."
    hide natasha
    show onka angry with Dissolve(.3)
    narrator "Хозяин Фабрики положил в рот хрустящее насекомое."
    hide onka
    show natasha regular with Dissolve(.3)
    narrator "Девушка твердо смотрела перед собой. Аш чувствовал себя неловко, он боялся, что подруга заплачет."
    hide natasha
    hide natasha
    show onka sneaky with Dissolve(.3)
    onka "Спасибо за выход. Не обижайтесь, конкурс субъективный. "
    narrator "К Илли снова вернулся интерес."
    onka "Кто выступает следующим?"
    hide onka
    show natasha sad with Dissolve(.3)
    narrator "Наташа в расстроенных чувствах спустилась со сцены. Аш ждал у лестницы."
    hide natasha
    hide natasha
    show black surprised_var with Dissolve(.3)
    black "Меня тоже недавно Онка слил."
    hide black
    show natasha sad with Dissolve(.3)
    natasha "Все из-за вчерашнего..."
    narrator "На глазах Наташи наворачивались слезы."
    natasha "Хотя бы в одной сфере жизни было так, как хочется! "
    natasha "И я все транслировала в сеть! Вот позор!"
    hide natasha
    show black surprised_var with Dissolve(.3)
    black "Ничего страшного нет, даже если это кто-то и увидит."
    black "Наоборот, больше шансов найти инвестора. "
    black "Глядишь, какой-нибудь Онка-ненавистник решит дать тебе денег, чтобы насолить ему."
    hide black
    show natasha angry with Dissolve(.3)
    narrator "Наташа подняла глаза на сцену. Там стояла Вечна."
    hide natasha
    show black regular with Dissolve(.3)
    narrator "Аш не отрывал взгляд от сестры. Подруга это заметила."
    hide black
    hide black
    show natasha angry with Dissolve(.3)
    natasha "Останься с сестрой, мне нужно побыть одной."
    show natasha sad with Dissolve(.3)
    narrator "На глаза девушки опять навернулись слезы, она старалась глубоко дышать. "
    hide natasha
    show black regular with Dissolve(.3)
    narrator "Только Аш не обращал на нее внимания."
    hide black
    show vechna smile2 with Dissolve(.3)
    narrator "Вечна стояла на сцене в сопровождении Облачного лиса."
    show vechna smile2 with Dissolve(.3)
    vechna "Рада вас приветствовать!"
    narrator "Перед глазами конкурсантов появился полупрозрачный слой с презентацией. Оратор стояла прямо перед ним."
    vechna "На снимках можно видеть активность мозга при любви к фиолетовым мячам."
    narrator "Показывает новый кадр."
    vechna "Перед вами - мозг моего ассистента-лиса."
    show fox angry with Dissolve(.3)
    hide fox
    vechna "Если кратко, то за одну ночь я смогла научить мозг лиса любить неодушевленный предмет до дрожи. "
    vechna "Очень сильно любить. "
    vechna "Конечно, есть данные \"до\" и \"после\"."
    vechna "Они хранятся в открытом доступе..."
    vechna "...Поэтому вы можете ознакомиться с уровнем активности мозга до нейрохакинга и после него."
    vechna "Перспективы применения данной разработки огромные, вплоть до изменения психики. "
    vechna "Конечно, первые применения спорных технологий, — это всегда медицина."
    narrator "Она обратилась к Илли."
    vechna "Исследование монетизации и рынка для подобных инноваций требует больше времени, чем было доступно."
    vechna "Но я верю, что сфера применения нейрохакинга огромна, и это может действительно изменить мир."
    hide vechna
    show onka victory with Dissolve(.3)
    narrator "Онка аплодировал стоя."
    hide onka
    show black sad_var with Dissolve(.3)
    narrator "С момента ухода Наташи Аш смотрел лишь в одну точку на сцене и думал про свою сестру. "
    narrator "Краем глаза он заметил, что Вечна движется к выходу, и пошел за ней. "
    hide black
    show fox angry with Dissolve(.3)
    narrator "Его под руку поймал Облачный."
    show fox angry with Dissolve(.3)
    fox "Ай, ай, ай! Сейчас Ваш выход, молодой человек!"
    hide fox
    show black surprised_var with Dissolve(.3)
    black "Я пропускаю вперед кого-нибудь."
    hide black
    show fox angry with Dissolve(.3)
    fox "Вы же последний! Как всегда!"
    narrator "С этими словами он взял его зубами за рукав и повел за собой."
    hide fox
    hide fox
    show black disgust_var with Dissolve(.3)
    black "А как же манеры?"
    narrator "Лис выпустил рукав из пасти."
    hide black
    show fox angry with Dissolve(.3)
    fox "Что Вы знаете о нашей культуре?"
    hide fox
    show black sad_var with Dissolve(.3)
    narrator "Парень вздохнул и попробовал собраться с мыслями. "
    scene chip_factory_room
    show wild_fox crazy with Dissolve(.3)
    narrator "Перед глазами был только лис в клетке."
    scene chip_factory_audience
    hide wild_fox
    show black regular with Dissolve(.3)
    black "После таких открытий, как у Наташи или Вечны, моя работа не выглядит такой революционной."
    black "Конечно, можно найти полезное применение нейрохакингу, но я хочу разобраться с проблемами наших чувств. "
    black "За эту ночь я смог немного обучить ИИ распознавать удивление и отвращение."
    black "Кроме этого, внедрил автогенерацию дизайна: с помощью сторонней программы Уши ищут изображения, которые максимально ассоциируются с эмоцией и выводят их на себя."
    black "Технически они представляют собой интерфейс, подключенный к чипу, находящемуся в голове. Дисплеи — сами Уши."
    black "Из-за автогенерации изображений, Уши сами, без моего участия, создают визуальный язык."
    hide black
    show onka confused with Dissolve(.3)
    narrator "Илли слушал не отрываясь."
    show onka confused with Dissolve(.3)
    onka "Ваша теория заключается в том, что одни люди, наблюдая эмоции других людей, будут менять свое отношение к ним?"
    hide onka
    show black regular with Dissolve(.3)
    black "Да, это позволит человеку быть  более открытым с самим собой и с другими людьми. "
    black "Часто мы сами не хотим признаваться себе в собственных чувствах."
    hide black
    show onka sneaky with Dissolve(.3)
    onka "Если все будут видеть мои эмоции, это приведет к серьезному изменению образа жизни. "
    onka "Я тогда с Фабрики носа не покажу."
    hide onka
    show black angry_var with Dissolve(.3)
    black "Это изменение культуры. "
    black "Как мы знаем, минимальный шаг значимых культурных изменений — одно поколение."
    hide black
    show fox angry with Dissolve(.3)
    fox "Почему именно Уши зайца? Не лис... Не кошачьи, например?"
    hide fox
    show black angry_var with Dissolve(.3)
    black "Это решение необоснованно технически. "
    black "Можно сделать дисплеи в форме разных Ушей. Дело вкуса."
    hide black
    show fox smile with Dissolve(.3)
    narrator "Скрестив руки на груди и чувствуя себя неимоверно важным, Облачный внимательно выслушал ответ и утвердительно покачал головой, говоря самому себе, что так он и думал."
    hide fox
    hide fox
    show onka sneaky with Dissolve(.3)
    onka "И значит, у Вас есть патент на софт?"
    hide onka
    show black angry_var with Dissolve(.3)
    black "Да, я дал его в безвозмездное пользование сестре."
    black "Думаю, Вы и так все уже знаете."
    hide black
    show onka regular with Dissolve(.3)
    narrator "Онка повернулся к другим участникам."
    show onka smile with Dissolve(.3)
    onka "Через два часа отдел контроля проверит данные ваших проектов и сообщит результаты. "
    onka "Победитель сможет присоединиться к любой исследовательской группе на Фабрике. "
    hide onka
    show black surprised_var with Dissolve(.3)
    narrator "Через пару часов все были поражены тем, что выиграл Аш. "
    hide black
    show vechna sad with Dissolve(.3)
    narrator "Второе место принадлежало Вечне. "
    show vechna angry with Dissolve(.3)
    narrator "От досады она рвала на голове волосы."
    hide vechna
    hide vechna
    show black regular_happy1 with Dissolve(.3)
    black "Я отказываюсь от победы. И я прочел правила – так можно."
    hide black
    show onka sneaky with Dissolve(.3)
    onka "Ожидаемо... Но не расстраивайся!"
    onka "Занявший второе место получит утешительный приз — ужин с самым выдающимся инноватором нашего поколения – ..."
    hide onka
    show black angry_var with Dissolve(.3)
    black "...Со мной."
    narrator "Договорил за него Аш и закатил глаза."
    hide black
    show vechna smile1 with Dissolve(.3)
    narrator "Вечна сидела, не шевелясь, красная, как помидор, от приливающей к лицу крови."
    show vechna smile1 with Dissolve(.3)
    vechna "Я победила! Задача выполнена!"
    jump scene_21


label scene_21:
    scene home
    #Девушка продолжает нейрохакинг. Аш отговаривает его, напоминая, сколько лис она убила ради этого на конкурсе...
    show black regular with Dissolve(.3)
    narrator "Прошел месяц."
    #(Черный экран. Появляется кнопка с текстом.)
    show black regular with Dissolve(.3)
    black "Соединить с Вечной."
    scene planet
    show black surprised_var with Dissolve(.3)
    narrator "Мир вокруг изменился: парень стоял на планете, чувствуя резкий запах кислот. "
    narrator "Они обжигали легкие. Звучали свист и раскаты грома. "
    narrator "Руку резко прибило к земле. Аш понял – что-то падает с неба."
    narrator "\"Кристаллы\" — мелькнуло в голове. И снова боль пробила руку."
    narrator "Оглядевшись, он начал двигаться в сторону невысокой пещеры."
    narrator "Дойдя до нее, Аш попробовал вытащить один из кристаллов."
    narrator "Никак не получалось нащупать его конец, чтобы подцепить и вытащить из руки."
    narrator "На глаза ему попались рубины, лежащие у входа в укрытие, они были сантиметров пять в длину и острые, как иглы."
    black "Ааа, я такие длинные не вытащу!"
    narrator "Из-под рубинов, застрявших в руке, стали выделяться капли крови."
    black "Что за жесть! "
    narrator "\"Красиво\" — успел подумать парень, пока рука не онемела. Ему казалось, что пробиты даже кости."
    narrator "Вытащить из себя пятигранные клинки казалось невозможным. "
    black "Вечна! Фак! Выключи это все нафиг!"
    narrator "Но никто не ответил."
    black "Все, я тогда пас! Выйти из сети."
    voice_cartoon "Пожалуйста, закончите симуляцию."
    hide voice_cartoon
    black "Что?"
    voice_cartoon "Вход в симуляцию подразумевает подписание пользовательского соглашения."
    narrator "Перед Ашем появилось соглашение."
    hide voice_cartoon
    black "Так не пойдет. Я присоединился не к симуляции, а к пользователю."
    voice_cartoon "Для минимизации получения нежелательного опыта в сети рекомендуется перед переходом ознакомиться с локацией."
    narrator "Аш злился на себя за то, что всегда пропускал этот шаг, настроив мгновенный переход после одобрения запроса."
    hide voice_cartoon
    black "Ладно, как закончить игру?"
    narrator "Перед ним высветились правила."
    narrator "\"Наблюдай за Нихалом и найди новое открытие — свое серендипити\"."
    call surprised_disgust
    black "О, то, что нужно для человека с раздробленной рукой! "
    black "Самое оно, мать вашу."
    narrator "Рука заныла."
    black "А если я умру?"
    voice_cartoon "Симуляция закончиться."
    hide voice_cartoon
    black "Выбор очевиден. Кристаллы еще сыплются с неба?"
    narrator "Он посмотрел на небо - дождь из рубинов закончился."
    black "Не вовремя."
    show black regular with Dissolve(.3)
    narrator "Спустя десять минут он сидел в позе лотоса у входа в пещеру и глубоко дышал, наблюдая за ландшафтом."
    hide black
    show vechna smile2 with Dissolve(.3)
    narrator "Появилась Вечна."
    show vechna smile2 with Dissolve(.3)
    vechna "Прости, я только-только включила уведомления. Не знала, что ты тут."
    hide vechna
    show black angry_var with Dissolve(.3)
    black "Я тут такой боли натерпелся!"
    narrator "Он хотел выругаться, что из симуляции просто так не выйти, но вспомнил, что, будь он сам внимательнее, мог бы этого избежать."
    narrator "Она бы точно на это указала."
    hide black
    show vechna smile1 with Dissolve(.3)
    show vechna smile1 with Dissolve(.3)
    vechna "Прости! Планета с атмосферой из синильной кислоты и дождями из драгоценных камней..."
    vechna "..Может показаться неприветливой в первое время."
    hide vechna
    show black disgust_var with Dissolve(.3)
    black "То-то я чувствую, что легких уже нет. Почему я жив?"
    hide black
    show vechna smile1 with Dissolve(.3)
    vechna "Если я все буду включать на полную катушку, то не продержусь тут и пары минут. "
    vechna "Поэтому, обычно, то, что разрабатываю сейчас,- включаю полностью, а остальные внешние факторы – приглушаю."
    hide vechna
    show black surprised_var with Dissolve(.3)
    black "Что за фишка с серендипити?"
    hide black
    show vechna smile1 with Dissolve(.3)
    vechna "Ааа, ну это мое упражнение, перед выходом из симуляции."
    vechna "Я наблюдаю за миром вокруг и записываю какое-то потенциальное открытие."
    vechna "Я понимаю под серендипити глубокий вывод из случайных наблюдений."
    hide vechna
    show black regular with Dissolve(.3)
    narrator "Девушка сделала несколько манипуляций рукой, и Аш облегченно вздохнул. "
    narrator "Боль пропала, но чувствовался холод рубинов, когда дотрагиваешься пальцами."
    hide black
    show vechna thinking with Dissolve(.3)
    show vechna thinking with Dissolve(.3)
    vechna "У тебя какое-то дело? А то у меня..."
    hide vechna
    show black sad_var with Dissolve(.3)
    black "...Еще столько задач незакрытых есть."
    hide black
    show vechna thinking with Dissolve(.3)
    vechna "Именно."
    hide vechna
    show black regular_fear with Dissolve(.3)
    black "Ты что, все это сейчас на себе тестишь?"
    black "Почему не на модели? Ты вон вся какая драная."
    hide black
    show vechna angry with Dissolve(.3)
    vechna "Сам ты \"драная\"! Я подвожу итоги."
    vechna "Когда поставлена задача - сделать дожди, как на других планетах..."
    vechna "...то удар камня по голове может обрадовать тебя больше, чем рождество!"
    hide vechna
    show black disgust_var with Dissolve(.3)
    black "Это нездорОво и не ЗдОрово."
    hide black
    show vechna thinking with Dissolve(.3)
    vechna "Я делаю великие вещи."
    hide vechna
    show black regular_confused with Dissolve(.3)
    narrator "Аш пристально на нее посмотрел. Одна рука девушки была выбита из плеча. На теле виднелись ожоги."
    hide black
    show vechna angry with Dissolve(.3)
    vechna "Это не вредит мне!"
    hide vechna
    show black angry_var with Dissolve(.3)
    black "А не вредит ли? Пусть тело это не проживает, но зато проживает мозг."
    hide black
    show vechna thinking with Dissolve(.3)
    narrator "Девушка была недовольна непредвиденным конфликтом на пустом месте."
    show vechna thinking with Dissolve(.3)
    vechna "Для меня это просто инструмент, понимаешь? "
    vechna "Может быть, странный, но это новая культура. "
    vechna "Хоть умри, с этим уже ничего не сделаешь. "
    vechna "Оглянись, мы на другой планете. "
    vechna "Где люди даже жить не могут. "
    vechna "Остальное – е-рун-да. Я бы за это сотни раз умирала без притупления чувств."
    hide vechna
    narrator "С неба снова сыпались кристаллы."
    narrator "Сестра показала рукой на выход из пещеры. "
    narrator "Над дождем из кристаллов садилась звезда — местное Солнце."
    narrator "Сквозь минералы преломлялись лучи, на секунду зажигая камни яркими вспышками."
    narrator "Словно блестящие звезды падают с неба."
    narrator "В такие моменты все кажется неважным, никчемным, в сравнении с вселенной и её чудесами. И грусть отпускает."
    show black sad_var with Dissolve(.3)
    narrator "А позже, от осознания этой никчемности, становится еще хуже."
    show black sad_var with Dissolve(.3)
    black "Ты делаешь великие вещи."
    black "Но ты постоянно лежишь, подключившись к Фабрике, работаешь по семнадцать часов."
    hide black
    show vechna thinking with Dissolve(.3)
    vechna "Ты сюда подключился просто так? На мозг мне капать?"
    hide vechna
    show black sad_var with Dissolve(.3)
    black "Пообщаться, узнать как дела."
    hide black
    show vechna thinking with Dissolve(.3)
    vechna "Отлично дела! Были!"
    vechna "Я работаю в месте своей мечты. "
    vechna "Мне теперь платят за моделирование других планет. "
    vechna "Счастливое везение, что Онка просто помешан на космосе."
    vechna "И, опережая твои комментарии, я очень благодарна, что ты отдал мне победу!"
    vechna "Пойми, у меня правда загруженный период. Потом будет проще."
    vechna "Я использую нейрохакинг. И буду успевать то же, что и сейчас, часов за тринадцать-четырнадцать."
    hide vechna
    show black sad_var with Dissolve(.3)
    black "Только не говори, что подключишь себя к системе жизнеобеспечения."
    black "Тогда и на зрение ресурсы мозга не тратятся, и легкие от аппарата смогут работать!"
    hide black
    show vechna smile2 with Dissolve(.3)
    narrator "Вечна засмеялась."
    show vechna smile2 with Dissolve(.3)
    vechna "Я хочу повысить производительность мозга, убрать какую-нибудь внешнюю информацию, которую ему требуется обрабатывать. "
    vechna "Я не отключу свои легкие."
    hide vechna
    show black regular_confused with Dissolve(.3)
    black "Если честно, звучит плохо."
    hide black
    show vechna thinking with Dissolve(.3)
    vechna "Ты доверяешь мне?"
    hide vechna
    show black sad_var with Dissolve(.3)
    black "Опять этот вопрос..."
    jump scene_22


label scene_22:
    scene lake
    #Он приглашает к ней знакомого лиса, для скандального интервью, лис просит анонимности, чтоб ему не влетело
    narrator "Друзья сидели на берегу реки для переработки мусора. "
    narrator "Возле самой красивой свалки в мире. "
    narrator "Зеркальная масса наноботов отражала в себе цветную подсветку с потолка."
    show black regular_happy1 with Dissolve(.3)
    narrator "Аш что-то читал вслух Наташе. "
    hide black
    show natasha regular with Dissolve(.3)
    narrator "Она слушала невнимательно и всем своим видом показывала, как ей скучно."
    hide natasha
    hide natasha
    show black regular_happy1 with Dissolve(.3)
    black "Ты должна разбираться не только в микробиологии, но и в других смежных дисциплинах, быть в тренде."
    narrator "Они сидели на застеленном пледом полу, где были разложены печенье b чашечки. "
    narrator "У них был настоящий пикник. "
    black "Нельзя так долго грустить из-за проекта. "
    black "Ты все равно хорошо шаришь в микробиологии. "
    black "Чем занимаются у тебя в семье?"
    hide black
    show natasha angry with Dissolve(.3)
    natasha "Что ты все время спрашиваешь про семью?"
    natasha "Я думала, что воспитанных обществом это не интересует."
    hide natasha
    show black regular_happy2 with Dissolve(.3)
    black "У меня есть семья, просто в ней не было родителей. "
    black "И я вижу, что моя психика вышла более устойчивой."
    hide black
    show natasha angry with Dissolve(.3)
    natasha "Ну да, ищешь, с кем бы пообщаться, пока твоя сестра пожинает плоды победы, обрабатывая данные Онки в режиме 24/7."
    hide natasha
    show black regular_happy2 with Dissolve(.3)
    black "Только 17/7."
    black "И это было очень грубо."
    hide black
    show natasha sad with Dissolve(.3)
    natasha "Да. Прости. "
    natasha "Просто я со своей традиционной семьей общаюсь еще хуже."
    narrator "Она поджала под себя колени, длинные волосы свесились цветными волнами на лицо."
    hide natasha
    hide natasha
    show black regular_happy1 with Dissolve(.3)
    black "Тебе все равно нужно решить, чем ты хочешь заниматься. "
    black "Какие у тебя баллы на учебе?"
    hide black
    show natasha sad with Dissolve(.3)
    natasha "Мы с тобой познакомились на конкурсе для ботанов. Догадайся."
    hide natasha
    show black regular_confused with Dissolve(.3)
    black "Что тебе еще интересно?"
    hide black
    show natasha sad with Dissolve(.3)
    natasha "Вот новость для тебя:"
    natasha "Я учусь, как и большинство, не потому, что хочу собирать звезды, а чтобы выдержать всю эту бешеную конкуренцию! "
    natasha "Иногда кажется, эта гонка словно... "
    natasha "Словно, чем сложнее тебе двигаться, тем быстрее приходится это делать, чтобы не выбыть из игры. "
    natasha "Безумие, но даже дело моей жизни пришло не изнутри, а извне."
    natasha "Сказали: \"Наташ, факультет оки-доки\". А мне ни оки это и ни доки."
    natasha "Я не знаю, чем мне заниматься. "
    natasha "Где, блин, моя кьюти-марка??? Я хочу быть пони..."
    narrator "Наташа схватилась за голову."
    hide natasha
    hide natasha
    show black regular_happy1 with Dissolve(.3)
    black "У тебя есть блог. Кажется, тебе реально интересно им заниматься."
    hide black
    show natasha sad with Dissolve(.3)
    natasha "Интересно. Но это же не так круто, как наука."
    narrator "Она мило вытерла носик."
    hide natasha
    hide natasha
    show black regular_happy1 with Dissolve(.3)
    black "У тебя действительно проблема с чужим мнением."
    black "Есть сюрприз: сейчас придет лис — он готов рассказать про самые внутренности Фабрики! "
    black "Но без видео, анонимно."
    hide black
    show natasha smile with Dissolve(.3)
    narrator "Наташа сложила руки перед лицом, словно сейчас прочитает Ашу молитву. "
    narrator "Девушка подползла к нему на коленях, и по ее взгляду было не понятно, заплачет она сейчас или упадет в обморок."
    hide black
    show natasha smile with Dissolve(.3)
    natasha "Спасибо! Я не верю, что кто-то что-то сделал для меня!"
    hide natasha
    show fox angry with Dissolve(.3)
    narrator "За их спиной кто-то прочистил горло со всей возможной важностью."
    show fox angry with Dissolve(.3)
    fox "Кхм-кхм… Простите, я не знал, что у вас время молитвы. "
    fox "Какую религию вы исповедуете?"
    hide fox
    show black regular_happy2 with Dissolve(.3)
    narrator "Аш засмеялся и подал Нате руку."
    hide black
    hide black
    show natasha angry with Dissolve(.3)
    natasha "Мы не молимся! Это жуткая глупость."
    hide natasha
    fox "Неверное, нахальное утверждение!"
    fox "Это полезно для нервов."
    hide fox
    show natasha smile with Dissolve(.3)
    narrator "Наташа жестом пригласила Облачного сесть рядом. "
    narrator "Она уже не выглядела вялой и апатичной. "
    narrator "Громко хлопнула в ладоши. От неожиданности ее друг вздрогнул. "
    hide natasha
    show black regular_fear with Dissolve(.3)
    narrator "Аш вспомнил, что сестра всегда хлопала в ладоши, чтобы вокруг замолчали."
    hide black
    hide black
    show fox angry with Dissolve(.3)
    fox "Можем поскорее начать?"
    hide fox
    show natasha smile with Dissolve(.3)
    natasha "Конечно. Только мне нужно придумать вопросы. "
    natasha "Буду импровизировать."
    narrator "Про себя она ругала Аша, которого больше волновал \"вау\" эффект сюрприза, чем ее подготовка к интервью."
    hide natasha
    hide natasha
    show fox angry with Dissolve(.3)
    fox "Заранее оговариваю: никто не должен знать источник. "
    fox "Я возвращаю старый долг."
    hide fox
    show black regular_happy2 with Dissolve(.3)
    black "Лис имеет в виду, что съел входной жетон на конкурс, а я не стал жаловаться и подождал, когда он из него выйдет."
    narrator "Лис смешался и поправил воротник."
    hide black
    hide black
    show fox angry with Dissolve(.3)
    fox "\"Выйдет\" — это очень грубо звучит, можно подумать..."
    hide fox
    show black disgust_var with Dissolve(.3)
    black "Тут ничего эстетичного все равно не подумаешь."
    hide black
    show natasha angry with Dissolve(.3)
    narrator "Наташа заметила, что гость чувствует себя некомфортно."
    show natasha smile with Dissolve(.3)
    natasha "Мы очень признательны, что Вы тут."
    natasha "Скажите, Вы — разумный лис, потому что имеете имплант неокортекса? "
    natasha "Как ваше имя?"
    narrator "Девушка попыталась опустить ноги в массу нанороботов, но Аш успел привлечь ее внимание. Наташа очень не хотела бы остаться без ногтей. Мертвые ткани наноботы расщепляют быстро."
    hide natasha
    hide natasha
    show fox angry with Dissolve(.3)
    fox "Я предпочитаю скрыть свое имя."
    narrator "Сердито ответил лис."
    fox "Щенками мы проходим процедуру имплантации."
    hide fox
    show natasha smile with Dissolve(.3)
    natasha "Вы знаете, как работает имплант?"
    hide natasha
    show fox shock with Dissolve(.3)
    fox "Не знаю. Если б я был распределен в касту Высших, может знал бы."
    hide fox
    show natasha smile with Dissolve(.3)
    natasha "Как вы говорите?"
    hide natasha
    show fox shock with Dissolve(.3)
    fox "С помощью имплантов. "
    fox "После установки неокортекса, Высшие и Низшие получают возможность говорить."
    hide fox
    show black regular with Dissolve(.3)
    narrator "Аш все это знал, поэтому сидел молча и старался не мешать."
    hide black
    hide black
    show natasha smile with Dissolve(.3)
    natasha "Можно ли сменить касту?"
    hide natasha
    show fox angry with Dissolve(.3)
    fox "Очень редко лисы могут переходить между кастами."
    narrator "Лис выглядел очень гордым собой."
    hide fox
    show natasha smile with Dissolve(.3)
    natasha "Вы говорите о себе?"
    hide natasha
    show fox angry with Dissolve(.3)
    fox "Стараюсь, очень стараюсь."
    narrator "Наташа отправила в реку помятое печенье, и зеркальные капли попали на воротник лиса."
    fox "Аккуратнее! Никто не должен знать, что я тут был!"
    fox "Это Вам не кожа, а фабричная ткань! Ее разъест!"
    narrator "Лис судорожно счищал капли наноботов с воротника, но в некоторых местах всё же остались маленькие дырочки."
    narrator "Наташа кивнула головой на реку."
    hide natasha
    hide fox
    show natasha smile with Dissolve(.3)
    natasha "Наноботы Онки тоже имеют касты?"
    hide natasha
    show fox angry with Dissolve(.3)
    fox "Что за глупость?"
    narrator "В ответ она пожала плечами."
    hide fox
    show natasha regular with Dissolve(.3)
    natasha "Значит, Вы правда молитесь? "
    hide natasha
    show fox angry with Dissolve(.3)
    fox "Да, мы молимся, нас так воспитала Фабрика. "
    hide fox
    show natasha regular with Dissolve(.3)
    natasha "Почему одни лисы ходят на задних лапах, а другие - нет?"
    hide natasha
    show fox smile with Dissolve(.3)
    fox "Часто Высшие лисы могут ходить на задних лапах "
    fox "Но это - не ограничение, а привычка. Поэтому Низшие тоже ходят на задних."
    fox "Мне пора. "
    hide fox
    show natasha angry with Dissolve(.3)
    narrator "Наташа толкнула парня в бок, привлекая его внимание."
    hide natasha
    hide natasha
    show fox angry with Dissolve(.3)
    fox "В моей касте: сколько часов за день ты отработал, плюс шесть часов на сон, — столько времени ты проживешь."
    hide fox
    show natasha angry with Dissolve(.3)
    narrator "Наташа одним прыжком встала на ноги. Даже Аш вернулся из своих мыслей."
    show natasha angry with Dissolve(.3)
    natasha "Вы зарабатываете часы жизни?"
    hide natasha
    show fox shock with Dissolve(.3)
    fox "Все справедливо. "
    fox "Содержание каждого лиса требует ресурсов."
    fox "Как будто люди содержат детей, чтобы те потом ушли на все четыре стороны, и ничего им не дали."
    narrator "Лис встал и стал внимательно себя оглядывать."
    hide fox
    hide fox
    show natasha sad with Dissolve(.3)
    natasha "Уходите?"
    hide natasha
    show fox angry with Dissolve(.3)
    fox "Завтра я проживу десять часов, плюс шесть часов на сон. "
    fox "А я не хочу, чтобы мой день длился одиннадцать часов! Имейте совесть."
    hide fox
    show natasha regular with Dissolve(.3)
    narrator "Наташа не нашлась, что ответить. Лис уже удалялся. Девушка обняла Аша со спины."
    show natasha smile with Dissolve(.3)
    natasha "А этот Онка - чистое зло!"
    natasha "Теперь я не удивляюсь, почему он позволил Вечне ставить эксперименты на лисах."
    hide natasha
    show black sad_var with Dissolve(.3)
    narrator "Аш отвернул голову, ему было стыдно за сестру."
    hide black
    hide black
    show natasha angry with Dissolve(.3)
    natasha "Сделал на заводе свою собственную страну, где он - Бог!"
    narrator "Она встала и начала собирать свои вещи: баночку для воды, чашки."
    hide natasha
    hide natasha
    show black surprised_var with Dissolve(.3)
    black " Ты уходишь?"
    hide black
    show natasha angry with Dissolve(.3)
    natasha "Мы же договорились встретиться вечером?"
    hide natasha
    show black sad_var with Dissolve(.3)
    black "Хорошо."
    hide black
    narrator "Но вечером девушка была занята."
    jump scene_23


label scene_23:
    scene home
    #Парень поддерживает как может, рассказываем, что он вырос без родителей
    show black sad_var with Dissolve(.3)
    narrator "Темноволосый точно знал, какую эмоцию он может научить распознавать ИИ сегодня. "
    narrator "С самого утра он испытывал тревогу. "
    narrator "Его мысли прервал поток сообщений с одинаковым содержанием: \"Ты не идешь на учебу, ты идешь со мной к реке.\""
    scene station_corridor
    show black regular_fear with Dissolve(.3)
    narrator "Парень вышел из жилого отсека. Ему потребовалось время, чтобы убедить себя, что поводов для тревоги нет."
    scene lake
    narrator "Наташа сидела на пледе там же, где и в прошлый раз."
    hide black
    show natasha sad with Dissolve(.3)
    natasha "Она умерла. Она убила себя."
    hide natasha
    show black surprised_var with Dissolve(.3)
    black "О ком ты говоришь? "
    black "Ты рассказывала про семью: отца, брата, мать..."
    hide black
    show natasha sad with Dissolve(.3)
    narrator "По щекам Наташи потекли слезы."
    hide natasha
    show black sad_var with Dissolve(.3)
    narrator "Аш догадался."
    show black sad_var with Dissolve(.3)
    black "Прости. У меня не было родителей, никогда."
    narrator "Ему было очень стыдно, что он не испытывает жалости к родителям, только - к Наташе."
    narrator "Хотя знал, что это нормально. У него же не было традиционной модели семьи."
    narrator "Множество взрослых, и - сестра. Но его беспокоило, что Наташа видит, что ему не жаль."
    narrator "Уши молчали. Был бы на Ушах стыд, — она хотя бы знала, что у него есть совесть."
    black "Я бы хотел разделить с тобой, но..."
    hide black
    show natasha sad with Dissolve(.3)
    natasha "Ничего, я понимаю. "
    hide natasha
    show black regular with Dissolve(.3)
    black "Хочешь поговорить? Это твоя мать убила себя?"
    hide black
    show natasha sad with Dissolve(.3)
    narrator "Наташа сильнее заплакала."
    hide natasha
    hide natasha
    show black regular with Dissolve(.3)
    black "А где твой отец, брат?"
    hide black
    show natasha sad with Dissolve(.3)
    narrator "Девушка зарыдала и начала задыхаться."
    hide natasha
    show black sad_var with Dissolve(.3)
    narrator "Он решил ничего не спрашивать. Аш вспомнил, что такое \"паническая атака\". Вспомнил про термос в рюкзаке."
    narrator "Аш обнял ее так, что она не видела ничего, и уткнулась лицом ему в плечо."
    hide black
    show natasha sad with Dissolve(.3)
    narrator "Спустя несколько минут Наташа перестала реветь и начала говорить."
    show natasha sad with Dissolve(.3)
    natasha "Отца тоже нет, уже год. После копировании в сеть он пропал."
    hide natasha
    show black surprised_var with Dissolve(.3)
    black "А оригинал?"
    hide black
    show natasha sad with Dissolve(.3)
    natasha "Ты делаешь копию в сеть – и убиваешь тело, чтобы решить парадокс двойников."
    natasha "Потому что мы верим, что человек должен быть индивидуален. "
    natasha "Он должен быть единственным."
    hide natasha
    show black angry_var with Dissolve(.3)
    black "Но оригинал же - главный!"
    hide black
    show natasha angry with Dissolve(.3)
    natasha "Если он при жизни отдаст права на личность копии, то нет."
    hide natasha
    show natasha sad with Dissolve(.3)
    narrator "Она вытирала лицо салфетками, слезы так и текли из глаз, но девушка стала спокойней. "
    hide natasha
    show black angry_var with Dissolve(.3)
    narrator "Внутри Аша все перевернулось. Он сделал глубокий вход."
    show black regular with Dissolve(.3)
    black "Нужно выпить что-нибудь сладкое."
    narrator "Наташа смотрела в пол."
    black "А где твой брат? Вы нужны друг другу."
    hide black
    show natasha sad with Dissolve(.3)
    natasha "Мы не общаемся с тех пор, как отец пропал."
    hide natasha
    show black regular with Dissolve(.3)
    black "Наверное, ему нужно время."
    narrator "Девушка одобрительно качнула головой и вытерла нос."
    scene station_corridor
    hide black
    show natasha sad with Dissolve(.3)
    natasha "Куда мы идем?"
    hide natasha
    show black regular with Dissolve(.3)
    black "В кафе рядом с универом, если его можно так назвать. "
    black "Выпьем густой горячий шоколад. Это, конечно, яд, но помогает."
    hide black
    show natasha sad with Dissolve(.3)
    narrator "Наташа взяла его за руку и шла, тихо плача себе под нос."
    narrator "Еще издалека была заметна какая-то шумиха рядом с аудиторией университета. "
    hide natasha
    show black regular with Dissolve(.3)
    narrator "Аш хотел уйти."
    show black surprised_var with Dissolve(.3)
    black "На станции так просто толпы не собираются. "
    black "Пойдем другим путем."
    hide black
    show natasha angry with Dissolve(.3)
    narrator "Но Наташа, как дикая, побежала в сторону скопления роботов и нескольких человек, все еще держа его за руку."
    narrator "Они вошли внутрь."
    scene audience
    show black regular_fear with Dissolve(.3)
    narrator "Наташа сбавила шаг, и Аш заметил кровь среди людей и устройств. "
    hide black
    show natasha sad with Dissolve(.3)
    narrator "Подруга отпустила его руку и медленно подошла поближе."
    narrator "Почему-то ему захотелось остановить ее. Но он не решился, просто шел вслед."
    show natasha angry with Dissolve(.3)
    narrator "Совсем рядом кто-то сказал ей, чтобы она ушла, но девушка оттолкнула человека."
    show natasha sad with Dissolve(.3)
    narrator "На скамейке лежало что-то, накрытое черной тканью. Если вы думаете, что на темной ткани не видно кровь — вы ошибаетесь."
    narrator "В стороне лежал галстук. Инстинктивно, девушка все поняла. "
    narrator "Кто-то до последнего отказывается верить в происходящее, но она была не тем человеком. "
    narrator "Несчастная выросла среди людей – которые верят в худшее."
    show natasha sad with Dissolve(.3)
    natasha "Зачем?! Теперь я совсем одна!"
    hide natasha
    show black sad_var with Dissolve(.3)
    narrator "Кто-то из присутствующих заплакал. А Аш вспомнил слова Макса: \"У меня отец пропал в сети...\"."
    show black surprised_var with Dissolve(.3)
    narrator "Как же он раньше не догадался? "
    narrator "Наташу, бьющуюся в истерике, увели. "
    show black sad_var with Dissolve(.3)
    narrator "Ему не позволили пойти с ней."
    show black angry_var with Dissolve(.3)
    narrator "Аш уже был готов идти следом, в Медцентр. "
    narrator "Он же, при необходимости, выполнял функцию Центра Копирования во время переноса в сеть, и Центра Помощи - при проблемах с психикой."
    show black regular with Dissolve(.3)
    show black surprised_var with Dissolve(.3)
    narrator "Но ему пришло уведомление. Тот же Медцентр, комната №33."
    jump scene_24


label scene_24:
    scene helpcentre
    #Аш пытается дозвониться до Вечны, но выясняется, что та в больнице из-за неудачного теста с нейрохакингом. Девушка заходит все дальше. Оставаясь в тишине она думает, что сегодня могла лишиться всего (тела). И она готова, готова оставить брату оригинал. Она отправляет Онке запрос, можно ли так сделать
    narrator "В палате №33 без сознания лежала Вечна."
    show black sad_var with Dissolve(.3)
    narrator "Он хотел спрятаться от зрелища, которое все равно уже будет преследовать его всю жизнь."
    narrator "В смешанной реальности появился автоматический помощник — мобильная камера."
    mobile_camera "Состояние пациента удовлетворительное. "
    mobile_camera "Диагноз: отключение сигналов с рецепторов и скелетной мускулатуры. "
    mobile_camera "Последствия: возможно, чувствительность и активность мышц не восстановятся. "
    mobile_camera "Лечение: нет. Профилактика: прекращение неквалифицированного вмешательства в мозг."
    narrator "Парень схватился за волосы."
    hide mobile_camera
    show black surprised_var with Dissolve(.3)
    black "Как она могла отключить свою кожу и скелетные мышцы? Как?"
    mobile_camera "Могу найти информацию в сети. Отправить запрос?"
    hide mobile_camera
    black "Нет. Она в коме?"
    narrator "Он стал быстро ходить туда-сюда."
    mobile_camera "По текущим прогнозам, пациент придет в сознание через несколько часов."
    narrator "Аш начал вытирать слезы трясущимися руками."
    hide mobile_camera
    black "Как она поступила к вам?"
    mobile_camera "Она отправила запрос из сети."
    narrator "Парень развернулся к кровати сестры, пытаясь осознать ситуацию."
    hide mobile_camera
    black "Думала, что все контролируешь?"
    narrator "У него появился порыв дернуть сестру за руку, сбросить с кушетки, разбудить."
    narrator "Вместо этого, он почувствовал холодную ладонь сестры и одернул свою. "
    narrator "На секунду перестав дышать, он постарался отогнать страшную мысль."
    narrator "В голове загудело. Сердце стало биться громче, адреналин выплескивал ярость, разжигая кровь."
    black "Как у тебя хватило смелости сделать все это?"
    call surprised_disgust
    black "Как у тебя хватило совести?"
    narrator "Он игнорировал ответы на свои вопросы: \"Что тут такого? Врачи бы приехали, в сети я в сознании...\"."
    black "Почему? Почему из всего, что есть в этом мире, ты выбираешь различные способы покончить с собой?"
    narrator "У него появилось желание поступить с ней так же, как и она с ним. Взять шприц, взять нож: \"Интересно, тут есть, чем убить себя?\""
    black "Хай, Алиса, чем себя можно убить в радиусе двух метров?"
    alise "Острый угол тумбы. Рекомендуется удариться виском с расстояния десяти шагов от нее."
    hide alise
    black "Совсем не то."
    alise "Вы можете придавить паховую область ножкой кушетки и умереть от болевого шока."
    narrator "Парня передернуло."
    alise "Вариант №3. Вы можете съесть плед и умереть."
    show black regular_happy1 with Dissolve(.3)
    narrator "Ашу стало смешно. Он решил про себя: \"Понятно, почему разработчикам разрешили ввести такую функцию\"."
    narrator "Он услышал шелест ткани. Вечна очнулась. "
    show black sad_var with Dissolve(.3)
    narrator "Ему было сложно сдержаться и не обнять сестру, но она зашла слишком далеко."
    narrator "Он думал, что не должен поощрять такие действия."
    narrator "Руки еще дрожали, ноги стали подкашиваться, и он сел на пол рядом с кушеткой. Посмотрел на нее снизу вверх."
    black "Ты просто не знаешь меру. "
    black "Может, все же, подключиться к аппарату жизнеобеспечения? "
    black "Например, можно выключить легкие, или сердце. "
    black "Интересно, как это повлияет на твою производительность?"
    hide black
    show vechna thinking with Dissolve(.3)
    narrator "Вечна задумалась. Осторожно села на постели."
    hide vechna
    show black angry_var with Dissolve(.3)
    black "Хорошо, что можешь двигаться. "
    black "Но это уже глупо. Если хочешь уйти в сеть, - уходи."
    black "Только какая тебе от этого польза?"
    black "Жизнью в сети будет наслаждаться копия."
    show vechna thinking with Dissolve(.3)
    hide black
    narrator "Вечна молча смотрела на брата. Она словно выжидала: сказать или нет? Брат продолжал."
    hide vechna
    show black angry_var with Dissolve(.3)
    black "Удел настоящих людей - жизнь в реальности. "
    black "И если что-то нельзя сделать в ней - делать в сети."
    hide black
    show vechna thinking with Dissolve(.3)
    vechna "Ты не против моего копирования в сеть?"
    narrator "Парень закатил глаза."
    hide vechna
    show black disgust_var with Dissolve(.3)
    black "Не судьба тебе оптимизироваться на сто процентов, или даже на девяносто пять."
    black "Копия - это уже не жизнь. "
    black "Что это вообще? Ее симуляция?"
    hide black
    show vechna thinking with Dissolve(.3)
    vechna "Симуляция как раз полностью ее повторяет. "
    vechna "То, что похоже на жизнь, называется «эмуляция»."
    hide vechna
    show black surprised_var with Dissolve(.3)
    black "?"
    hide black
    show vechna thinking with Dissolve(.3)
    vechna "Сеть - это жизнь, просто ты ее не узнаешь в новой форме."
    hide vechna
    show black sad_var with Dissolve(.3)
    black "Все плохо закончится."
    black "Как ты смогла отключить импульсы от кожи и мышц? "
    black "Там же столько расчетов! Даже начни ты это до конкурса – не успела бы!"
    hide black
    show vechna thinking with Dissolve(.3)
    vechna "Я же на Фабрике работаю."
    hide vechna
    show black angry_var with Dissolve(.3)
    black "Начинаю понимать Макса..."
    black "Парень из университета, оказывается, брат Наташи. "
    black "И он умер. "
    black "К слову, после конфликта на Фабрике."
    hide black
    show vechna angry with Dissolve(.3)
    vechna "Оставь свои домыслы. "
    vechna "Если я и покорю дальний космос, то только за ресурсы Онки."
    hide vechna
    show black angry_var with Dissolve(.3)
    black "Одно другому не мешает."
    narrator "Он поднялся на ноги."
    black "Я подожду пока ты оденешься."
    hide black
    show vechna thinking with Dissolve(.3)
    vechna "Вообще-то... Мне кажется, я еще не оправилась и мне стоит провести здесь еще день."
    narrator "Брат разозлился."
    hide vechna
    show black angry_var with Dissolve(.3)
    black "Очень удобно - никто не помешает побыть в сети еще часиков двадцать."
    hide black
    show vechna angry with Dissolve(.3)
    vechna "Хватит."
    hide vechna
    show black angry_var with Dissolve(.3)
    black "Ты чуть не убила себя! Понимаешь, каково мне?"
    hide black
    show vechna angry with Dissolve(.3)
    vechna "А ты понимаешь, каково мне?"
    narrator "Она приподнялась на кушетке. Руки дрожали, но злость придавала сил."
    vechna "Я делаю то, что считаю верным!"
    mobile_camera "Не рекомендуется вставать с кровати в ближайшие три-пять часов."
    hide mobile_camera
    vechna "Вот видишь? Все решилось само. Я остаюсь."
    narrator "Голос парня дрожал."
    hide vechna
    show black angry_var with Dissolve(.3)
    black "Ты считаешь, что у тебя все нормально? "
    black "Ты можешь не восстановить чувствительность многих мышц и рецепторов."
    hide black
    show vechna thinking with Dissolve(.3)
    vechna "А оно мне надо?"
    hide vechna
    show black angry_var with Dissolve(.3)
    black "Ты чуть не умерла!"
    hide black
    show vechna angry with Dissolve(.3)
    vechna "Это побочный эффект!"
    hide vechna
    show black angry_var with Dissolve(.3)
    narrator "Зубы Аша скрипели друг о друга."
    narrator "Он пнул кушетку. Аппаратура для измерения показателей жизнеобеспечения затряслась. Вечна испугалась."
    mobile_camera "Законные разрушения невозможны в медицинском учреждения."
    narrator "Парень не обращал внимание на автоматического помощника. Вечна кричала."
    hide black
    hide mobile_camera
    show vechna angry with Dissolve(.3)
    vechna "Что ты делаешь? Успокойся!"
    narrator "Он стал задыхаться, злость отступала. Но нарастала в его сестре."
    narrator "Она снова приподнялась на постели."
    vechna "Ты лицемер. Ты сам..."
    narrator "В ее голосе слышалась желчь."
    vechna "Ты цифровизируешь чувства. Твои Уши..."
    vechna "Ты запрещаешь мне жить так, как я хочу! Где я хочу!"
    hide vechna
    show black angry_var with Dissolve(.3)
    black "Потому что ты выбрала самый короткий путь в могилу!"
    black "Ты просто не доживешь до отлета на Землю! "
    black "А, Вечна? Ты не вечна! Очнись уже!"
    hide black
    show vechna smile2 with Dissolve(.3)
    vechna "Пока не вечна."
    hide vechna
    show black angry_var with Dissolve(.3)
    black "Хочешь, делай копию в сеть."
    black "Все равно, как только ты поймешь, что та копия лучше тебя, – ты сама ее удалишь."
    black "Больше открытий! Ты, похоже, любишь только свое эго!"
    show black angry_var with Dissolve(.3)
    narrator "Он вылетел в коридор. "
    hide black
    show vechna sad with Dissolve(.3)
    narrator "Сестра долго смотрела в стену, она и забыла, что ее сознание не живет в сети, оно лишь заходит в нее."
    show vechna smile2 with Dissolve(.3)
    show vechna smile1 with Dissolve(.3)
    narrator "Ей пришло уведомление. Прочитав, девушка улыбнулась. Она смотрела в потолок и шептала сама себе: \"Скоро, задача будет выполнена\"."
    jump scene_25


label scene_25 :
    scene lake
    #Раскрываются карты, что Макс ее брат. Он винит в своей смерти Онку и Аша (чисто из вредности. А еще, саму Наташу в смерти отца, это ей нужны были ресурсы. Из-за этого, он пропал в сети
    show black angry_var with Dissolve(.3)
    narrator "Со стороны Аш выглядел, как сумасшедший. Наташа сидела на пледе, скрестив ноги."
    show black angry_var with Dissolve(.3)
    black "Куда ты? Луна маленькая."
    hide black
    show natasha angry with Dissolve(.3)
    natasha "Я не могу и не хочу тут находиться."
    natasha "Мой брат вынес себе мозги в университете. "
    natasha "Как мне тут жить?"
    hide natasha
    show black angry_var with Dissolve(.3)
    black "Это пройдет."
    hide black
    show natasha angry with Dissolve(.3)
    natasha "Что, прости, пройдет? "
    natasha "Люди стали оживать? О, как-то я пропустила эту новость!"
    natasha "Ты действительно не можешь поставить себя на мое место?"
    hide natasha
    show black angry_var with Dissolve(.3)
    black "Знаешь, я более, чем на твоем месте."
    black "Разве мы должны ругаться, а не поддержать друг друга?"
    black "Разве я - не твой родной человек?"
    hide black
    show natasha angry with Dissolve(.3)
    natasha "Кто тебе родной? Для общественников родной - любой, с кем знаком месяц."
    hide natasha
    show black regular with Dissolve(.3)
    narrator "Аш сделал шаг вперед. Наташа подалась назад."
    show black sad_var with Dissolve(.3)
    black "Почему ты не рассказала про свои проблемы?"
    hide black
    show natasha sad with Dissolve(.3)
    natasha "Для чего?"
    natasha "Расскажи я, что отец пропал во время копирования в сеть, а свое тело при этом сам умертвил... "
    natasha "Что бы ты делал? "
    natasha "Ходил бы за своей сестрой! А мне тоже нужно было внимание!"
    natasha "Расскажи я, что мать, которая при попытке удалить воспоминания экспериментальным нейрохакингом..."
    natasha "...Спалила себе мозг, что бы ты сделал?"
    hide natasha
    show black angry_var with Dissolve(.3)
    narrator "Аш молчал. Никогда он не чувствовал такого разочарования."
    show black angry_var with Dissolve(.3)
    black "Почему ты не сказала про Максима?"
    hide black
    show natasha angry with Dissolve(.3)
    natasha "Он во всем винил меня! "
    natasha "Что я требовала себе и факультет получше, и вещи, и вообще..."
    narrator "По ее щекам снова покатились слезы. "
    hide natasha
    show black angry_var with Dissolve(.3)
    narrator "Аш стоял напротив. За ним серебрилась река по переработке. "
    narrator "Девушка стояла и смотрела в глаза Аша."
    show black angry_var with Dissolve(.3)
    black "Теперь ты точно одна."
    hide black
    show natasha regular with Dissolve(.3)
    narrator "Плечи девушки на секунду опустились, но автоматически вытянулись в струну. Она вздернула подбородок."
    show natasha angry with Dissolve(.3)
    natasha "Ты хоть иногда думаешь о том, каково другим? "
    natasha "Не о том, что они сделают тебе, и как ты себя будешь чувствовать, а о том, что будут чувствовать они?"
    hide natasha
    show black disgust_var with Dissolve(.3)
    black "Ты неадекватная. "
    black "Ты, как и все, кто пережил подростковый возраст под Лунным Куполом – психованная."
    black "Ведь ты молчала, зная, что светит Вечне от самопального нейрохакинга!"
    black "Не пытайся выставить меня виноватым."
    show black fear_regular with Dissolve(.3)
    narrator "Темноволосый почувствовал толчок в грудь. Он понял, что стоит на краю. "
    hide black
    show natasha angry with Dissolve(.3)
    narrator "Наташа прижалась к нему. И он испугался, что она его столкнет."
    hide natasha
    show black fear_regular with Dissolve(.3)
    hide black
    hide black
    show natasha angry with Dissolve(.3)
    natasha "Стоило бы сбросить тебя. "
    natasha "Оставить с повреждениями мозга от переработанного протеза."
    hide natasha
    show black regular with Dissolve(.3)
    black "Импланта. "
    black "И я даже не против."
    hide black
    show natasha angry with Dissolve(.3)
    narrator "Она говорила сквозь зубы. Четко произнося каждый звук. "
    show natasha angry with Dissolve(.3)
    natasha "Пусть ты и твои идеи будут никому не нужны."
    hide natasha
    show black regular_happy2 with Dissolve(.3)
    black "Это и есть, моя текущая ситуация."
    hide black
    show natasha angry with Dissolve(.3)
    narrator "Наташа держала парня за толстовку, потом резко дернула на себя, заставив сделать несколько шагов вперед."
    show natasha angry with Dissolve(.3)
    natasha "Еще объяснительные писать."
    natasha "И без моей помощи сгниешь."
    hide black
    show black regular with Dissolve(.3)
    call surprised_disgust
    show black mood with Dissolve(.3)
    black "Кто бы мог подумать, что вместо трогательных прощаний, я познакомлюсь с тобой настоящей."
    hide black
    show natasha regular with Dissolve(.3)
    narrator "Девушка сложила плед, собрала влажные от слез платки и бросила в реку."
    show natasha regular with Dissolve(.3)
    natasha "Не пытайся всех контролировать! Я – не твоя сестра!"
    show natasha angry with Dissolve(.3)
    narrator "Уходя, она не подняла глаза на Аша. "
    hide natasha
    show black sad_var with Dissolve(.3)
    narrator "Он повернулся лицом к массе наноботов, подался вперед, словно намереваясь броситься вниз."
    show black sad_var with Dissolve(.3)
    black "Живого они меня не переработают, но Уши в голове расщипят."
    black "Смысл оставаться овощем и радовать Наташу?"
    show black sad_var with Dissolve(.3)
    narrator "Он получил уведомление, и, подумал было, что это Онка вспомнил про \"утешительный приз – ужин\"."
    show black surprised_var with Dissolve(.3)
    narrator "Темноволосый поставил ногу, нависшую над субстанцией, назад на берег и собрался домой."
    show black regular_sad with Dissolve(.3)
    narrator "Когда открыл сообщение – пришел в ужас и со всех ног помчался в Медцентр, выполняющий функцию Центра Копирования."
    scene station_corridor
    narrator "В голове стучал быстрый пульс и звучали слова: «Твоя сестра в Центре Копирования... Говорят, копии пропадают»."
    #Показываем полную сцену копирования Вечны. Она не хотела убивать оригинал, но что-то пошло не так. Почему-то рядом с Ашем оказался Лис. После этого, лиса повысит онка
    show black regular_fear with Dissolve(.3)
    narrator "Аш чувствовал, что плохой конец ближе, чем он думал."
    jump scene_26


label scene_26:
    scene helpcenter
    narrator "Спустя 30 минут."
    show vechna sad with Dissolve(.3)
    narrator "Вечна повернула голову к Ашу, лицо брата искажалось сквозь стекло, заляпанное кровью. Он бился лбом и руками. Зря."
    show black regular_blood with Dissolve(.3)
    hide black
    hide black
    show vechna angry with Dissolve(.3)
    vechna "Это все он... !"
    show vechna sad with Dissolve(.3)
    narrator "Ее заглушил голос станции:"
    robotic_voice "Автоматическая подача газа запущена."
    jump scene_27


label scene_27:
    scene helpcentere_3
    narrator "Настоящее время."
    show black sad_var with Dissolve(.3)
    black "Это все я? Неужели, она так думала? "
    black "Что это я во всем виноват?"
    black "Как я жалею, что дал код Ушей..."
    black "Не только сестра должна платить. Я - тоже."
    black "Здесь и закончу. "
    narrator "Он видит перед собой дверь, в смешанной реальности на ней выведено: \"Центр Помощи. Особые услуги. Статус: Ожидается Аш Хом.\""
    show black sad_var with Dissolve(.3)
    narrator "Аш с сидит с мешками под глазами. "
    help_center "Я должен произнести речь о красоте жизни."
    narrator "Ашу показывают фото их и Вечны."
    hide help_center
    black "Разве я давал разрешение на обработку этих данных?"
    help_center "Да. Я не произвожу оценочных суждений, поэтому можете чувствовать себя комфортно. "
    hide help_center
    black "Мне бы хотелось быстрее начать."
    help_center "Пройдите."
    narrator "Аш подходит к металлической двери. Нажимает «вход» и заходит. "
    scene blood_room
    narrator "Дверь сразу закрывается. Раздается мужской голос."
    man "На таком заказе нужен живой человек. Ну ты, парень, и удумал."
    show black regular_fear with Dissolve(.3)
    narrator "Внутри, парень не может ничего разглядеть. "
    show black regular with Dissolve(.3)
    narrator "Глаза привыкают к темноте. Он слышит рычание. "
    show black regular_sad with Dissolve(.3)
    narrator "Тело парализует страх, но в следующий момент его охватывает адреналиновая эйфория, и он чувствует отчаяние и злость."
    narrator "На него бросаются три собаки."
    call mad_fear
    black "Не только я виноват! Ты меня бросила!"
    show black mad_var with Dissolve(.3)
    narrator "Он сам не понимает, как под зубами оказывается пульсирующая шея пса."
    narrator "Все происходит быстро, у него во рту словно лопается помидорка-черри, забрызгав своим соком-кровью все вокруг."
    narrator "Вцепившаяся мертвой хваткой в руку собака остается без глаза, еще одна спешно убегает в соседний угол и начинает скулить."
    narrator "Аша качает, он чувствует тошноту."
    narrator "Открывается дверь."
    narrator "Вбегает мужчина с аптечкой в руке. "
    narrator "Он бросается к псам, обрабатывает рану одному из них и пытается остановить кровь."
    man "Ты ему артерию перегрыз!"
    man "Не по договору! Сиди! Надолго здесь останешься!"
    man "Решил сдохнуть - так бы и делал!"
    narrator "Пес, оставшийся без глаза, жалобно скулит. Мужчина, чуть не плача, осматривает голову пса, с любовью гладя его по морде."
    show black fear_var with Dissolve(.3)
    narrator "Аш начинает приходить в себя. Руки стали трястись только сейчас."
    narrator "Мужчина держит голову пса и гладит."
    man "Помощь скоро будет."
    man "Псы не должны были пострадать. Ты же сам заплатил, чтобы тебя съели!"
    show black sad_var with Dissolve(.3)
    narrator "Аш молчит. Что здесь можно сказать?"
    scene chip_factory_laboratory
    narrator "В лаборатории Онки: он и лисы смотрят на экран. Видят на нем Аша в крови и мужчину, бинтующего псов."
    hide black
    show onka danger with Dissolve(.3)
    onka "А вы так можете?"
    hide onka
    show fox shock with Dissolve(.3)
    fox "Мы в двадцать втором веке."
    hide fox
    show onka sneaky with Dissolve(.3)
    onka "Ну, чисто теоретически: что вы думаете о боях?"
    hide onka
    show fox angry with Dissolve(.3)
    narrator "Лис показывает всем своим видом, что он не будет это обсуждать."
    hide fox
    show onka thinking with Dissolve(.3)
    onka "Ладно. Пора провести обещанный ужин. "
    onka "Он же все-таки выиграл утешительный приз."
    jump scene_28


label scene_28:
    #Онка связывается с Ашем. Рассказывая, как с помощью кода ушей можно жить вечно. Аш задачется вопросом, почему сейчас тот говорит ему это все? Но соглашается - ведь это способ вернуть сестру. Но ему кое-что нужно (тело)
    scene blood_room
    show black sad_var with Dissolve(.3)
    narrator "Сидя в комнате изоляции, Аш проваливается в сон. Заключенный получает приглашение — в сети. "
    narrator "Забыв, где и по каким обстоятельствам находится, он автоматически принимает вызов и заходит в сеть."
    scene planet
    narrator "Виртуальный мир и понимание происходящего захлестывают его с головой."
    show black surprised_var with Dissolve(.3)
    black "Что мы тут делаем? Как ты получил доступ?"
    hide black
    show onka sneaky with Dissolve(.3)
    onka "Это работа моей сотрудницы. Почему бы не зайти?"
    hide onka
    show black angry_var with Dissolve(.3)
    black "Что тебе нужно? Все это чертовски странно. "
    black "Мне же должны были заблокировать сеть."
    hide black
    show onka smile with Dissolve(.3)
    onka "Я, что - зря в ней главный? Код, может, и открытый, а ядро - мое."
    onka "Это очень серьезно, если нельзя связаться с человеком в сети."
    onka "Поэтому я сразу принялся тебя искать."
    onka "Решил, здесь тебе будет уютно. "
    onka "Не бойся, разрушающие факторы окружающего мира отключены."
    hide onka
    show black angry_var with Dissolve(.3)
    black "Я принял все наказания, которые мне дали."
    hide black
    show onka smile with Dissolve(.3)
    onka "Да, охранник сообщил, что ты даже не пытался торговаться по праву субъективной оценки для личностей со здоровыми моральными ценностями."
    hide onka
    show black disgust_var with Dissolve(.3)
    black "Я в это число не попадаю."
    hide black
    show onka danger with Dissolve(.3)
    onka "У нас здоровые, моральные ценности! "
    onka "Мое и твое понимание хорошего и плохого совпадает с пониманием большей части людей."
    hide onka
    show black regular_happy1 with Dissolve(.3)
    narrator "Аш смеется."
    show black regular_happy1 with Dissolve(.3)
    black "Что, если наоборот? Мы все - больные?"
    hide black
    show onka smile with Dissolve(.3)
    onka "Думал, и считаю маловероятным, что сумасшедшие - почти девяносто пять процентов всех жителей Луны и Земли."
    hide onka
    show black sad_var with Dissolve(.3)
    hide black
    show onka smile with Dissolve(.3)
    onka "Тебе нравится космос?"
    hide onka
    show black angry_var with Dissolve(.3)
    black "Земля мне нравится больше."
    hide black
    show onka thinking with Dissolve(.3)
    onka "Это был риторический вопрос."
    hide onka
    show black angry_var with Dissolve(.3)
    black "Что тебе нужно? Можно покороче? Мне здесь тяжело."
    narrator "Аш смотрит на кристаллы под ногами и невольно думает про сестру."
    hide black
    show onka thinking with Dissolve(.3)
    onka "Мои предки видели в чипе лишь способ заработка, с помощью которого они финансировали борьбу с голодом и покорение Луны. "
    onka "Ерунду, одним словом."
    hide onka
    show black angry_var with Dissolve(.3)
    black "Поскольку, с недавних пор, мне наплевать на манеры... К чему ты ведешь?"
    hide black
    show onka angry with Dissolve(.3)
    onka "Я вижу в чипе большее."
    onka "Кое-что сумасшедшее - возможность жить вечно."
    hide onka
    show black surprised_var with Dissolve(.3)
    narrator "Аш не находит, что сказать. Он изо всех сил пытается понять, что говорит Илли."
    hide black
    hide black
    show onka victory with Dissolve(.3)
    onka "Чип - это то, что фиксирует карту активности мозга, вплоть до мощности сигналов в нем. И может передавать эти сигналы обратно в мозг."
    onka "Теоретически, цифровую копию можно использовать, как прослойку, - между переносом из одного тела в другое."
    onka "Сейчас люди могут уйти в сеть, но не вернуться в реальность."
    hide onka
    hide onka
    show black surprised_var with Dissolve(.3)
    black "Ты предлагаешь это исправить?"
    narrator "Аша прошибает пот."
    hide black
    show onka sneaky with Dissolve(.3)
    narrator "Онка еле сдерживается, чтобы не похвалить себя."
    show onka sneaky with Dissolve(.3)
    onka "Но мне нужен кто-то, кто готов заниматься проектом. "
    onka "Раз ты уже знаком с чипом, и написал для него прекрасный ИИ..."
    hide onka
    show black angry_var with Dissolve(.3)
    black "Какая-то слабая причина..."
    hide black
    show onka thinking with Dissolve(.3)
    onka "Ладно. Ты знаешь, в душе я – монополист, и занимаюсь дальним космосом."
    onka "Мне нравится концепция универсального языка: она может объединить людей из разных галактик лет через триста-пятьсот."
    hide onka
    show black surprised_var with Dissolve(.3)
    black "То есть, за работу над проектом по возвращению копий из сети, ты просто хочешь ИИ ушей? Он же простой."
    hide black
    show onka thinking with Dissolve(.3)
    onka "Он работает, и это главное. Считай, такая прихоть."
    onka "Конечно, всегда можно остаться в одиночке."
    narrator "Он выжидающе смотрит на парня."
    onka "Мы сделаем тебя очень популярным. Имплантируем Уши детям, вместе с чипом. А?"
    onka "Права – мне, а популярность – тебе."
    hide onka
    show black regular_confused with Dissolve(.3)
    black "Неплохо."
    black "Но с возвращением копии в тело столько технических моментов... И экспериментов..."
    hide black
    show onka danger with Dissolve(.3)
    narrator "Улыбка Илли становится все шире. Он поднимает руки и поправляет цилиндр."
    show onka danger with Dissolve(.3)
    onka "Сложный проект, но благой. Возможно, ты решишь за счет него некоторые проблемы..."
    onka "Ради вечной жизни в теле, а не в сети, стоит попробовать."
    onka "Ведь разве это жизнь? В цифре?"
    hide onka
    show black regular with Dissolve(.3)
    black "Ты прав..."
    narrator "Ему кажется, что что-то тут не так, но возможность вернуть сестру заглушает все остальное."
    narrator "Он вспоминает ее последние слова: \"Это все он...\"."
    narrator "Сердце Аша снова сжимается."
    call mad_fear
    black "Я виноват."
    hide black
    show onka danger with Dissolve(.3)
    onka "Что?"
    hide onka
    show black mood with Dissolve(.3)
    black "Хорошо, Уши Зайца станут твоей дочерней компанией."
    black "Но ты должен дать мне кучу ресурсов для возвращения..."
    narrator "Он оборвал себя."
    black "Для загрузки копий в живое тело."
    hide black
    show onka danger with Dissolve(.3)
    onka "Я так и хотел! "
    onka "Придумаем тебе крутой псевдоним."
    onka "Уже придумал! Черный Заяц! А как тебе?"
    $ash_name="Черный заяц"
    hide onka
    show black mad_var with Dissolve(.3)
    black "Публичный псевдоним?"
    narrator "Аш смеется, вспоминая пасти псов."
    hide black
    hide black
    show onka sneaky with Dissolve(.3)
    onka "Кстати, Черного Зайца отпустят, как только он выйдет из сети."
    onka "Сразу иди на Фабрику Чипов. "
    onka "Жду не дождусь подписания документов."
    jump scene_29


label scene_29:
    scene chip_factory_laboratory
    narrator "Войдя в помещение на Фабрике Чипов, им не приходится зажигать свет. Все вокруг светится причудливым образом. "
    narrator "Помещение представляет собой лабиринт, разделенный панелями с жидкостью — плоскими аквариумами с разноцветными сгустками слизи. "
    narrator "Каждый аквариум уникален по цвету, подсветке и наполнению."
    show onka victory with Dissolve(.3)
    narrator "Глаза владельца Фабрики горят."
    show onka victory with Dissolve(.3)
    onka "Добро пожаловать домой!"
    hide onka
    show black fear_var with Dissolve(.3)
    black "Это не мой дом."
    hide black
    show onka sneaky with Dissolve(.3)
    onka "Зря ты так... Привыкнешь."
    hide onka
    show black disgust_var with Dissolve(.3)
    black "Что это за аквариумы с плесенью?"
    hide black
    show onka sneaky with Dissolve(.3)
    onka "Это колонии бактерий! Созданы заселять космические объекты. Считай - Боги."
    hide onka
    show black surprised_var with Dissolve(.3)
    black "Это же гигантские чашечки петри?"
    hide black
    show onka confused with Dissolve(.3)
    onka "Что это?"
    hide onka
    show black regular_happy2 with Dissolve(.3)
    black "Я думал, ты шаришь в биотехнологиях, ну, или в школьной программе."
    hide black
    show onka thinking with Dissolve(.3)
    onka "Лисы из Высшей касты знают. А я — это космос, деньги и видение развития компании."
    onka "Я верю, что только эти бактерии способны стать космосу родными."
    hide onka
    show black regular_happy2 with Dissolve(.3)
    black "Или умереть."
    hide black
    show onka thinking with Dissolve(.3)
    onka "Если есть вычислительные мощности и время — нет нерешаемых задач."
    narrator "Илли Онка стоит посреди дела всей-всей своей жизни."
    hide onka
    hide onka
    show black regular_happy2 with Dissolve(.3)
    black "Исследуя Фабрику на конкурсе, я не нашел тут сухих лабораторий. Ну, таких, чтобы кто-то мог выйти в сеть и обработать там данные."
    hide black
    show onka thinking with Dissolve(.3)
    onka "Все вычисления делегированы копиям в сети и касте №2."
    hide onka
    show black regular_happy2 with Dissolve(.3)
    black "Все это, конечно, мило, но давай ближе к делу."
    black "Ты сам понимаешь, что нужно для создания технологии копирования из сети в тело?"
    hide black
    show onka danger with Dissolve(.3)
    onka "Я хочу узнать твое видение."
    hide onka
    show black fear_var with Dissolve(.3)
    narrator "Аш обводит взглядом помещение и продолжает шепотом:"
    show black fear_var with Dissolve(.3)
    black "Где взять живого человека, который согласится, чтобы в его тело посадили чужое сознание? Это же нелегально... И смертельно!"
    black "Копировать в лис? На первой стадии - ок, но нужен и человек."
    narrator "Онка наклоняется к Ашу. Тот чувствует запах манго."
    hide black
    hide black
    show onka sneaky with Dissolve(.3)
    onka "А что - тело смертельно больного мужчины может не подойти?"
    onka "Или нужна молодая девушка?"
    hide black
    show black regular_confused with Dissolve(.3)
    narrator "Аш серьезно смотрит на Онку. Тот точно знает, зачем он согласился на эту работу. Смысл кривить душой?"
    call mad_fear
    show black mood with Dissolve(.3)
    black "Раз так, то - да. Лет восемнадцати. Когда поймем, что все точно работает."
    black "До этого даже дед подойдет."
    hide black
    show onka danger with Dissolve(.3)
    onka "Придумай эксперимент, все его стадии, а там – подумаем."
    narrator "Илли хищно улыбается, и у Аша мелькает в голове мысль, что у Онки зубов больше, чем у Пеннивайза."
    hide black
    show black mad_var with Dissolve(.3)
    narrator "Но ради сестры он готов на любую сделку."
    jump scene_30


label scene_30:
    scene lake
    show black regular with Dissolve(.3)
    narrator "Парень чувствует невыносимое желание начинать действовать, не откладывая, двигаться к цели. Но, как же все сложно..."
    narrator "Аш смотрит на свое отражение в зеркальной поверхности реки из наноботов."
    show black mad_var with Dissolve(.3)
    narrator "Он смотрит в отражение своих глаз и понимает, каким был его взгляд, когда он решил убить собак. Автоматически, бессознательно, глупо..."
    call mad_fear
    show black mood with Dissolve(.3)
    black "Это всегда во мне было?"
    narrator "Когда он выбирал - жить или умереть, да или нет, один или ноль - Аш первый раз почувствовал ту эмоцию - безумие."
    narrator "Автоматическая генерация дизайна живет своей жизнью."
    narrator "Аш знает, что в конце концов Уши выберут тот дизайн, который лучшего всего ассоциируется у людей с эмоцией. Но еще рано."
    black "Вечнуть Вечну... "
    narrator "Он вспоминает, как она любила каламбуры. Пока не захакала свой мозг до неузнаваемости."
    black "Дьявол в деталях. И этих деталей тысячи..."
    black "Для того, чтобы понять, возвращается копия в тело или нет..."
    black "..Нужно провести эксперимент статистически достоверное количество раз."
    black "А это - сотни, в идеале - тысячи раз."
    black "Тысячи, мать его, людей!"
    black "Понятно, почему Онка не хочет брать это на себя."
    black "Он точно знает о Вечне. "
    black "Как-никак она у него работала. Поэтому и пришел ко мне."
    black "Очевидно, без его помощи я ничего не смогу..."
    narrator "Человек, который может позволить себе самую большую роскошь..."
    narrator "...Возможность собственным умом и ресурсами реализовывать свои дикие идеи и добиться успеха."
    show black regular with Dissolve(.3)
    narrator "Парень смотрит вверх: взгляд всегда упирается в далекие, но вездесущие стенки купола или потолки лавовых тоннелей под ним."
    narrator "Мысли в голове Аша в который раз бегут по кругу."
    narrator "Он представляет себе мягкие кресла корабля, рядом сидит сестра, разглядывает маленьких собачек и пушистых ящериц на руках у пассажиров поблизости. "
    narrator "Приятный голос сообщает, что корабль отправляется, и скоро они вернутся на Землю."
    narrator "Из мечтаний его вырывает рычание лиса. Перед парнем - Облачный, он стоит на четвереньках."
    hide black
    hide black
    show fox angry with Dissolve(.3)
    fox "Мне конец! Видео с интервью попало в сеть."
    fox "За мной и так есть другие грехи."
    hide fox
    show black disgust_var with Dissolve(.3)
    black "Успокойся, не убить же ты его пытался."
    hide black
    show fox angry with Dissolve(.3)
    narrator "Лис рассердился."
    hide fox
    show black surprised_var with Dissolve(.3)
    black "Или пытался?"
    black "Расскажи, что за видео?"
    narrator "Ответ сразу приходит ему в голову. Лис ложится на пол и закрывает лапами голову."
    black "Она не могла так поступить! Покажи."
    narrator "Да. Это действительно был тот замечательный день, когда Наташа брала у Лиса интервью."
    black "Как может быть настолько на всех наплевать?"
    hide black
    show fox shock with Dissolve(.3)
    fox "Еще как может быть! Я же ей помог, показал лианы..."
    hide fox
    show black regular_happy1 with Dissolve(.3)
    black "Месть уже в ее стиле..."
    black "А ты словно ненавидишь Онку! Раз показал ей его сокровища!"
    hide black
    show fox angry with Dissolve(.3)
    fox "Не важно, мой путь - на переработку."
    narrator "Зверь обреченно смотрит на реку с расщепляющими наноботами."
    fox "Вам, скорее всего, тоже."
    hide fox
    show black angry_var with Dissolve(.3)
    black "До сих пор не верю. После всего того, что произошло с ее семьей, с моей…"
    black "Она должна лучше всех меня понимать, но осознанно делает хуже и хуже!"
    hide black
    show fox angry with Dissolve(.3)
    narrator "Лис нервно машет хвостом и оглядывается по сторонам."
    show fox angry with Dissolve(.3)
    fox "Все труды насмарку! Я сбегу. Сбегу."
    hide fox
    show black regular with Dissolve(.3)
    narrator "Друг опускается на колени рядом с лисом."
    show black regular with Dissolve(.3)
    black "Ты напуган, это мешает тебе здраво рассуждать."
    black "Мы на Луне, в сети пещер, а над нами - купол."
    black "За ним – радиация, и нет атмосферы."
    narrator "Аш дотрагивается до Лиса."
    black "Куда ты хочешь сбежать?"
    hide black
    show fox smile with Dissolve(.3)
    narrator "Лис поднимает свою мордочку и рисует носом в воздухе круг."
    show fox smile with Dissolve(.3)
    fox "На Землю."
    hide fox
    show black regular_happy2 with Dissolve(.3)
    black "Ты не сможешь улететь в этом году."
    hide black
    show fox angry with Dissolve(.3)
    fox "Я могу пробраться на корабль через месяц."
    hide fox
    show black regular_confused with Dissolve(.3)
    black "Как можно не заметить лиса?"
    black "Но я мог бы взять тебя с собой. Как неразумное домашнее животное."
    hide black
    show fox angry with Dissolve(.3)
    fox "Унизительно!"
    hide fox
    show black regular_confused with Dissolve(.3)
    narrator "Парень пожимает плечами."
    show black regular_confused with Dissolve(.3)
    black "Зато не смертельно!"
    narrator "Лис перестает драматизировать."
    hide black
    show fox angry with Dissolve(.3)
    fox "Когда? Когда мы сможем вылететь?"
    hide fox
    show black regular_confused with Dissolve(.3)
    black "Через год. Я ручаюсь, что Онка тебя не тронет."
    hide black
    show fox angry with Dissolve(.3)
    fox "С чего мне Вам верить? Какая Вам выгода?"
    hide fox
    show black angry_var with Dissolve(.3)
    black "Да никакой выгоды! Что вы все..."
    hide black
    show fox angry with Dissolve(.3)
    fox "Вы нужны хозяину, только это ничего не значит."
    hide fox
    show black angry_var with Dissolve(.3)
    black "Мы закончим свои дела на Луне. Тебе же есть, чем заняться?"
    hide black
    show fox angry with Dissolve(.3)
    fox "Еще как есть!"
    hide fox
    show black angry_var with Dissolve(.3)
    black "Ты же хотел в высшую касту?"
    black "На счет видео..."
    hide black
    show fox angry with Dissolve(.3)
    fox "Оно по всей сети!"
    hide fox
    show black angry_var with Dissolve(.3)
    black "Это я тебя попросил об интервью. Сам и решу."
    hide black
    show fox shock with Dissolve(.3)
    fox "Как, как вы это решите?"
    hide fox
    show black mad_var with Dissolve(.3)
    black "У твоего хозяина, я уверен, рыльце тоже в пушку."
    black "Именно поэтому он, должно быть, сам все решил."
    narrator "Парень подталкивает Лиса в сторону выхода, и тот понуро плетется за ним на Фабрику Чипов."
    jump scene_31


label scene_31:
    scene chip_factory_laboratory
    show black sad_var with Dissolve(.3)
    narrator "Ученый осматривает лабораторию, не глядя никуда конкретно. Аш сосредоточен на мыслях."
    show black fear_var with Dissolve(.3)
    black "Значит, пункт один: решить, что такое «сознание»."
    black "Эксперимент будет успешен, если мы сможем понять: в новом теле - оригинал сознания или химера? "
    black "Значит, мне вообще не обязательно понимать, что такое «сознание»."
    black "Нужно лишь сравнить оригинал и копию в теле."
    black "Если они будут считать себя одним человеком, тогда сделаем допущение – это успех."
    narrator "Аш водит пальцем по панели со светящимися бактериями. От тепла они меняют цвет на малиновый."
    black "Ладно, значит, с этим разобрались."
    black "Пункт два: провести эксперимент по пересадке сознания. Безумный."
    black "Трудности: нужно пересадить сознание примерно в тысячу людей, чтобы удостовериться, что это работает. "
    black "На тысячу испытуемых, однозначно, будут ошибки. Вопрос: один процент или девяносто девять?"
    narrator "Он устало протирает глаза. Как хороший брат, он бы никогда не стал переселять сознание Вечны в качестве теста в тысячу непонятных тел. Мне нужна всего одна сестра."
    black "Копии Вечны, наверное, будет плевать, что ее еще раз скопируют в тело."
    black "Но что скажет Вечна в новом теле?"
    black "Стоит ли этим заниматься?"
    narrator "Панель с бактериями перед ним становится холодной, движение сгустков бактерий останавливается. На поверхности появляется конденсат."
    black "Ценой тысяч испытуемых. Тысяч жертв."
    black "Я действительно - зло?"
    narrator "Аш рисует перед собой единицу. А потом еще, и еще одну. Прошло минут десять, а он, как в трансе, все рисует и рисует. В зале слышатся шаги."
    hide black
    hide black
    show onka danger with Dissolve(.3)
    onka "Забыл кое-что!"
    show onka confused with Dissolve(.3)
    narrator "Хозяин Фабрики удивленно рассматривает Аша, который отрешенно рисует палочки."
    onka "Все хорошо?"
    hide onka
    show black sad_var with Dissolve(.3)
    black "Хочу прочувствовать. Как много это – тысяча жертв."
    black "Примерно столько нужно народа для эксперимента. А лис - еще больше."
    hide black
    show onka sneaky with Dissolve(.3)
    onka "Это не стоит победы над смертью?"
    hide onka
    show black fear_var with Dissolve(.3)
    black "Если облажаемся, то не стоит..."
    hide black
    show onka smile with Dissolve(.3)
    onka "Я забыл предложить закрепить сделку. Устрою обещанный ужин."
    onka "Не знаю как ты, но в таких ситуациях пьют что-то одурманивающее."
    onka "Лучше друг друга узнаем."
    hide onka
    show black surprised_var with Dissolve(.3)
    black "Не смогу пропустить такое зрелище. Лисы тоже пьют?"
    hide black
    show onka thinking with Dissolve(.3)
    onka "ИИ Фабрики им не позволяет. Они же сотрудники."
    onka "Я не спросил, как ты предпочитаешь веселиться: алкоголь, галлюциногены, убийства? "
    onka "Я имею в виду игры, конечно."
    hide onka
    show black surprised_var with Dissolve(.3)
    black "Ты так веселишься?"
    hide black
    show onka smile with Dissolve(.3)
    onka "Только на мамин день рождения. Почему нет?"
    hide onka
    show black surprised_var with Dissolve(.3)
    black "Куда я попал?"
    hide black
    show onka danger with Dissolve(.3)
    narrator "Онка отмахивается рукой и наклоняется к парню."
    show onka danger with Dissolve(.3)
    onka "Всем регулярно бывает невыносимо — это здоровое состояние человека."
    onka "Особенно в космосе. "
    onka "Луна никогда не станет такой, как Земля. Разве что - для бактерий."
    hide onka
    show black regular with Dissolve(.3)
    black "Надеюсь, у тебя есть другие темы для разговоров."
    show black disgust_var with Dissolve(.3)
    narrator "Илли продолжает держаться рядом, и Аш чувствует приторный фруктовый запах."
    hide black
    hide black
    show onka regular with Dissolve(.3)
    onka "Самое сложное для меня в реализации научных причуд - делиться ими."
    onka "Например, хочу я розовых крыс — это генетика."
    onka "Хочу, чтобы светились – это системная биология."
    onka "Хочешь, чтобы они играли с тобой в шашки и жгли твое электричество —"
    onka "– умей работать с железяками. "
    onka "Одному это сделать нереально."
    hide onka
    show black disgust_var with Dissolve(.3)
    black "А с лисами - реально?"
    hide black
    show fox smile with Dissolve(.3)
    narrator "В дверь заходят лисы с подносами, японским столиком и подушками. Расставляют в центре комнаты."
    narrator "Облачный остается, остальные выходят за дверь."
    hide fox
    show black regular with Dissolve(.3)
    narrator "Аш напрягается, ожидая, когда Илли отреагирует на видео в сети."
    hide black
    show onka smile with Dissolve(.3)
    narrator "Илли качает головой в сторону подушки рядом со столиком, жестом приглашая Аша сесть."
    show onka smile with Dissolve(.3)
    onka "Я с ними рос. Рядом, не среди них. Как я говорил, судьба лис — это Фабрика. "
    onka "ИИ которой заботиться о производстве лис. "
    onka "Она выбрала буддизм для одних каст и выращивание в загонах - для других."
    onka "Иначе они хуже будут выполнять свои функции."
    onka "Ты знал, что не так давно Высшая каста ела мозг Второй и Третьей каст?"
    hide onka
    show black disgust_var with Dissolve(.3)
    black "Рад, что это в прошлом."
    hide black
    show onka sneaky with Dissolve(.3)
    onka "Надеюсь."
    hide onka
    show black surprised_var with Dissolve(.3)
    black "Почему вечеринка в японском стиле?"
    hide black
    show onka sneaky with Dissolve(.3)
    onka "Для разнообразия. Дед, который сделал чип массовым, был японцем."
    hide onka
    show black regular_happy2 with Dissolve(.3)
    narrator "Аш пытается разрядить обстановку, избегая неприятных разговоров, которые могут возникнуть во время паузы."
    narrator "Лис наполняет отёко."
    show black regular_happy2 with Dissolve(.3)
    black "О, ты лучше, чем первая гейся Осаки."
    hide black
    show fox angry with Dissolve(.3)
    narrator "Лис недовольно смотрит на парня, он явно нервничает, но старается не подавать виду."
    show fox angry with Dissolve(.3)
    fox "Лисята надоели: убегают по ночам к Онке."
    fox " Они могут попасть в беду."
    hide fox
    show onka thinking with Dissolve(.3)
    narrator "Онка цыкает на лиса, показывая взглядом, что разговоров достаточно."
    hide onka
    show fox smile with Dissolve(.3)
    narrator "Тот дожидается, когда хозяин отвернется, и лакает подогретое саке из его чашечки."
    hide fox
    show black surprised_var with Dissolve(.3)
    narrator "Аш удивляется, думая при этом, что со стороны ничего не видно. Но Уши выдают его."
    hide black
    hide black
    show onka confused with Dissolve(.3)
    onka "Что такое?"
    hide onka
    show black regular_happy2 with Dissolve(.3)
    black "Я, знаешь, тоже ребенком спал среди кроликов."
    black "Когда попал на Луну."
    black "Как-то раз это спасло мне жизнь."
    black "Основной купол разгерметизировался, но загоны для животных имеют отдельную систему жизнеобеспечения."
    hide black
    show onka smile with Dissolve(.3)
    onka "Помню эту аварию. Я на Луне уже двадцать пять лет."
    hide onka
    show black regular_happy2 with Dissolve(.3)
    black "И как себя чувствуешь?"
    hide black
    show onka angry with Dissolve(.3)
    onka "Последний месяц - ужасно! Думаю, это стресс."
    onka "Еще вопросы?"
    hide onka
    show black regular_confused with Dissolve(.3)
    black "Был ли ты влюблен?"
    hide black
    show onka smile with Dissolve(.3)
    onka "В человека или явление?"
    narrator "Он обводит взглядом лабораторию со светящимися пластинами—петри."
    hide onka
    show black regular_confused with Dissolve(.3)
    black "Думаю, ты ответил на мой вопрос."
    hide black
    show onka confused with Dissolve(.3)
    narrator "Хозяин Фабрики пожимает плечами. Раздается лакающий звук – это лис."
    show onka victory with Dissolve(.3)
    onka "Этот сад! Он кишит жизнью для разных космических объектов."
    narrator "Илли краснеет и упирается взглядом в один из стендов - с зелеными замерзшими бактериями."
    hide onka
    show black angry_var with Dissolve(.3)
    black "Сменим тему..."
    black "Почему от тебя пахнет манго? Ты специально прыскаешься?"
    narrator "Онка медленно отворачивает голову от бактерий, его глаза заметно округляются."
    hide black
    hide black
    show onka confused with Dissolve(.3)
    onka "Манго? Ты не путаешь?"
    narrator "Аш утвердительно кивает головой."
    hide onka
    show black surprised_var with Dissolve(.3)
    black "Ты сам не чувствуешь?"
    hide black
    show onka thinking with Dissolve(.3)
    onka "Я не чувствую запахи."
    onka "Но теперь ясно, почему мне все время плохо."
    narrator "Онка встает и начинает снимать с себя одежду. "
    hide onka
    hide onka
    show black surprised_var with Dissolve(.3)
    black "Думал, что уже привыкаю к тебе."
    hide black
    show onka angry with Dissolve(.3)
    narrator "Стоящему рядом лису Онка бросает:"
    show onka angry with Dissolve(.3)
    onka "Проверь мою комнату! Найди на Фабрике манго или эфирные масло, все, что возможно! "
    onka "Никому не рассказывай, записи тоже все собери."
    onka "И без интервью, будь добр."
    hide black
    show fox smile with Dissolve(.3)
    narrator "Лис, немного покачиваясь, делает реверанс. Теперь он не так сильно нервничает."
    hide fox
    hide fox
    show black regular_confused with Dissolve(.3)
    black "Мне не то чтобы сильно интересно, но для чего ты разделся?"
    hide black
    show onka thinking with Dissolve(.3)
    onka "Нашел нам развлечение. Нужно это сжечь. "
    onka "У меня – аллергия!"
    hide onka
    show black regular_happy2 with Dissolve(.3)
    narrator "Аш хлопает себя по коленке."
    show black regular_happy2 with Dissolve(.3)
    black "На Фабрике есть возможность жечь?"
    hide black
    show onka sneaky with Dissolve(.3)
    onka "Значит, такое веселье подходит?"
    hide onka
    show black regular_happy2 with Dissolve(.3)
    black "То, что обыденность - на Земле, в закрытом куполе - дорогое удовольствие."
    hide black
    show onka danger with Dissolve(.3)
    onka "У меня есть бензин!"
    hide onka
    show black regular_happy1 with Dissolve(.3)
    black "Это действительно хорошая идея!"
    show black mad_var with Dissolve(.3)
    narrator "Весело произносит Аш, потом серьезно добавляет:"
    black "Для того, кто пару дней назад пытался скормить себя псам."
    hide black
    show onka sneaky with Dissolve(.3)
    onka "Безотходное производство – это прекрасно."
    hide onka
    show black mad_var with Dissolve(.3)
    black "Поэтому ты миллиардер?"
    narrator "Онка сделал испуганные глаза."
    hide black
    hide black
    show onka smile with Dissolve(.3)
    onka "Что ты, не дай Фабрика, чтоб я остался миллиардером."
    scene black_background
    narrator "Спустя несколько часов, Аш вспоминает, как Илли жег свою одежду в костре, и последнее, что они сказали друг другу:"
    hide onka
    show black mad_var with Dissolve(.3)
    black "Чтобы добиться вечной жизни, нам нужно нарушить все законы."
    hide black
    show onka danger with Dissolve(.3)
    onka "С какого начнем?"
    call mad_fear
    narrator "Аш смотрит в черноту и думает, готов ли взять на себя ответственность за смерть тысячи людей? А то и больше тысячи?"
    jump scene_32


label scene_32:
    scene chip_factory_laboratory
    #Аш получает триггер заняться разработкой, не только ради сестры, но и ради остальных, кто может прожить не двойную жизнь в сети, а в другом теле
    narrator "Спустя несколько недель."
    show onka thinking with Dissolve(.3)
    narrator "Онка вместе с лисом наблюдают за Ашем, который лежит на полу в лаборатории. Он в сети."
    show onka angry with Dissolve(.3)
    onka "Я думал, что после того, как получит добро, он восстановит сестру и начнет эксперимент по копированию в тело."
    onka "Но он медлит."
    onka "Когда я смогу получить столько ресурсов для обработки данных, что совершу революцию? "
    hide onka
    fox "По вашему запросу - насчет пяти-шести тысяч испытуемых. Мы нашли три варианта их получения."
    fox "С разной тяжестью последствий, так как закон не поощряет такие испытания. Тем более, на живых. Даже на добровольцах."
    hide fox
    onka "Какая разница. Наш Заяц все равно тянет время. "
    hide onka
    show fox smile with Dissolve(.3)
    fox "Ему очень сложно жертвовать людьми. И лисами."
    hide fox
    show onka thinking with Dissolve(.3)
    onka "Да. Но я до последнего надеялся, что он - самостоятельный мальчик. Зря."
    onka "Поэтому..."
    hide onka
    show fox shock with Dissolve(.3)
    narrator "Здание заметно вздрагивает. Лисы тревожно шепчутся. Снова чувствуется толчок."
    hide fox
    show onka danger with Dissolve(.3)
    onka "Скоро вернусь."
    hide onka
    show black sad with Dissolve(.3)
    narrator "Аш вышел из сети. Первые секунды тело не двигается."
    narrator "Вокруг все трясется. Парень выбегает в коридор. Лисы спокойно перемещаются по Фабрике, явно зная, что делать."
    show black fear_var with Dissolve(.3)
    black "Что происходит?"
    hide black
    show fox angry with Dissolve(.3)
    fox "Тоннель под куполом провалился!"
    hide fox
    show black fear_var with Dissolve(.3)
    black "Какой именно?"
    hide black
    show fox angry with Dissolve(.3)
    fox "На периферии... И он продолжает разрушаться."
    hide fox
    show black fear_var with Dissolve(.3)
    narrator "Аш, ошеломленный новостью, хватает себя за Уши и тянет их вниз. Его ноги подкашиваются. Он вспоминает крики людей, стучавших в отчаянии по куполу, под которым он когда-то сидел вместе с кроликами."
    show black fear_var with Dissolve(.3)
    black "Обвал пещеры на периферии — это стопроцентная разгерметизация!"
    black "Но я должен узнать, что там происходит!"
    hide black
    show fox angry with Dissolve(.3)
    narrator "Лис отворачивает мордочку."
    show fox angry with Dissolve(.3)
    fox "В аудитории есть окно. "
    fox "Но я боюсь, что зрелище может оказаться не из приятных."
    hide fox
    scene chip_factory_audience
    narrator "Аш поднимается в знакомое помещение. Лис отключает затемнение стекла."
    show black surprised_var with Dissolve(.3)
    narrator "Черный Заяц не сразу понимает, что произошло. С внешней стороны купола поднимаются клубы пыли. Клубы острой режущей пыли."
    narrator "Которую не обтачивает ветер. Она вступит в реакцию с жидкостью в легких и отравит организм токсичными соединениями."
    show black fear_var with Dissolve(.3)
    black "Мы должны открыть им!"
    narrator "Воспоминания о ночи с кроликами накрывают его. Воздух застревает в легких, и парень начинает задыхаться. "
    narrator "Он падает на пол, больно ударяясь коленями."
    narrator "Аш чувствует, как нарастает давление в голове. Перед ним, опираясь на одно колено, сидит Илли."
    narrator "Он смотрит Ашу в лицо и что-то говорит, но Аш его не слышит. Он лишь сжимает кулаки, ощущая под ногтями кровь."
    hide black
    hide black
    show onka danger with Dissolve(.3)
    onka "Это паническая атака."
    narrator "Он берет Аша за плечи, когда тот начинает заваливаться вперед. Холодные-холодные руки Илли приводят Аша в чувство."
    hide onka
    hide onka
    show black fear_var with Dissolve(.3)
    black "Нужно помочь остальным!"
    hide black
    show onka thinking with Dissolve(.3)
    onka "Как только возобновят герметичность. Но не сейчас."
    hide onka
    show black fear_var with Dissolve(.3)
    black "Ты не можешь их не пустить."
    hide black
    show onka thinking with Dissolve(.3)
    onka "Это лунная станция, тут все знают, что надо делать в такой ситуации."
    onka "Сейчас все должны оставаться в помещениях."
    hide onka
    show black sad_var with Dissolve(.3)
    call mad_fear
    narrator "Аш смотрит в окно, на площадь. Над ней клубится пыль, повисая в воздухе."
    narrator "И он точно знает, что, когда ее отфильтруют, все будет покрыто телами."
    narrator "Он точно знает, что ему теперь делать. Выбрать тысячу трупов или победу над смертью?"
    jump scene_33


label scene_33:
    scene Chip_factory_Laboratory
    #Онка предлагает как тело – Наташу. и не принимает отговорки, Аш мечется
    narrator "На следующий день."
    narrator "Онка лежит в углу, не двигается. Голова безжизненно свешивается вниз."
    show black surprised_var with Dissolve(.3)
    narrator "Аш входит вместе с Облачным, но тут же отскакивает назад."
    hide black
    hide black
    show fox shock with Dissolve(.3)
    fox "Неужели! Получилось?"
    hide fox
    show black regular with Dissolve(.3)
    narrator "Аш стоит, как вкопанный. Только думает: «Так не вовремя»!"
    narrator "Илли резко подскакивает и вскрикивает от испуга. Он смотрит на Аша заспанными, непонимающими глазами."
    hide black
    hide black
    show fox shock with Dissolve(.3)
    fox "Я решил, Вы мертвы..."
    hide fox
    show black angry_var with Dissolve(.3)
    black "Ты прикидывался мертвым?"
    hide black
    show onka angry with Dissolve(.3)
    onka "Что? Нет. Я всего лишь долго работал."
    onka "Ты не видел спящих людей?"
    show onka smile with Dissolve(.3)
    narrator "Онка щурит взгляд и расплывается в широкой улыбке."
    onka "Ты успел испугаться!"
    narrator "Он довольно потягивается."
    hide onka
    hide onka
    show black angry_var with Dissolve(.3)
    black "Потому что отдал Фабрике свое изобретение!"
    hide black
    show onka smile with Dissolve(.3)
    onka "Но я не о том."
    hide onka
    show black angry_var with Dissolve(.3)
    black "Есть план. "
    black "Нам нужно поместить одну копию в большое количество человек – от девятисот до двух тысяч."
    black "Потом проверяем, сколько из них соответствуют оригиналу. "
    black "Будет здорово, если хотя бы семьдесят процентов людей, оказавшихся в новом теле, будут считать себя исходной личностью."
    narrator "Илли сделал потрясенное лицо."
    black "Потом нужен итоговый тест — копию из сети поместить в тело. Да, это..."
    hide black
    show onka danger with Dissolve(.3)
    onka "Это того стоит!"
    hide onka
    show black fear_var with Dissolve(.3)
    black "Мы могли бы спасти всех тех, кто умер вчера."
    hide black
    show onka danger with Dissolve(.3)
    onka "Помню недавно, ты сомневался."
    hide onka
    show black fear_var with Dissolve(.3)
    black "Столько людей погибло вчера."
    hide black
    show onka sneaky with Dissolve(.3)
    narrator "Онка подходит к Ашу. Как всегда, неприятно близко, отчего Аш чувствует дискомфорт."
    show onka sneaky with Dissolve(.3)
    onka "Что бы ты ни потерял, распространение Ушей..."
    onka "..И возможность пересадить сознание в тело сделают жизнь людей намного лучше."
    onka "Ты сможешь довести дело до конца?"
    hide onka
    show black sad_var with Dissolve(.3)
    black "Идя на съедение к собакам, я не имел цели, надежды и желания."
    black "Но сейчас все это - не только для меня."
    narrator "Заяц не хочет говорить Илли обо всем. Он ему не доверяет, слишком все гладко..."
    hide black
    hide black
    show onka sneaky with Dissolve(.3)
    onka "Я нашел то, что ты просил. "
    onka "Для итогового теста \"копия-тело\" я выбрал кандидата. "
    onka "Одинока, доверчива и та еще заноза. "
    onka "Станет испытуемой или умрет."
    onka "Наташа."
    scene chip_factory_vines2
    show natasha smile with Dissolve(.3)
    narrator "В голове Аша возникает образ девушки, стоящей в комнате с инопланетными растениями."
    scene chip_factory_laboratory
    hide natasha
    show black fear_var with Dissolve(.3)
    black "Это как-то связано с видео?"
    black "Не удивительно."
    hide black
    show onka thinking with Dissolve(.3)
    onka "Связана с целой трансляцией с конкурса!"
    hide onka
    show black angry_var with Dissolve(.3)
    black "Может, ты и с Максимом связан?"
    hide black
    show onka sneaky with Dissolve(.3)
    narrator "Илли сжимает губы, плохо сдерживая улыбку, и пожимает плечами."
    show onka sneaky with Dissolve(.3)
    onka "Эта информация не нужна для принятия решения. "
    onka "Ты отказываешься?"
    narrator "За спиной хозяина Фабрики появляются лисы из Высшей касты, они скалятся."
    onka "А еще я нашел манго."
    narrator "Из толпы лис вырывается Облачный."
    hide onka
    hide onka
    show fox angry with Dissolve(.3)
    fox "Это он разрушил туннель!"
    hide fox
    show onka danger with Dissolve(.3)
    onka "Я же не кричу: «Это он хотел меня отравить»!"
    hide onka
    show black surprised_var with Dissolve(.3)
    black "Что ты сделал?"
    hide black
    show onka danger with Dissolve(.3)
    narrator "Но Хозяин Фабрики улыбается, показывая острые зубы."
    show onka danger with Dissolve(.3)
    onka "Разве это что-то изменит для всех тех людей?"
    hide onka
    show black angry_var with Dissolve(.3)
    narrator "\"Кроме того, что они были бы живы\" — сказал Заяц сам себе."
    show black angry_var with Dissolve(.3)
    black "От тебя пришло сообщение, что Вечна копируется?"
    hide black
    show onka sneaky with Dissolve(.3)
    narrator "Онка молчит."
    hide onka
    show black angry_var with Dissolve(.3)
    narrator "Парень вспоминает последние слова сестры: \"Это все он...\". В голове сверкает, словно молния: «Это все Онка»!"
    show black regular with Dissolve(.3)
    narrator "Аш думает про себя: «Вот кто помог копии убить оригинал. Вот с кем был договор...»"
    call mad_fear
    show black mood with Dissolve(.3)
    black "Хорошо - начали игру, значит, и закончим."
    hide black
    show onka confused with Dissolve(.3)
    onka "Так просто, готов продолжать?"
    show black mad_var with Dissolve(.3)
    narrator "Черный Заяц достает из кармана фиолетовый мяч, похожий на тот, из-за которого лис на конкурсе отгрыз себе лапу."
    narrator "В глазах Облачного загорается безумный огонь."
    show black mad_var with Dissolve(.3)
    black "Самый целеустремленный человек - тот, у кого нет выбора."
    #Здесь мы рассказываем о том, где они живую и что это - опасное место. Где бояться нужно не только природы, но и себя. Аш винит себя, что это он подвел Вечну к копированию. В сцене герой должен быть крут и логичен. Он рассказывает о законе копирования.
