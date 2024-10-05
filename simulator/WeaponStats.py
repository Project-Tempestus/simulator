from dataclasses import dataclass

_BASE_BURST = 3
_BASE_DMG = 20
_BASE_CLIP_CAPACITY = 10
_BASE_RELOAD = 1


@dataclass
class WeaponStats:
    burst: int = _BASE_BURST
    dmg: int = _BASE_DMG
    clip_capacity: int = _BASE_CLIP_CAPACITY
    clip_current: int = _BASE_CLIP_CAPACITY
    time_reload: int = _BASE_RELOAD
