# Usage
The **md-reporting** app performs two functions:

1. Archives an existing git repo
2. Runs a set of reports off of the archived repo

## Current supported branches
There are currently four supported branches. They are:

1. ga-threshold
2. master
3. sc-rtm-branch
4. essentials-master

## Assumptions and requirements
1. Python 3.4
2. GitHub files on local machine:
    * c:\git-src\WindowsServerDocs-pr
    * c:\git-src\SystemCenterDocs-pr
3. An archive folder located at:
    * c:\git-arch

# Parameter usage and examples

## Parameters
**-b** (required) - indicates the branch to work with. Valid branches are *ga-threshold*, *master*, 
*sc-rtm-branch* and *essentials-master*

**-s** (optional) - indicates to skip the archiving step. If this option is set to **True**, the current day's archive will be used as the source. To override the current day's archive and use a previous one as the source of reporting, use the optional **-d** argument.

**-d** (optional) - indicates a specific archive dates to use as the source of reporting. Note, set the optional **-s** parameter to skip an archive attempt when working historical archives.


## To archive and report current day
If you wanted to archive and run reports against a particular branch like ga-threshold, you'd:
1. In your Git client, ensure you are in the ga-threshold branch and pull from origin to ensure
that you have the most up to date files locally. 
2. After verifying the above, use the following syntax for app.py:

```Python
c:\mypy\learning\md-reporting Python app.py -b ga-threshold
```
**Note**: Upon completion, you can locate the report spreadsheets in the appropriate repo > branch > date hierarchy of the required c:\git-arch folder. Folder and files dates following the following format: *YYYY.MM.DD*, or *2016.09.23*

## To run reports against a historical archived branch skipping archiving steps

```python
c:\mypy\learning\md-reporting Python app.py -b ga-threshold -s True -d 2016.09.23
``` 
**Note**: You will find the report spreadsheets in the dated archived in c:\git-arch for the branch and date provided.



