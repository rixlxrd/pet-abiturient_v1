from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup

# Главное меню
mens = [
    [InlineKeyboardButton(text="📝 Расписание", callback_data="shedule"),
     InlineKeyboardButton(text="📃 Факультеты", callback_data="facult")],
    [InlineKeyboardButton(text="📞 Контакты", callback_data="contacts"),
     InlineKeyboardButton(text="💰 Стоимость обучения", callback_data="price")],
    [InlineKeyboardButton(text="📇 Сроки приема в Колледж", callback_data="timing"),
     InlineKeyboardButton(text="😄 Бюджетное обучение", callback_data="free")],
    [InlineKeyboardButton(text="🔎 Как поступить в колледж БФ УУНиТ", callback_data="apply")],
    [InlineKeyboardButton(text="📋 Информация об учебном заведении", callback_data="info")],
    [InlineKeyboardButton(text="❓ Почему колледж БФ УУНиТ?", callback_data="why")],
    [InlineKeyboardButton(text="🪪 Приказы о зачислении", callback_data="order")]
]
menu = InlineKeyboardMarkup(inline_keyboard=mens)

# Клавиатура для возврата в главное меню
back_to_main_menu = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text="Вернуться в главное меню")]],
    resize_keyboard=True
)

# Пример другой клавиатуры для inline-действий
exit_menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Отмена", callback_data='cancel-request')]
])

artist_menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="HarryFox", callback_data='harryfox'),
     InlineKeyboardButton(text="MLC", callback_data='mlc')],
    [InlineKeyboardButton(text="Отмена", callback_data='cancel-request')],
])

track_menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Да", callback_data='correct'),
     InlineKeyboardButton(text="Нет", callback_data='incorrect')],
    [InlineKeyboardButton(text="Отмена", callback_data='cancel-request')],
])
