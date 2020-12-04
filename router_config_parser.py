from itertools import islice

config_text = """
...
description CUR:ATT:IUEP12345ATI,L,ETH:156MB,MPLS,20KGG12345
...
"""
KEY_INDEX = 0
VALUE_INDEX = 1


class RouterConfig():
    def __init__(self, path=""):
        self.attributes = {}
        if path != "":
            self.loadFromPath(path)

    def get(self, attribute_key):
        return self.attributes[attribute_key]

    def loadFromPath(self, path):
        with open(path, "r") as f:
            self.loadFromIterable(f)

    def loadFromString(self, text):
        lines = text.split("\n")
        self.loadFromIterable(lines)

    def loadFromIterable(self, lines):
        for line in lines:
            parts = self.get_line_parts(line)
            if len(parts) == 2:
                key = parts[KEY_INDEX]
                value = parts[VALUE_INDEX]
                self.attributes[key] = value

                if key == "description":
                    self.parse_description(value)

    @staticmethod
    def get_line_parts(line):
        return line.strip().lower().split()

    def parse_description(self, description):
        ETH_INDEX = 2

        parts = description.split(",")
        self.attributes["circuit_size"] = parts[ETH_INDEX].split(":")[1].strip("mb")

    def __str__(self):
        output = []
        for key in self.attributes:
            value = self.attributes[key]
            output.append(f"{key}=\"{value}\"")
        return "\n".join(output)


rc = RouterConfig()
rc.loadFromString(config_text)
cs = rc.get("circuit_size")
print(cs)
print(rc)
