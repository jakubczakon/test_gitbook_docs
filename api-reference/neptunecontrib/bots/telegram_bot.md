Module neptunecontrib.bots.telegram_bot
=======================================
Spins of a Neptune bot with which you can interact on telegram

You can see which experiments are running, check the best experiements based
on defined metric and even plot it in Telegram.

Full list of options:
 * /project list NAMESPACE
 * /project select NAMESPACE/PROJECT_NAME
 * /project help
 * /experiments last NUMBER_OF_EXPERIMENTS
 * /experiments best METRIC_NAME NUMBER_OF_EXPERIMENTS
 * /experiments state STATE NUMBER_OF_EXPERIMENTS
 * /experiments help
 * /experiment link SHORT_ID
 * /experiment plot SHORT_ID METRIC_NAME OTHER_METRIC_NAME
 * /experiment help

Attributes:
    telegram_api_token(str): Your telegram bot api token.
        You can pass it either as --telegram_api_token or -t.
    neptune_api_token(str): Your neptune api token. If you
        set the NEPTUNE_API_TOKEN environemnt variable, you
        don't have to pass it here.
        You can pass it either as --neptune_api_token or -n.
        Default None.

Example:
    Spin off your bot::

        $ python neptunecontrib.bots.telegram
            --telegram_api_token 'a1249auscvas0vbia0fias0'
            --neptune_api_token 'asdjpsvdsg987das0f9sad0fjasdf='

    Go to your telegram and type.

    `/project list neptune-ai`

    Use help to see what is implemented.

     * '/project help'
     * '/experiments help'
     * '/experiemnt help'

Functions
---------

    
`parse_args()`
:   

Classes
-------

`TelegramBot(telegram_api_token, neptune_api_token)`
:   

    ### Methods

    `experiment(self, bot, update, args)`
    :

    `experiments(self, bot, update, args)`
    :

    `project(self, bot, update, args)`
    :

    `run(self)`
    :

    `unknown(self, bot, update)`
    :