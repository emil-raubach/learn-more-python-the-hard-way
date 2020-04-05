import sh
from unittest.mock import patch


def test_parse_input():
    result = sh.parse_input(lambda: 'ls -l')
    assert result == ['ls', '-l']


@patch('subprocess.run')
def test_run_command(mocked_subprocess):
    parsed_in_str = sh.parse_input(lambda: 'ls -l')
    mocked_subprocess.run.return_value = ''  # mock CompletedProcess object?
    mocked_subprocess.run(parsed_in_str)
    mocked_subprocess.run.assert_called_with(['ls', '-l'])


@patch('sys.exit')
@patch('subprocess.run')
def test_run_process(mocked_subprocess, sys_exit):
    _ = sh.run_process(['exit'])
    assert sys_exit.called
