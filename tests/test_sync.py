from unittest.mock import Mock

from dennisync.sync import Actor, AdvertiseMessage, RequestMessage


def always_newer(_table, _name, _timestamp):
    return True


def test_request():
    a = Actor(print, always_newer)
    con = Mock()
    con.send = Mock()
    msg = AdvertiseMessage("table", "name", "timestamp")

    a.on_message(con, msg)

    assert con.send.call_args.args == (RequestMessage("table", "name"),)
