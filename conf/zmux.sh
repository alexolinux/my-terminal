mux() {
  local created=()
  local existed=()
  for s in RASPBERRY OCI DEVOPS; do
    if tmux has-session -t "$s" 2>/dev/null; then
      existed+=("$s")
    else
      tmux new-session -d -s "$s" -t "$s" && created+=("$s")
      if [[ "$s" == "RASPBERRY" ]]; then
        tmux rename-window -t "$s:0" "blackberry"
        tmux new-window -t "$s" -n "raspberry"
      fi
    fi
  done

  (( ${#created[@]} )) && echo "✅ Created: ${created[*]}"
  (( ${#existed[@]} )) && echo "ℹ️  Already running: ${existed[*]}"
}

mux-widget() { BUFFER="mux"; zle accept-line }
zle -N mux-widget
bindkey '^[M' mux-widget          # Alt+Shift+M -> create all sessions

adx-widget() { BUFFER="tmux attach -t DEVOPS"; zle accept-line }
zle -N adx-widget
bindkey '^[D' adx-widget          # Alt+Shift+D -> attach DEVOPS

arx-widget() { BUFFER="tmux attach -t RASPBERRY"; zle accept-line }
zle -N arx-widget
bindkey '^[R' arx-widget          # Alt+Shift+R -> attach RASPBERRY

aox-widget() { BUFFER="tmux attach -t OCI"; zle accept-line }
zle -N aox-widget
bindkey '^[O' aox-widget          # Alt+Shift+O -> attach OCI

mls() {
  echo "── tmux sessions ──────────────────────"
  if tmux list-sessions 2>/dev/null 1>/dev/null; then
    tmux list-sessions -F "#{session_name}: #{?session_attached,attached,not attached} (#{session_windows} windows)"
  else
    echo "(no active sessions)"
  fi

  echo ""
  echo "── keybindings ─────────────────────────"
  echo "Alt+Shift+M  ->  mux   (create all: RASPBERRY, OCI, DEVOPS)"
  echo "Alt+Shift+D  ->  adx   (attach DEVOPS)"
  echo "Alt+Shift+R  ->  arx   (attach RASPBERRY)"
  echo "Alt+Shift+O  ->  aox   (attach OCI)"
}
#-- -------------------------------------------
tkill() {
    if command -v tmux >/dev/null 2>&1; then
      tmux kill-server
    else
      printf 'Error: tmux is not installed.\n' >&2
      return 1
    fi
}

helpmux() {
    if command -v tmux >/dev/null 2>&1; then
      python3 "${HOME}/.tmux/helpmux.py"
    else
      printf 'Error: tmux is not installed.\n' >&2
      return 1
    fi
}
