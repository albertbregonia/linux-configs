from typing import List  # noqa: F401
from libqtile import bar, layout, widget, qtile
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy

mod = 'mod4'
keys = [ #https://docs.qtile.org/en/latest/manual/config/lazy.html commands
    # Switch between windows
    Key([mod], 'h', lazy.layout.left(), desc='Move focus to left'),
    Key([mod], 'l', lazy.layout.right(), desc='Move focus to right'),
    Key([mod], 'j', lazy.layout.down(), desc='Move focus down'),
    Key([mod], 'k', lazy.layout.up(), desc='Move focus up'),
    Key(['mod1'], 'Tab', lazy.layout.next(), desc='Move window focus to other window'),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, 'shift'], 'h', lazy.layout.shuffle_left(), desc='Move window to the left'),
    Key([mod, 'shift'], 'l', lazy.layout.shuffle_right(), desc='Move window to the right'),
    Key([mod, 'shift'], 'j', lazy.layout.shuffle_down(), desc='Move window down'),
    Key([mod, 'shift'], 'k', lazy.layout.shuffle_up(), desc='Move window up'),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, 'control'], 'h', lazy.layout.grow_left(), desc='Grow window to the left'),
    Key([mod, 'control'], 'l', lazy.layout.grow_right(), desc='Grow window to the right'),
    Key([mod, 'control'], 'j', lazy.layout.grow_down(), desc='Grow window down'),
    Key([mod, 'control'], 'k', lazy.layout.grow_up(), desc='Grow window up'),
    Key([mod], 'n', lazy.layout.normalize(), desc='Reset all window sizes'),

    # Toggle between different layouts as defined below
    Key([mod], 'Tab', lazy.next_layout(), desc='Toggle between layouts'),
    Key([mod, 'shift'], 'Tab', lazy.layout.toggle_split(), desc='Toggle maximize of the sub-stack'),
    Key([mod], 'w', lazy.window.kill(), desc='Kill focused window'),

    Key([mod, 'shift'], 'r', lazy.reload_config(), desc='Reload the config'),
    Key([mod, 'control'], 'q', lazy.shutdown(), desc='Shutdown Qtile'),
    Key([mod], 'r', lazy.spawncmd(), desc='Spawn a command using a prompt widget'),
    Key([mod], 'f', lazy.window.toggle_floating(), desc='Toggle Floating'),

    # keybinds for programs 
    Key([mod], 't', lazy.spawn('alacritty'), desc='Launch terminal'),
    Key([mod], 'c', lazy.spawn('code'), desc='Launch vscode'),
    Key([mod], 'd', lazy.spawn('discord'), desc='Launch discord'),
    Key(['mod1'], 'f', lazy.spawn('firefox'), desc='Launch firefox'),
    Key([mod], 'r', lazy.spawn('rofi -show drun'), desc='Run App Launcher')
]

mouse = [ # Drag floating layouts.
    Drag([mod], 'Button1', lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], 'Button3', lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], 'Button2', lazy.window.bring_to_front())
]

# initialize desktops
for i in [Group(i) for i in '123456789']:
    keys.extend([
        Key([mod], i.name, lazy.group[i.name].toscreen(), desc='Switch to group {}'.format(i.name)), # bring group to current monitor
        Key([mod, 'shift'], i.name, lazy.window.togroup(i.name), desc=f'Move focused window to group {i.name}'), # send focused window to group
    ])

layouts = [
    layout.Columns(
        border_focus='#D27AF0',
        border_width=1,
        margin=8,
    ),
    layout.Max(),
]

widget_defaults = dict(
    font='Noto Sans',
    fontsize=14,
    padding=5,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.TextBox(padding=0),
                widget.Image(margin=2, filename='~/.config/qtile/ph-sun.svg', mouse_callbacks={'Button1': lazy.spawn('rofi -show drun')}),
                widget.TextBox(padding=0),
                widget.AGroupBox(border=None, padding=2),

                widget.Sep(),
                widget.WindowName(max_chars=60, padding=10),

                widget.Spacer(),
                widget.Clock(format='%I:%M:%S %p %A, %b %d, %Y'),
                widget.Spacer(),

                widget.Systray(padding=10),
                widget.Sep(),
                widget.PulseVolume(padding=10),
                widget.Sep(),
                widget.CPU(),
                widget.ThermalSensor(padding=5),
                widget.Sep(),
                widget.Memory(format='RAM {MemUsed:.0f} MB/{MemTotal:.0f} MB', padding=5),
                widget.TextBox(padding=0),
            ],
            size=32,
            margin=[5, 5, 0, 5],
            background='#1C1D30', # add a string of opacity
            opacity=1,
        ),
        wallpaper='~/Wallpapers/sunset.jpg',
        wallpaper_mode='fill',
    ),
    Screen(wallpaper='~/Wallpapers/sunset.jpg', wallpaper_mode='fill'),
    Screen(wallpaper='~/Wallpapers/sunset.jpg', wallpaper_mode='fill'),
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
auto_minimize = True
wmname = 'LG3D' # fix java toolkit incompatibility
