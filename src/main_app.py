import src.files.addresses.hexvals as hexvals
import shutil
import subprocess
import os
from functools import partial
from pathlib import Path

loop_point_file = "src/files/clean_files/bgm_ingame_cmn.nbnk"
sound_package_iceborne = "src/files/clean_files/bgm_slugger_ingame.npck"
sound_package_vanilla = "src/files/clean_files/bgm_ingame_pg.npck"
sound_package_zorahxeno = "src/files/clean_files/bgm_ingame.npck"


sel_sel_day = "Default"
sel_sel_night = "Default"
sel_ast_day = "Default"
sel_ast_night = "Default"
sel_shara = "Default"
sel_zorah = "Default"
sel_xeno = "Default"
sel_hub_sel = "Default"
sel_hub_ast = "Default"

def change_dict(key, value):
    settings_bgm_slugger_ingame[key] = value;

# needs to be set dynamically! -> GUI
settings_loop_points = {
    "seliana_day": partial(hexvals.apply_bytes, passed_dict="seliana_day", selection=sel_sel_day),
    "seliana_night": partial(hexvals.apply_bytes, passed_dict="seliana_night", selection=sel_sel_night),
    "astera_day": partial(hexvals.apply_bytes, passed_dict="astera_day", selection=sel_ast_day),
    "astera_night": partial(hexvals.apply_bytes, passed_dict="astera_night", selection=sel_ast_night),
    "shara": partial(hexvals.apply_bytes, passed_dict="shara", selection=sel_shara),
    "zorah": partial(hexvals.apply_bytes, passed_dict="zorah", selection=sel_zorah),
    "xeno": partial(hexvals.apply_bytes, passed_dict="xeno", selection=sel_xeno),
    "gathering_hub_seliana": partial(hexvals.apply_bytes, passed_dict="gathering_hub_seliana", selection=sel_hub_sel),
    "gathering_hub_astera": partial(hexvals.apply_bytes, passed_dict="gathering_hub_astera", selection=sel_hub_ast)
}

# needs to be set dynamically! -> GUI
# seli day - 04, seli night - 46, shara - 18, astera day - 21, astera night - 18, zorah - 58, xeno - 47
settings_bgm_slugger_ingame = {
    "seliana_day": sel_sel_day,
    "seliana_night": sel_sel_night,
    "shara": f"shara_{sel_shara}",
    "gathering_hub_seliana": f"{sel_hub_sel}_hub"
}

settings_bgm_ingame_pg = {
    "astera_day": f"shara_{sel_ast_day}",
    "astera_night": f"shara_{sel_ast_night}"
}

settings_bgm_ingame = {
    "zorah": f"shara_{sel_zorah}",
    "xeno": f"shara_{sel_xeno}",
    "gathering_hub_astera": f"{sel_hub_ast}_hub"
}

theme_wem_values = {
    "seliana_day": "04",
    "seliana_night": "46",
    "shara": "18",
    "astera_day": "21",
    "astera_night": "18",
    "gathering_hub_astera": "16",
    "gathering_hub_seliana": "65",
    "zorah": "58",
    "xeno": "47"
}

def read_file(addr):
    fh = open(loop_point_file, "r+b")
    fh.seek(addr)
    data = fh.read(8)
    fh.close()
    return data

def copy_work_contents():
    shutil.copy(loop_point_file, "src/converted/")
    return True

def edit_file(fh, addr, data):
    fh.seek(addr)
    fh.write(data)


def set_loop_points(settings):
    fh = open("src/converted/bgm_ingame_cmn.nbnk", "r+b")
    # loop through dictionary values, in hexvals
    for hexpos, hexval in settings.items():
        # print(f"{hexpos} : {hexval}")
        edit_file(fh=fh, addr=hexpos, data=hexval)
    fh.close()



def move_music_files(key, mhgame, filename):
    print("selected file " + filename + ".wem from " + mhgame)
    shutil.copy(f"src/files/wems/{mhgame}/{filename}.wem", f"src/files/wems/selected_wems/{key}.wem")



