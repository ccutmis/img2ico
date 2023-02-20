from PySide6.QtWidgets import QApplication,QMessageBox
from PySide6.QtGui import QKeySequence,QIcon
from PySide6.QtCore import QSize
from customLib.CustomMain import CustomUi
from customLib.TableWidget import TableWidget
from PySide6.QtCore import Qt,QCoreApplication
import os

from PIL import Image

class Ui2(CustomUi):
    def set_folder_path(self):
        tmp = self.select_dir()
        self.main.label_folder.setText(tmp)
    def set_file_path(self):
        tmp = self.select_file()
        self.main.label_file.setText(tmp[0])
    def on_btn_go_clicked(self):
        img_dir = self.main.label_folder.text()
        img_ls = self.get_img_list(img_dir)
        if img_ls != []:
            for i in img_ls:
                self.img2ico(img_dir,i)
            self.show_dialog('轉檔完成', '轉檔完成，可以在 '+img_dir + ' 資料夾裡面找到同名的 ico 圖檔!')
        else:
            self.show_dialog('找不到圖檔', img_dir + ' 資料夾裡面找不到圖檔! 請確認後再重試一次...')

    def img2ico(self,img_dir,img_name):
        logo = Image.open(img_dir+'/'+img_name)
        logo.save(img_dir+'/'+img_name[:-4]+'.ico',format='ICO')

    #創建目錄，如果目錄不存在
    def mkdir_if_not_exists(self,out_dir)->bool:
        try:
            if not os.path.exists(out_dir):
                os.makedirs(out_dir)
            else:
                pass
            return True
        except:
            return False

    #刪除目錄，包含目錄裡面的所有檔案
    def delete_folder(self,dir_path)->bool:
        try:
            shutil.rmtree(dir_path, ignore_errors=True)
            self.log(f"\tDeleted '{dir_path}' directory successfully")
            return True
        except:
            return False

    #取得目錄裡面的所有圖像列表，傳回值為list
    def get_img_list(self,source_dir,img_type=['jpg','png'])->list:
        try:
            if os.path.exists(source_dir):
                img_type_str_lower=""
                for i in img_type:
                    img_type_str_lower+=(i).lower()
                myimages = []
                dirFiles = os.listdir(source_dir)
                dirFiles.sort()
                sorted(dirFiles)
                for files in dirFiles:
                    if (files.split('.')[-1].lower() in img_type_str_lower) and '.db' not in files:
                        myimages.append(files)
            else:
                print(f"\t{source_dir} directory not found!")
            return myimages
        except:
            return []

def main():
    import sys
    QCoreApplication.setAttribute(Qt.AA_ShareOpenGLContexts)
    app = QApplication(sys.argv)
    with open("resource/styles.qss") as f: 
        app.setStyleSheet(f.read())
    w = Ui2("resource/main.ui","Img2Ico GENERATOR")
    w.main.setFixedSize(QSize(590,160))
    w.main.setWindowIcon(QIcon("resource/images/idea.ico"))
    w.main.btn_sel_folder.clicked.connect(lambda:w.set_folder_path())
    w.main.btn_go.clicked.connect(lambda:w.on_btn_go_clicked())

    app.exec()

if __name__ == "__main__" : main()