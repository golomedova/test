import config
import telebot
import words_bot

games = {}

bot = telebot.TeleBot(config.token)

class Game:
    def __init__(self):
        self.char = ''
        self.used_words = []
        self.computer_words = {}
        self.turn = 'player'

    def player_turn(self):
        self.turn = 'bot'
        return self(words_bot.player_word)

    def bot_turn(self):
        return words_bot.get_last_chr(words_bot.bot_choice)

    def next_word(self):
        return words_bot.new_player_word



@bot.message_handler(command=['start'])
def start_game(message):
    game = Game()
    game[message.chat.id] = game

new_word = ''

@bot.message_handler(func=lambda message: True, content_types=['text'])
def get_message(message):
    global new_word
    game = Game()
    Game[message.chat.id] = game
    new_word = game.next_word(message.text)
    bot.send_message(message.chat.id)

if __name__ == '__main__':
    bot.polling(none_stop=True)