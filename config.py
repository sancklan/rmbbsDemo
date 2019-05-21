import os

DB_USERNAME = 'root'
DB_PASSWORD = 'root'
DB_HOST = '127.0.0.1'
DB_PORT = '3306'
DB_NAME = 'rmbbsDemo'

DB_URI = 'mysql+pymysql://%s:%s@%s:%s/%s?charset=utf8' % (DB_USERNAME, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME)

SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = os.urandom(24)

# ID字段
CMS_USER_ID = 'cms_user_id'
FRONT_USER_ID = 'front_user_id'

MAIL_SERVER  = 'smtp.163.com'
MAIL_PORT = '994'

# MAIL_USE_TLS = True
MAIL_USE_SSL = True
MAIL_USERNAME = 'sancklan@163.com'
MAIL_PASSWORD = 'sancklan520'
MAIL_DEFAULT_SENDER = 'sancklan@163.com'

# 阿里大于短信验证码相关配置
ALIDAYU_APP_KEY = 'LTAIAVKroPsDA65O'
ALIDAYU_APP_SECRET = 'k6YD8zQmnRwJ6EMoifzReOTDKbz5xA'
ALIDAYU_SIGN_NAME = '皇家马德里球迷论坛'
ALIDAYU_TEMPLATE_CODE = 'SMS_160571783'

# 七牛上传
UEDITOR_UPLOAD_TO_QINIU = True
UEDITOR_QINIU_ACCESS_KEY = "rw9PsY0AB0TbdTpWV6YN03ovz50xLruaR6VPSJiC"
UEDITOR_QINIU_SECRET_KEY = "5b4jiUdDR7IVwjYisNcnsJA9324WA4dkv9kFuUxR"
UEDITOR_QINIU_BUCKET_NAME = "rma_qny"
UEDITOR_QINIU_DOMAIN = "https://poyp9yrz8.bkt.clouddn.com/"

# 帖子分页相关配置

PER_PAGE = 10

# celery配置
CELERY_RESULT_BACKEND = "redis://127.0.0.1:6379/0"
CELERY_BROKER_URL = "redis://127.0.0.1:6379/0"