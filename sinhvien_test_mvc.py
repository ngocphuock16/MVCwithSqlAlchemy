import db_exceptions
import sinhvien_db
import sinhvien_model, sinhvien_view, sinhvien_controller

def start():
    try:

        # Khởi tạo đối tượng model
        model = sinhvien_model.SinhvienModel("localhost", "root", "123456", "qlsinhvien")
        # Khởi tạo đối tượng view
        view = sinhvien_view.SinhvienView()
        # Khởi tạo controller
        controller = sinhvien_controller.SinhvienController(model, view)

        item = menu()
        while item in ["1", "2", "3", "4"]:

            if item == "1":
                controller.show_all_sinhvien()
            elif item == "2":
                hoten = input("Nhập họ tên: ")
                tuoi = int(input("Nhập tuổi: "))
                sdt = int(input("Nhập số điện thoại: "))
                address = input("Nhập địa chỉ: ")
                controller.them_sinhvien(hoten, tuoi, sdt, address)
            elif item == "3":
                idsv = int(input("Nhập id sinh viên: "))
                hoten = input("Nhập họ tên: ")
                tuoi = int(input("Nhập tuổi: "))
                sdt = int(input("Nhập số điện thoại: "))
                address = input("Nhập địa chỉ: ")
                controller.update_sinhvien(idsv, hoten, tuoi, sdt, address)
            elif item =="4":
                idsv = int(input("Nhập id sinh viên cần xóa: "))
                controller.xoa_sinhvien(idsv)
            item = menu()

    except db_exceptions.DatabaseConnection as err:
        print(err)


def menu():
    print("1: Hiển thị tất cả sinh viên")
    print("2: Thêm mới sinh viên")
    print("3. Cập nhật sinh viên")
    print("4. Xóa sinh viên")
    choice = input("Chọn thao tác từ 1 đến 4. Nhập số khác để thoát khỏi chương trình!")
    return choice


if __name__ == "__main__":
    start()
