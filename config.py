##OPEN API STUFF
OPENAI_API_KEY = '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'



## FLASK STUFF
class Config(object):
    DEBUG = True
    TESTING = False

class DevelopmentConfig(Config):
    SECRET_KEY = "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"


config = {
    'development': DevelopmentConfig,
    'testing': DevelopmentConfig,
    'production': DevelopmentConfig
}
