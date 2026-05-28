class MoveResponse:
    OK      = "MOVE_OK"
    BARRIER = "HIT_BARRIER"


class SetStateResponse:
    OK       = "STATE_OK"
    NO_WATER = "OUT_OF_WATER"
    NO_SOAP  = "OUT_OF_SOAP"


# единый "успех" — удобно сравнивать в монаде
OK = "OK"


def is_ok(response):
    # любой код, начинающийся с *_OK, считаем успехом
    return response.endswith("_OK") or response == OK