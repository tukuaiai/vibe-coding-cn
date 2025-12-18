## tmux Shortcut Cheatsheet (Prefix Ctrl+b)

### Sessions
| Operation | Shortcut |
|---|---|
| Detach session | d |
| List sessions | s |
| Rename session | $ |

### Windows
| Operation | Shortcut |
|---|---|
| Create new window | c |
| Close window | & |
| Next window | n |
| Previous window | p |
| Switch to Nth window | 0-9 |
| Rename window | , |
| List windows | w |

### Panes
| Operation | Shortcut |
|---|---|
| Split pane horizontally | % |
| Split pane vertically | " |
| Switch pane | Arrow keys |
| Close pane | x |
| Show pane numbers | q |
| Toggle pane fullscreen/restore | z |
| Swap pane positions | { / } |
| Break pane into new window | ! |

### Others
| Operation | Shortcut |
|---|---|
| Enter copy mode | [ |
| Paste | ] |
| Show time | t |
| Command mode | : |
| List shortcuts | ? |

### Command Line
bash
tmux                  # Create new session
tmux new -s name      # Create named session
tmux ls               # List sessions
tmux attach -t name   # Attach to session
tmux kill-session -t name  # Kill session
