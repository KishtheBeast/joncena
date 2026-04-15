# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

A static PWA (Progressive Web App) that displays a mobile-optimized digital transit ticket with a live countdown timer. No build step, no framework, no dependencies — just HTML, CSS, and vanilla JavaScript deployed to GitHub Pages.

## Development

**Local preview:** Open HTML files directly in a browser:
```
open index.html
```

**Deploy:** Push to `main` — GitHub Actions automatically deploys to GitHub Pages via `.github/workflows/static.yml`. There is also a convenience script:
```
bash gitpush.sh
```

## Architecture

**Two pages:**
- `index.html` — compact mobile ticket view with QR code, color strips, progress bar, and "Tap to enlarge" link
- `ticket-details.html` — full-size view; zone number is clickable and cycles 1–11; has an adult count updater

**Timer logic (in both HTML files):**
- 60-minute countdown stored in `localStorage` (`deadlineDate`, `deadlineStart`)
- Auto-resets if 10 minutes have elapsed since the deadline
- Updates every second via `setInterval`

**Styling:**
- `ticket-master/style.css` — all layout and component styles
- `ticket-master/color.css` — CSS custom properties for theming; this is the only file that needs editing to change the color scheme:
  - `--first` — QR code border color (can be any color — pink, blue, etc.)
  - `--stripone` — leftmost color block in the bottom strip bar
  - `--striptwo` — middle color block in the bottom strip bar
  - `--stripthree` — rightmost color block in the bottom strip bar

## Updating Colors from an Image

When the user provides a screenshot or image and says to match colors, **do not read color.css first** — go straight to editing it. The file always has exactly these four variables.

**Visual map of where each variable appears in the ticket screenshot:**
```
┌─────────────────────────────┐
│        [header bar]         │  ← NOT controlled by color.css
│  ┌──────────────────────┐   │
│  │  [QR code border]    │   │  ← --first
│  └──────────────────────┘   │
│                             │
│  [stripone][striptwo][stripthree]  ← bottom strip bar, left to right
└─────────────────────────────┘
```

**Workflow:**
1. Look at the image. For each region above, identify its color.
2. Derive an accurate hex value — study hue, saturation, and brightness precisely. Do not default to generic approximations (e.g. "green" → `#008000`).
3. Edit `ticket-master/color.css` — update all four `--variable` values.
4. All four variables must be updated every time, even if some look similar — confirm each one independently.

**Note:** The header bar color is NOT in color.css and does not need to change.

**Fonts:** SF Pro Display Bold and Medium loaded from `ticket-master/` as local `.otf` files via `@font-face`.
