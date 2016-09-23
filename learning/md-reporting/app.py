import sys
import datetime
import getopt
import archive_local_git_repo as algr
import import_md_metadata as md_import
import md_cleanup_tests as mdct
import my_Py_kit as mpk

def build_reporting(git_repo_src, git_repo_dest, skip_archiving, branch, date_target=mpk.double_digit_date(datetime.date.today())):
    
    # Archive
    if skip_archiving is False:
        print('\n### Archive process started...')
        algr.archive_git_repo(git_repo_src, git_repo_dest)
        print('complete')
    else:
        print('\n### Archive process skipped, per skip_archiving_step')
    
    # Metadata
    print('\n\n### Metadata parse started...')
    archive_dir = git_repo_dest + '\\' + date_target
    result_file = archive_dir + '\\md_metadata_' + date_target + '.csv'
    md_import.runit(archive_dir, result_file)
    print('complete')

    # Reporting 
    print('\n\n### reporting started...')
    mdct.build_testing_spreadsheet(archive_dir + '\\md_metadata_' + date_target + '.csv', archive_dir + '\\' + branch + '_md_cleanup_' + date_target + '.csv')
    print('complete')


def main():
    # Initialize the constants
    date_part = ''
    local_git_src = 'c:\\git-src'
    local_git_archive = 'c:\\git-archive'
    skip_archiving_step = False
    branch = ''
    valid_branches = ['ga-threshold', 'master', 'sc-rtm-branch']

    # read the commandline arguments
    myopts, args = getopt.getopt(sys.argv[1:],"b:a:d:")
    for option, a in myopts:
        if option == '-b':
            branch = a
        elif option == '-a':
           skip_archiving_step = a
        elif option == '-d':
            date_part = a
   
    if date_part == '':
        date_part = mpk.double_digit_date(datetime.date.today())

    # check to see if a valid branch name was passed in. 
    # If so, fire the appropriate action
    # if not, raise an error       
    if branch in valid_branches:
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