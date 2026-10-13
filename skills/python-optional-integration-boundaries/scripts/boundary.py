"""Synthetic optional boundary; no provider or concrete SDK dependency."""
from importlib import import_module
from collections.abc import Mapping
from typing import Protocol, cast

class Client(Protocol):
    def fetch(self) -> object: ...

def build(module: str = "draft_optional_sdk") -> Client | None:
    try:
        sdk = import_module(module)
    except ModuleNotFoundError as exc:
        if exc.name == module:
            return None
        raise
    factory = getattr(sdk, "Client")
    if not callable(factory):
        raise TypeError("factory must be callable")
    client = factory()
    if not callable(getattr(client, "fetch", None)):
        raise TypeError("client must expose fetch")
    return cast(Client, client)

def normalize(value: object) -> dict[str, object]:
    if not isinstance(value, Mapping) or not all(isinstance(k, str) for k in value):
        raise TypeError("expected string-key mapping")
    result: dict[str, object] = dict(value)
    items = result.get("items")
    if not isinstance(items, list) or not all(isinstance(x, str) for x in items):
        raise TypeError("expected string items")
    return result
