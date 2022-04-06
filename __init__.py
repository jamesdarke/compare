@run_async
def start(update, context):
    start_string = f'''
This bot can mirror all your links to Google drive!
Type /{BotCommands.HelpCommand} to get a list of available commands
'''
    update.effective_message.reply_photo(IMAGE_URL, start_string, parse_mode=ParseMode.MARKDOWN)
