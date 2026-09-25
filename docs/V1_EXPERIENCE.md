# V1 experience — proposal for product review

## What this product feels like

A Linux desktop surface that adapts to the task without making the user learn four separate apps. It can sit at an edge, float nearby, serve as a dock, or combine task navigation with activity status. It uses k4's working Linux capabilities, has its own visual identity, and treats file handoff, clipboard access and system activity as everyday work. This is the intended experience, not a claim that the current repository already behaves this way.

## The four modes

| Mode | What remains visible | What opens |
| --- | --- | --- |
| Notch | A compact edge-attached status and access point | Activity, controls, files or a chosen tool expand inward from the edge. |
| Island | The same information in a detached surface | Content grows from its floating position while keeping a stable visual anchor. |
| Dock | Pinned and running apps, with a small reachable activity affordance | App previews, drawer and deliberate activity access. |
| Hybrid | Dock tasks and a compact activity surface together | Each expands for its own task without discarding the other. |

The user can choose top or bottom placement, size, alignment, offsets, hover/click behavior, hide policy, reserve/overlay behavior and preferred display. The selected mode changes the form, not the ownership of media, files or plugin state. Existing side placement remains available, while top and bottom receive the v1 polish work.

## A day with the surface

- **Idle:** The surface is quiet. It shows a small useful status or the app dock, not a stream of decorative motion. Disabled modules do not keep expensive visual work running.
- **Hover:** After a tunable delay, it reveals just enough context to decide what to do. Moving the pointer into revealed content is forgiving; a casual pass does not seize keyboard focus.
- **Click:** A deliberate click opens the user's chosen destination. ESC or click-outside closes an intentional view consistently. A shortcut opens its configured destination directly and leaves focus where typing will work.
- **Media starts:** Playback gets a compact place in Notch, Island or Hybrid. Opening it shows useful controls. Dock mode keeps apps primary while offering a small route to activity.
- **A notification arrives:** It may appear briefly over passive media, then media returns if still active. Notifications enter history. An open launcher, clipboard search or file view is not pushed aside by routine alerts.
- **Volume changes:** A short, readable HUD appears, repeated changes update it, and the previous eligible content returns. Recording continues to have a visible stop path. Brightness receives this treatment only on hardware with a verified source.
- **A file is dragged toward the surface:** The Shelf target becomes clear. Dropping stages a reference; the original file remains where it was. The user can inspect, pin, open, reveal, copy its path, remove it, or drag a copy onward. A missing source is shown rather than silently failing. Keyboard access covers the same core actions.
- **Clipboard is opened:** Text and images have distinct previews, search is immediate, pinned items are obvious, and keyboard selection is fast. Secret-copy behavior is explained honestly. File references are included only if the Linux clipboard path proves reliable.
- **Dock or Hybrid is selected:** Pinned/running apps and their order remain stable. The dock feels like the same product, while activity remains reachable. Hybrid keeps task navigation and passive status visible together.
- **Fullscreen starts:** The policy for that display decides whether the surface stays, overlays on deliberate access, or hides. Shortcuts still offer a recovery path; another monitor should not be hidden by the wrong screen's fullscreen state.
- **A monitor disconnects:** The active view and keyboard path move to a surviving display. No offscreen settings window, stranded focus or lost file staging.
- **Reduced motion is enabled:** The same states and information remain, with immediate changes or brief fades instead of travel, pulse or idle effects.

## Visual, accessibility and privacy principles

The visual language should be calm, legible and distinct from k4, Droppy and Apple's Dynamic Island. Shared typography, spacing, shape and motion rules keep the dock, surface, settings and modules related. Focus is visible, labels do not depend on color alone, text can scale, and blur never makes content unreadable. Visual effects stop when out of view. Clipboard and Shelf metadata remain local, and optional network features are clear and controllable. No telemetry.

## Deliberate v1 limits

V1 does not add Basket/shake detection, OCR/PDF/conversion suites, cloud services, calendar/meetings, broad AI workflows, universal camera detection, a plugin store, other compositor backends, X11 or distro-wide installers. Existing k4 tools in those areas may remain available; the limit is on major new work. The first release is judged by coherent daily behavior, not by the number of features in its menu.

The detailed contract and feasibility gates are in [V1_SPEC.md](V1_SPEC.md). This experience still needs product approval before implementation.
