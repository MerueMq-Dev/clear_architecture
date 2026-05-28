def project(events, initial):
    state = initial
    for e in events:
        if hasattr(e, 'apply'):
            state = e.apply(state)
    return state