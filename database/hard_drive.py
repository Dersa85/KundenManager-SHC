import json


class SaverLoader:

    def save(self, data, path):
        """Speichert die dict als json in den angegeben Pfad"""
        with open(path, 'w') as f:
            json.dump(data, f)




    def load(self, path):
        """Ladet die json aus dem Pfad und gibt es als dict zurück"""
        with open(path, 'r') as f:
            dict = json.load(f)
            return dict


HardDrive = SaverLoader()