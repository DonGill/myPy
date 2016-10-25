import sys
import datetime
import getopt
import archive_local_git_repo as algr
import import_md_metadata as md_import
import md_cleanup_tests as mdct
import my_Py_kit as mpk

def build_reporting(git_repo_src, git_repo_dest, skip_archiving, branch, dt=mpk.double_digit_date(datetime.date.today())):
    
    # Archive
    if skip_archiving is False:
        print('\n### Archive process started...')
        algr.archive_git_repo(git_repo_src, git_repo_dest)
        print('complete')
    else:
        print('\n### Archive process skipped, per skip_archiving_step')
    
    # Metadata
    print('\n\n### Metadata parse started...')
    archive_dir = git_repo_dest + '\\' + dt
    result_file = archive_dir + '\\md_metadata_' + dt + '.csv'
    md_import.runit(archive_dir, result_file)
    

    # Reporting 
    print('\n\n### reporting started...')
    rpt_src = archive_dir + '\\md_metadata_' + dt + '.csv'
    rpt_dest = archive_dir + '\\' + branch + '_md_cleanup_' + dt + '.csv'
    mdct.build_mylist_from_metadata_spreadsheet(rpt_src, rpt_dest)
    


def main():
    # Initialize the constants
    date_part = ''
    local_git_src = 'c:\\git-src'
    local_git_archive = 'c:\\git-archive'
    skip_archiving_step = False
    branch = ''
    valid_branches = ['ga-threshold', 'master', 'sc-rtm-branch', 'essentials-master']

    # read the commandline arguments
    myopts, args = getopt.getopt(sys.argv[1:],"b:s:d:")
    for option, a in myopts:
        if option == '-b':
            branch = a
        elif option == '-s':
           skip_archiving_step = a
        elif option == '-d':
            date_part = a
   
    if date_part == '':
        date_part = mpk.double_digit_date(datetime.date.today())

    # check to see if a valid branch name was passed in. 
    # If so, fire the appropriate action
    # if not, raise an error       
    if branch in valid_branches:
        if branch == 'essentials-master':
            if skip_archiving_step:
                build_reporting(local_git_src + "\\WindowsServerDocs-pr\essentialsdocs", local_git_archive + "\\_Essentials Archive\\master", True, branch, date_part)
            else:
                build_reporting(local_git_src + "\\WindowsServerDocs-pr\essentialsdocs", local_git_archive + "\\_Essentials Archive\\master", False, branch, date_part)
        if branch == 'ga-threshold':
            if skip_archiving_step:
                build_reporting(local_git_src + "\\WindowsServerDocs-pr\windowsserverdocs", local_git_archive + "\\_WS16 Archive\\ga-threshold", True, branch, date_part)
            else:
                build_reporting(local_git_src + "\\WindowsServerDocs-pr\windowsserverdocs", local_git_archive + "\\_WS16 Archive\\ga-threshold", False, branch, date_part)
        elif branch == 'master':
            if skip_archiving_step:
                build_reporting(local_git_src + "\\WindowsServerDocs-pr\windowsserverdocs", local_git_archive + "\\_WS16 Archive\\master", True, branch, date_part)
            else:
                build_reporting(local_git_src + "\\WindowsServerDocs-pr\windowsserverdocs", local_git_archive + "\\_WS16 Archive\\master", False, branch, date_part)
        elif branch == 'sc-rtm-branch':
            if skip_archiving_step:
                build_reporting(local_git_src + "\\SystemCenterDocs-pr\\SystemCenterDocs", local_git_archive + "\\_SC16 Archive\\sc-rtm-branch", True, branch, date_part)
            else:
                build_reporting(local_git_src + "\\SystemCenterDocs-pr\\SystemCenterDocs", local_git_archive + "\\_SC16 Archive\\sc-rtm-branch", False, branch, date_part)
    else:
        raise ValueError ('branch %s is not a supported branch name.' % branch)
                

if __name__ == "__main__":
    main()