map_bgm_slugger_ingame = {
    "mhxx": partial(move_music_files, mhgame="mhxx", filename="generic"),
    "mhfu": partial(move_music_files, mhgame="mhfu", filename="generic"),
    "mhswing": partial(move_music_files, mhgame="swing", filename="generic"),
    "mhswing_loud": partial(move_music_files, mhgame="swing/loud", filename="generic"),
    "mh3u": partial(move_music_files, mhgame="mh3u", filename="generic"),
    "mhfu_hub": partial(move_music_files, mhgame="gathering_hub", filename="mhfu"),
    "mh4u_hub": partial(move_music_files, mhgame="gathering_hub", filename="mh4u"),
    "mhp3_hub": partial(move_music_files, mhgame="gathering_hub", filename="mhp3"),
    "mh2_hub": partial(move_music_files, mhgame="gathering_hub", filename="mh2"),
    "mh3u_hub": partial(move_music_files, mhgame="gathering_hub", filename="mh3u"),
    "mhswing_hub": partial(move_music_files, mhgame="gathering_hub", filename="swing"),
    "mhf_kokoto_hub": partial(move_music_files, mhgame="gathering_hub", filename="kokoto"),
    "mhp3_yukumo_hub": partial(move_music_files, mhgame="gathering_hub", filename="yukumo"),
    "mh4u_cathar_hub": partial(move_music_files, mhgame="gathering_hub", filename="cathar"),
    "mh2_jumbo_hub": partial(move_music_files, mhgame="gathering_hub", filename="jumbo"),
    "mhxx_bherna_hub": partial(move_music_files, mhgame="gathering_hub", filename="bherna"),
    "shara_mhxx": partial(move_music_files, mhgame="alert", filename="mhxx"),
    "shara_mhfu": partial(move_music_files, mhgame="alert", filename="mhfu"),
    "shara_mh3u": partial(move_music_files, mhgame="alert", filename="mh3u"),
    "shara_mhswing": partial(move_music_files, mhgame="alert", filename="swing"),
    "shara_mhf_kokoto": partial(move_music_files, mhgame="alert", filename="kokoto"),
    "shara_mhp3_yukumo": partial(move_music_files, mhgame="alert", filename="yukumo"),
    "shara_mh4u_cathar": partial(move_music_files, mhgame="alert", filename="cathar"),
    "shara_mh2_jumbo": partial(move_music_files, mhgame="alert", filename="jumbo"),
    "shara_mhxx_bherna": partial(move_music_files, mhgame="alert", filename="bherna"),
    "mhf_kokoto": partial(move_music_files, mhgame="mhf", filename="kokoto"),
    "mhp3_yukumo": partial(move_music_files, mhgame="mhp3", filename="yukumo"),
    "mh4u_cathar": partial(move_music_files, mhgame="mh4u", filename="cathar"),
    "mh2_jumbo": partial(move_music_files, mhgame="mh2", filename="jumbo"),
    "mhxx_bherna": partial(move_music_files, mhgame="mhxx", filename="bherna")
}


import time
def subprocess_add_wems(sound_package_file, filename):
    filepath = sound_package_file
    target = "src/files/wems/selected_wems/"
    output = f"src/converted/{filename}"
    args = f"src/wwiseutil.exe -replace -filepath {filepath} -target {target} -output {output}"
    try:
        subprocess.call(args)
    except Exception as e:
        print(e)
        print("file not changed - " + filepath)

def delete_selection(soundpackage, filename):
    print("deleting wems...")
    subprocess_add_wems(soundpackage, filename)
    folder = "src/files/wems/selected_wems"
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            os.unlink(file_path)
        except Exception as e:
            print("Failed to delete %s. Reason: %s.\n Make sure deleting files in files/wems/selected_wems is allowed on your end." % (file_path, e))


def queue_fileoperations():
    for key, value in settings_bgm_slugger_ingame.items():
        try:
            map_bgm_slugger_ingame[value](theme_wem_values[key])
        except Exception as e:
            print(e)

    delete_selection(sound_package_iceborne, "bgm_slugger_ingame.npck")
    for key, value in settings_bgm_ingame.items():
        try:
            map_bgm_slugger_ingame[value](theme_wem_values[key])
        except Exception as e:
            print(e)
    delete_selection(sound_package_zorahxeno, "bgm_ingame.npck")
    for key, value in settings_bgm_ingame_pg.items():
        try:
            map_bgm_slugger_ingame[value](theme_wem_values[key])
        except Exception as e:
            print(e)
    delete_selection(sound_package_vanilla, "bgm_ingame_pg.npck")


def delete_converted_content():
    print("deleting preconverted files...")
    folder = "src/converted"
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            os.unlink(file_path)
        except Exception as e:
            print("Failed to delete %s. Reason: %s.\n Make sure deleting files in files/wems/selected_wems is allowed on your end." % (file_path, e))

def run_main():
    copy_work_contents()
    queue_fileoperations()
    for key, value in settings_loop_points.items():
        try:
            set_loop_points(settings_loop_points[key]())
        except Exception as e:
            print(e)

