class interpret():
    def __init__(self, filename):
        self.filename = filename
        self.fileContent = []

    def read(self):
        with open(f"{self.filename}", "r") as f:
            self.fileContent = f.readlines()

    def format(self):
        self.fileContent = [line.strip() for line in self.fileContent]

    def loop(self):
        for line in self.fileContent:
            if line[:5] == "write":
                print(line[6:])

