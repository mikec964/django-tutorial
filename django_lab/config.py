import ruamel.yaml as yaml

class Config:
    with open("django_lab/keys.yaml", 'r') as config_f:
        keys = yaml.safe_load(config_f)
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = keys['EMAIL_USER']
    MAIL_PASSWORD = keys['EMAIL_PASS']
