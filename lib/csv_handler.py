import os
import csv


def parse_csv(csv_path, delimiter=',', quotechar='"'):
    if not os.path.isfile(csv_path):
        raise AssertionError('%s is not a valid file path.' % csv_path)
    ret = []
    with open(csv_path) as f:
        for row in csv.reader((x.replace('\0', '') for x in f), delimiter=delimiter, quotechar=quotechar):
            if row == list([]):
                continue
            ret.append(row)
    return ret
