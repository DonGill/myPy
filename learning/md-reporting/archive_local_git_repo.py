# ================================================================================================ #
# Project: Archive_Local_Git_Repo.py                                                                  #
# Version: 0.42                                                                                    #
# Lst Mod: 09.06.2016                                                                              #
# Author: Don Gill                                                                                 #
# ================================================================================================ #

import shutil
import my_Py_kit as mpt
import datetime

date_part = mpt.double_digit_date(datetime.date.today())

def archive_git_repo (src, dest):
    try:
        dest += '\\' + date_part
        shutil.copytree(src, dest,  True, None)
    except Exception as err_inst:
        print(err_inst)

