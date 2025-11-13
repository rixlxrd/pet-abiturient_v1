from aiogram import types, F, Router, flags
from aiogram.types import Message, ContentType
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types.callback_query import CallbackQuery
from aiogram.types import InputFile, InputMediaPhoto

import aiogram

import kb

router = Router()


## api.example.com/router_name/


@router.message(Command("start"))
async def cmd_start(msg: Message):
    await msg.reply(
        text="Здравствуйте, выберите интересующую кнопку снизу",
        reply_markup=kb.menu,
    )

@router.message(F.text == "Вернуться в главное меню")
async def back_to_menu(msg: Message):
    await msg.reply(
        text="Вы вернулись в главное меню.",
        reply_markup=kb.menu  
    )

@router.callback_query(F.data == "shedule")
async def get_shedule(clbck: CallbackQuery):
    await clbck.message.reply(
        text="Расписание можно посмотреть перейдя по ссылке <a href='https://cabinet.birsk.ru/public-schedule/'>Расписание (birsk.ru)</a>",
        reply_markup=kb.back_to_main_menu  
    )

@router.callback_query(F.data == "shedule")
async def get_shedule(clbck: CallbackQuery):
        await clbck.message.reply(text="Расписание можно посмотреть перейдя по ссылке <a href='https://cabinet.birsk.ru/public-schedule/'>Расписание (birsk.ru)</a>",reply_markup=kb.back_to_main_menu )

@router.callback_query(F.data == "facult")
async def get_shedule(clbck: CallbackQuery):
        await clbck.message.reply(text="""<b>Фаультеты</b>:

Адаптивная физическая культура (3г, 10м)
Физическая культура  (3г, 10м)
Банковское дело (2г,10м)
Правоохранительная деятельность(3г,6м)
Физическая культура(3г, 10м)
Коррекционная педагогика в начальном образовании(3г, 10м)
Дошкольное образование – (3г, 10м)
Юриспруденция(2г, 10м)
Дизайн (по отраслям) (3г, 10м)
Экологическая безопасность природных комплексов (2г, 10м)
Компьютерные системы и комплексы (3г, 10м)
Разработка электронных устройств и систем(2г, 10м)
""", reply_markup=kb.back_to_main_menu )

@router.callback_query(F.data == "contacts")
async def get_shedule(clbck: CallbackQuery):
        await clbck.message.reply(text="""<b>Контакты:</b>

<b>Адрес:</b> 452450, Башкортостан, г. Бирск, ул. Интернациональная, 10
<b>телефон(факс):</b> 8(34784)4-04-55 - приемная
<b>e-mail:</b> academy@birsk.ru
<b>Сайт:</b> БФ УУНиТ (birsk.ru)
<b>Группа Вконтакте:</b> https://vk.com/kbfbashgu
""", reply_markup=kb.back_to_main_menu )

@router.callback_query(F.data == "price")
async def get_shedule(clbck: CallbackQuery):
        await clbck.message.reply(text="""<b>Стоимость обучения:</b>\n
Адаптивная физическая культура - 77 700 ₽
Физическая культура  - 77 700 ₽
Банковское дело - 61 900 ₽
Правоохранительная деятельность - 61 900 ₽
Физическая культура - 77 700 ₽
Дошкольное образование  - 61 900₽
Коррекционная педагогика в начальном образовании - 61 900₽
Юриспруденция - 61 900₽
Дизайн (по отраслям) - 77 700 ₽
Экологическая безопасность природных комплексов - 67 200 ₽
Компьютерные системы и комплексы - 67 200 ₽
Разработка электронных устройств и систем - 67 200 ₽
""", reply_markup=kb.back_to_main_menu )

@router.callback_query(F.data == "timing")
async def get_shedule(clbck: CallbackQuery):
        await clbck.message.reply(text="""<b>Сроки приема в Колледж:</b>\n
20 июня – начало приёма документов
10 августа – окончание приёма заявлений на специальности, где есть вступительные испытания (бюджет)
15 августа – окончание приёма заявлений (бюджет)
19 августа – окончание приёма оригиналов аттестатов (бюджет)
21 августа – зачисление (бюджет)
29 августа – зачисление (коммерция)
""", reply_markup=kb.back_to_main_menu )

