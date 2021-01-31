import db_exceptions
import sinhvien_db

class SinhvienView(object):

    #Hàm hiển thị tất cả dữ liệu về sinhvien
    def display_all_sinhvien(self, items):
        print("Dữ liệu về các sinh viên thu được như sau:")
        for item in items:
            print("Id: {}, Họ tên: {}, Tuổi: {}, SDT:{}, Address:{}".format(item.IdSV, item.Hoten, item.Age,
                                                                           item.SDT,item.Address))
        print("----------------------------Kết thúc hiển thị dữ liệu!-------------------------------")
    # Hàm thông báo kết quả insert
    def ket_qua_insert(self, resultID):
        id = resultID[0]
        if id > 0:
            print("-------------------------Insert thành công!-----------------------")
        else:
            print("Fail")

    def ket_qua_update(self):
        print("-----------------------------Cập nhật thành công!-------------------------")

    def ket_qua_delete(self):
        print("-----------------------------Xóa thành công!-------------------------------")

    def thong_bao_loi(self, err_msg):
        print('-' * 50)
        print(err_msg)
        print('-' * 50)