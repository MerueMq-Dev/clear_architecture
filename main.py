import public_api.robot_api_stateless as api

def main() -> None:
    state = api.initial_state()
    state = api.set_mode("soap", state)
    state = api.start(state)
    state = api.move(100, state)
    state = api.turn(90, state)
    state = api.move(50, state)
    state = api.stop(state)

if __name__ == '__main__':
    main()