from hexd mp import *
import subprocess

def test_hex_plus_ascii():
    output = b'00000000  48 65 6c 6c 6f 20 54 68  65 72 65 0a              |Hello There.|\n0000000c\n'
    cmd = subprocess.Popen(('echo', 'Hello There'), stdout=subprocess.PIPE)
    out = subprocess.check_output(('hexdump', '-C'), stdin=cmd.stdout)
    assert out == output