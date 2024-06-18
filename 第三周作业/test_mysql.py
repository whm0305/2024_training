#import sqlalchemy
from sqlalchemy import Column,Integer,String,create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
#create_engine 用于创建与mysql数据库的连接引擎
#declarative_base 用于创建一个基类
#session 用于创建会话类，与数据库进行交互


# 创建一个基类
Base = declarative_base()
# 定义学生的ORM模型类
class Student(Base):
    __tablename__ = 'students'

    # 定义属性，对应表中的列
    id = Column(Integer,primary_key=True)
    name = Column(String(50),nullable=False)
    phonenumber = Column(Integer,nullable=False)

    # 定义一个方法打印一个Student的实例
    def __repr__(self):
        return f"<Student(id={self.id},name='{self.name}',phonenumber='{self.phonenumber}')>"

# 连接mysql
# 创建引擎（PyMySQL作为驱动程序）
engine = create_engine('mysql+pymysql://root:200133@localhost/whm_database')

# 创建表
Base.metadata.create_all(engine)

# 创建session类
Session = sessionmaker(bind = engine)
session = Session()

# CRUD
# 增
student1 = Student(name='Wang',phonenumber='123')
student2 = Student(name='Fang',phonenumber='456')
student3 = Student(name='Hu',phonenumber='456')
session.add(student1)
session.add(student2)
session.add(student3)
session.commit()

# 删 (query构建查询进行其他操作
student4 = session.query(Student).filter_by(name='Hu').first()
if student4:
    session.delete(student4)
    session.commit()

# 查所有用户
print("---All Students---")
all_Students = session.query(Student).all()
for student in all_Students:
    print(student) # 调用Student类的__repr__方法

# 查询特定用户
print("---Find the specified student---")
student = session.query(Student).filter_by(name='Wang').first()
print(student)

# 更新用户信息
student = session.query(Student).filter_by(name='Wang').first()
if student:
    student.phonenumber = '123123123'
    session.commit()

session.close()