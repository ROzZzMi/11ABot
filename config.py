TOKEN = '1075116953:AAEK6WMAYuG-PTRaDhJzybkBieV6uBizVyg'

qst_list = ['Я ніколи не курив(ла)', 'Я ніколи не фліртував(ла) з людиною,старшою за себе',
            'Я ніколи не думав(ла) про самогубство', 'Я ніколи не одягав(ла) пакет на голову під дощем',
            'Я ніколи не говорив(ла) друзям,що я їх люблю', 'Я ніколи не мав(ла) симпатії до Павла',
            'Я ніколи не хотів(ла) прибити штукатуркою свого однокласника/ однокласницю',
            'Я ніколи не влаштовував(ла) пікнік на уроці', 'Я ніколи не уявля(ла) свій перший раз',
            'Я ніколи не брав(ла) участь у мітингу', 'Я ніколи не пив(ла) джин тонік',
            'Я ніколи не подорожував(ла) у гори з наметами', 'Я ніколи не хамив(ла) Ларисі Ігорівні',
            'Я ніколи не знімав(ла) на відео свій танець', 'Я ніколи не  складав(ла) пошлі пісні',
            'Я ніколи не думав(ла),що вагітна', 'Я ніколи не уявляв(ла) напад на школу',
            'Я ніколи не мав(ла) симпатії до своєї однокласниці/свого однокласника(у даному складі)',
            'Я ніколи не ставив(ла) засос', 'Я ніколи не списував(ла) на ДПА',
            'Я ніколи не займався (лась) мастурбацією', 'Я ніколи не плакав(ла) над фільмом',
            'Я ніколи не їв(ла) суп носом', 'Я ніколи не їв(ла) сніг',
            'Я ніколи не сміявся(лась)над жартами з сексуальним підтекстом',
            'Я ніколи не дзвонив(ла) у двері та тікав після цього', 'Я ніколи не ‌займався(лась) сексом',
            'Я ніколи не цілувався(лась) з людиною тієї ж статі', 'Я ніколи не фотографувався(лась) на даху',
            'Я ніколи не вибігав(ла) голим на вулицю', 'Я ніколи не ходив(ла) голим по хаті',
            'Я ніколи не ‌зраджував(ла) друзів', 'Я ніколи не грав(ла) на гроші', 'Я ніколи не ‌купувала прокладки',
            'Я ніколи не не відчував(ла) сексуального бажання до вчительки/вчителя',
            'Я ніколи не грубіянив(ла) старшим', 'Я ніколи не грав(ла) у покер',
            'Я ніколи не ‌думав(ла) про друга(подругу) у ролі коханця', 'Я ніколи не крав(ла)',
            'Я ніколи не фанатів(ла) від важкого року', 'Я ніколи не напивався(лась)до втрати памяті',
            'Я ніколи не ‌закохувалась в Олександра Дмитровича', 'Я ніколи не сідав(ла) на шпагат',
            'Я ніколи не мав(-ла) сексуального потягу до людини з свого класу(у даному складі)',
            'Я ніколи не ‌ходив(ла) у нічний клуб', 'Я ніколи не був(ла) на нудистському пляжі',
            'Я ніколи не був(ла) кинутий другою половинкою', 'Я ніколи не купався(лась) у фонтані',
            'Я ніколи не був(ла) у відносинах більше року', 'Я ніколи не виставляв(ла) аватарку з другою половинкою',
            'Я ніколи не кидав(ла) другу половинку', 'Я ніколи не уявляв(ла) в еротичних фантазіях друга чи подругу',
            'Я ніколи не спав(ла) на підлозі після вечірки', 'Я ніколи не бачила еротичні сни',
            'Я ніколи не кидатиму свою другу половинку через те,що незадоволення у сексуальному плані',
            'Я ніколи не вигравав(ла) у якомусь гіві', 'Я ніколи не пікапив дівчину/хлопця у соцмережах',
            'Я ніколи не відчував(ла) сильну ненависть до свого однокласника/однокласниці', 'Я ніколи не доїла корову',
            'Я ніколи не зачинявся(лась) у кімнаті з малознайомою дівчиною/хлопцем', 'Я ніколи не сідав(ла) на дієту',
            'Я ніколи не купався в одязі', 'Я ніколи не спав на підлозі', 'Я ніколи не боявся замовляти таксі',
            'Я ніколи не їздив «зайцем» у транспорті', 'Я ніколи не плював у чай людині, яку я не люблю',
            'Я ніколи не крав мівіну', 'Я ніколи не грав у карти', 'Я ніколи не їв пісок', 'Я ніколи не гладив козу',
            'Я ніколи не дивився аніме', 'Я ніколи не користувався принтером НВ',
            'Я ніколи не бажав Гарного дня! незнайомцям', 'Я ніколи не переписувся з арабами',
            'Я ніколи не купував презервативи', 'Я ніколи не ходив по вулиці без нижньої білизни',
            'Я ніколи не дивився Вінкс', 'Я ніколи не  їздив автостопом',
            'Я ніколи не брав флаєрів у людей,які їх роздають', 'Я ніколи не був у протестантській церкві',
            'Я ніколи не плутав сало з бананом', 'Я ніколи не купував вазелін', 'Я ніколи не мріяв мати вуса']

