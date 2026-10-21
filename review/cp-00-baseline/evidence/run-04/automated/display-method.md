# Fixed private display method

The final compositor creates CP00-STABLE headless at 1280x720/60 Hz/scale 1 and mirrors it into only
its nested WAYLAND-1 window. The application cannot reach the parent socket or host compositor.
The headless output keeps rendering when the parent window is on another workspace. The owner can
view the same scene through the nested window. A second virtual output remains a separate case.

Primary references and installed verification:
- https://wiki.hypr.land/0.55.0/Configuring/Basics/Monitors/ (Lua mirror/disabled fields).
- /usr/share/hypr/stubs/*.lua on installed Hyprland 0.56.2 confirms mirror and disabled fields.
- Private hyprctl output create headless CP00-STABLE and Lua monitor rules succeeded; private grim
  and live Atalaya capture then succeeded while the parent remained on another workspace.

No physical mode, host workspace, owner keybinding or desktop service was changed.
