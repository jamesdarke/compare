def start(update, context):
    start_string = f'''
This bot can mirror all your links to Google drive!
Type /{BotCommands.HelpCommand} to get a list of available commands
'''
    update.effective_message.reply_photo(IMAGE_URL, start_string, parse_mode=ParseMode.MARKDOWN)


def chat_list(update, context):
    chatlist =''
    chatlist += '\n'.join(str(id) for id in AUTHORIZED_CHATS)
    sendMessage(f'<b>Authorized List:</b>\n{chatlist}\n', context.bot, update)


def repo(update, context):
    button = [
    [InlineKeyboardButton("Repo", url=f"https://github.com/NamasteIndia/slam-mirror-bot")],
    [InlineKeyboardButton("Support Group", url=f"https://t.me/mirrorupdatesnnews")]]
    reply_markup = InlineKeyboardMarkup(button)
    update.effective_message.reply_photo(IMAGE_URL, reply_markup=reply_markup)
