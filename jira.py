# imports
from pathlib import Path
import os

class ConfigDetails:
    def __init__(self):
        self.configFile=".jirafile"
        self.home=Path.home()

    def ConfigFilePath(self):
        return os.path.join(self.home, self.configFile)
        
def main():
    config_worker=ConfigDetails()
    file=config_worker.ConfigFilePath()
    print(file)
        
if __name__ == "__main__":
    main()

