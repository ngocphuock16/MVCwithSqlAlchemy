import db_exceptions
import sinhvien_db

class SinhvienController(object):
    #Phương thức khởi tạo
    def __init__(self, model, view):
        self.model = model
        self.view = view

    #Phương thức hiển thị tất cả dữ liệu của bảng sinhvien
    def show_all_sinhvien(self):
        try:
            items = self.model.get_all_sinhvien()
            self.view.display_all_sinhvien(items)
        except db_exceptions.SelectError as err_msg:
            self.view.thong_bao_loi(err_msg)


    #Phương thức insert
    def them_sinhvien(self, Hoten, Age, SDT, Address):
        try:
            resultID = self.model.them_sinhvien(Hoten, Age, SDT, Address)
            self.view.ket_qua_insert(resultID)
        except db_exceptions.InsertError as err_msg:
            self.view.thong_bao_loi(err_msg)
    #Phương thức update
    def update_sinhvien(self, IdSV, Hoten, Age, SDT, Address):
        try:
            self.model.update_sinhvien(IdSV, Hoten, Age, SDT, Address)
            self.view.ket_qua_update()
        except db_exceptions.UpdateError as err:
            self.view.thong_bao_loi(err)

    #Phương thức delete
    def xoa_sinhvien(self, IdSV):
        try:
            self.model.xoa_sinhvien(IdSV)
            self.view.ket_qua_delete()
        except db_exceptions.DeleteError as err:
            self.view.thong_bao_loi(err)