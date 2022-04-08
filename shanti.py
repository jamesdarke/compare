@run_async
def stats(update, context):
    currentTime = get_readable_time((time.time() - botStartTime))
    current = now.strftime('%Y/%m/%d %I:%M:%S %p')
    total, used, free = shutil.disk_usage('.')
    total = get_readable_file_size(total)
    used = get_readable_file_size(used)
    free = get_readable_file_size(free)
    sent = get_readable_file_size(psutil.net_io_counters().bytes_sent)
    recv = get_readable_file_size(psutil.net_io_counters().bytes_recv)
    cpuUsage = psutil.cpu_percent(interval=0.5)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    stats = f'<b>🤖Bot Uptime:</b> {currentTime}\n' \
            f'<b>💪Start Time:</b> {current}\n' \
            f'<b>Total disk space:</b> {total}\n' \
            f'<b>📀Used:</b> {used}  ' \
            f'<b>💿Free:</b> {free}\n\n' \
            f'📊Data Usage📊\n<b>🔼Upload:</b> {sent}\n' \
            f'<b>🔽Download:</b> {recv}\n\n' \
            f'<b>🔳CPU:</b> {cpuUsage}% | ' \
            f'<b>🔲RAM:</b> {memory}% | ' \
            f'<b>🔵DISK:</b> {disk}%'
    update.effective_message.reply_photo(IMAGE_URL, stats, parse_mode=ParseMode.HTML)


@run_async
def start(update, context):
    start_string = f'''
This bot can mirror all your links to Google drive!
Type /{BotCommands.HelpCommand} to get a list of available commands
'''
    update.effective_message.reply_photo(IMAGE_URL, start_string, parse_mode=ParseMode.MARKDOWN)


@run_async
def chat_list(update, context):
    chatlist =''
    chatlist += '\n'.join(str(id) for id in AUTHORIZED_CHATS)
    sendMessage(f'<b>Authorized List:</b>\n{chatlist}\n', context.bot, update)


@run_async
def repo(update, context):
    button = [
    [InlineKeyboardButton("Repo", url=f"https://github.com/NamasteIndia/slam-mirror-bot")],
    [InlineKeyboardButton("Support Group", url=f"https://t.me/mirrorupdatesnnews")]]
    reply_markup = InlineKeyboardMarkup(button)
    update.effective_message.reply_photo(IMAGE_URL, reply_markup=reply_markup)
