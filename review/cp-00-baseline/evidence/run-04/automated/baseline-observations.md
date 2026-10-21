# Original k4 observations — engineering exploration

App source: clean 818993b candidate, with inherited runtime files unchanged from ff520e3. Initial
captures used an archive export; the later smoke uses an independent clean Git checkout. Tool patch
and exact commands are retained. This run is not an owner-ready application revision.

Observed matrix:
- Top/bottom collapsed surface and expanded launcher render. Left/right surfaces and launchers render
  as compatibility observations; this is not a claim of full side parity.
- Default Dual viaje has a 2100 ms travel plus earlier/later phases. Initial 1.5-second waits captured
  animation in progress; later state/actual capture confirms a settled dock. Both edge arrangements
  are represented. The instant-effect fixture also reaches the top dock. No default-stall defect is
  claimed. The driver now polls estado for settled dock/barra rather than guessing a sleep.
- Settings Capture page renders. Actual harmless text and PNG selections appear in clipboard; the
  inherited captura.py screen path saves a 951x1028 PNG to the dummy HOME and returns success JSON.
- VLC 3.0.23 plays a synthesized local sine WAV through adummy. MPRIS metadata is read back, and
  k4 pause/resume changes VLC status to Paused/Playing. No host sound output is touched.
- The dummy document enters real fullscreen and returns; the surface returns in the actual capture.
  A second virtual Hyprland output renders a surface; removal returns to one. Physical second display,
  hotplug and device/audio integrations remain untested, not implicitly certified.
- hola/piezas/efectos/snake render in the inherited standalone plugin bank using only repository
  examples copied to dummy plugin paths. Piezas state returns values; Snake starts, accepts direction
  IPC and reports a live three-cell game. This does not prove full external-plugin host lifecycle.
- Atalaya on the stable headless display enumerates two dummy windows, reports abierto=true and
  error empty, and renders live previews. Its source catalog default is on; saved overrides take
  precedence. The complete timed on/off/open/closed matrix remains for the final fixed-display run.

Captures are inventoried with hashes. The agent opened all selected states through contact sheets
and inspected the larger settings, launcher, dock, fullscreen, clipboard, plugin and Atalaya images.
No concepts or visual references were generated; CP-00 Gate A is inapplicable.

Known inherited findings and boundaries:
- services/Enganches.qml repeatedly reports gruposAjustes binding loops at startup. Preserve for
  CP-01/CP-09 investigation; no product behavior repair was made here.
- Game catalog disabled does not suppress the separate default juegoActivo pill/service path. A
  dummy game/chest indicator is visible. This affects idle workload and is recorded as inherited
  behavior, not silently disabled to improve a benchmark. Future performance work belongs to CP-03.
- Actual QSG_RENDER_TIMING profiling crashes this installed Quickshell 0.2.1/Qt 6.11.2 logger with a
  segmentation fault in LogMessage::formatMessage. qsg-logging-crash.txt preserves environment and
  stack. Ordinary launches remain usable; no dependency or runtime-code repair is authorized here.
- Font package Meslo and swaybg are missing, optional whisper-cli is missing. Native captures use
  available system fallback fonts. Host audio/network/Bluetooth/system bus/portals are intentionally
  unreachable, so unavailable messages in those integrations are environment limits.
- Read-only runtime checkout prevents creation of the inherited external-plugin bridge/recargas;
  sample bank work uses a separate disposable writable copy. Installation/reload is not certified.

Benchmark failure retained:
The initial 15 traced samples are not a valid steady performance baseline. The parent nested window
was on host workspace 4 while workspace 3 was active; its output size changed from 951x1028 to
1908x1028 and eventually stopped frame delivery. Low media/dock readings and a timed-out grim must
not be interpreted as idle-efficiency proof. Both sandbox payloads remained live. A private
CP00-STABLE headless output at 1280x720/60 Hz/scale 1, mirrored into WAYLAND-1, immediately restored
capture and live Atalaya previews without any host workspace change. Final measurements must use
that output from a fresh clean checkout. The final driver retains failed commands and uses kernel
CPU/RSS/DRM counters plus Wayland frame callbacks; Qt render-stage timing remains unavailable.

Rights inventory: 157 asset/data/shader paths hashed: 104 Game assets, 35 Digivice files, four
Atalaya shader/source blobs, catalog/registry JSON and 12 inherited screenshots/GIFs. No bundled
font binary was found. MIT source terms are preserved; non-code creator/license/data attribution
and screenshot rights gaps remain exactly the release boundary in docs/ASSET_LICENSE_AUDIT.md.
No downloads, clearance claims, deletions or publication occurred.
