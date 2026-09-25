# Proposed v1 product specification — approval pending

**Status: proposal, not an authorized implementation lock.** Research completed 2026-09-25. Target is Wayland + Hyprland, Qt 6/QML/Quickshell. Preserve MIT notices and existing k4 functionality. The v1 identity is one configurable Linux desktop surface with a practical dock and a local file handoff tray, not a macOS replica. This specification is intentionally smaller than the combined feature lists in [FEATURE_MATRIX.md](FEATURE_MATRIX.md).

## MUST HAVE — CORE V1

1. **One surface model, four modes.** Notch (edge-attached compact surface), Island (visually detached pill near top/bottom edge), Dock (app/task dock), Hybrid (activity pill and persistent dock). Reuse `shell.qml` and `plugins/Dual` behavior. Modes are named user choices; mode switches preserve open work and keep working IPC shortcuts. Top and bottom must work. Existing left/right behavior remains available but does not set v1 polish gates.
2. **Bounded geometry controls.** Settings expose mode, top/bottom edge, width/height within safe ranges, alignment/position, edge offset, corner radius where applicable, expansion trigger, hover/click action, hide delay, fullscreen rule, reserve vs overlay, and preferred monitor. Save validated settings and restore safely after bad JSON/monitor loss. “Drag behavior” means moving/reordering dock items and dropping files into the Shelf; free dragging the whole panel across the desktop is later.
3. **Predictable activity handoff.** Extend the existing priority owner. Recording stays discoverable, a brief volume/notification view may interrupt media, explicit user-opened views win against automatic transients, and the previous eligible state returns after the interruption. No duplicate state router. Plugins retaining the old `active/priority/view` contract keep working through an adapter. See [ARCHITECTURE.md](ARCHITECTURE.md).
4. **Local file Shelf.** A compact/expanded file staging area accepts Wayland file/folder URI drops from apps that offer them, lists staged references, allows drag-out, open/reveal, remove, clear and optional pin. Default must preserve originals: staged items are references, drag-out advertises copy, and destructive move is not implicit. Handle missing files and unsupported MIME offers visibly. Keep list local; metadata stays local. Start with one Shelf, one display at a time, no Basket. Validate drag-in/out with real Hyprland apps before promising universal compatibility.
5. **Existing dock and Linux essentials.** Preserve pinned/running apps, focus, previews, reordering and drawer. Keep k4 media, launcher, notification center, clipboard, control center, audio/Wi-Fi/Bluetooth, screenshot/recording, editor, wallpaper/theme, settings, terminal/SSH, plugins and other enabled features functional. Do not redesign every module. A source feature with an optional unmet dependency may show an explicit unavailable state, not silently disappear.
6. **Privacy and accessibility baseline.** No telemetry. Explain any network lookup before it occurs; weather IP geolocation and agent usage requests must be transparent and user-controlled. Clipboard stays local and secret exclusion gets real-case tests. Keyboard access, visible focus, ESC/back behavior, accessible labels, contrast, large-text clipping checks and reduced-motion choice apply to the shell, modes, settings and Shelf. Preserve original MIT notice.
7. **Performance baseline.** Measure idle, media-playing, dock-visible and transition resource use on a representative Hyprland machine. Transition target: smooth at display refresh when practical, with no perpetual animation while hidden. Report measured CPU/RSS/GPU/frame timing with hardware and resolution rather than promising a fixed universal number.

## SHOULD HAVE — V1 POLISH

- One distinct visual grammar across shell, dock, launcher, media, notification and settings: typography, spacing, radius, icons, opacity/shadow, light/dark and motion tokens. Target visual coherence; keep component behavior. See [UX_DIRECTION.md](UX_DIRECTION.md).
- Make mode/geometry settings understandable through previews and clear descriptions. Give users a fast switch and a safe recovery shortcut if a surface is hidden or placed offscreen.
- Tune hover delays and transient priorities, media restoration, notification interruption and recording status. Keep expansion tied to one surface when focus and accessibility remain sound.
- Improve clipboard search/list hierarchy and secret-handling feedback without adding a new storage format unless necessary.
- Improve file/capture handoff: “send screenshot to Shelf” after capture is valuable if implemented through existing capture output, but should not block initial Shelf if capture integration needs a new path.
- Preserve existing external plugin API and add clear incompatibility diagnostics for any new surface contribution. Do not promise arbitrary third-party compact activities in the first build until adapters and tests exist.
- Document a manual Hyprland install path and dependency checks without adding installers for every distro.

