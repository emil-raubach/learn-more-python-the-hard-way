from fsm_class import FSMSocket

# basically stealing Zed's test to help get unstuck...
def test_basic_connection():
    fsm = FSMSocket()
    script = ["connect", "accept", "read", "read", "write", "close", "connect"]

    for event in script:
        print(event, ">>>", fsm)
        fsm.handle(event)