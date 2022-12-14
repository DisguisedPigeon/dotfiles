from libqtile.config import Key, KeyChord
from libqtile.command import lazy


mod = "mod4"
terminal = "kitty"
browser = "firefox"
file_manager = "pcmanfm"
# Rofi_theme
rofi_theme = "catppuccin-macchiato"

app_launcher = f"rofi -combi-modi window,drun,ssh\
 -theme {rofi_theme} -font 'hack 10' -show combi -show-icons"
screenshot = "scrot 'Arch-%y-%m-%d-%s.jpg' -e 'mv $f ~/Imágenes/screenshots'"

raise_volume = "amixer set Master 5%+"
lower_volume = "amixer set Master 5%-"

# Keybindings
keys = [Key(key[0], key[1], *key[2:]) for key in [
    # Basic movement
    ([mod], "j", lazy.layout.down()),
    ([mod], "k", lazy.layout.up()),
    ([mod], "h", lazy.layout.left()),
    ([mod], "l", lazy.layout.right()),

    # Change window positions
    ([mod, "shift"], "h", lazy.layout.shuffle_left()),
    ([mod, "shift"], "l", lazy.layout.shuffle_right()),
    ([mod, "shift"], "j", lazy.layout.shuffle_down()),
    ([mod, "shift"], "k", lazy.layout.shuffle_up()),
    ([mod], "Tab", lazy.next_layout()),

    # Qtile interactions
    ([mod], "w", lazy.window.kill()),
    ([mod, "control"], "r", lazy.reload_config()),
    ([mod, "control"], "q", lazy.shutdown()),
    ([mod, "control"], "t", lazy.window.toggle_floating()),
    ([mod, "control"], "x", lazy.spawn("reboot")),

    # Launch apps
    ([mod], "Return", lazy.spawn(terminal)),
    ([mod], "b", lazy.spawn(browser)),
    ([mod], "f", lazy.spawn(file_manager)),
    ([mod], "r", lazy.spawn(app_launcher)),
    ([mod], "v", lazy.spawn(f"{terminal} nvim")),

    # Other actions
    ([], "Print", lazy.spawn(screenshot)),
    ([], "XF86AudioRaiseVolume", lazy.spawn(raise_volume)),
    ([], "XF86AudioLowerVolume", lazy.spawn(lower_volume)),

    ]]

# KeyChords
keys.extend([
    KeyChord(key[0], key[1], key[2], mode=True, name=name)
    for name, key in [
        # Resize
        ("Resize", ([mod, "shift"], "r", [Key(key[0], key[1], *key[2:]) for key in [
            # Actions
            ([], "a", lazy.layout.grow()),
            ([], "d", lazy.layout.shrink()),
            ([], "s", lazy.layout.normalize()),
            ([], "w", lazy.layout.maximize()),

            # Movement in resize mode
            ([], "h", lazy.layout.left()),
            ([], "l", lazy.layout.right()),
            ([], "j", lazy.layout.down()),
            ([], "k", lazy.layout.up()),
        ]])),
        ("Power", ([mod, "control"], "p", [Key(key[0], key[1], *key[2:]) for key in [
            # Actions
            ([], "s", lazy.spawn("shutdown now")),
            ([], "r", lazy.spawn("reboot"))
        ]]))
    ]
])
