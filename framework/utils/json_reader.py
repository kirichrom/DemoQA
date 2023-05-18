import json

from project.resources import path


class JsonReader:

    def read_data(self, *args, directory: str = path.framework_config_path):
        data = self.open_data_file(directory).get(args[0])
        for arg in args[1:]:
            data = data.get(arg)
        return data

    @staticmethod
    def open_data_file(directory: str) -> dict:
        with open(directory, 'r') as json_file:
            data = json.load(json_file)
            return data
