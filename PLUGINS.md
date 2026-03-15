# TMUX Plugins Guide

This document explains the plugins used in the provided `tmux.conf` and how to use them effectively. All plugins are installed via **TPM (Tmux Plugin Manager)**.

## Plugin Manager

### tmux-plugins/tpm

Repository: https://github.com/tmux-plugins/tpm

#### Purpose of TPM

TPM is the **plugin manager for tmux**. It installs, updates, and removes plugins automatically.

#### Install Plugins

TPM installs **all plugins listed in your `~/.tmux.conf`** under `set -g @plugin ...`.

For more details about my Tmux Plugins, check **[Plugins Document](PLUGINS.md)**

To add your plugins:

1. Add a line like:

```tmux
set -g @plugin 'github_user/your-plugin'
```

2. Reload tmux config:

```shell
Ctrl + a r
```

*Wait for a few seconds. Tmux will display a promt to confirm the reload.*

3. Install the plugin:

```shell
Ctrl + a I
```

This will clone each plugin into `~/.tmux/plugins/` and load it immediately.

To remove a plugin, delete the `set -g @plugin ...` line from your config and run:

```shell
Ctrl + a Alt + u
```

#### Update Plugins

```shell
Ctrl + a U
```

#### Remove Unused Plugins

Remove the plugin from `.tmux.conf`, then run:

```shell
Ctrl + a Alt + u
```

### Sensible Defaults

### tmux-plugins/tmux-sensible

Repository: https://github.com/tmux-plugins/tmux-sensible

#### Purpose of tmux-sensible

Provides **safe default settings** for tmux such as:

* improved key repeat handling
* better pane navigation defaults
* optimized terminal behavior

#### How to Use tmux-sensible

No manual interaction is required.
It simply applies best-practice defaults automatically.

### Session Persistence

### tmux-plugins/tmux-resurrect

Repository: https://github.com/tmux-plugins/tmux-resurrect

#### Purpose of tmux-resurrect

Restores tmux sessions after:

* system reboot
* terminal crash
* tmux restart

It saves:

* windows
* panes
* commands running in panes
* working directories

### Save Session

```shell
Ctrl + a Ctrl + s
```

### Restore Session

```shell
Ctrl + a Ctrl + r
```

Session data is stored in:

```shell
~/.tmux/resurrect/
```

### tmux-plugins/tmux-continuum

Repository: https://github.com/tmux-plugins/tmux-continuum

#### Purpose of tmux-continuum

Adds **automatic session saving and restoring** on top of `tmux-resurrect`.

Features:

* autosaves every 15 minutes
* restores tmux automatically when the system boots

#### How to Use tmux-continuum

No manual interaction required.

Just ensure:

```shell
tmux-resurrect
tmux-continuum
```

are both enabled.

### spywhere/tmux-named-snapshot

Repository: https://github.com/spywhere/tmux-named-snapshot

#### Purpose of tmux-named-snapshot

Allows saving **multiple named snapshots** of tmux sessions.

Useful for:

* switching between project layouts
* saving different workspace states

#### Save Snapshot

```shell
Prefix + Ctrl-s
```

Then type a snapshot name.

Example:

```shell
backend-dev
```

#### Restore Snapshot

```shell
Prefix + Ctrl-l
```

Choose a snapshot to restore.

## Clipboard

### tmux-plugins/tmux-yank

Repository: https://github.com/tmux-plugins/tmux-yank

#### Purpose of tmux-yank

Provides **cross-platform clipboard integration** for tmux.

Works with:

* `xclip`
* `xsel`
* `pbcopy`
* `wl-copy`

#### How to Use tmux-yank

Enter copy mode:

```shell
Ctrl + a M
```

Select text using **vim movement keys**, then press:

```shell
y
```

The text will automatically be copied to the **system clipboard**.

## Searching

### tmux-plugins/tmux-copycat

Repository: https://github.com/tmux-plugins/tmux-copycat

#### Purpose of tmux-copycat

Adds powerful **regex search inside tmux history**.

You can quickly jump to:

* URLs
* IP addresses
* Git SHAs
* file paths
* numbers

#### How to Use tmux-copycat

Start a search:

```shell
Prefix + /
```

Choose a pattern:

Example:

```shell
url
ip
sha
```

Then navigate through matches.

## Network Monitoring

### xamut/tmux-network-bandwidth

Repository: https://github.com/xamut/tmux-network-bandwidth

#### Purpose of tmux-network-bandwidth

Displays **current network upload and download speed** in the tmux status bar.

Example display:

```shell
Network ↓1.2MB/s ↑350KB/s
```

#### How to Use tmux-network-bandwidth

No interaction required.

The plugin automatically updates the status bar variable:

```shell
#{network_bandwidth}
```

## CPU Monitoring

### tmux-plugins/tmux-cpu

Repository: https://github.com/tmux-plugins/tmux-cpu

#### Purpose of tmux-cpu

Shows **CPU usage statistics** in the tmux status bar.

Displayed information:

* CPU load
* CPU percentage
* CPU icon indicator

#### Status Bar Variables

```shell
#{cpu_percentage}
#{cpu_icon}
#{cpu_bg_color}
```

#### How to Use tmux-cpu

No manual interaction required.

## UI Utilities

### jaclu/tmux-menus

Repository: https://github.com/jaclu/tmux-menus

#### Purpose of tmux-menus

Adds **popup menus** inside tmux for easier interaction.

Menus allow:

* pane actions
* session management
* window control

#### Open Menu

Right-click inside a pane.

#### Menu Features

* rename windows
* close panes
* resize panes
* create splits
* switch sessions

## Scroll Improvements

### noscript/tmux-mighty-scroll

Repository: https://github.com/noscript/tmux-mighty-scroll

#### Purpose of noscript/tmux-mighty-scroll

Improves **mouse scrolling behavior** inside tmux.

Benefits:

* smooth scrolling
* better history navigation
* improved mouse wheel handling

#### How to Use noscript/tmux-mighty-scroll

Simply scroll with the mouse wheel.

The plugin automatically:

* enters copy mode when scrolling
* allows scrolling through pane history

## Troubleshooting

### Plugins not installing

Run:

```shell
Ctrl + a I
```

If the plugin directory is missing:

```shell
~/.tmux/plugins/
```

install TPM again.

### Plugin logs

Check logs:

```shell
~/.tmux/plugins/
```

or restart tmux:

```shell
tmux kill-server
```

## Recommended Workflow

Typical daily workflow:

1. Start tmux

```shell
tmux new -s work
```

2. Split panes and start tools.

3. Work normally.

4. Session is **automatically saved** by `tmux-continuum`.

5. After reboot, reopen tmux and the workspace returns automatically.

## Summary

This plugin set provides:

* automatic workspace persistence
* clipboard integration
* status monitoring
* powerful search
* better scrolling
* popup menus
* plugin management

Together they create a **stable and productive terminal environment**.
