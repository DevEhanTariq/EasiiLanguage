class interpret():
    def __init__(self, filename):
        self.filename = filename
        self.fileContent = []
        self.variables = {}

    def read(self):
        with open(f"{self.filename}", "r") as f:
            self.fileContent = f.readlines()

    def format(self):
        self.fileContent = [line.strip() for line in self.fileContent]

    def loop(self):
        for line in self.fileContent:
            if line.strip() == "":
                continue
            components = line.split()
            if line[:5] == "write":
                text = line[6:]
                newText = ""
                listen = False
                variableNames = []
                for char in text:
                    if char == "}":
                        listen = False
                    elif listen:
                        variableNames[-1] = variableNames[-1] + char
                    elif char == "{":
                        listen = True
                        variableNames.append("")
                listen = False
                for char in text:
                    if char == "}":
                        listen = False
                    elif char == "{":
                        listen = True
                        newText += self.variables[variableNames[0]]
                        variableNames.pop(0)
                    elif not listen:
                       newText += char
                print(newText)


            elif components[0] == "var":
                self.variables[components[1]] = components[3]

