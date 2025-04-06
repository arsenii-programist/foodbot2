from config import TOKEN
from PIL import Image, ImageOps  # Install pillow instead of PIL
from logic import detect_food
import telebot

bot = telebot.TeleBot(TOKEN)

# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """
Привет, Я FoodBot я создан что-бы определять еду.
сейчас я могу определить только 9 еды
вот вся едакоторую я могу показать:
1 хлеб
2 апельсин
3 банан
4 мясо
5 морковь
6 лук
7 молоко
8 огурец
9 креветка
10 яблоко
""")

@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    file_info = bot.get_file(message.photo[-1].file_id)
    file_name = file_info.file_path.split('/')[-1]
    downloaded_file = bot.download_file(file_info.file_path)
    with open(file_name, 'wb') as new_file:
        new_file.write(downloaded_file)
    image=Image.open(file_name)
    result, score = detect_food(image)
    bot.reply_to(message, result + '\n' + str(score))
    if result.startswith('яблоко'):
        bot.send_message(message.chat.id,'Это яблоко! Оно вкусное. В яблоке содержится витамин C, который помогает с лечением, так что ешь яблоки, когда ударился или заболел.')
    elif result.startswith('хлеб'):
        bot.send_message(message.chat.id,'Это хлеб! Белый хлеб вкуснее черного, но черный хлеб намного полезнее белого.')
    elif result.startswith('апельсин'):
        bot.send_message(message.chat.id,'Это апельсин! Вот интересный факт про апельсины:Апельсины бывают не только оранжевые, но и зелёные.')
    elif result.startswith('банан'):
        bot.send_message(message.chat.id,'Это банан! Банан — это ягода, хотя многие привыкли считать его фруктом.')
    elif result.startswith('мясо'):
        bot.send_message(message.chat.id,'Это мясо!Мясо - один из наиболее ценных продуктов питания. Оно необходимо человеку как материал для построения тканей организма, синтеза и обмена веществ, а ещё как источник энергии.')
    elif result.startswith('морковь'):
        bot.send_message(message.chat.id,'Это морковь! Многие думают, что морковь улучшает зрение, но сама по себе морковь не улучшит остроту зрения, если уже есть проблемы. Однако витамины, содержащиеся в этом овоще, способствуют укреплению здоровья глаз.')
    elif result.startswith('лук'):
        bot.send_message(message.chat.id,'Это лук! Лук — хорошее витаминное средство, особенно рекомендуемое в зимне-весенний период, но используемое круглый год.')
    elif result.startswith('молоко'):
        bot.send_message(message.chat.id,'''Это молоко! 
                         --Почему молоко белое?
                         --Молоко становится белым из-за белка казеина, который в нём содержится. Казеин образует частицы шарообразной формы — мицеллы, они-то и окрашивают молоко в белый цвет.''')
    elif result.startswith('огурец'):
        bot.send_message(message.chat.id,'Это огурец! Огурцы состоят из воды примерно на 95–97%. ')
    elif result.startswith('креветка'):
        bot.send_message(message.chat.id,'Это креветка! Многие виды креветок — гермафродиты, то есть за время своей жизни они иногда превращаются из самцов в самок.')
    else:
        bot.send_message(message.chat.id,'я не знаю что это за еда!')
    


bot.infinity_polling()