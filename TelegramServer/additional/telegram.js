const TelegramBot = require('node-telegram-bot-api');

const token = '6067752322:AAHu_wi5U227pk4s7K1FjJTZzA_7ZzTaoLA'
const bot = new TelegramBot(token, {polling: false});

function alert_user(chat_id){
    bot.sendMessage(chat_id, 'Ваш аккаунт одобрен администатором')
}

function training_is_ready(chat_id){
    bot.sendMessage(chat_id,"Ваша тренировка доступна")
}

module.exports={
    alert_user,training_is_ready
}
