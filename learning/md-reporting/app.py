import sys
import getopt
import archive_local_git_repo as algr
import import_md_metadata as md_import
import md_cleanup_tests as mdct
import my_Py_kit as mpk

# constants
global _DATE_PART_ 
global _LOCAL_GIT_SRC_ 
global _LOCAL_GIT_ARCHIVE_ 
global _SKIP_ARCHIVING_STEP_
global _BRANCH_
global _BRANCHES_

def main():
    # Initialize the constants
    _DATE_PART_ = ''
    _LOCAL_GIT_SRC_ = 'c:\\git-src'
    _LOCAL_GIT_ARCHIVE_ = 'c:\\git-archive'
    _SKIP_ARCHIVING_STEP_ = False
    _BRANCH_ = ''
    _BRANCHES_ = ['ga-threshold','sc-rtm-branch']
    
    # read the commandline arguments
    myopts, args = getopt.getopt(sys.argv[1:],"b:a:")
    for option, a in myopts:
        if option == '-b':
            _BRANCH_ = a
        elif option == '-a':
            _SKIP_ARCHIVING_STEP_ = a

    print(_BRANCH_)
    # now that we have the options, lets run the program
    # lets assume we want to rerun a single existing

    if _BRANCH_ != '':
        #
                

if __name__ == "__main__":
    main()