import os


def kill_process_by_name(name):
    if name:
        os.system('taskkill /F /im %s' % name)


def kill_log_processor():
    kill_process_by_name('LogProcessor.exe')
