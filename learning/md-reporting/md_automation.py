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
DATE_PART = ''
LOCAL_GIT_SRC = 'c:\\git-src'
LOCAL_GIT_ARCHIVE = 'c:\\git-archive'
SKIP_ARCHIVING_STEP = True

# Run/Build Cleanup spreadsheet

def build_reporting(git_repo_src, git_repo_dest, branch):
    # Archive
    if SKIP_ARCHIVING_STEP is False:
        print('\n### Archive process started...')
        algr.main(git_repo_src, git_repo_dest)
        print('complete')
    else:
        print('\n### Archive process skipped, per SKIP_ARCHIVING_STEP')
    
    # Metadata
    print('\n\n### Metadata parse started...')
    ws_archive_dir = git_repo_dest + '\\' + DATE_PART
    result_file = ws_archive_dir + '\\md_metadata_' + DATE_PART + '.csv'
    md_import.runit(ws_archive_dir, result_file)
    print('complete')

    # Reporting 
    print('\n\n### reporting started...')
    mdct.build_testing_spreadsheet(ws_archive_dir + '\\md_metadata_' + DATE_PART + '.csv', ws_archive_dir + '\\' + branch + '_md_cleanup_' + DATE_PART + '.csv')
    print('complete')


if SKIP_ARCHIVING_STEP:
    DATE_PART = '2016.09.22'
else:
    DATE_PART = mpk.double_digit_date(datetime.date.today())

# ws16 - master
#build_reporting(LOCAL_GIT_SRC + "\\WindowsServerDocs-pr\windowsserverdocs", LOCAL_GIT_ARCHIVE + "\\_WS16 Archive\\master", 'master')

# ws16 - ga-threshold
build_reporting(LOCAL_GIT_SRC + "\\WindowsServerDocs-pr\windowsserverdocs", LOCAL_GIT_ARCHIVE + "\\_WS16 Archive\\ga-threshold",'ga_threshold')

# sc16 - ga-threshold
#build_reporting(LOCAL_GIT_SRC + "\\SystemCenterDocs-pr\\SystemCenterDocs", LOCAL_GIT_ARCHIVE + "\\_SC16 Archive\\sc-rtm-branch", 'sc_rtm_branch')