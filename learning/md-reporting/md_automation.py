# ================================================================================================ #
# Project: md_automation.py                                                                        #
# Version: 0.42                                                                                    #
# Lst Mod: 09.16.2016                                                                              #
# Author: Don Gill                                                                                 #
# ================================================================================================ #
# This script will link together various maintenance scripts to help automate:
#   1. [Done] Daily archive of the WS and SC 16 local machine MD files
#   2. [Done] Run metadata report
#   3. Run 'find string report' report
#   4. Run the TOC report


import archive_local_git_repo as algr
import import_md_metadata as md_import
import md_cleanup_tests as mdct
import my_Py_kit as mpk
import datetime

# constants
DATE_PART = mpk.double_digit_date(datetime.date.today())
LOCAL_GIT_SRC = 'c:\\git-src'
LOCAL_GIT_ARCHIVE = 'c:\\git-archive'



# print('\nArchive Process*****')
# WS16 - ga-threshold
# src = r'C:\git-src\WindowsServerDocs-pr'
# dest = r'C:\git-archive\_WS16 Archive\ga-threshold'
# label = 'WS16'
# algr.main(src, dest, label)

# WS16 - master
# src = r'C:\git-src\WindowsServerDocs-pr'
# dest = r'C:\git-archive\_WS16 Archive\master'
# label = 'WS16'
# algr.main(src, dest, label)

# SC16 - sc-rtm-branch
# src = r'C:\git-src\SystemCenterDocs-pr'
# dest = r'C:\git-archive\_SC16 Archive\sc-rtm-branch'
# label = 'SC16'
# algr.main(src, dest, label)


# print('\n\nMetadata Spreadsheet*****')
# WS16 - ga-threshold
# ws_archive_dir = 'C:\\git-archive\\_WS16 Archive\\ga-threshold\\' + date_part
# result_file = ws_archive_dir + '\\ws16_metadata_' + date_part + '.csv'
# md_import.runit(ws_archive_dir, result_file)
# print(result_file)

# WS16 - master
# ws_archive_dir = 'C:\\git-archive\\_WS16 Archive\\master\\' + date_part
# result_file = ws_archive_dir + '\\ws16_metadata_' + date_part + '.csv'
# md_import.runit(ws_archive_dir, result_file)
# print(result_file)

# SC16 - sc-rtm-branch
# sc_archive_dir = 'C:\\git-archive\\_SC16 Archive\\sc-rtm-branch\\' + date_part
# result_file = sc_archive_dir + '\\sc16_metadata_' + date_part + '.csv'
# md_import.runit(sc_archive_dir, result_file)
# print(result_file)



# Run/Build Cleanup spreadsheet

def build_reporting(git_repo_src, git_repo_dest):
    # Archive
    print('\n### Archive process started...')
    algr.main(git_repo_src, git_repo_dest)
    print('complete')
    
    # Metadata
    print('\n\n### Metadata parse started...')
    ws_archive_dir = git_repo_dest + '\\' + DATE_PART
    result_file = ws_archive_dir + '\\md_metadata_' + DATE_PART + '.csv'
    md_import.runit(ws_archive_dir, result_file)
    print('complete')

    # Reporting 
    print('\n\n### Reporting started...')
    mdct.build_testing_spreadsheet(ws_archive_dir + '\\md_metadata_' + DATE_PART + '.csv', ws_archive_dir + '\\md_cleanup_' + DATE_PART + '.csv')
    print('complete')


#ws16 - master
build_reporting(LOCAL_GIT_SRC + "\\WindowsServerDocs-pr\windowsserverdocs", LOCAL_GIT_ARCHIVE + "\\_WS16 Archive\\master")

#ws16 - ga-threshold
#build_reporting(LOCAL_GIT_SRC + "\\WindowsServerDocs-pr\windowsserverdocs", LOCAL_GIT_ARCHIVE + "\\_WS16 Archive\\ga-threshold")

#sc16 - ga-threshold
#build_reporting(LOCAL_GIT_SRC + "\\SystemCenterDocs-pr\\SystemCenterDocs", LOCAL_GIT_ARCHIVE + "\\_SC16 Archive\\sc-rtm-branch")