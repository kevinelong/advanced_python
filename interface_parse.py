interface_config_list = """
interface FiveGigabitEthernet1/0/4
 switchport access vlan 5
 switchport mode access
 switchport voice vlan 10
 device-tracking attach-policy IPDT
 authentication control-direction in
!
interface GigabitEthernet1/0/5
 description Some Device
 switchport access vlan 12
 switchport mode access
 switchport voice vlan 10
 device-tracking attach-policy IPDT
 authentication control-direction in
"""
# GOAL: Extract just the vlan access port for each interface into a list of dicts.
results = []
for line in interface_config_list.split("\n"):
    parts = line.strip().lower().split()
    if len(parts) > 1:
        if parts[0] == "interface":
            interface = {"name": parts[1]}
            results.append(interface)
        if parts[1] == "access":
            interface["access"] = parts[-1]
print(results)
# OUTPUT:
# [{'name': 'fivegigabitethernet1/0/4', 'access': '5'}, {'name': 'gigabitethernet1/0/5', 'access': '12'}]
