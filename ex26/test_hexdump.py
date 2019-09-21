from hexdmp import *
import subprocess

def test_hex_plus_ascii():
    output = b'00000000  48 65 6c 6c 6f 20 54 68  65 72 65 0a              |Hello There.|\n0000000c\n'
    cmd = subprocess.Popen(('echo', 'Hello There'), stdout=subprocess.PIPE)
    out = subprocess.check_output(('hexdump', '-C'), stdin=cmd.stdout)
    assert out == output

def test_main(): # not working 'cause my script outputs [, ], and '.
    test_string = 'Test the hexdump program.'
    output = b'0000000 54 65 73 74 20 74 68 65 20 68 65 78 64 75 6d 70\n0000010 20 70 72 6f 67 72 61 6d 2e 0a                  \n000001a\n'
    cmd = subprocess.Popen(('echo', test_string), stdout=subprocess.PIPE)
    out = subprocess.check_output(("./hexdmp.py"), stdin=cmd.stdout)
    assert out == output