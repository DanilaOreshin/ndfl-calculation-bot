from decouple import Config, RepositoryEnv

config = Config(RepositoryEnv("resources/config.env"))

BOT_AUTHOR = config('BOT_AUTHOR')
BOT_VERSION = config('BOT_VERSION')
BOT_TOKEN = config('BOT_TOKEN')
