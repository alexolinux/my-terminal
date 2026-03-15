#!/usr/bin/env bash

# Helper to get tmux options
get_tmux_option() {
    local option=$1
    local default_value=$2
    local option_value=$(tmux show-option -gqv "$option")
    if [ -z "$option_value" ]; then
        echo "$default_value"
    else
        echo "$option_value"
    fi
}

# Find resurrect/snapshot directory
if [ -d "$HOME/.tmux/resurrect" ]; then
    DEFAULT_DIR="$HOME/.tmux/resurrect"
else
    DEFAULT_DIR="${XDG_DATA_HOME:-$HOME/.local/share}"/tmux/resurrect
fi

RESURRECT_DIR=$(get_tmux_option "@resurrect-dir" "$DEFAULT_DIR")
SNAPSHOT_DIR=$(get_tmux_option "@named-snapshot-dir" "$RESURRECT_DIR")

# List symlinks (named snapshots) and use fzf-tmux to pick one
# Filters out 'last' which is used by standard resurrect
choice=$(find "$SNAPSHOT_DIR" -maxdepth 1 -type l ! -name "last" -printf "%f\n" | fzf-tmux -p 60%,40% --header="Select Tmux Snapshot to Restore")

if [ -n "$choice" ]; then
    # Use the existing plugin script to restore the selected snapshot
    # This ensures consistency with symlink handling logic
    bash "$HOME/.tmux/plugins/tmux-named-snapshot/scripts/restore-snapshot.sh" "$choice"
fi
