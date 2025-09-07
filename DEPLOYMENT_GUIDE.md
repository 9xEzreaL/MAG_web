# 購物網站部署指南

## 🚀 一鍵啟動

### 方法一：使用啟動腳本（推薦）
```bash
python start_server.py
```

### 方法二：手動啟動
```bash
# 1. 安裝依賴
pip install -r requirements.txt

# 2. 初始化資料庫
python init_database.py

# 3. 啟動應用程式
python app.py
```

## 📋 系統需求

- Python 3.7+
- MySQL 5.7+ 或 8.0+
- 至少 1GB RAM
- 至少 1GB 磁碟空間

## 🔧 環境配置

### 1. 資料庫配置
編輯 `config.py` 檔案：
```python
# MySQL配置
MYSQL_HOST = 'localhost'
MYSQL_PORT = 3306
MYSQL_USER = 'your_username'
MYSQL_PASSWORD = 'your_password'
MYSQL_DATABASE = 'shopping_db'
```

### 2. 創建資料庫
```sql
CREATE DATABASE shopping_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

### 3. 環境變數（可選）
```bash
export FLASK_ENV=production
export FLASK_DEBUG=False
```

## 🌐 訪問地址

- **前台網站**: http://your-domain:5000
- **管理員後台**: http://your-domain:5000/admin
- **預設管理員帳號**: admin / admin123

## 📁 專案結構

```
MAG_web/
├── app.py                 # 主應用程式
├── config.py              # 配置檔案
├── init_database.py       # 資料庫初始化
├── start_server.py        # 一鍵啟動腳本
├── requirements.txt       # Python依賴
├── templates/            # HTML模板
│   ├── admin_dashboard.html
│   ├── admin_login.html
│   ├── base.html
│   ├── cart.html
│   ├── checkout.html
│   ├── index.html
│   └── order_success.html
├── uploads/              # 上傳檔案
│   ├── categories/       # 分類圖片
│   ├── products/         # 商品圖片
│   └── IQOS_Logo.svg    # Logo
└── README.md
```

## 🔐 安全配置

### 1. 修改預設管理員密碼
登入管理員後台後，建議修改預設密碼。

### 2. 配置HTTPS（生產環境）
```bash
# 生成SSL證書
openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365 -nodes
```

### 3. 防火牆配置
```bash
# 開放5000端口
sudo ufw allow 5000
```

## 🐳 Docker部署（可選）

### Dockerfile
```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "start_server.py"]
```

### docker-compose.yml
```yaml
version: '3.8'
services:
  web:
    build: .
    ports:
      - "5000:5000"
    environment:
      - MYSQL_HOST=db
      - MYSQL_USER=root
      - MYSQL_PASSWORD=password
      - MYSQL_DATABASE=shopping_db
    depends_on:
      - db
  
  db:
    image: mysql:8.0
    environment:
      - MYSQL_ROOT_PASSWORD=password
      - MYSQL_DATABASE=shopping_db
    volumes:
      - mysql_data:/var/lib/mysql

volumes:
  mysql_data:
```

## 📊 功能特色

### 前台功能
- ✅ 商品瀏覽和分類
- ✅ 購物車功能
- ✅ 結帳流程
- ✅ 7-11門市選擇
- ✅ 訂單成功頁面
- ✅ 表單資料持久化

### 管理員功能
- ✅ 管理員登入
- ✅ 分類管理
- ✅ 商品管理
- ✅ 訂單管理
- ✅ 訂單狀態更新
- ✅ 訂單搜尋和篩選
- ✅ 統計資料

### 技術特色
- ✅ 響應式設計
- ✅ 7-11 API整合
- ✅ 資料庫優化
- ✅ 錯誤處理
- ✅ 安全性配置

## 🔧 故障排除

### 常見問題

1. **資料庫連接失敗**
   - 檢查MySQL服務是否運行
   - 確認資料庫配置正確
   - 檢查防火牆設置

2. **上傳檔案失敗**
   - 檢查uploads目錄權限
   - 確認磁碟空間充足

3. **7-11門市選擇失敗**
   - 檢查網路連接
   - 確認HTTPS配置（生產環境）

### 日誌查看
```bash
# 查看應用程式日誌
tail -f app.log

# 查看系統日誌
journalctl -u your-service-name
```

## 📞 支援

如有問題，請檢查：
1. 系統需求是否滿足
2. 依賴套件是否正確安裝
3. 資料庫配置是否正確
4. 網路連接是否正常

## 🎉 部署完成

部署完成後，你可以：
1. 訪問前台網站開始購物
2. 使用管理員帳號管理商品和訂單
3. 根據需要調整配置和功能
