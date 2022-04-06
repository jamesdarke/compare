        sendMarkup(start_string, context.bot, update, reply_markup)
    else:
        sendMarkup(
            'Oops! not a Authorized user.\nPlease join our Channel.\nOr Host Your Own Bot Using My Repo).',
            context.bot,
            update,
            reply_markup,
        )
