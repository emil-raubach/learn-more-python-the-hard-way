from fsm_socket import FSMSocket


def test_basic_connection():
    script = ["connect", "accept", "read", "read", "write", "close", "connect"]
    fsm = FSMSocket()
    result = fsm.transduce(script)
    assert result == ['CONNECTED',
                      'ACCEPTED',
                      'READING',
                      'READING',
                      'WRITING',
                      'CLOSED',
                      'LISTENING']
