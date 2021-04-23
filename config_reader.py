class ConfigReader:
    """Read the config file.
    Save the content as the dictionary: keys and values are separated by '=' sign
    Remove spaces in dictionary"""

    def __init__(self, file_path: str):
        self.path = file_path
        self.data = {}

    def read_file(self):
        with open(self.path, "r") as reader:
            for line in reader:
                k, v = line.strip().split("=")
                self.data[k] = v
            self.data = {k.replace(" ", ""): v.replace(" ", "") for k, v in self.data.items()}

    def __repr__(self):
        return f"Class ConfigReader read the file - {self.path} with some data {self.data}"
