#!/usr/bin/env python3
"""
資料庫初始化腳本
用於在伺服器上初始化完整的資料庫結構和初始資料
"""
import os
import sys
from datetime import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash

# 添加當前目錄到Python路徑
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app import app, db, Admin, Category, Item, Customer, Order, OrderItem

def init_database():
    """初始化資料庫"""
    print("🚀 開始初始化資料庫...")
    
    with app.app_context():
        try:
            # 1. 刪除所有現有表格
            print("🗑️  清理現有資料庫...")
            db.drop_all()
            
            # 2. 創建所有表格
            print("📋 創建資料庫表格...")
            db.create_all()
            
            # 3. 創建管理員帳號
            print("👤 創建管理員帳號...")
            admin = Admin(
                username='admin',
                password_hash=generate_password_hash('admin123'),
                email='admin@example.com',
                created_at=datetime.utcnow()
            )
            db.session.add(admin)
            
            # 4. 創建初始分類
            print("📂 創建初始分類...")
            #categories_data = [
            #    {
            #        'name': 'IQOS',
            #        'description': 'IQOS電子煙產品',
            #        'image_url': '/uploads/IQOS_Logo.svg'
            #    },
            #    {
            #        'name': '加熱菸草',
            #        'description': '加熱菸草相關產品',
            #        'image_url': '/uploads/placeholder.jpg'
            #    },
            #    {
            #        'name': '配件',
            #        'description': 'IQOS配件和周邊商品',
            #        'image_url': '/uploads/placeholder.jpg'
            #    }
            #]
            
            #categories = []
            #for cat_data in categories_data:
            #    category = Category(
            #        name=cat_data['name'],
            #        description=cat_data['description'],
            #        image_url=cat_data['image_url'],
            #        is_active=True,
            #        created_at=datetime.utcnow()
            #    )
            #    db.session.add(category)
            #    categories.append(category)
            
            # 5. 創建初始商品
            print("📦 創建初始商品...")
            # items_data = [
            #    {
            #        'name': 'IQOS 3 DUO',
            #        'description': 'IQOS 3 DUO 電子煙主機',
            #        'price': 2990.0,
            #        'quantity_left': 50,
            #        'image_url': '/uploads/placeholder.jpg',
            #        'category': categories[0]  # IQOS分類
            #    },
            #    {
            #        'name': 'IQOS 3 MULTI',
            #        'description': 'IQOS 3 MULTI 電子煙主機',
            #        'price': 2490.0,
            #        'quantity_left': 30,
            #        'image_url': '/uploads/placeholder.jpg',
            #        'category': categories[0]  # IQOS分類
            #    },
            #    {
            #        'name': 'HEETS 黃色',
            #        'description': 'HEETS 黃色口味加熱菸草',
            #        'price': 200.0,
            #        'quantity_left': 100,
            #        'image_url': '/uploads/placeholder.jpg',
            #        'category': categories[1]  # 加熱菸草分類
            #    },
            #    {
            #        'name': 'HEETS 藍色',
            #        'description': 'HEETS 藍色口味加熱菸草',
            #        'price': 200.0,
            #        'quantity_left': 80,
            #        'image_url': '/uploads/placeholder.jpg',
            #        'category': categories[1]  # 加熱菸草分類
            #    },
            #    {
            #        'name': 'IQOS 充電器',
            #        'description': 'IQOS 專用充電器',
            #        'price': 500.0,
            #        'quantity_left': 25,
            #        'image_url': '/uploads/placeholder.jpg',
            #        'category': categories[2]  # 配件分類
            #    },
            #    {
            #        'name': 'IQOS 清潔套組',
            #        'description': 'IQOS 清潔保養套組',
            #        'price': 300.0,
            #        'quantity_left': 40,
            #        'image_url': '/uploads/placeholder.jpg',
            #        'category': categories[2]  # 配件分類
            #    }
            #]
            
            #for item_data in items_data:
            #    item = Item(
            #        name=item_data['name'],
            #        description=item_data['description'],
            #        price=item_data['price'],
            #        quantity_left=item_data['quantity_left'],
            #        image_url=item_data['image_url'],
            #        category_id=item_data['category'].id,
            #        is_active=True,
            #        created_at=datetime.utcnow()
            #    )
            #    db.session.add(item)
            
            # 6. 提交所有變更
            print("💾 提交資料庫變更...")
            db.session.commit()
            
            print("✅ 資料庫初始化完成！")
            print("\n📊 初始化結果:")
            print(f"  - 管理員帳號: admin / admin123")
            #print(f"  - 分類數量: {len(categories)}")
            #print(f"  - 商品數量: {len(items_data)}")
            print(f"  - 資料庫表格: {len(db.metadata.tables)}")
            
        except Exception as e:
            print(f"❌ 資料庫初始化失敗: {e}")
            db.session.rollback()
            raise

def verify_database():
    """驗證資料庫初始化結果"""
    print("\n🔍 驗證資料庫初始化結果...")
    
    with app.app_context():
        try:
            # 檢查管理員
            admin_count = Admin.query.count()
            print(f"  ✅ 管理員數量: {admin_count}")
            
            # 檢查分類
            category_count = Category.query.count()
            print(f"  ✅ 分類數量: {category_count}")
            
            # 檢查商品
            item_count = Item.query.count()
            print(f"  ✅ 商品數量: {item_count}")
            
            # 檢查客戶
            customer_count = Customer.query.count()
            print(f"  ✅ 客戶數量: {customer_count}")
            
            # 檢查訂單
            order_count = Order.query.count()
            print(f"  ✅ 訂單數量: {order_count}")
            
            print("✅ 資料庫驗證完成！")
            
        except Exception as e:
            print(f"❌ 資料庫驗證失敗: {e}")

if __name__ == "__main__":
    print("=" * 60)
    print("🗄️  資料庫初始化工具")
    print("=" * 60)
    
    try:
        init_database()
        verify_database()
        
        print("\n" + "=" * 60)
        print("🎉 資料庫初始化成功完成！")
        print("=" * 60)
        print("\n💡 下一步:")
        print("1. 運行應用程式: python app.py")
        print("2. 訪問管理員頁面: http://localhost:5000/admin")
        print("3. 使用帳號: admin / admin123")
        print("4. 開始管理商品和訂單")
        
    except Exception as e:
        print(f"\n❌ 初始化失敗: {e}")
        sys.exit(1)
