TOKEN = '1075116953:AAEK6WMAYuG-PTRaDhJzybkBieV6uBizVyg'
TOKEN2 = '1252385617:AAFvxYzzCnT-abSugBwY-zYfuVjYCsoGu48'

qst_list = []
qst2_list = ['Хто з нас найвірніший','Хто з нас підійде на роботу стюардеси','Хто з нас найбільше любить провокації',
             'Хто з нас не вірить у діда мороза','Кому з нас найважче ладити з дітьми','Хто буде найкрутішим татом',
             'Хто з нас найбільше любить тварин','Хто з нас Флатершай','Хто з нас найбільше любить дивитись "гиденькі передачкі"',
             'Хто з нас вірить в любов з першого погляду','Хто з нас носить найсексуальнішу білизну','Хто з нас найбільше любить їсти',
             'Хто з нас виграв б у шоу "Суперінтуїція"','Хто з нас найкраще тримає усе під контролем','Хто з нас сновида',
             'Хто з нас не любить гостей','Хто з нас пізнав дзен','Хто з нас хропить вночі','Хто з нас має найбільше одягу',
             'Хто з нас та ще штучка','Хто з нас найчастіше дивиться мультфільми','Хто з нас любить експерементувати',
             'Хто з нас відвідав найбільше концертів','Хто з нас найбільше ходить','Хто з нас в душІ Захар Беркут',
             'Хто з нас має найбільший ментальний вік','Хто з нас найбільше любить м‘ясо','Хто з нас найобережніший',
             'Хто з нас найкраще лазить по деревам','Хто з нас має самий легкий характер','Хто з нас хто','Хто з нас найвірніший',
             'Хто з нас підійде на роботу стюардеси','Хто з нас найбільше любить провокації','Хто з нас не вірить у діда мороза',
             'Кому з нас найважче ладити з дітьми','Хто буде найкрутішим татом','Хто з нас найбільше любить тварин','Хто з нас Флатершай',
             'Хто з нас найбільше любить дивитись "гиденькі передачкі"','Хто з нас вірить в любов з першого погляду',
             'Хто з нас носить найсексуальнішу білизну','Хто з нас найбільше любить їсти','Хто з нас виграв б у шоу "Суперінтуїція"',
             'Хто з нас найкраще тримає усе під контролем','Хто з нас сновида','Хто з нас найзатишніша людина',
             'Хто з нас поголиться налисо','Хто з нас найкращий актор','Хто з нас вміє міняти підгузки','Хто з нас любить Чіполіно',
             'Хто з нас найбільше схожий на Токмакову','Хто з нас не прасує одяг','Хто з нас найкращий однокласник',
             'Хто з нас найбільше любить сало','У кого з нас найгарніший тембр голосу','Хто з нас найсмішніше чхає',
             'Хто з нас знає найбільше таємниць ','Хто з нас вміє підтримати','Хто з нас найбільше схожий на четвер',
             'Хто з нас найчастіше перемагає','Хто з нас перфекціоніст','Хто з нас найзагадковіший','Хто з нас найбільше любить плавати',
             'Хто з нас найшвидше забуває','Хто з нас свободен, словно птица в небесах','Хто з нас найкраще вміє сидіти на кортанах',
             'Хто з нас найчастіше чистить зуби','Хто з нас найчастіше падає','Хто з нас найбільший бунтар','Хто з нас схожий на бурштинокопача',
             'Хто з нас шарить що таке чортополох','Кого з нас найбільше кусають комарі','Хто з нас найчастіше носить плаття','Хто з нас найтоксичніший(-ша)',
             'Кому з нас ти найбільше довіряєш','Хто з нас найвідповідальніший','Хто з нас найбільш аграрна душа?!','Хто з нас врізався у прозорі двері',
             'Хто з нас найрідше чистить зуби','Хто з нас найбільш толерантний','Хто з нас мав найвеселіше дитинство','Хто з нас стане порно-зіркою',
             'Хто з нас найбільш перебірливий у їжі','Хто з нас зробить пластичну операцію','Хто з нас найкраще робить макіяж','Хто з нас їсть найбільше м\'яса',
             'Хто з нас має найбільше шансів стити медійною персоною','Кого з нас ти вважаєш найбільш схожим на себе за світоглядом',
             'Хто з нас може кохати одну людину найдовше','Кому з нас найбільше личить ім\'я Владислав','Кого з нас ти найбільш асоціюєш з червоним кольором',
             'Хто з нас найраціональніше мислить','У кого з нас найбільше енергії','Хто з нас першим би вступив до піонерських рядів',
             'Хто з нас вміє варити суп з хвощів','Хто з нас зможе з\'їсти лимон без жодної емоції','Хто з нас найкраще грає у карти',
             'Хто з нас сталкерить інших людей у соц. мережах','Хто з нас найшвидше пристосовується у нових компаніях','Хто з нас не любить сало',
             'Кого б ви вибрали в якості сурогатного батька/матері для ваших дітей, якби це було потрібно','Хто б з нас поступив на Слизарин',
             'Кого з нас боїться НВ','Хто з нас був би крутим вчителем','Хто з нас найцікавіше розповідає історії','Хто з нас найкраще орієнтується на місцевості',
             'Хто з нас ніколи не одружиться/вийже заміж','У кого з нас найприкольніше прізвище','Хто з нас назве свою дитину Заподозар',
             'Хто з нас найчастіше потрапляє у пригоди','Хто з нас катався на сміттєвозі','Хто з нас для тебе є найцікавішим знайомством у житті',
             'Хто серед нас набільший лідер думок','З ким з нас ти б нізащо не погодився/погодилась переспати','Хто з нас читав найбільше книг',
             ',Хто з настнайкраще говорить українською','Хто з нас вміє користуватись пральною машинкою','У кого з нас найгарніша срака',
             'Хто з нас ходить їсти вночі','Хто з нас найменше думає перед тим, як робити','Хто з нас набільш «балуваний»','Хто з нас вміє користуватись насосом',
             'Хто з нас не вміє вдягатись по погоді','У кого з нас в кімнаті найбільший безлад','У кого з нас відсутній інстинкт самозбереження',
             'Хто з нас проводить найбільше часу у ванній','Хто з нас може плюнити на найбільшу відстань','Хто з нас має прихований дар робити пророцтва',
             'Чиї смаки у музиці вам найбільш імпонують','Хто звєрь????','Хто міг би бути п\'ятою Настею в нашому класі','Хто з нас носить у сумці найбільш небезпечні речі',
             'Хто з нас найбільш ризикує своїм життям','Хто з нас найгірше робить компліменти','З ким із нас ви б відправились у довгу подорож']
