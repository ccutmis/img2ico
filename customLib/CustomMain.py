from PySide6.QtWidgets import *
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QIODevice,Qt
import sys, os, re, codecs

class CustomUi(QMainWindow):
    def __init__(self,ui_path,window_title='title name'):
        super(CustomUi,self).__init__()
        self.setting_file_path = "resource/setting.txt"
        self.setting = {}
        self.read_setting()
        ui_file = QFile(ui_path)
        if not ui_file.open(QIODevice.ReadOnly):
            print(f"Cannot open {ui_path}: {ui_file.errorString()}")
            sys.exit(-1)
        loader = QUiLoader()
        self.main = loader.load(ui_file)
        ui_file.close()
        if not self.main:
            print(loader.errorString())
            sys.exit(-1)
        self.main.setWindowTitle(window_title)
        self.main.show()

    def open_file(self):
        path = QFileDialog.getOpenFileName(self, "Open")[0]
        if path:
            if self.detect_by_bom(path) == 'utf-8':
                with open(path, 'r', encoding='utf-8') as f:
                    tmp = f.read()
            else: #utf-16
                with open(path,'rb') as f:
                    tmp = f.read()
                tmp = str(tmp, 'utf-16')
            self.file_path = path
            print(tmp)
            return ( tmp )
        else:
            return None

    def close_app(self): sys.exit()

    def detect_by_bom(self,path, default='utf-8'):
        with open(path, 'rb') as f:
            raw = f.read(4)  # will read less if the file is smaller
        for enc, boms in \
                ('utf-8-sig', (codecs.BOM_UTF8,)),\
                ('utf-16', (codecs.BOM_UTF16_LE, codecs.BOM_UTF16_BE)),\
                ('utf-32', (codecs.BOM_UTF32_LE, codecs.BOM_UTF32_BE)):
            if any(raw.startswith(bom) for bom in boms):
                return enc
        return default 

    def read_setting(self):
        app_current_path = os.getcwd()+'\\'
        if os.path.exists(self.setting_file_path)==False: # 找不到設定檔
            # 用 resource\\setting_template 重建
            with open(app_current_path+'resource/setting_template','r',encoding='utf-8') as f:
                template_txt = f.read()
            value_ls=re.findall(r"^([^\t]+)\t([^\n]*)",template_txt,re.M)
            out_txt=""
            for i in value_ls:
                if i[0].find('DIR')!=-1:
                    self.setting[i[0].strip()]=app_current_path+i[1].strip()
                    out_txt += i[0].strip()+"\t"+app_current_path+i[1].strip()+"\n"
                else:
                    self.setting[i[0].strip()]=i[1].strip()
                    out_txt += i[0].strip()+"\t"+i[1].strip()+"\n"
            with open(self.setting_file_path,'w+',encoding='utf-8') as f:
                f.write(out_txt)
        else:
            if self.detect_by_bom(self.setting_file_path) == 'utf-8':
                with open(self.setting_file_path, 'r', encoding='utf-8') as f:
                    tmp = f.read()
            else: #utf-16
                with open(self.setting_file_path,'rb') as f:
                    tmp = f.read()
                tmp = str(tmp, 'utf-16')
            value_ls=re.findall(r"^([^\t]+)\t([^\n]*)",tmp,re.M)
            for i in value_ls:
                self.setting[i[0].strip()]=i[1].strip()
    # Reference => https://doc.qt.io/qt-6/qfiledialog.html#static-public-members
    def select_dir(self):
        selected_folder = QFileDialog.getExistingDirectory(None,"Select Directory...")
        #print(selected_folder)
        return selected_folder

    def select_file(self):
        selected_file = QFileDialog.getOpenFileName(None,"Select File...")
        #print(selected_folder)
        return selected_file

    def show_dialog(self,dialog_title,dialog_body,iconType='Information',buttonType=QMessageBox.StandardButton.Ok):
        dialog = QMessageBox(parent=self, text=dialog_body)
        dialog.setWindowTitle(dialog_title)
        if iconType == 'Question':
            dialog.setIcon(QMessageBox.Icon.Question)
        elif iconType == 'Information':
            dialog.setIcon(QMessageBox.Icon.Information)
        elif iconType == 'Warning':
            dialog.setIcon(QMessageBox.Icon.Warning)
        elif iconType == 'Critical':
            dialog.setIcon(QMessageBox.Icon.Critical)
        # more StandardButton options --> https://coderslegacy.com/python/pyqt6-qmessagebox/
        dialog.setStandardButtons(buttonType)
        dialog.exec()

    # 開啟新QWidget 以匯入ui處理版面問題
    def open_error_msg_win(self,error_title,error_msg): # 槽的連結寫在 ui 裡
        self.error_msg_win = QWidget(self)
        ui_path = "resource/error_msg_win.ui"
        ui_file = QFile(ui_path)
        if not ui_file.open(QIODevice.ReadOnly):
            print(f"Cannot open {ui_path}: {ui_file.errorString()}")
            sys.exit(-1)
        loader = QUiLoader()
        self.error_msg_win = loader.load(ui_file)
        ui_file.close()
        if not self.error_msg_win:
            print(loader.errorString())
            sys.exit(-1)
        self.error_msg_win.setWindowTitle(error_title)
        self.error_msg_win.setWindowFlags(Qt.WindowType.WindowCloseButtonHint)
        self.error_msg_win.error_msg_detail.setPlainText(error_msg)
        self.error_msg_win.error_msg_win_close_btn.clicked.connect(lambda: self.error_msg_win.close()) 
        self.error_msg_win.show()

    def show_about_dialog(self,title_txt,body_txt):
        text = body_txt
        QMessageBox.about(self,'關於 '+title_txt , text)