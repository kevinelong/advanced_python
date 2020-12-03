

raw_input_data = {
    "hostname": "ROS-SC01-1-C104A-ORc",
    "model": "xxx-yyy-zzz",
    "management": "",
    "ip": "",
}
model_options = [
    "c1",
    "b2",
    "N3K",
    "N3K",
    "N5K",
    "N7K",
    "N9K",
]

input_data = {
    "hostname": "ROS-SC01-1-C104A-OR",
    "site_code": "ROS",
    "raw_switch_type": "SC01",
    "switch_type": "SC",
    "sequence_number": "01",
    "state": "OR",
    "model": "c1",
    "management": "",
    "ip": "10.0.0.1",
}

class Device:
    def __init__(self):
        # TODO LOAD FROM  EXTERNAL FILE
        self.config = core = {
            "a": [
                "AAA",
                "BBB",
                "CCC",
            ],
            "b": [
                "XXX",
                "YYY",
                "ZZZ",
            ]
        }
        self.config_additions = {}
        self.subtractions = {}
        self.replacements = {}

    def additions(self):
        for key in self.additions:
            self.config[key] = self.additions[key]

    def subtractions(self):
        for key in self.additions:
            self.config[key] = self.additions[key]


    def replacements(self):
        pass


class N9K(Device):
    pass

DEVICES = {
    "N9K" : N9K
}

device = DEVICES[device_name]()

# output = f"""
# {
# "source" : "{p.server}",
#     "target" : "{p.server}",
#     "user"   : "{p.username}",
#     "passwd" : "{p.password}",
# }
# """
#
# print(output)
