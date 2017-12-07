import re
def is_malformed(command):
    targeted_commands = r"[a-zA-V]\d+ (mov|atk|spt|inf) [a-zA-V]\d+"
    info_command = r"info [a-zA-V]\d{1,2}"
    return not(re.search(info_command, command) != None or re.search(targeted_commands, command) != None or command == "pass")
