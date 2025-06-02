# tmux

Some basics about tmux (terminal multiplexer), a command-line tool that lets you manage multiple terminal sessions from a single window.

You can...

- split your terminal into multiple panes (either horizontally or vertically).
- run multiple programs (like shells, editors, logs, etc.) side-by-side in the same terminal.
- detach from a tmux session (leave it running in the background), then reattach later—even after disconnecting from SSH.
- have multiple windows within a session, each with its own set of panes.

**Default Prefix Key:** `Ctrl+b`
(press this, then the next key)

```sh
tmux source-file ~/.tmux.conf    # Reload config file
tmux kill-server                 # Kill all tmux sessions
```

| Command                     | Description             |
| --------------------------- | ----------------------- |
| `tmux`                      | Start new tmux session  |
| `tmux new -s name`          | Start session with name |
| `tmux ls`                   | List sessions           |
| `tmux attach -t name`       | Attach to session       |
| `tmux kill-session -t name` | Kill session            |
| `exit`                      | Close tmux pane         |

## Sessions

| Command                      | Description         |
| ---------------------------- | ------------------- |
| `:new -s name`               | Create new session  |
| `:rename-session -t old new` | Rename session      |
| `:kill-session -t name`      | Kill session        |
| `:switch -t name`            | Switch session      |
| `:detach` or `d`             | Detach from session |

## Windows

| Command    | Description           |
| ---------- | --------------------- |
| `c`        | Create new window     |
| `,`        | Rename window         |
| `w`        | List windows          |
| `&`        | Kill current window   |
| `p`        | Previous window       |
| `n`        | Next window           |
| `l`        | Last window           |
| `<number>` | Go to window <number> |

## Panes

| Command | Description         |
| ------- | ------------------- |
| `%`     | Split vertically    |
| `"`     | Split horizontally  |
| `o`     | Go to next pane     |
| `;`     | Go to previous pane |
| `{`     | Move pane left      |
| `}`     | Move pane right     |
| `x`     | Kill current pane   |
| `q`     | Show pane numbers   |
| `space` | Toggle pane layouts |
| `z`     | Zoom/unzoom pane    |

## Resizing Panes

| Command                                          | Description        |
| ------------------------------------------------ | ------------------ |
| `Ctrl+b` then `:`                                | Enter command mode |
| `resize-pane -L`                                 | Resize left        |
| `resize-pane -R`                                 | Resize right       |
| `resize-pane -U`                                 | Resize up          |
| `resize-pane -D`                                 | Resize down        |
| *(or use `Ctrl+b` + arrow keys in some configs)* |                    |

## Copy Mode

| Command | Description     |
| ------- | --------------- |
| `[`     | Enter copy mode |
| `Space` | Start selection |
| `Enter` | Copy selection  |
| `]`     | Paste           |

## Miscellaneous

| Command | Description           |
| ------- | --------------------- |
| `?`     | List all key bindings |
| `:`     | Command prompt        |
| `t`     | Show clock            |
| `~`     | Show command history  |
| `s`     | Select session        |
| `$`     | Rename session        |
