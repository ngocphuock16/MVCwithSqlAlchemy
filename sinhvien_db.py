import db_exceptions
import sqlalchemy as db


#Xây dựng hàm thiết lập kết nối đến csdl
#Trả về đối tượng là connection, metadata và engine
def ket_noi_den_csdl(database_server, username, password, database):
    connection_str = "mysql://{}:{}@{}/{}".format(username, password, database_server, database)
    engine = db.create_engine(connection_str)
    connection = engine.connect()
    metadata = db.MetaData()
    return connection, metadata, engine

#Xây dựng hàm lấy tất cả dữ liệu của bảng sinhvien
def lay_tat_ca_du_lieu_bang_sinhvien(connection, metadata, engine):
    try:
        # Lấy đối tượng  từ bảng sinhvien trong csdl
        sinhvien = db.Table('sinhvien', metadata, autoload=True, autoload_with=engine)

        # Lấy tất cả dữ liệu của bảng sinhvien - tương đương câu lênh SELECT * FROM sinhvien
        query = db.select([sinhvien])

        ResultProxy = connection.execute(query)
        ResultSet = ResultProxy.fetchall()

        return ResultSet

    except:
        raise db_exceptions.SelectError("Xảy ra lỗi trong quá trình thực hiện lấy dữ liệu!")




#Hàm insert - tra ve id vua duoc tao
def them_sinhvien(connection, metadata, engine,
                Hoten, Age, SDT, Address):
    try:
        # Lấy đối tượng person từ bảng sinhvien trong csdl
        sinhvien = db.Table('sinhvien', metadata, autoload=True, autoload_with=engine)
        # Chèn 1 dòng vào bảng person
        query = db.insert(sinhvien).values(Hoten=Hoten, Age=Age, SDT=SDT, Address=Address)
        ResultProxy = connection.execute(query)
        # Trả về giá trị id vừa được sinh
        return ResultProxy.inserted_primary_key
    except:
        raise db_exceptions.InsertError("Xảy ra lỗi trong quá trình thêm mới dữ liệu!")


#Hàm update
def update_sinhvien(connection, metadata, engine,
                IdSV, Hoten, Age, SDT, Address):
    try:
    # Lấy đối tượng person từ bảng sinhvien trong csdl
        sinhvien = db.Table('sinhvien', metadata, autoload=True, autoload_with=engine)
        query_update = db.update(sinhvien).values(Hoten=Hoten, Age=Age, SDT=SDT, Address=Address).where(sinhvien.columns.IdSV == IdSV)
        ResultProxy = connection.execute(query_update)
        return ResultProxy
    except:
        raise db_exceptions.UpdateError("Xảy ra lỗi trong quá trình cập nhật dữ liệu!")

#Hàm delete
def xoa_sinhvien(connection,metadata, engine,IdSV):
  try:
    sinhvien = db.Table('sinhvien', metadata, autoload=True, autoload_with=engine)
    query_delete = db.delete(sinhvien).where(sinhvien.columns.IdSV == IdSV)
    ResultProxy = connection.execute(query_delete)
    return ResultProxy
  except:
      raise db_exceptions.DeleteError("Xảy ra lỗi trong quá trình thực hiện xóa dữ liệu!")