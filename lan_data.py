"""
vlan 31
 name L3-MISC-APC_31
!

interface FastEthernet1/0/1
 switchport access vlan 249
"""
vlans = {}

f = open("lan_data.txt", "r")
data = f.readlines()
current = {}
current_interface = {}
for line in data:
    line = line.strip()

    if len(line) == 0:
        continue

    parts = line.split()

    if parts[0] == "vlan":
        vlan_id = parts[1]
        current = {"vlan_id":vlan_id, "interfaces":[]}

    elif parts[0] == "name":
        name = parts[1]
        current["name"] = name
        if "USER-PC" in name or "VOICE" in name:
            vlans[vlan_id] = current

    elif parts[0] == "interface":
        switch_port = parts[1]
        switch_port_parts = switch_port.split("/")
        if len(switch_port_parts) > 1:
            current_interface = {"switch_port": switch_port_parts}
    elif parts[0] == "switchport":
        access_type = parts[1]
        if access_type in ["access", "voice"]:
            vlan_id = parts[3]
            current_interface["access_type"] = access_type
            current_interface["vlan_id"] = vlan_id
            if vlan_id in vlans:
                vlans[vlan_id]["interfaces"].append(current_interface)

print("RESULTS:")

import json
print(json.dumps(vlans, indent=4))