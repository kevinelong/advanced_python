import argparse
import csv
from concurrent.futures import ThreadPoolExecutor, as_completed

from netmiko import ConnectHandler
from netmiko.ssh_exception import NetMikoAuthenticationException, NetMikoTimeoutException

"""
Below is a list of common device types with their corresponding Netmiko device type.

This is not an all inclusive list, if the device type you are looking for is not in this list, check netmiko
documentation

- Cisco IOS: cisco_ios
- Cisco IOS-XR: cisco_xr
- Cisco NXOS: cisco_nxos
- Cisco ASA: cisco_asa
- Cisco WLC: cisco_wlc
- A10: a10
- ALU SROS: alcatel_sros
"""


def collect_device_output(host, username, password, commands, ip=None, device_type=None, **kwargs):
    """
    Connect to a device and send commands specified.
    :param host: (str) FQDN of host to connect to
    :param username: (str) Username to authenticate with
    :param password: (str) Password to authenticate with
    :param commands: (list) List of commands to send to a device
    :param ip: (str) IP address of device
    :param device_type: (str) Netmiko device type needed for connecting
    :return: (dict)
    """
    # Assertions to verify correct arguments have been passed to the device
    assert device_type
    assert isinstance(commands, list)
    # Create dictionary that will hold results for parsing later.
    result = dict(
            host=host,
            error=None,
            output=[]
            )
    # Try/except block to catch an error if they occur.
    print("Connecting to %s" % host)
    try:
        with ConnectHandler(ip=ip, host=host, username=username, password=password,
                            device_type=device_type, **kwargs) as conn:
            # Iterate through command list and append output to results dictionary
            for cmd in commands:
                output = conn.send_command(cmd)
                result["output"].append({
                    "command": cmd,
                    "output": output
                    })
    except NetMikoAuthenticationException:
        result["error"] = "Unable to authenticate"
    except NetMikoTimeoutException:
        result["error"] = "Connection to device timed out"
    except Exception as exc:
        print("An error occurred connecting to %s - %r" % (host, exc))
        result["error"] = str(exc)
    # If no output and no error generated, define an error for no output
    if not result["error"] and not result["output"]:
        result["error"] = "No output from device"
    return result


def parse_host_file(hostfile):
    # Verify hostfile is of a support file type
    assert hostfile.endswith("txt") or hostfile.endswith("csv")
    # Open the host file with context manager
    with open(hostfile) as f:
        # Parse hostfile based off file type
        if hostfile.endswith("txt"):
            hostlist = f.read().splitlines(keepends=False)
        else:
            hostlist = csv.DictReader(f)
    return hostlist


# noinspection SqlDialectInspection
def run_many_commands_on_many_server_to_get_results(hostfile, threads, username, password, device_type, commands, filename):
    hostlist = parse_host_file(hostfile)
    all_results = []
    print("""
    Starting network audit script
    Device count: %d
    Threads: %d
    Device type: %s
    Commands: %s
    Output file: %s
    """ % (len(hostlist), threads, device_type, ', '.join(commands), filename))
    # Start up thread pool to process each device
    with ThreadPoolExecutor(max_workers=threads) as e:
        # Create iterator over hostlist based off host list data
        if isinstance(hostlist[0], str):
            futures = {e.submit(collect_device_output, h, username, password, commands, device_type=device_type):
                           h for h in hostlist}
        else:
            futures = {e.submit(collect_device_output, h['host'], username, password, commands,
                                device_type=device_type, ip=h['ip']): h for h in hostlist}
        # Iterate through all future objects as they return
        for fut in as_completed(futures):
            # Get the host that was called
            host = futures[fut]
            try:
                # Attempt to get the results from the call to 'collect_device_output'
                result = fut.result()
                all_results.append(result)
            except Exception as exc:
                # If an uncaught exception occurred, add the exception to the result data with host
                all_results.append(dict(
                        host=host,
                        error=str(exc),
                        output=[],
                        ))
    # Generate CSV file with device output
    with open(filename, "w", newline="") as f:
        wr = csv.writer(f)
        wr.writerow(["host", "error", "command", "output"])
        for h in all_results:
            if h["error"]:
                wr.writerow([h["host"], h["error"]])
                continue
            for o in h["output"]:
                wr.writerow([h["host"], "", o["command"], o["output"]])
    print("All hosts completed!")


if __name__ == "__main__":
    # Set up command line arguments
    parser = argparse.ArgumentParser(description="Run a list of commands across multiple network devices "
                                                 "and write the output to a CSV")
    parser.add_argument("hostfile", metavar="Host file", help="The txt file containing all hosts to be executed")
    parser.add_argument("-t", "--threads", type=int, help="Number of threads to use for this script", default=5)
    parser.add_argument("-u", "--username", help="Your NT username", required=True)
    parser.add_argument("-p", "--password", help="Your NT password", required=True)
    parser.add_argument("-d", "--device-type", help="Type of device to connect to", required=True)
    parser.add_argument("-c", "--commands", action="append", help="commands to be sent to device", required=True)
    parser.add_argument("-f", "--filename", help="File name for output", default="network-audit.csv")
    args = parser.parse_args()
    # Execute main script
    run_many_commands_on_many_server_to_get_results(args.hostfile, args.threads, args.username, args.password, args.device_type, args.commands, args.filename)
