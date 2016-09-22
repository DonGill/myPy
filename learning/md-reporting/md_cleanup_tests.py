

# will run tests
import csv
import re

# BASE_METADATA_CSV = r'C:\GIT_Archive\_WS16 Archive\2016.09.21\ws16_metadata_2016.09.21.csv'
mylist = []
md_fieldnames = ['filepath', 'ms.date','ms.prod', 'ms.technology', 'ms.author', 'author', 'manager', 'ms.topic', 'title', 'description', 't-technical-preview', 't-preliminary', 't-2012', 't-img-alt-text']

def count_inst(src_file, string_to_find):
    # WA using encoding='Latin-1' to get around some files with ASCII encoding issues
    try:
        #src = open(src_file, encoding='Latin-1').read()
        return src_file.count(string_to_find)
    except Exception as err_inst:
        print(err_inst)
        return 1000
        pass

def missing_img_alt_text(src_file):
    regex = r'!\[\s*\]'
    if re.search(regex, src_file):
        match = re.search(regex, src_file)
        #print ('match - %s, %s' % (match.start(), match.end()))
        return True
    else:
        return False

def build_testing_spreadsheet(metadata_csv_path, result_csv_path):
    # open the original spreadsheet, load into list-of-dictionaries
    with open(metadata_csv_path, encoding='Latin-1') as orig_csv:
        reader = csv.DictReader(orig_csv)
        for row in reader:
            mylist.append(row)
    orig_csv.close()

    # per file in the spreadsheet, run the following tests and persist back to another csv
    for row in mylist:
        with open(row['filepath'], encoding='Latin-1') as test:
            # run a lot of tests
            md_file_text = test.read().lower()
            result1 = count_inst(md_file_text, 'technical preview')
            result2 = count_inst(md_file_text, 'preliminary')
            result3 ='Boo'
            result4 = missing_img_alt_text(md_file_text)
            
            row.update({'t-technical-preview': result1, 't-preliminary': result2, 't-2012': result3, 't-img-alt-text': result4})
        test.close()

    with open(result_csv_path, 'w', newline='\n') as csvfile:
        writer = csv.DictWriter(csvfile, dialect='excel', fieldnames=md_fieldnames)
        writer.writeheader()
        writer.writerows(mylist)

    csvfile.close()

