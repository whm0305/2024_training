import os
import uvicorn
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy import create_engine, MetaData, Table, select
from sqlalchemy.orm import Session, sessionmaker
from starlette.responses import FileResponse
from sqlalchemy import create_engine

app = FastAPI()

# 表
TABLE_NAME = 'data_info_table'
# 数据库配置
DATABASE_URL = "mysql+pymysql://root:200133@localhost:3307/whm_database"

# 创建SQLAlchemy引擎
engine = create_engine(DATABASE_URL)
metadata = MetaData()

# 创建会话工厂
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 依赖项函数，用于提供数据库会话
def get_db():
    db = SessionLocal()
    try:
        yield db # 返回一个数据库会话实例
    finally:
        db.close()

# 表
table = Table(TABLE_NAME, metadata, autoload_with=engine)

# 根
@app.get("/")
def read_root():
    return {"message": "Welcome to my API!"}

# 输入http://127.0.0.1:8000/image/image_name（文件名查询）
@app.get("/image/{image_name}")
def query_data(image_name: str, db: Session = Depends(get_db)):
    # 查询数据库以获取相关记录
    # 统一路径格式
    image_path = f'image/{image_name}.jpg'
    # sql语句
    stmt = select([table]).where(table.c.image_path == image_path)
    # 从数据库获取
    db_result = db.execute(stmt).first()
    if not db_result:
            raise HTTPException(status_code=404, detail=f"Image {image_name} not found in the database")
    return db_result

# 输入http://127.0.0.1:8000/download/image_name（下载文件）
@app.get("/download/{image_name}")
def download_image(image_name: str, db: Session = Depends(get_db)):
    # 构造完整的图片路径
    image_search_path = f'single-vehicle-side-example\\image\\{image_name}.jpg'
    # 检查图片文件是否存在
    if not os.path.isfile(image_search_path):
        raise HTTPException(status_code=404, detail=f"Image {image_name} not found")
    # 使用FastAPI的FileResponse来提供文件下载
    return FileResponse(image_search_path, filename=image_name + '.jpg')

# 运行应用
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)