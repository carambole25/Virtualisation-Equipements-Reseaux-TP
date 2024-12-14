import subprocess
import re
import time

def run_cmd(cmd):
    return subprocess.check_output(cmd, shell=True).decode('utf-8')

def get_non_permanent_lines(arp_tables):
    return [i for i in arp_tables.splitlines() if "PERMANENT" not in i]

def make_it_permanent(non_permanent_lines):
    for line in non_permanent_lines:
        ip = line.split()[0]
        mac = line.split()[4]
        run_cmd(f"ip neigh replace {ip} lladdr {mac} dev enp0s3 nud perm")

while True:
    arp_tables = run_cmd('ip n')
    non_permanent_lines = get_non_permanent_lines(arp_tables)
    make_it_permanent(non_permanent_lines)
    time.sleep(10)