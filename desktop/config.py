from typing import List  # noqa: F401
from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

mod = 'mod4'
terminal = guess_terminal()

custom_config_constants = {
    'background': '#0e0f17',
    'bar-size': 30,
    'opacity': 0.82,
    'wallpaper': '~/Wallpapers/dawn.jpg',
    'wallpaper-mode': 'fill',
}

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html

    # Switch between windows
    Key([mod], 'h', lazy.layout.left(), desc='Move focus to left'),
    Key([mod], 'l', lazy.layout.right(), desc='Move focus to right'),
    Key([mod], 'j', lazy.layout.down(), desc='Move focus down'),
    Key([mod], 'k', lazy.layout.up(), desc='Move focus up'),
    Key(['mod1'], 'Tab', lazy.layout.next(), desc='Move window focus to other window'),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, 'shift'], 'h', lazy.layout.shuffle_left(),
        desc='Move window to the left'),
    Key([mod, 'shift'], 'l', lazy.layout.shuffle_right(),
        desc='Move window to the right'),
    Key([mod, 'shift'], 'j', lazy.layout.shuffle_down(),
        desc='Move window down'),
    Key([mod, 'shift'], 'k', lazy.layout.shuffle_up(), desc='Move window up'),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, 'control'], 'h', lazy.layout.grow_left(),
        desc='Grow window to the left'),
    Key([mod, 'control'], 'l', lazy.layout.grow_right(),
        desc='Grow window to the right'),
    Key([mod, 'control'], 'j', lazy.layout.grow_down(),
        desc='Grow window down'),
    Key([mod, 'control'], 'k', lazy.layout.grow_up(), desc='Grow window up'),
    Key([mod], 'n', lazy.layout.normalize(), desc='Reset all window sizes'),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, 'shift'], 'Return', lazy.layout.toggle_split(),
        desc='Toggle between split and unsplit sides of stack'),
    Key([mod], 't', lazy.spawn(terminal), desc='Launch terminal'),

    # Toggle between different layouts as defined below
    Key([mod], 'Tab', lazy.next_layout(), desc='Toggle between layouts'),
    Key([mod], 'w', lazy.window.kill(), desc='Kill focused window'),

    Key([mod, 'shift'], 'r', lazy.reload_config(), desc='Reload the config'),
    Key([mod, 'control'], 'q', lazy.shutdown(), desc='Shutdown Qtile'),
    Key([mod], 'r', lazy.spawncmd(),
        desc='Spawn a command using a prompt widget'),
]

groups = [Group(i) for i in '123']

for i in groups:
    keys.extend([
        # mod1 + letter of group = switch to group, bring group to current monitor
        Key([mod], i.name, lazy.group[i.name].toscreen(),
            desc='Switch to group {}'.format(i.name)),

        # mod1 + shift + letter of group = move focused window to group
        Key([mod, 'shift'], i.name, lazy.window.togroup(i.name),
            desc='move focused window to group {}'.format(i.name)),
    ])

layouts = [
    layout.Columns(
        # border_focus_stack=['#d27af0', '#267dff'], 
        border_width=4,
        margin=10,
    ),
    layout.Max(),
]

widget_defaults = dict(
    font='Consolas',
    fontsize=14,
    padding=3,
)
extension_defaults = widget_defaults.copy()

bar_size = 30
margin = [10, 10, 0, 10]
screens = [
    Screen(
        top=bar.Bar(
            [
                widget.AGroupBox(margin_x=10),
                widget.QuickExit(),
                widget.CurrentLayout(),
                widget.TextBox('mid'),
                widget.Prompt(),
                widget.WindowName(),

                # widget.TextBox(text='\uE0B2', padding=0, fontsize=bar_size, foreground='#d27af0'),
                widget.Memory(format='{MemUsed:.0f}{mm}/{MemTotal:.0f}{mm}',padding=10),

                widget.Net(format='{down} ⬍ {up}', padding=10),

                widget.ThermalSensor(fmt='🌡 {}',padding=10),

                widget.PulseVolume(fmt='🕪 {}', padding=10),

                widget.Clock(format='%I:%M:%S %p %a %Y-%m-%d',padding=10),

                widget.Systray(padding=8),
                widget.TextBox(padding=12)
            ],
            bar_size,
            background=custom_config_constants['background'],
            margin=margin,
            opacity=0.85,
        ),
        wallpaper=custom_config_constants['wallpaper'],
        wallpaper_mode=custom_config_constants['wallpaper-mode'],
    ),
    Screen(
        top=bar.Bar(
            [
                widget.AGroupBox(),
                widget.CurrentLayout(),
                widget.TextBox('right'),
            ],
            bar_size,
            background=custom_config_constants['background'],
            margin=margin,
            opacity=0.85,
        ),
        wallpaper=custom_config_constants['wallpaper'],
        wallpaper_mode=custom_config_constants['wallpaper-mode'],
    ),
    Screen(
        top=bar.Bar(
            [
                widget.AGroupBox(),
                widget.CurrentLayout(),
                widget.TextBox('left'),
            ],
            bar_size,
            background=custom_config_constants['background'],
            margin=margin,
            opacity=0.85,
        ),
        wallpaper=custom_config_constants['wallpaper'],
        wallpaper_mode=custom_config_constants['wallpaper-mode'],
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], 'Button1', lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], 'Button3', lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], 'Button2', lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
])
auto_fullscreen = True
focus_on_window_activation = 'smart'
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = 'LG3D'
