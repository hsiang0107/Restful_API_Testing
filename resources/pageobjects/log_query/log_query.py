import os
import re
import datetime
from lib.LogSender.LogSender import LogSender
from lib import DBHelper
from lib import csv_handler

test_data_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                              r'..\..\..\tests\testdata\Log_Query')
csv_download_path = os.path.join(os.getenv('USERPROFILE'), 'Downloads')


def log_query_suite_setup():
    log_sender = LogSender()
    register_path = os.path.join(test_data_path, 'Initialize')
    log_sender.register_with_csv_file('RAT', register_path)
    log_sender.send_log(os.path.join(register_path, 'Status.csv'))


def clear_log():
    DBHelper.clear_log_query_logs()


def _get_test_case_id(test_case_name):
    pre_idx = test_case_name.index('(')
    post_idx = test_case_name.index(')')
    return test_case_name[pre_idx + 1:post_idx]


def send_log(test_case_name, file_name):
    test_case_name = _get_test_case_id(test_case_name)
    log_sender = LogSender()
    log_sender.send_log(os.path.join(test_data_path, test_case_name, file_name))


def downloaded_result_should_same_as_expected(test_case_name, expected_file_name):
    test_case_name = _get_test_case_id(test_case_name)
    expected_file = os.path.join(test_data_path, test_case_name, expected_file_name)
    current_file = _get_current_csv_path()
    ignore = ['Generated', 'Received']
    ignore_index = []
    expected = csv_handler.parse_csv(expected_file, delimiter='\t')
    current = csv_handler.parse_csv(current_file, delimiter='\t')
    for row_idx in range(len(expected)):
        if row_idx == 0:
            for i in ignore:
                if i in expected[row_idx]:
                    ignore_index.append(expected[row_idx].index(i))
        for column_idx in range(len(expected[row_idx])):
            if column_idx in ignore_index:
                continue
            if expected[row_idx][column_idx] != current[row_idx][column_idx]:
                raise AssertionError(
                    'Content comparison failed, expected: %s, current: %s at %d, %d.' %
                    (expected[row_idx][column_idx], current[row_idx][column_idx], row_idx, column_idx)
                )


def verify_csv_with_ui(ui):
    current_file = _get_current_csv_path()
    ignore = ['Generated', 'Received']
    equivalent_value = ['', 'N/A']
    ignore_index = []
    current = csv_handler.parse_csv(current_file, delimiter='\t')
    for row_idx in range(len(ui)):
        current[row_idx] = current[row_idx][1:]
        if row_idx == 0:
            for i in ignore:
                if i in ui[row_idx]:
                    ignore_index.append(ui[row_idx].index(i))
            continue
        for column_idx in range(len(ui[row_idx])):
            if column_idx in ignore_index:
                continue
            # An comparison exception
            if ui[row_idx][column_idx] in equivalent_value and current[row_idx][column_idx] in equivalent_value:
                continue
            if ui[row_idx][column_idx] != current[row_idx][column_idx]:
                raise AssertionError(
                    'Content comparison failed, expected: %s, current: %s at %d, %d.' %
                    (ui[row_idx][column_idx], current[row_idx][column_idx], row_idx, column_idx)
                )


def _get_matched_files():
    path = csv_download_path
    today_string = datetime.datetime.now().strftime('%m%d%Y')
    pattern = re.compile('.+%s_AdHoc_.+.csv$' % today_string)
    files = [os.path.join(path, f) for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    matched_files = list(filter(pattern.match, files))
    return matched_files


def _get_current_csv_path():
    matched_files = _get_matched_files()
    if len(matched_files) == 0:
        raise AssertionError('Log Query result csv file was not found.')
    return matched_files[-1]


def remove_result_files():
    matched_files = _get_matched_files()
    for f in matched_files:
        os.remove(f)


def column_items_should_be(expected, current):
    current = current[1:]
    if len(expected) != len(current):
        raise AssertionError('Column count is not correct, expected: %d, current: %d.' % (len(expected), len(current)))
    for index, item in enumerate(expected):
        if item != current[index].text:
            raise AssertionError('Column item is not correct, expected: %s, current: %s.' % (item.text, current[index]))
