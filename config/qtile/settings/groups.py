from libqtile.config import Key, Group
from libqtile.command import lazy
from .keys import mod, keys

groups = [Group(i) for i in [
    " "," "," "," ","阮"," "," "," "," "
    ]]

for i, group in enumerate(groups):
    actual_key = str(i + 1)
    keys.extend([Key(key[0], key[1], *key[2:]) for key in [
        ([mod], actual_key, lazy.group[group.name].toscreen()),
        ([mod, "shift"], actual_key, lazy.window.togroup(group.name))
    ]])

