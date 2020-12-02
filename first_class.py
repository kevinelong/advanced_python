# first class objects - classes and functions are just regular values

def parse_ip4(text):
    separator = "."
    parts = text.split(separator)
    numbers = []
    for item in parts:
        numbers.append(int(item))
    return numbers


print(parse_ip4("127.0.0.128"))


def parse_ip6(text):
    separator = ":"
    parts = text.split(separator)
    numbers = []
    for item in parts:
        hex_text = f"0x{item}"
        numbers.append(int(hex_text, base=16))
    return numbers


print(parse_ip6("FE80:0000:0000:0000:0202:B3FF:FE1E:8329"))  # six sixteen bit numbers

parsers = {
    "4": parse_ip4,
    "6": parse_ip6
}


def parse_ip(text, ip_type="4"):
    return parsers[ip_type](text)
    # if ip_type == 4:
    #     return parse_ip4(text)
    # else:
    #     return parse_ip6(text)


print(parse_ip("127.0.0.128"))
print(parse_ip("FE80:0000:0000:0000:0202:B3FF:FE1E:8329", ip_type="6"))
