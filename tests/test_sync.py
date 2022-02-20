from unittest.mock import Mock

import pytest

from dennisync.sync import Actor, AdvertiseMessage, RequestMessage


def always_newer(_table, _name, _timestamp):
    return True


@pytest.fixture
def con():
    peer_connection = Mock()
    peer_connection.send = Mock()
    return peer_connection


def test_request(con):
    a = Actor(print, always_newer)
    msg = AdvertiseMessage("users", "Sam", "now")

    a.on_message(con, msg)

    assert con.send.call_args == ((RequestMessage("users", "Sam"),),)
