#!/usr/bin/env python3

import sys

class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    RESET = '\033[0m'
    BOLD = '\033[1m'

bindings = [
    ("tmux", "Ctrl + a", "Prefix Key"),
    ("tmux", "Prefix + v", "Toggle Mouse (enabled/disabled)"),
    ("tmux", "Ctrl + Shift + c", "Copy to system clipboard"),
    ("tmux", "Ctrl + Shift + v", "Paste from system clipboard"),
    ("tmux", "Prefix + M", "Enter copy mode (vi keys)"),
    ("tmux", "Prefix + b", "Synchronize panes (toggle)"),
    ("tmux", "Prefix + z", "zoom current pane (toggle)"),
    ("tmux", "Prefix + |", "Split window horizontally"),
    ("tmux", "Prefix + _", "Split window vertically"),
    ("tmux", "Alt + Arrows", "Resize panes (Left/Right/Up/Down)"),
    ("tmux", "Prefix + h/j/k/l", "Select panes (Left/Down/Up/Right)"),
    ("tmux", "Prefix + K", "Kill current pane"),
    ("tmux", "Prefix + X", "Kill all sessions"),
    ("tmux", "Prefix + r", "Reload tmux configuration"),
    ("tpm", "Prefix + I", "Install plugins"),
    ("tpm", "Prefix + U", "Update plugins"),
    ("tpm", "Prefix + Alt + u", "Remove unused plugins"),
    ("tmux-resurrect", "Prefix + Ctrl + s", "Save session"),
    ("tmux-resurrect", "Prefix + Ctrl + r", "Restore session"),
    ("tmux-named-snapshot", "Prefix + S", "Save a named snapshot"),
    ("tmux-named-snapshot", "Prefix + R", "Restore a named snapshot"),
    ("tmux-named-snapshot", "Prefix + g", "List and restore snapshots (FZF)"),
    ("tmux-yank", "y (in copy mode)", "Copy selection to system clipboard"),
    ("tmux-menus", "Right-click", "Open interactive popup menu"),
]

def print_table():
    print(f"\n{Colors.BOLD}{Colors.CYAN}╭──────────────────────────────────────────────────╮{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.CYAN}│              Tmux BindKeys Cheat Sheet           │{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.CYAN}╰──────────────────────────────────────────────────╯{Colors.RESET}\n")
    
    col_scope_width = max(len(b[0]) for b in bindings) + 2
    col_bind_width = max(len(b[1]) for b in bindings) + 2
    col_desc_width = max(len(b[2]) for b in bindings) + 2

    # Table drawing characters
    top_border = f"┌{'─' * (col_scope_width + 2)}┬{'─' * (col_bind_width + 2)}┬{'─' * (col_desc_width + 2)}┐"
    header_sep = f"├{'─' * (col_scope_width + 2)}┼{'─' * (col_bind_width + 2)}┼{'─' * (col_desc_width + 2)}┤"
    bot_border = f"└{'─' * (col_scope_width + 2)}┴{'─' * (col_bind_width + 2)}┴{'─' * (col_desc_width + 2)}┘"

    # Header
    header = f"│ {Colors.BOLD}{'Scope'.ljust(col_scope_width)}{Colors.RESET} │ {Colors.BOLD}{'BindKeys'.ljust(col_bind_width)}{Colors.RESET} │ {Colors.BOLD}{'Description'.ljust(col_desc_width)}{Colors.RESET} │"
    
    print(top_border)
    print(header)
    print(header_sep)

    for scope, bind, desc in bindings:
        if scope == "tmux":
            scope_str = f"{Colors.GREEN}{scope.ljust(col_scope_width)}{Colors.RESET}"
        elif scope == "tpm":
            scope_str = f"{Colors.YELLOW}{scope.ljust(col_scope_width)}{Colors.RESET}"
        else:
            scope_str = f"{Colors.BLUE}{scope.ljust(col_scope_width)}{Colors.RESET}"
            
        bind_str = f"{Colors.HEADER}{bind.ljust(col_bind_width)}{Colors.RESET}"
        desc_str = f"{desc.ljust(col_desc_width)}"
        
        row = f"│ {scope_str} │ {bind_str} │ {desc_str} │"
        print(row)
        
    print(bot_border)
    print()

if __name__ == '__main__':
    print_table()
