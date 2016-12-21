# -*- coding: utf-8 -*-
#!/usr/bin/env python

import csv, xlrd, os
from os import listdir
from os.path import isfile, join

def xls_to_csv(xls_file):
    wb = xlrd.open_workbook(xls_file)
    for sheet in wb.sheet_names():
        sh = wb.sheet_by_name(sheet)
        csv_file_name = os.path.splitext(xls_file)[0] + "_" + sheet + ".csv"
        with open(csv_file_name, 'w', encoding='utf8') as file:
            wr = csv.writer(file, quoting=csv.QUOTE_ALL)
            for rownum in range(sh.nrows):
                wr.writerow(sh.row_values(rownum))

if __name__ == '__main__':
    onlyfiles = [f for f in listdir(os.getcwd()) if isfile(join(os.getcwd(), f))]
    for file in onlyfiles:
        if os.path.splitext(file)[1] == ".xls" or os.path.splitext(file)[1] == ".xlsx":
            xls_to_csv(file)
