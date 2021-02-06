import subprocess

def status():
    # need to make this it's own module if I start
    # digging in here for more lines other than status
    result = subprocess.run(['cmus-remote', '-Q'], stdout=subprocess.PIPE)
    result = result.stdout.decode('utf-8')
    result_lines = result.splitlines()
    status = result_lines[0].split("status ")[1]
    return status

def pause():
    subprocess.call(['cmus-remote', '-U'])

def play():
    subprocess.call(['cmus-remote', '-p'])

def raw_command(text):
    """
    Equivalent to entering command into focused cmus.
    For testing/example purposes only - Do not let users pass 
    text to this function.
    """
    subprocess.call(['cmus-remote', '-C', f'{text}'])
