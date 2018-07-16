import yaml
import os


class ConfigHelper(object):
    def __init__(self):
        self.config_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..\config\settings.yaml')
        with open(self.config_file, 'r') as stream:
            self.config_content = yaml.load(stream)

    def get_data_from_config(self, *keys):
        temp = self.config_content
        for key in keys:
            temp = temp[key]
        return temp
