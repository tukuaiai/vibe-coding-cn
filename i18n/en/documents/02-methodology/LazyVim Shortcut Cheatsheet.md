# LazyVim Shortcut Cheatsheet

| Shortcut    | Function                        |
|-------------|---------------------------------|
| **General** |                                 |
| `<Space>`   | Show keybinds menu (after 1s)   |
| `<Space>sk` | Search all keybinds             |
| `u`         | Undo                            |
| `Ctrl+r`    | Redo                            |
| `.`         | Repeat last operation           |
| `Esc`       | Exit insert mode/cancel         |
| **File**    |                                 |
| `<Space>ff` | Find file                       |
| `<Space>fr` | Recently opened files           |
| `<Space>fn` | New file                        |
| `<Space>fs` | Save file                       |
| `<Space>fS` | Save as                         |
| `<Space>e`  | Toggle sidebar                  |
| `<Space>E`  | Locate current file in sidebar  |
| **Search**  |                                 |
| `<Space>sg` | Global text search (grep)       |
| `<Space>sw` | Search word under cursor        |
| `<Space>sb` | Search current buffer           |
| `<Space>ss` | Search symbol                   |
| `<Space>sS` | Workspace search symbol         |
| `<Space>sh` | Search help documentation       |
| `<Space>sm` | Search marks                    |
| `<Space>sr` | Search and replace              |
| `/`         | Search current file             |
| `n`         | Next search result              |
| `N`         | Previous search result          |
| `*`         | Search word under cursor        |
| **Buffer (Tabs)** |                             |
| `Shift+h`   | Previous buffer                 |
| `Shift+l`   | Next buffer                     |
| `<Space>bb` | Switch to other buffer          |
| `<Space>bd` | Close current buffer            |
| `<Space>bD` | Force close buffer              |
| `<Space>bo` | Close other buffers             |
| `<Space>bp` | Pin buffer                      |
| `<Space>bl` | Delete left buffers             |
| `<Space>br` | Delete right buffers            |
| `[b`        | Previous buffer                 |
| `]b`        | Next buffer                     |
| **Window/Split** |                             |
| `Ctrl+h`    | Move to left window             |
| `Ctrl+j`    | Move to down window             |
| `Ctrl+k`    | Move to up window               |
| `Ctrl+l`    | Move to right window            |
| `<Space>-`  | Horizontal split                |
| `<Space>|` | Vertical split                  |
| `<Space>wd` | Close current window            |
| `<Space>ww` | Switch window                   |
| `<Space>wo` | Close other windows             |
| `Ctrl+Up`   | Increase window height          |
| `Ctrl+Down` | Decrease window height          |
| `Ctrl+Left` | Decrease window width           |
| `Ctrl+Right`| Increase window width           |
| **Terminal**|                                 |
| `Ctrl+/`    | Floating terminal               |
| `<Space>ft` | Floating terminal               |
| `<Space>fT` | Terminal in current directory   |
| `Ctrl+\`    | Exit terminal mode              |
| **Code Navigation** |                         |
| `gd`        | Go to definition                |
| `gD`        | Go to declaration               |
| `gr`        | View references                 |
| `gI`        | Go to implementation            |
| `gy`        | Go to type definition           |
| `K`         | View documentation hover        |
| `gK`        | Signature help                  |
| `Ctrl+k`    | Insert mode signature help      |
| `]d`        | Next diagnostic                 |
| `[d`        | Previous diagnostic             |
| `]e`        | Next error                      |
| `[e`        | Previous error                  |
| `]w`        | Next warning                    |
| `[w`        | Previous warning                |
| **Code Actions** |                             |
| `<Space>ca` | Code action                     |
| `<Space>cA` | Source code action              |
| `<Space>cr` | Rename                          |
| `<Space>cf` | Format file                     |
| `<Space>cd` | Line diagnostic info            |
| `<Space>cl` | LSP info                        |
| `<Space>cm` | Mason (Manage LSP)              |
| **Comments**|                                 |
| `gcc`       | Comment/uncomment current line  |
| `gc`        | Comment selected area           |
| `gco`       | Add comment below               |
| `gcO`       | Add comment above               |
| `gcA`       | Add comment at end of line      |
| **Git**     |                                 |
| `<Space>gg` | Open lazygit                    |
| `<Space>gG` | Lazygit in current directory    |
| `<Space>gf` | Git file list                   |
| `<Space>gc` | Git commit history              |
| `<Space>gs` | Git status                      |
| `<Space>gb` | Git blame current line          |
| `<Space>gB` | Open repository in browser      |
| `]h`        | Next git hunk                   |
| `[h`        | Previous git hunk               |
| `<Space>ghp`| Preview hunk                    |
| `<Space>ghs`| Stage hunk                      |
| `<Space>ghr`| Reset hunk                      |
| `<Space>ghS`| Stage entire file               |
| `<Space>ghR`| Reset entire file               |
| `<Space>ghd`| Diff current file               |
| **Selection/Edit** |                           |
| `v`         | Enter visual mode               |
| `V`         | Line visual mode                |
| `Ctrl+v`    | Block visual mode               |
| `y`         | Yank                            |
| `d`         | Delete/Cut                      |
| `p`         | Paste                           |
| `P`         | Paste before                    |
| `c`         | Change                          |
| `x`         | Delete character                |
| `r`         | Replace character               |
| `~`         | Toggle case                     |
| `>>`        | Increase indent                 |
| `<<`        | Decrease indent                 |
| `=`         | Auto indent                     |
| `J`         | Join lines                      |
| **Movement**|                                 |
| `h/j/k/l`   | Left/Down/Up/Right              |
| `w`         | Next word start                 |
| `b`         | Previous word start             |
| `e`         | Next word end                   |
| `0`         | Start of line                   |
| `$`         | End of line                     |
| `^`         | First non-blank char of line    |
| `gg`        | Start of file                   |
| `G`         | End of file                     |
| `{`         | Previous paragraph              |
| `}`         | Next paragraph                  |
| `%`         | Jump to matching parenthesis    |
| `Ctrl+d`    | Scroll down half page           |
| `Ctrl+u`    | Scroll up half page             |
| `Ctrl+f`    | Scroll down full page           |
| `Ctrl+b`    | Scroll up full page             |
| `zz`        | Center current line             |
| `zt`        | Top current line                |
| `zb`        | Bottom current line             |
| `Number+G`  | Go to specific line             |
| **Folding** |                                 |
| `za`        | Toggle fold                     |
| `zA`        | Recursively toggle fold         |
| `zo`        | Open fold                       |
| `zc`        | Close fold                      |
| `zR`        | Open all folds                  |
| `zM`        | Close all folds                 |
| **UI**      |                                 |
| `<Space>uf` | Toggle format                   |
| `<Space>us` | Toggle spell check              |
| `<Space>uw` | Toggle word wrap                |
| `<Space>ul` | Toggle line numbers             |
| `<Space>uL` | Toggle relative line numbers    |
| `<Space>ud` | Toggle diagnostics              |
| `<Space>uc` | Toggle invisible characters     |
| `<Space>uh` | Toggle highlights               |
| `<Space>un` | Close notifications             |
| **Exit**    |                                 |
| `<Space>qq` | Quit all                        |
| `<Space>qQ` | Force quit all                  |
| `:w`        | Save                            |
| `:q`        | Quit                            |
| `:wq`       | Save and quit                   |
| `:q!`       | Force quit without saving       |
