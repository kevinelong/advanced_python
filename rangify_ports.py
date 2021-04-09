
def rangify_ports(switch_ports):
    data = {}
    for item in switch_ports:
        parts = item.split("/")

        blade = parts[0]
        slot = parts[1]
        port = parts[2]
        
        both = blade + "/" + slot
        if both not in data:
            data[both] = []
        data[both].append(int(port))
    print(data)

    for key in data:
        ports = data[key]
        ports.sort()
        sequence = []
        last = -1
        output = []
        for p in ports:
            if last == - 1 or p - 1 == last:
                sequence.append(p)
            else:
                if len(sequence) > 1:
                    output.append(f"{sequence[0]}-{sequence[-1]}")
                elif len(sequence) > 0:
                    output.append(f"{sequence[0]}")
                sequence = []
                sequence.append(p)
            last = p
        if len(sequence) > 1:
            output.append(f"{sequence[0]}-{sequence[-1]}")
        elif len(sequence) > 0:
            output.append(f"{sequence[0]}")
        data[key] = output #replace port series with the range
    with_ranges = []
    for both in data:
        for ports in data[both]:
            with_ranges.append(f"{both}/{ports}")
    return with_ranges

if __name__ == "__main__":
    #TEST
    switch_ports = ['1/0/38', '1/0/48', '1/0/10', '1/0/11', '1/0/12', '1/0/20', '1/0/21', '2/0/8', '2/0/9', '2/0/10']

    result = rangify_ports(switch_ports)
    print(result)
    #EXPECTED OUTPUT: ['1/0/10-12', '1/0/20-21', '1/0/38', '1/0/48', '2/0/8-10']