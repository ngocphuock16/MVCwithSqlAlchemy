import db_exceptions
import sinhvien_db


class SinhvienModel(object):
    # Phương thức khởi tạo
    def __init__(self, database_server, username, password, database):
        self.connection, self.metadata, self.engine = sinhvien_db.ket_noi_den_csdl(database_server,
                                                                                   username,
                                                                                   password,
                                                                                   database)

    # Phương thức lấy dữ liệu
    def get_all_sinhvien(self):
        results = sinhvien_db.lay_tat_ca_du_lieu_bang_sinhvien(self.connection,
                                                               self.metadata,
                                                               self.engine)
        return results

    # Phương thức insert
    def them_sinhvien(self, Hoten, Age, SDT, Address):
        resultID = sinhvien_db.them_sinhvien(self.connection,
                                             self.metadata,
                                             self.engine,
                                             Hoten, Age, SDT, Address)
        return resultID

    # Phương thức update
    def update_sinhvien(self, IdSV, Hoten, Age, SDT, Address):
        resultID = sinhvien_db.update_sinhvien(self.connection,
                                               self.metadata,
                                               self.engine,
                                               IdSV, Hoten, Age, SDT, Address)

    # Phương thức delete
    def xoa_sinhvien(self, IdSV):
        resultID = sinhvien_db.xoa_sinhvien(self.connection,
                                            self.metadata,
                                            self.engine, IdSV)
        return resultID