## OPTIONALOT V1 — DEFER

Basket/shake-to-summon; multiple baskets; global drag detection; general OCR/PDF/image conversion; cloud file sharing; LocalSend tile; calendar/reminders; meetings control; full media queue/lyrics; live voice dictation; AI background removal; privacy/camera indicators beyond verified sources; advanced touchpad gestures; per-monitor independent activity queues; side-edge visual polish; Niri/KDE/GNOME/X11 backends; broad distro packaging. Existing k4 functionality in these areas, if any, remains accessible; “defer” applies to **new work**.

## REJECT for this product direction

- A pixel-copy of Droppy or Apple's island, copied assets, or bundled proprietary Droppy code.
- A framework rewrite without a demonstrated Quickshell blocker.
- Silent cloud uploads, telemetry, or implicit sensitive data sharing.
- Mac-only integrations presented as Linux features (AirDrop, iMessage reply, Finder Service, Mission Control, Apple Clock sync).
- Removing k4 games, editor, wallpaper, Atalaya or plugins solely because they are not core v1. Optional modules may remain optional and receive later attention.

## V1 feature lock by product role

| Category | Feature | Why this belongs here |
| --- | --- | --- |
| CORE V1 | Notch, Island, Dock and Hybrid modes | Configurable form is the product identity; Dock/Hybrid reuse existing `Dual`. |
| CORE V1 | Geometry, monitor and fullscreen policy | The form must be usable on real Hyprland desktops, including top and bottom placement. |
| CORE V1 | Activity handoff and recording visibility | A multi-purpose surface needs predictable interruption and restoration. |
| CORE V1 | Existing Linux services, plugin compatibility and IPC | Preserving k4 plumbing is the reason for the fork. |
| V1 POLISH | Media, notifications, launcher, clipboard and control center | Frequent daily interactions already exist but need one coherent hierarchy and motion language. |
| V1 POLISH | Existing dock, settings, capture and wallpaper entry points | Improve discoverability and consistency while retaining their current depth. |
| V1 POLISH | Privacy, accessibility, performance and manual install clarity | These determine whether the surface is trustworthy and comfortable all day. |
| DROPPY-INSPIRED V1 | Local file Shelf with safe drag handoff | Fills the clearest missing workflow; standard Wayland DnD offers a bounded implementation path. |
| DEFER | Basket, OCR, conversion tiles, calendar, meetings, voice dictation, gestures, other desktop backends | They either need a separate platform spike or expand v1 beyond a coherent first release. |
| REJECT | Copying proprietary visuals/code, Apple-only parity, silent cloud/telemetry, novelty stack rewrite | They conflict with originality, platform scope, privacy or the k4 foundation. |

## V1 acceptance examples

| Scenario | Expected result |
| --- | --- |
| Media is playing; volume changes | Volume appears briefly, media state remains valid and returns afterward. |
| User opens launcher during a notification | Launcher remains in focus; transient notification does not steal it back. |
| Screen recording starts then a notification arrives | Recording status remains accessible and stop control is not lost. |
| Dock toggles on/off in single and hybrid mode | Pinned/running apps remain stable; reserve/overlay behavior and one reflow are verified. |
| File is dragged from file manager into Shelf, then into another app | Original persists, target receives valid URI/copy; canceled drop leaves the staged item. |
| File disappears after staging | Shelf shows missing-file state and safely offers removal. |
| Preferred monitor disconnects or becomes fullscreen | Surface rehomes or hides per policy without offscreen controls or stranded focus. |
| Reduced motion enabled | State changes are immediate or brief fades; no long travel effect or idle shader loop. |
| Third-party k4 sample plugin enabled | Old `K4.Plugin`, IPC, settings, view and lifecycle work or an explicit compatibility error is shown. |

Approval of this package should explicitly settle the few choices listed in [DECISIONS.md](DECISIONS.md). No implementation begins before approval.
