import telebot
import sqlite3

bot = telebot.TeleBot("8097771017:AAF3VW7FXxCFhK1AtvQsVlbYK_LCECV0sIQ")

main_menu = telebot.types.ReplyKeyboardMarkup(resize_keyboard = True)
main_menu.row("Expenses", "History")
main_menu.row("Settings")

add_e = telebot.types.ReplyKeyboardMarkup(resize_keyboard = True)
add_e.row("Add expenses", "Back")


def send(m, text):
    bot.send_message(m, text)
    
@bot.message_handler(commands = ["start"])
def start_message(m):
    sq_create = f"""
         CREATE TABLE IF NOT EXISTS '{m.from_user.id}' (
             id INTEGER PRIMARY KEY AUTOINCREMENT,
             title TEXT,
             content TEXT
         )
         """
    db = sqlite3.connect("base.db") 
    sql = db.cursor()
    sql.execute(sq_create) 
    db.commit()    
    bot.reply_to(m, "Blinq / Analysis", reply_markup = main_menu)

@bot.message_handler(content_types = ['text'])
def send_message(m):
    text = m.text.lower()
    mid = m.chat.id
    if text == "expenses":
        bot.send_message(mid, "Your Expenses", reply_markup = add_e)
        
    elif text == "back":
        bot.send_message(mid, "Main", reply_markup = main_menu)
    
    elif text == "Add expenses":
        send(mid, "Your expense name:")
        bot.register_text_step_handler(m, exp_name)
        
              
        
bot.infinity_polling()