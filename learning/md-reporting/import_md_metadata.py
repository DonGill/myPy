# pass in an md document and it passess back a standard dictionary containing all the values in that file
import csv
import os

md_list = []
md_fieldnames = ['filepath', 'ms.date','ms.prod', 'ms.technology', 'ms.author', 'author', 'manager', 'ms.assetid', 'ms.topic', 'title', 'description']


def _write_csv(csv_dest):
    with open(csv_dest, 'w', newline='\n') as csvfile:
        writer = csv.DictWriter(csvfile, dialect='excel', fieldnames=md_fieldnames)
        writer.writeheader()
        writer.writerows(md_list)
        print(csv_dest)
    csvfile.close()

def _get_title(md):
    result = 'blank'
    for line in str(md).split('\\n'):
        if line.__contains__('title: '):
            result = line[7:].strip().replace('\\r', '').replace(',', '')
            break
    return result

def _get_ms_assetid(md):
    result = 'blank'
    for line in str(md).split('\\n'):
        if line[0:12] == ('ms.assetid: '):
            result = line[12:].strip().replace('\\r', '').replace(',', '')
            break
    return result

def _get_mstopic(md):
    result = 'blank'
    for line in str(md).split('\\n'):
        if line.__contains__('ms.topic: '):
            result = line[9:].strip().replace('\\r', '')
            break
    return result

def _get_description(md):
    result = 'blank'
    for line in str(md).split('\\n'):
        if line.__contains__('description: '):
            result = line[13:].strip().replace('\\r', '')
            break
    if len(result) <= 3: # work around values being captured as " "
        result = 'blank'
    return result

def _get_manager(md):
    result = 'blank'
    for line in str(md).split('\\n'):
        if line.__contains__('manager:'):
            result = line[9:].strip().replace('\\r', '').lower()
            break
    return result

def _get_msprod(md):
    result = 'blank'
    for line in str(md).split('\\n'):
        if line.__contains__('ms.prod: '):
            result = line[9:].strip().replace('\\r', '').lower()
            break
    return result

def _get_msdate(md):
    result = 'blank'
    for line in str(md).split('\\n'):
        if line.__contains__('ms.date:'):
            result = line[8:].strip().replace('\\r', '').lower()
            break

    return result

def _get_mstech(md):
    lines = str(md).split('\\n')

    for line in lines:
        result = ''
        if line.__contains__('ms.technology:'):
            if lines.index(line) <= len(lines) - 2:
                # print ('contidtion met', lines[lines.index(line) + 1], lines[lines.index(line) + 2])
                if lines[lines.index(line) + 1].__contains__('- '):
                    result = lines[lines.index(line) + 1][4:].strip().replace('\\r', '')
                if lines[lines.index(line) + 2].__contains__('- '):
                    result += ' + ' + lines[lines.index(line) + 2][4:].strip().replace('\\r', '')
            else:
                result = line[15:].strip().replace('\\r', '')
            if result == '':
                result = line[15:].strip().replace('\\r', '')
            break
    return result.strip().replace('\\r', '')

def _get_author(md, skip):
    result = 'blank'
    for line in str(md).split('\\n'):
        # print(line[0:7])
        if line[0:7] == 'author:':
            result = line[8:].strip().replace('\\r', '').lower()
            break
    return result

def _get_msauthor(md, skip):
    result = 'blank'
    for line in str(md).split('\\n'):
        if line[0:9] == 'ms.author':
            result = line[10:].strip().replace('\\r', '').lower()
            break

    return result

def first_in(md):
    lines = str(md).split('\\n')
    winner = ''
    for line in lines:
        if line[0:9] == 'ms.author:':
            return 'ms.author'
            break
        if line[0:6] == 'author:':
            return 'author'
            break
    
def parse_md_metadata(md_file, file_path):
    mstopic = _get_mstopic(md_file)
    title = _get_title(md_file)
    description = _get_description(md_file)
    manager = _get_manager(md_file)
    msprod = _get_msprod(md_file)
    mstechnology = _get_mstech(md_file)
    msdate = _get_msdate(md_file)
    msassetid = _get_ms_assetid(md_file)

    # lets test which comes first
    if first_in(md_file) == 'ms.author':
        msauthor = _get_msauthor(md_file, True)
        author = _get_author(md_file, False)
    else:
        author = _get_author(md_file, True )
        msauthor = _get_msauthor(md_file, False)

    return {'ms.topic': mstopic,
            'ms.date': msdate,
            'title': title,
            'description': description,
            'ms.author': msauthor,
            'author': author,
            'manager': manager,
            'ms.prod': msprod,
            'ms.assetid': msassetid,
            'ms.technology': mstechnology,
            'filepath': file_path}


def runit(test_directory, csv_result):
    for root, subdirs, files in os.walk(test_directory):
        for filename in files:
            if filename.endswith(".md"):
                file_path = os.path.join(root, filename)
                with open(file_path, 'rb') as f:
                    md_list.append(parse_md_metadata(f.read(), file_path))
                f.close()

    _write_csv(csv_result)

