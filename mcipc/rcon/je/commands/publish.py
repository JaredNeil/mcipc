"""Implementation of the publish command."""

from mcipc.rcon.proto import Client


__all__ = ['publish']


def publish(self: Client, port: int) -> str:
    """Opens singleplayer world to the local network."""

    return self.run('publish', port)