@router.callback_query(F.data == "free")
async def get_shedule(clbck: CallbackQuery):
        await clbck.message.reply(text="""<b>Бюджетное обучение:</b>\n
Адаптивная физическая культура – 20 Мест
Физическая культура  - 20 Мест,  Проходной балл 4.1 
Экологическая безопасность природных комплексов – 20 мест 
Компьютерные системы и комплексы – 15 мест, Проходной балл 4.1
Разработка электронных устройств и систем – 10 мест""")
        
@router.callback_query(F.data == "apply")
async def get_shedule(clbck: CallbackQuery):
        await clbck.message.reply(text="""Перечень документов, необходимых для поступления в колледж:
1. Аттестат об основном или среднем образовании или его ксерокопия;
2. Паспорт (справка из РОВД об утере документа) предоставляется лично;
3. 4 фотографии (3х4 см); 
4. Медицинская справка;
5. 2 почтовых конверта с марками
При подаче в электронном виде:
                                  
Личный адрес электронной почты
Паспорт – вторая и третья страницы (скан/фото)
Паспорт – разворот с регистрацией по месту жительства (скан/фото)
Страховое свидетельство обязательного пенсионного страхования (СНИЛС) (скан/фото)
Документ о полученном образовании – титульный лист аттестата/диплома (скан/фото)
Документ о полученном образовании – приложение к аттестату/диплому (скан/фото)
Медицинская справка 086-у (скан/фото) (не для всех направлений)
Подписанное согласие на обработку персональных данных (скан/фото)
Подписанное заявление (скан/фото)Подписанное заявление (скан/фото)
                                  
Зачисление осуществляется на основании представленных документов (без сдачи вступительных экзаменов)
""", reply_markup=kb.back_to_main_menu )
        
@router.callback_query(F.data == "info")
async def get_shedule(clbck: CallbackQuery):
        await clbck.message.reply(text="""<b>Уфимский университет науки и технологий</b> - - это флагман науки и образования в республике Башкортостан. Наш университет появился в результате консолидации ведущих университетов республики - Башкирского государственного и Уфимского авиационного университетов.\n
                                  
Главной нашей целью всегда была и остается подготовка высококвалифицированных профессионалов, знающих и любящих свое дело, способных в любых условиях принимать правильные решения.
                                  
Мы - это компетентный преподавательский состав, мощная материальная база, ваш надежный трамплин в вашу будущую профессию.
                                  
У нас вы получите диплом <b>Уфимского университета науки и технологий</b> - показатель высокого уровня Ваших знаний, навыков и владения профессией.
""", reply_markup=kb.back_to_main_menu )

@router.callback_query(F.data == "why")
async def get_shedule(clbck: CallbackQuery):
        await clbck.message.reply(text="""<b>Почему колледж БФ УУНиТ?</b>\n
Отсрочка от службы в армии – Юношам предоставляется отсрочка от слубы в рядах Вооруженных сил РФ
Предоставляется общежитие – Всем нуждающимся предоставляется место для проживания в общежитии
Диплом УУНиТ – Диплом ФГБОУ ВО Уфимского университета науки и технологий г. Уфа
""", reply_markup=kb.back_to_main_menu )

@router.callback_query(F.data == "order")
async def get_shedule(clbck: CallbackQuery):
        await clbck.message.reply(text="""Приказы о зачислении можно посмотреть перейдя по этой ссылке: <a href='https://www.birsk.ru/%D0%B0%D0%B1%D0%B8%D1%82%D1%83%D1%80%D0%B8%D0%B5%D0%BD%D1%82/%D0%B4%D0%BE%D0%BA%D1%83%D0%BC%D0%B5%D0%BD%D1%82%D1%8B/2916?lang=en'>БФ УУНиТ</a>
""", reply_markup=kb.back_to_main_menu )