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
  - `--first` — blue used for QR code border
  - `--stripone` — left color block in the strip bar
  - `--striptwo` — middle color block in the strip bar
  - `--stripthree` — right color block in the strip bar

## Updating Colors from an Image

When the user provides a screenshot or image and says to match colors:

1. **Inspect the image carefully.** Identify the exact colors for each UI region:
   - The blue used on the header bar and QR code border → `--first`
   - The left segment of the bottom strip bar → `--stripone`
   - The middle segment of the bottom strip bar → `--striptwo`
   - The right segment of the bottom strip bar → `--stripthree`

2. **Extract accurate hex values.** Do not guess approximate colors — study the hue, saturation, and brightness of each region in the image as precisely as possible. Avoid defaulting to generic color names (e.g. "purple" → `#800080`); derive the specific shade shown.

3. **Edit only `ticket-master/color.css`.** Update the four `--variable` values. No other file needs to change for color updates.

4. **All four variables must be updated** every time colors are changed from an image, even if some appear similar — confirm each one independently from the image.

**Fonts:** SF Pro Display Bold and Medium loaded from `ticket-master/` as local `.otf` files via `@font-face`.
