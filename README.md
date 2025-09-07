# 購物網站

一個功能完整的購物網站，包含前台購物和後台管理功能。

## 🚀 快速開始

### 一鍵啟動
```bash
python start_server.py
```

### 手動啟動
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

## 🌐 訪問地址

- **前台網站**: http://localhost:5000
- **管理員後台**: http://localhost:5000/admin
- **預設管理員帳號**: admin / admin123

## ✨ 主要功能

### 前台功能
- 🛍️ 商品瀏覽和分類
- 🛒 購物車功能
- 💳 結帳流程
- 🏪 7-11門市選擇
- 📋 訂單成功頁面
- 💾 表單資料持久化

### 管理員功能
- 👤 管理員登入
- 📂 分類管理
- 📦 商品管理
- 📋 訂單管理
- 🔄 訂單狀態更新
- 🔍 訂單搜尋和篩選
- 📊 統計資料

## 🏗️ 技術架構

- **後端**: Python Flask
- **資料庫**: MySQL
- **前端**: HTML, CSS, JavaScript
- **ORM**: SQLAlchemy
- **認證**: JWT
- **檔案上傳**: Werkzeug

## 📁 專案結構

```
MAG_web/
├── app.py                 # 主應用程式
├── config.py              # 配置檔案
├── init_database.py       # 資料庫初始化
├── start_server.py        # 一鍵啟動腳本
├── requirements.txt       # Python依賴
├── templates/            # HTML模板
├── uploads/              # 上傳檔案
└── README.md
```

## 🔧 配置

### 資料庫配置
編輯 `config.py` 檔案：
```python
MYSQL_HOST = 'localhost'
MYSQL_PORT = 3306
MYSQL_USER = 'your_username'
MYSQL_PASSWORD = 'your_password'
MYSQL_DATABASE = 'shopping_db'
```

### 創建資料庫
```sql
CREATE DATABASE shopping_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

## 🚀 部署

詳細的部署指南請參考 [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md)

### 快速部署
1. 上傳專案檔案到伺服器
2. 配置資料庫連接
3. 運行 `python start_server.py`
4. 訪問網站開始使用

## 🔐 安全功能

- JWT認證
- 密碼加密
- SQL注入防護
- XSS防護
- 檔案上傳安全

## 📱 響應式設計

- 支援桌面和行動裝置
- 現代化UI設計
- 流暢的用戶體驗

## 🏪 7-11整合

- 門市選擇API整合
- 同分頁跳轉體驗
- 門市資訊記錄
- 訂單狀態追蹤

## 📊 管理功能

- 商品庫存管理
- 訂單狀態管理
- 客戶資料管理
- 統計報表
- 搜尋和篩選

## 🛠️ 開發

### 本地開發
```bash
# 克隆專案
git clone <repository-url>
cd MAG_web

# 創建虛擬環境
python -m venv venv
source venv/bin/activate  # Linux/Mac
# 或
venv\Scripts\activate     # Windows

# 安裝依賴
pip install -r requirements.txt

# 初始化資料庫
python init_database.py

# 啟動開發伺服器
python app.py
```

### 環境變數
```bash
export FLASK_ENV=development
export FLASK_DEBUG=True
```

## 📝 更新日誌

### v1.0.0
- ✅ 基本購物功能
- ✅ 管理員後台
- ✅ 7-11門市選擇
- ✅ 訂單管理
- ✅ 響應式設計

## 🤝 貢獻

歡迎提交Issue和Pull Request！

## 📄 授權

MIT License

## 📞 支援

如有問題，請檢查：
1. 系統需求是否滿足
2. 依賴套件是否正確安裝
3. 資料庫配置是否正確
4. 網路連接是否正常

---

**享受購物！** 🛍️