qst2_list = ['Хто з нас першим вийде заміж (одружиться)?','Хто з нас першим закурив?','Хто з нас матиме (мав) перший секс','Хто з нас найкраще цілується','Хто з нас найкраще вчиться','Хто з нас найсмачніше готує','Хто з нас найгірше танцює','Хто з нас найталановитіший','Хто з нас найкраще співає','Хто з нас найпопулярніший','Хто з нас найлегший','Хто з нас найвідвертіший','Хто з нас найбільший боягуз','Хто з нас найбільш лицемірний','Хто з нас найсексуальніший','Хто з нас першим заробив власні гроші','Хто з нас найсмішніше жартує','Хто з нас найзанудніший','Хто з нас має найбільше шкідливих звичок','Хто з нас найпримхливіший','Хто з нас має  найкрутіший смак','Хто з нас найщасливіший','Хто з нас найбільш вразливий','Хто з дівчат найжіночніша','Хто з хлопців наймужніший','Хто з нас наймудріший','Хто з нас найкраще вирулює ситуації','Хто з нас найкращий організатор','Хто з нас найкраще шарить в комп','ютерах','Хто з нас найбільше бдсм','Хто з нас перфекціоніст','Хто з дівчат першою зломить каблук','Хто з нас найбільше серцеїд','Хто з нас першим матиме дитя','Хто з нас найбільше безтурботний','Хто з нас найлінивіший','Хто з нас найбільше подобається вчителям','Хто з нас найсильніший','Хто з нас найнепередбачуваніший','Хто з нас матиме найбільше дітей','Хто з нас має найбільше психічних розладів','Хто з нас має найменше комплексів','Хто з нас найбільше підходить для роботи з людьми','Хто з нас наймиліший','Хто з нас найбільше підлиза','Хто варить найсмачніший суп','Хто з нас найбільше любить тусовки','Хто з нас найкумарніший','Хто з нас найбільше спить','Хто з нас найхитріший','Хто з нас найбільший балабол','Хто з нас найжорстокіший','Хто з нас найбільш нервовий','Хто з нас перший зляже,якщо ми напємось','Хто перший лягає спати','Хто знає більше віршів','Хто найкращий староста на віки',' Хто з нас першим захворіє на коронавірус','Хто з нас першим захворіє на коронавірус','Хто з нас найбільше впливає на своє оточення','Хто з нас найслухніша дитина','Хто з нас найбільший меломан','Хто з нас останній знайде роботу','Хто з нас першим здасть на права','Хто з нас найазартніший','Хто з нас першим посивіє','Хто з нас найкраще ладить з дітьми','Хто з нас найрозкутіший','Хто з нас найкрутіше фоткає','Хто з нас першим наб’є татуху','Хто з нас найбільше бреше','Хто з нас найбільше любить Винника','Хто з нас житиме за кордоном','Хто з нас котик-муркотик?','Кого з нас тобі хочеться обійняти саме зараз?','Хто з нас бачив найбільше фільмів','Хто з нас виглядає найстаршим','Хто з нас найсмачніше готує','Хто з нас найкраще вміє списувати','В кого з нас буде найбільше дітей','Хто з нас найстильніше одягається','Хто з нас найкраще пристосований до виживння у  дикій природі','Хто з нас веде найкрутіший інстаграм','Хто з нас мав найбільше хлопців/дівчат','Хто з нас найкраще здасть ЗНО','Хто з нас має найгірший музичний смак','Хто з нас має найкраще почуття гумору','Хто з нас прихований маньяк','Хто з нас виграє 1000000€ у лотерею','Хто з нас найбільш солодкоїжка','Хто з нас житиме за кордоном','Хто з нас любить найгострішу їжу','Хто найчастіше дон в мафії','Хто найчастіше перебігає дорогу на червоний колір','Хто з нас закохувався ще у дитячому садочку','Хто з нас найбільш опитмістична особистість','Хто все таки буде танцювати на виспускному з Пашой?!','Хто з нас найвредніший', 'Хто з нас найшвидше закохується','Хто з нас найбільше киця','Хто з нас найрадикальніший','Хто з нас найбільше загально розвинутий','Хто з нас знає столицю Гондураса','Хто з нас виглядає, як бубочка','Хто з нас матиме пивний животік','Хто з нас першим зв’яже світер внукам','Хто з нас зніметься у фільмі','Хто з нас має найбільший талант до створення різних смішних капостей','Хто з нас в дитинстві втикав пальці у розетку','Хто з нас поливав людей водою з вікна','Хто з нас вбив Кеннеді?!','Хто з нас таємно належить до масонів','Хто з нас застрягав у батареї/паркані/під диваном','Хто з нас найкраще вміє доїти корову','Хто з нас має вдома наручники','Хто з нас отримає Нобелівську премію','Хто з нас найкраще вміє стріляти (цигарки не рахуються!)','Хто з нас найбільший(а) чистюля','Хто з нас найчастіше знайомиться з людьми','Хто з нас за своє життя розбив найбільше посуду','Хто з нас найгучніше сміється','Хто з нас вміє в\'язати макраме','Кого з нас найбільше не любить Мар\'яна Романівна','Хто з нас найшвидше вміє чистити картопю','Хто з нас вміє міняти колесо в машині','З ким із нас найцікавіше гуляти','Хто з нас фєєчка Блум','Хто з нас вміє варити мило','Хто з нас вміє випрошувати знижку на базарі','Хто з нас має пакет з пакетами','Хто з нас найбільше схожий на Пашу Кортекса','Хто з нас матиме партнерські роди','Хто з нас першим закохався' ,'Хто з нас першим погоджується на авантюри(легальні!)','Кому з нас потрібно найменше часу, щоб закохатись','Кому з нас легше обманювати','Хто з нас найчастіше п\'є алкоголь','Кого з нас найлегше вмовити','Хто з нас найчастіше пропускає школу','Хто з нас найбільше любить вареники','Хто з нас найкраще готує','Хто з нас найкращий організатор','У кого з нас можуть бути найяскравіші мрії','Хто з нас найбільш забобонний','У кого з нас найвищі вимоги до людей з оточення','У кого з нас найкращий смак','Хто з нас найбільше ниє','Хто з нас найбільш гостинний','Хто з нас має найбільше страхів і фобій','Хто з нас найбільш комунікабельний','Кому з нас найлегше заводити нові знайомства?','Хто з нас найбільший інстаграмщик','Хто з нас міг би стати ютьюб блогером','Хто з нас найкраще зберігає таємниці','Хто з нас найменш говіркий','Хто з нас найбільш "тепличний" ','Хто з нас має найкращий почерк','Хто з нас найбільше не любить сюрпризи','Хто з нас найбільш романтичний','Хто з нас найбільш киця']