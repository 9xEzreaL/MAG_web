import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'testing')
    # 使用 MySQL 資料庫
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'mysql+pymysql://root:@localhost:3306/shopping_db')
    # 預設設定：用戶名=root, 密碼=空, 主機=localhost, 端口=3306, 資料庫=shopping_db
    # 如果需要修改，請設定環境變數 DATABASE_URL
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # JWT 配置
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'jwt-secret-string')
    JWT_ACCESS_TOKEN_EXPIRES = 86400  # 24 hours in seconds
    JWT_TOKEN_LOCATION = ['headers']
    JWT_HEADER_NAME = 'Authorization'
    JWT_HEADER_TYPE = 'Bearer'
