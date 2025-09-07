#!/usr/bin/env python3
"""
一鍵啟動腳本
用於在伺服器上快速啟動應用程式
"""
import os
import sys
import subprocess
import time
from pathlib import Path

def check_requirements():
    """檢查系統需求"""
    print("🔍 檢查系統需求...")
    
    # 檢查Python版本
    python_version = sys.version_info
    if python_version.major < 3 or (python_version.major == 3 and python_version.minor < 7):
        print("❌ 需要Python 3.7或更高版本")
        return False
    print(f"✅ Python版本: {python_version.major}.{python_version.minor}.{python_version.micro}")
    
    # 檢查必要檔案
    required_files = [
        'app.py',
        'config.py',
        'requirements.txt',
        'init_database.py'
    ]
    
    for file in required_files:
        if not os.path.exists(file):
            print(f"❌ 缺少必要檔案: {file}")
            return False
        print(f"✅ 檔案存在: {file}")
    
    return True

def install_dependencies():
    """安裝依賴套件"""
    print("\n📦 安裝依賴套件...")
    
    try:
        # 檢查是否有虛擬環境
        if hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix):
            print("✅ 檢測到虛擬環境")
        else:
            print("⚠️  建議使用虛擬環境")
        
        # 安裝requirements.txt中的套件
        result = subprocess.run([
            sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'
        ], capture_output=True, text=True)
        
        if result.returncode == 0:
            print("✅ 依賴套件安裝成功")
            return True
        else:
            print(f"❌ 依賴套件安裝失敗: {result.stderr}")
            return False
            
    except Exception as e:
        print(f"❌ 安裝依賴套件時發生錯誤: {e}")
        return False

def init_database():
    """初始化資料庫"""
    print("\n🗄️  初始化資料庫...")
    
    try:
        result = subprocess.run([
            sys.executable, 'init_database.py'
        ], capture_output=True, text=True)
        
        if result.returncode == 0:
            print("✅ 資料庫初始化成功")
            return True
        else:
            print(f"❌ 資料庫初始化失敗: {result.stderr}")
            return False
            
    except Exception as e:
        print(f"❌ 初始化資料庫時發生錯誤: {e}")
        return False

def create_upload_directories():
    """創建上傳目錄"""
    print("\n📁 創建上傳目錄...")
    
    upload_dirs = [
        'uploads',
        'uploads/categories',
        'uploads/products'
    ]
    
    for dir_path in upload_dirs:
        Path(dir_path).mkdir(parents=True, exist_ok=True)
        print(f"✅ 目錄已創建: {dir_path}")

def start_application():
    """啟動應用程式"""
    print("\n🚀 啟動應用程式...")
    
    try:
        # 檢查是否有SSL證書
        ssl_cert = 'cert.pem'
        ssl_key = 'key.pem'
        
        if os.path.exists(ssl_cert) and os.path.exists(ssl_key):
            print("✅ 檢測到SSL證書，使用HTTPS模式")
            ssl_context = (ssl_cert, ssl_key)
        else:
            print("⚠️  未檢測到SSL證書，使用HTTP模式")
            ssl_context = None
        
        # 啟動Flask應用程式
        print("🌐 應用程式啟動中...")
        print("📱 訪問地址:")
        print("   - 前台: http://localhost:5000")
        print("   - 管理員: http://localhost:5000/admin")
        print("   - 帳號: admin / admin123")
        print("\n按 Ctrl+C 停止應用程式")
        
        # 啟動應用程式
        from app import app
        app.run(
            host='0.0.0.0',
            port=5000,
            debug=False,
            ssl_context=ssl_context
        )
        
    except KeyboardInterrupt:
        print("\n\n👋 應用程式已停止")
    except Exception as e:
        print(f"❌ 啟動應用程式時發生錯誤: {e}")

def main():
    """主函數"""
    print("=" * 60)
    print("🚀 購物網站一鍵啟動工具")
    print("=" * 60)
    
    # 檢查系統需求
    if not check_requirements():
        print("\n❌ 系統需求檢查失敗")
        sys.exit(1)
    
    # 安裝依賴套件
    if not install_dependencies():
        print("\n❌ 依賴套件安裝失敗")
        sys.exit(1)
    
    # 創建上傳目錄
    create_upload_directories()
    
    # 初始化資料庫
    if not init_database():
        print("\n❌ 資料庫初始化失敗")
        sys.exit(1)
    
    # 啟動應用程式
    start_application()

if __name__ == "__main__":
    main()
