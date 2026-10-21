# CP-00 execution notes

These ordered instructions support the stable T01–T04 tasks in progress.json. They do not track status.

1. Preparation increment, T01: synchronize main, pin ff520e3 original product source, inventory actual
   binaries/dependencies/hardware and read-only host identities. Inspect arrancar/instalar, Paths,
   Settings, PluginManager, Notifs, Clipboard, startup singletons and external-process helpers. Run
   all inherited gates. Expect either recorded results or explicit missing-tool failures; no installer.
2. Isolation increment, T02: use installed bubblewrap namespaces with a synthetic filesystem/home,
   private network/PID/IPC/session bus/runtime; only the nested compositor may see a single parent
   display socket, and the app namespace must hide that socket. No system bus, host audio sockets,
   host HOME, input/DRM-card devices or inherited Hyprland identity. Inspect version-matched backend
   source; probe paths/services and compare host identities before any k4 launch. Stop on failed proof.
3. Recovery increment, T02: implement exact PID/start-time/config/full-ID guarded controls, rehearse
   refused foreign/stale identity and disposable-state backup/checksum/restore. Start the original
   pinned code only after the isolation proof, and demonstrate previous checkout plus matching state.
4. Characterization increment, T03: actual app capture matrix: top/bottom surface and Dual dock,
   experimental sides, fullscreen return, available one/two nested outputs; settings/launcher, local
   media fixture, harmless text/image clipboard, safe capture target, hola/piezas/efectos/snake.
   Save actual images under application/ and observations under automated/. Keep failures visible,
   assign later checkpoint responsibility; do not fix inherited product behavior in CP-00.
5. Validation/handoff increment, T04: fixed warmup and duration/repetitions for startup, idle, local
   media, dock, Atalaya catalog default/explicit overrides/open/closed; raw CPU/RSS/frame/GPU readings
   with tools and limitations. Inventory asset paths/hashes/provenance gaps. Rerun required checks,
   review full diff, append immutable run records, rehearse clean pinned Start/Stop/Restore, and provide
   the owner M01–M04 instructions only when engineering gates pass. Never self-approve Gate B.

Expected dummy inputs: a local synthesized audio track, CP00-only text/image clipboard, small test
windows/files and isolated settings. No credentials, real clipboard/history or external plugin copies.
Evidence directories get new run numbers when code/environment/instructions change. Keep prior runs.
