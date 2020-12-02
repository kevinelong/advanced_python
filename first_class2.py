# first class objects - classes and functions are just regular values

class IpParserBase:
    def __init__(self, ip_type="4", separator=".", base=10):
        self.ip_type = ip_type
        self.separator = separator
        self.base = base

    def parse(self, text: str) -> [int]:
        parts = text.split(self.separator)
        numbers = []
        for item in parts:
            numbers.append(int(item, base=self.base))
        return numbers


class IpParser4(IpParserBase):
    pass


class IpParser6(IpParserBase):

    def __init__(self):
        super().__init__(ip_type="6", separator=":", base=16)

    def parse(self, text: str) -> [int]:
        # TODO DEAL WITH :: ALSO
        # ...
        text = text.replace("::", "0000:0000")
        return super().parse(text)

parsers = {
    "4": IpParser4,
    "6": IpParser6
}


def parse_ip(text, ip_type="4"):
    cls = parsers[ip_type]()
    return cls.parse(text)


if __name__ == "__main__":
    print(parse_ip("127.0.0.128"))
    print(parse_ip("FE80:0000:0000:0000:0202:B3FF:FE1E:8329", ip_type="6"))
