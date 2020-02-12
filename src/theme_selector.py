import sys
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QImage, QPalette, QBrush
from PyQt5.QtWidgets import *
from functools import partial

import src.main_app as main_app
import src.files.addresses.hexvals as hexvals

text_to_values = {
    "Pokke Village (MHGen)": "mhxx",
    "Pokke Village (MHFU)": "mhfu",
    "Pokke Village (Swing Version)": "mhswing",
    "Moga Village (MH Tri)": "mh3u",
    "Gathering Hub Pokke (MHFU)": "mhfu",
    "Gathering Hub Val Habar (MH4U)": "mh4u",
    "Gathering Hub Yukumo (MHP3)": "mhp3",
    "Kokoto Village (MHF)": "mhf_kokoto",
    "Yukumo Village (MHP3rd)": "mhp3_yukumo",
    "Cathar (MH4U)": "mh4u_cathar"
}

combobox_pos = 230

class MainWindow(QWidget):

    def __init__(self):
        QWidget.__init__(self)
        self.setFixedSize(500, 375)
        self.setGeometry(500, 100, 500, 375)



        oImage = QImage("src/background_image.png")

        palette = QPalette()
        palette.setBrush(10, QBrush(oImage))  # 10 = Windowrole

        self.setPalette(palette)


        self.lbl_sd = QLabel("Seliana Day", self)

        sel_day = QComboBox(self)
        sel_day.addItem("Default")
        sel_day.addItem("Pokke Village (MHGen)")
        sel_day.addItem("Pokke Village (MHFU)")
        sel_day.addItem("Pokke Village (Swing Version)")
        sel_day.addItem("Kokoto Village (MHF)")
        sel_day.addItem("Moga Village (MH Tri)")
        sel_day.addItem("Yukumo Village (MHP3rd)")
        sel_day.addItem("Cathar (MH4U)")
        sel_day.move(combobox_pos, 20)
        self.lbl_sd.move(50, 20)

        sel_day.activated[str].connect(self.set_seliana_day)


        self.lbl_sn = QLabel("Seliana Night", self)

        sel_night = QComboBox(self)
        sel_night.addItem("Default")
        sel_night.addItem("Pokke Village (MHGen)")
        sel_night.addItem("Pokke Village (MHFU)")
        sel_night.addItem("Pokke Village (Swing Version)")
        sel_night.addItem("Kokoto Village (MHF)")
        sel_night.addItem("Moga Village (MH Tri)")
        sel_night.addItem("Yukumo Village (MHP3rd)")
        sel_night.addItem("Cathar (MH4U)")
        sel_night.move(combobox_pos, 50)
        self.lbl_sn.move(50, 50)

        sel_night.activated[str].connect(self.set_seliana_night)

        self.lbl_ad = QLabel("Astera Day", self)

        ast_day = QComboBox(self)
        ast_day.addItem("Default")
        ast_day.addItem("Pokke Village (MHGen)")
        ast_day.addItem("Pokke Village (MHFU)")
        ast_day.addItem("Pokke Village (Swing Version)")
        ast_day.addItem("Kokoto Village (MHF)")
        ast_day.addItem("Moga Village (MH Tri)")
        ast_day.addItem("Yukumo Village (MHP3rd)")
        ast_day.addItem("Cathar (MH4U)")
        ast_day.move(combobox_pos, 80)
        self.lbl_ad.move(50, 80)

        ast_day.activated[str].connect(self.set_astera_day)

        self.lbl_an = QLabel("Astera Night", self)

        ast_night = QComboBox(self)
        ast_night.addItem("Default")
        ast_night.addItem("Pokke Village (MHGen)")
        ast_night.addItem("Pokke Village (MHFU)")
        ast_night.addItem("Pokke Village (Swing Version)")
        ast_night.addItem("Kokoto Village (MHF)")
        ast_night.addItem("Moga Village (MH Tri)")
        ast_night.addItem("Yukumo Village (MHP3rd)")
        ast_night.addItem("Cathar (MH4U)")
        ast_night.move(combobox_pos, 110)
        self.lbl_an.move(50, 110)

        ast_night.activated[str].connect(self.set_astera_night)

        self.lbl_sh = QLabel("Shara Ishvalda Quest Alert", self)

        shara = QComboBox(self)
        shara.addItem("Default")
        shara.addItem("Pokke Village (MHGen)")
        shara.addItem("Pokke Village (MHFU)")
        shara.addItem("Pokke Village (Swing Version)")
        shara.addItem("Kokoto Village (MHF)")
        shara.addItem("Moga Village (MH Tri)")
        shara.addItem("Yukumo Village (MHP3rd)")
        shara.addItem("Cathar (MH4U)")
        shara.move(combobox_pos, 140)
        self.lbl_sh.move(50, 140)

        shara.activated[str].connect(self.set_shara)

        self.lbl_zh = QLabel("Zorah Magdaros Quest Alert", self)

        zorah = QComboBox(self)
        zorah.addItem("Default")
        zorah.addItem("Pokke Village (MHGen)")
        zorah.addItem("Pokke Village (MHFU)")
        zorah.addItem("Pokke Village (Swing Version)")
        zorah.addItem("Kokoto Village (MHF)")
        zorah.addItem("Moga Village (MH Tri)")
        zorah.addItem("Yukumo Village (MHP3rd)")
        zorah.addItem("Cathar (MH4U)")
        zorah.move(combobox_pos, 170)
        self.lbl_zh.move(50, 170)

        zorah.activated[str].connect(self.set_zorah)

        self.lbl_xn = QLabel("Xeno'Jiiva Quest Alert", self)

        xeno = QComboBox(self)
        xeno.addItem("Default")
        xeno.addItem("Pokke Village (MHGen)")
        xeno.addItem("Pokke Village (MHFU)")
        xeno.addItem("Pokke Village (Swing Version)")
        xeno.addItem("Kokoto Village (MHF)")
        xeno.addItem("Moga Village (MH Tri)")
        xeno.addItem("Yukumo Village (MHP3rd)")
        xeno.addItem("Cathar (MH4U)")
        xeno.move(combobox_pos, 200)
        self.lbl_xn.move(50, 200)

        xeno.activated[str].connect(self.set_xeno)

        self.lbl_hs = QLabel("Gathering Hub - Seliana", self)

        hub_sel = QComboBox(self)
        hub_sel.addItem("Default")
        hub_sel.addItem("Gathering Hub Pokke (MHFU)")
        hub_sel.addItem("Gathering Hub Val Habar (MH4U)")
        hub_sel.addItem("Gathering Hub Yukumo (MHP3)")
        hub_sel.addItem("Pokke Village (Swing Version)")
        hub_sel.move(combobox_pos, 250)
        self.lbl_hs.move(50, 250)

        hub_sel.activated[str].connect(self.set_hub_seliana)

        self.lbl_ha = QLabel("Gathering Hub - Astera", self)

        hub_ast = QComboBox(self)
        hub_ast.addItem("Default")
        hub_ast.addItem("Gathering Hub Pokke (MHFU)")
        hub_ast.addItem("Gathering Hub Val Habar (MH4U)")
        hub_ast.addItem("Gathering Hub Yukumo (MHP3)")
        hub_ast.addItem("Pokke Village (Swing Version)")
        hub_ast.move(combobox_pos, 280)
        self.lbl_ha.move(50, 280)

        hub_ast.activated[str].connect(self.set_hub_astera)

        self.lbl_loading = QLabel("", self)
        self.lbl_loading.move(270, 340)
        self.lbl_loading.setStyleSheet("color:green; font-size:14px")

        self.button = QPushButton("Create Custom Soundfile", self)
        self.button.setStyleSheet("padding:10px; width:160px;")
        self.button.move(50, 330)

        self.button.clicked.connect(self.on_click)

        self.show()

    def on_click(self):
        self.lbl_loading.setText("Please wait....")
        self.lbl_loading.adjustSize()
        main_app.delete_converted_content()
        main_app.run_main()
        self.lbl_loading.setText("Done. Please close the window.")
        self.lbl_loading.adjustSize()

    def set_seliana_day(self, text):
        main_app.settings_loop_points["seliana_day"] = partial(hexvals.apply_bytes, passed_dict="seliana_day", selection=text_to_values.get(text))
        main_app.settings_bgm_slugger_ingame["seliana_day"] = text_to_values.get(text)


    def set_seliana_night(self, text):
        main_app.settings_loop_points["seliana_night"] = partial(hexvals.apply_bytes, passed_dict="seliana_night", selection=text_to_values.get(text))
        main_app.settings_bgm_slugger_ingame["seliana_night"] = text_to_values.get(text)


    def set_astera_day(self, text):
        main_app.settings_loop_points["astera_day"] = partial(hexvals.apply_bytes, passed_dict="astera_day", selection=text_to_values.get(text))
        main_app.settings_bgm_ingame_pg["astera_day"] = f"shara_{text_to_values.get(text)}"


    def set_astera_night(self, text):
        main_app.settings_loop_points["astera_night"] = partial(hexvals.apply_bytes, passed_dict="astera_night", selection=text_to_values.get(text))
        main_app.settings_bgm_ingame_pg["astera_night"] = f"shara_{text_to_values.get(text)}"


    def set_shara(self, text):
        main_app.settings_loop_points["shara"] = partial(hexvals.apply_bytes, passed_dict="shara", selection=text_to_values.get(text))
        main_app.settings_bgm_slugger_ingame["shara"] = f"shara_{text_to_values.get(text)}"


    def set_zorah(self, text):
        main_app.settings_loop_points["zorah"] = partial(hexvals.apply_bytes, passed_dict="zorah", selection=text_to_values.get(text))
        main_app.settings_bgm_ingame["zorah"] = f"shara_{text_to_values.get(text)}"


    def set_xeno(self, text):
        main_app.settings_loop_points["xeno"] = partial(hexvals.apply_bytes, passed_dict="xeno", selection=text_to_values.get(text))
        main_app.settings_bgm_ingame["xeno"] = f"shara_{text_to_values.get(text)}"


    def set_hub_seliana(self, text):
        main_app.settings_loop_points["gathering_hub_seliana"] = partial(hexvals.apply_bytes, passed_dict="gathering_hub_seliana", selection=f"{text_to_values.get(text)}_hub")
        main_app.settings_bgm_slugger_ingame["gathering_hub_seliana"] = f"{text_to_values.get(text)}_hub"
        print(main_app.settings_bgm_slugger_ingame["gathering_hub_seliana"])


    def set_hub_astera(self, text):
        main_app.settings_loop_points["gathering_hub_astera"] = partial(hexvals.apply_bytes, passed_dict="gathering_hub_astera", selection=f"{text_to_values.get(text)}_hub")
        main_app.settings_bgm_ingame["gathering_hub_astera"] = f"{text_to_values.get(text)}_hub"
        print(main_app.settings_bgm_ingame["gathering_hub_astera"])


def run_gui():
    app = QApplication(sys.argv)
    oMainwindow = MainWindow()
    sys.exit(app.exec_())