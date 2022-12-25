from libqtile import widget
from .theme import colors

def base(fg='text', bg='dark'): 
    if not (fg in colors):
        fg = fg[:-1] + str(int(fg[-1:])-4)
    if not (bg in colors):
        bg = bg[:-1] + str(int(bg[-1:])-4)
    return {
        'foreground': colors[fg],
        'background': colors[bg]
    }


def separator():
    return widget.Sep(**base(), linewidth=0, padding=5)


def icon(fg='text', bg='dark', fontsize=16, text="?"):
    return widget.TextBox(
        **base(fg, bg),
        fontsize=fontsize,
        text=text,
        padding=3
    )


def powerline(bg="dark", fg="light", orientation="left"):
    if orientation == "left":
        return widget.TextBox(
            **base(fg, bg),
            text=" \ueb6f", # Icon: nf-oct-triangle_left
            fontsize=37,
            padding=-4
        )
    else:
        return widget.TextBox(
            **base(fg, bg),
            text="\ueb70", # Icon: nf-oct-triangle_left
            fontsize=37,
            padding=-4
        )



def workspaces(): 
    return [
        separator(),
        widget.GroupBox(
            **base(fg='light'),
            font='Hack Nerd Font',
            fontsize=19,
            margin_y=3,
            margin_x=0,
            padding_y=8,
            padding_x=5,
            borderwidth=1,
            active=colors['active'],
            block_highlight_text_color=colors['dark'],
            inactive=colors['inactive'],
            rounded=False,
            highlight_method='block',
            urgent_alert_method='block',
            urgent_border=colors['urgent'],
            this_current_screen_border=colors['focus'],
            this_screen_border=colors['grey'],
            other_current_screen_border=colors['dark'],
            other_screen_border=colors['dark'],
            disable_drag=True
        ),
        separator(),
        widget.WindowName(**base(fg='focus'), fontsize=14, padding=5),
        separator(),
    ]


primary_widgets = [
    *workspaces(),

    separator(),
    powerline('dark', 'color6'),

    widget.Chord(**base(bg='color6')),

    powerline('color6', 'color5'),

    icon(bg="color5", text=' '), # Icon: nf-fa-download
    
    widget.CheckUpdates(
        **base(bg='color5'),
        colour_have_updates=colors['text'],
        colour_no_updates=colors['text'],
        no_update_string='0',
        display_format='{updates}',
        update_interval=60,
        distro="Arch_paru"
    ),

    powerline('color5', 'color4'),

    icon(bg="color4", text=' '),  # Icon: nf-fa-feed
    
    widget.Net(**base(bg='color4'), interface='wlan0'),

    powerline('color4', 'color3'),

    widget.CurrentLayoutIcon(**base(bg='color3'), scale=0.65),

    widget.CurrentLayout(**base(bg='color3'), padding=5),

    powerline('color3', 'color2'),

    icon(bg="color2", fontsize=17, text=' '), # Icon: nf-mdi-calendar_clock

    widget.Clock(**base(bg='color2'), format='%d/%m/%Y - %H:%M '),

    powerline('color2', 'color1'),

    widget.Systray(**base(bg='color1'), padding=5),
]

secondary_widgets = [
    *workspaces(),

    separator(),
    powerline('dark', 'color6'),

    widget.Chord(**base(bg='color6')),

    powerline('color6', 'color5'),

    icon(bg="color5", text=' '), # Icon: nf-fa-download
    
    widget.CheckUpdates(
        **base(bg='color5'),
        colour_have_updates=colors['text'],
        colour_no_updates=colors['text'],
        no_update_string='0',
        display_format='{updates}',
        update_interval=60,
        distro="Arch_paru"
    ),

    powerline('color5', 'color4'),

    icon(bg="color4", text=' '),  # Icon: nf-fa-feed
    
    widget.Net(**base(bg='color4'), interface='wlan0'),

    powerline('color4', 'color3'),

    widget.CurrentLayoutIcon(**base(bg='color3'), scale=0.65),

    widget.CurrentLayout(**base(bg='color3'), padding=5),

    powerline('color3', 'color2'),

    icon(bg="color2", fontsize=17, text=' '), # Icon: nf-mdi-calendar_clock

    widget.Clock(**base(bg='color2'), format='%d/%m/%Y - %H:%M '),
]

widget_defaults = {
    'font': 'Hack Nerd Font Bold',
    'fontsize': 16,
    'padding': 1,
}
extension_defaults = widget_defaults.copy()
