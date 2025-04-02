from dataclasses import dataclass

@dataclass
class Distance:
    pathToFile: str
    data: list = None

    def open_file(self):
        f = open(self.pathToFile, "r")
        self.data = self.read_data(f.readlines())

    def read_data(self, lines=list):
        result = []
        for line in lines:
            line = line.split()
            if len(line) == 3:
                try:
                    result.append([line[0], line[1], float(line[2])])
                except ValueError:
                    print("Cannot convert to float")
            else:
                print("Wrong format")
        return result

    def export_data(self):
        return self.data