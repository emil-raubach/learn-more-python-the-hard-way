import fsm


# basically stealing Zed's test to help get unstuck...
def test_basic_connection():
    state = fsm.START()
    script = ["connect", "accept", "read", "read", "write", "close", "connect"]

    print()
    for event in script:
        print(event, ">>>", state)
        state = state(event)
