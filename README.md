# my-terminal

-------------

This is my favorite terminal multiplexer configuration using `tmux`.

## ⁉️ What is tmux?

[Tmux (terminal multiplexer)](https://github.com/tmux/tmux/wiki) is a tool that lets you run multiple terminal sessions in one window. 

Key features:

- Split screen into panes/windows
- Persistent sessions (survive SSH disconnects)
- Efficient navigation (keyboard/mouse)
- Plugins and status bar customization

Perfect for developers, sysadmins, and remote CLI work.

## ⚡ My Custom TMUX Environment

This repository contains a **productivity-focused tmux configuration** designed for sysadmins/devs working with terminal multiplexing, remote sessions, and CLI workflows.

The configuration emphasizes:

- Fast navigation
- Mouse + keyboard compatibility
- Clipboard integration
- Persistent sessions
- Lightweight status monitoring
- Plugin extensibility

## Installation

### 1 Install tmux

RHEL-based distros

```shell
sudo dnf install tmux
```

Ubuntu / Debian

```shell
sudo apt install tmux
```

Arch

```shell
sudo pacman -S tmux
```

Mac (brew)

```shell
brew install tmux
```

### 2 Install TPM (Plugin Manager)

To take advantage of the available tmux plugins, we first need to install TPM.

```shell
mkdir -p ~/.tmux/plugins
git clone https://github.com/tmux-plugins/tpm ~/.tmux/plugins/tpm
```

### 3 My Tmux Configuration

[tmux.conf](./conf/tmux.conf)

```shell
cp ./conf/tmux.conf ~/.tmux.conf
```

Reload the configuration (if you are using tmux (already active)):

```shell
Ctrl+a r
```

### 4 My installed plugins

These are my favorite tmux plugins. For more details about my Tmux plugins, please refer to **[Plugins Document](PLUGINS.md)**

Feel free to find tmux plugins that suit your needs here: <https://github.com/tmux-plugins>

#### Install the plugins

1. Start tmux (or reload your config):

```shell
# start a new tmux session (or attach to an existing one)
tmux new -s mysession

# (inside tmux) reload config
Ctrl+a r
```

2. Install all configured plugins via TPM:

```shell
# inside tmux
Ctrl+a I
```

3. Verify plugins are installed by checking the plugin directory:

```shell
ls ~/.tmux/plugins
```

> ✅ This installs **all** plugins configured in your `~/.tmux.conf` at once.

If you prefer installing plugins from the shell (outside tmux), you can run:

```shell
~/.tmux/plugins/tpm/bin/install_plugins
```

#### Plugins Included

| Plugin | Purpose |
| --- | --- |
| tmux-sensible | Sensible defaults |
| tmux-resurrect | Restore sessions |
| tmux-continuum | Automatic saving |
| tmux-yank | Clipboard integration |
| tmux-copycat | Regex search |
| tmux-network-bandwidth | Network monitoring |
| tmux-cpu | CPU usage indicator |
| tmux-mighty-scroll | Improved scroll behavior |
| tmux-menus | Popup menus |

## Status Bar

The status bar displays:

- Hostname
- Session
- Window
- Current directory
- Network bandwidth
- CPU usage
- Current time

### TMUX Customization

Inside tmux, press the following to install plugins:

```shell
Ctrl+a I
```

TPM will install all configured plugins.

## Prefix Key

The prefix key is:

```shell
Ctrl+a
```

Example usage:

```shell
Ctrl+a | split pane
Ctrl+a h move left
Ctrl+a z zoom pane
```

## Keybindings

### Pane Management

| Key | Action |
| --- | --- |
| Ctrl+a \| | Split horizontally |
| Ctrl+a _ | Split vertically |
| Ctrl+a h | Move left |
| Ctrl+a j | Move down |
| Ctrl+a k | Move up |
| Ctrl+a l | Move right |

### Resize Panes

| Key | Action |
| --- | --- |
| Alt + ← | Resize left |
| Alt + → | Resize right |
| Alt + ↑ | Resize up |
| Alt + ↓ | Resize down |

### Pane Utilities

| Key | Action |
| --- | --- |
| Ctrl+a z | Toggle pane zoom |
| Ctrl+a b | Toggle synchronized input |
| Ctrl+a K | Kill pane |

### Session Control

| Key | Action |
| --- | --- |
| Ctrl+a X | Kill tmux server |
| Ctrl+a r | Reload configuration |

### Copy Mode

Enter copy mode:

```shell
Ctrl+a M
```

Navigation uses **vim-style keys**.

Clipboard shortcuts:

```shell
Ctrl+Shift+C copy
Ctrl+Shift+V paste
```

## Mouse Features

Mouse support is enabled.

Toggle mouse mode:

```shell
Ctrl+a v
```

Mouse allows:

- pane resizing
- pane switching
- scrolling


## Performance Improvements

This configuration includes optimizations:

- reduced status refresh overhead
- native path rendering (no shell calls)
- modern `tmux-256color` terminal support
- truecolor support for editors like Neovim

## Useful tmux Commands

Create a session

```shell
tmux new -s dev
```

Attach session

```shell
tmux attach -t dev
```

List sessions

```shell
tmux ls
```

## 🔳 Recommended Terminal

My favourite terminals are:

- [Alacritty](https://alacritty.org/index.html)
- [Tilix](https://gnunn1.github.io/tilix-web/?ref=itsfoss.com)

In addition to these, there are more options if you want other alternatives:

Linux Native:

- [Gnome Terminal](https://help.gnome.org/gnome-terminal/)
- [KDE Terminal](https://apps.kde.org/en-gb/konsole/)

Additional Terminals:

- [Terminator](https://gnome-terminator.org/)
- [ghostty](https://ghostty.org/)
- [Kitty](https://sw.kovidgoyal.net/kitty/)
- [Tabby](https://tabby.sh/)
- [WezTerm](https://wezterm.org/)

Extra AI Terminals:

- [Warp](https://www.warp.dev/)
- [Wave](https://www.waveterm.dev/)

## ![Alacritty](https://alacritty.org/alacritty-simple.svg)My Alacritty Configuration

My Allacritty configuration is based on:

[alacritty.toml](./conf/alacritty.toml)

Optimized configuration for Alacritty terminal emulator:

- **Font**: JetBrains Mono (size 14) with box drawing support
- **Colors**: Cyberpunk neon theme (truecolor enabled)
- **Keybindings**: Ctrl+Shift+C/V for copy/paste, Ctrl+F/B for search, Ctrl+=/- font size
- **Features**: Live config reload (Ctrl+Shift+R), mouse support, dynamic padding, high scroll history (65k lines)
- **Performance**: Opacity 0.97, buttonless decorations, semantic URL/selection handling

```shell
cp conf/alacritty.toml ~/.config/alacritty/alacritty.toml
```

Reload Alacritty or restart for changes to take effect.

## Author

<https://alexolinux.com>
