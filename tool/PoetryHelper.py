import subprocess

import yaml


class PoetryHelper:
    def AddFromYml(self, yml_path):
        with open(yml_path, 'r') as yml:
            config = yaml.safe_load(yml)
            channel = config["channels"]
            depend = config["dependencies"]
            for item in channel:
                subprocess.call(f"poetry add {item}", shell=True)
            for item in depend:
                subprocess.call(f"poetry add {item}", shell=True)




helper = PoetryHelper()
helper.AddFromYml("environment.yml")