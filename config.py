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
