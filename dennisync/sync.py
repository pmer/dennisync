import json
from random import randint


MSG_ADVERTISE = 0
MSG_REQUEST = 1
MSG_ENTITY = 2


class AdvertiseMessage:
    def __init__(self, table, name, timestamp):
        self.type = MSG_ADVERTISE
        self.table = table
        self.name = name
        self.timestamp = timestamp

    def __eq__(self, other):
        return (
            self.type == other.type
            and self.table == other.table
            and self.name == other.name
            and self.timestamp == other.timestamp
        )


class RequestMessage:
    def __init__(self, table, name):
        self.type = MSG_REQUEST
        self.table = table
        self.name = name

    def __eq__(self, other):
        return (
            self.type == other.type
            and self.table == other.table
            and self.name == other.name
        )


class EntityMessage:
    def __init__(self, table, entity):
        self.type = MSG_ENTITY
        self.table = table
        self.entity = entity

    def __eq__(self, other):
        return (
            self.type == other.type
            and self.table == other.table
            and self.entity == other.entity
        )


class Actor:
    def __init__(self, log, is_newer):
        self.connections = set()
        self.log = log
        self.is_newer = is_newer

    def on_connect(self, con):
        # TODO: Start communication, but gossip.
        self.connections.add(con)

    def on_disconnect(self, con):
        self.connections.remove(con)

    def on_message(self, con, msg):
        # TODO: Message validation. raise?
        if msg.type == MSG_ADVERTISE:
            self._on_message_advertise(con, msg)
        elif msg.type == MSG_REQUEST:
            self._on_message_request(msg)
        elif msg.type == MSG_ENTITY:
            self._on_message_entity(msg)

    def _on_message_advertise(self, con, msg):
        self.log("on_message_advertise")
        if self.is_newer(msg.table, msg.name, msg.timestamp):
            Actor._send_request(con, msg.table, msg.name)

    def _on_message_request(self, _msg):
        self.log("on_message_request")

    def _on_message_entity(self, _msg):
        self.log("on_message_entity")

    # TODO: Scheduling? Queueing (and memory)?
    @staticmethod
    def _send_request(con, table, name):
        msg = RequestMessage(table, name)
        con.send(msg)


class PeerConnection:
    def __init__(self):
        self.receiver = None

    def send(self, msg):
        pass

    def recv(self, msg):
        if self.receiver:
            # TODO: Parse/decode mesage. try/catch
            self.receiver.on_message(self, msg)


# Test stub
class CommonEntity:
    def __init__(self):
        self.name = randint(0, 2**30)


# Test stub
class Entity:
    def __init__(self):
        self._name = None
        self._timestamp = None

    def name(self):
        return self._name

    def timestamp(self):
        return self._timestamp

    def to_bytes(self):
        return bytes(json.dumps(self))

    @staticmethod
    def from_bytes(bs):
        obj = json.loads(bs.decode("utf-8"))
        entity = Entity()
        entity._name = obj["name"]
        entity._timestamp = obj["timestamp"]
        return entity

    @staticmethod
    def from_template(common):
        entity = Entity()
        entity._name = common.name
        entity._timestamp = randint(0, 2**30)
        return entity


# Testing
def always_newer(_table, _name, _timestamp):
    return True


class Simulation:
    def __init__(self, n_commons, n_entities, n_actors):
        commons = [CommonEntity() for _ in range(n_commons)]

        self.actors = []
        for _ in range(n_actors):
            # Unique set of integers.
            indicies = {randint(0, n_commons - 1) for _ in range(n_entities)}

            # Subset of commons (no duplicates).
            # Each entity stands at a different version (last modified time).
            _entities = [Entity.from_template(commons[i]) for i in indicies]

            a = Actor(print, always_newer)
            self.actors.append(a)

    def run(self):
        pass
