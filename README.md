<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="logos/logo-primary-dark.svg">
    <img src="logos/logo-primary.svg" width="160" alt="The Wissahickon Analytics mark: a round survey seal with contour lines along the Wissahickon Creek where it meets the Schuylkill River">
  </picture>
</p>

# wissahickon-brand

The logo files, design tokens and writing guidance for Wissahickon Analytics, a one-person data
consultancy in Philadelphia, PA.

Other Wissahickon Analytics repos take the brand from this one instead of keeping their own
copies. This first version holds the source files and one check. Nothing is published to npm or
PyPI yet.

## What is here

| Path | What it holds |
| --- | --- |
| [`logos/`](logos/) | Six SVG masters and the square avatar |
| [`tokens/wissahickon.tokens.json`](tokens/wissahickon.tokens.json) | Colors and font families as design tokens |
| [`voice.md`](voice.md) | How the firm writes |
| [`scripts/check_tokens.py`](scripts/check_tokens.py) | Fails if a text color falls below its contrast minimum |
| [`reference/sample-brand.html`](reference/sample-brand.html) | The original reference sheet, July 2026 |

## The mark

The mark is a survey seal drawn from public data: USGS 3DEP elevation contours and Philadelphia
Water Department hydrology for the gorge where the Wissahickon Creek meets the Schuylkill River.

| File | Use |
| --- | --- |
| `logo-primary.svg` | The primary mark, on light backgrounds. Contour lines are kept only along the waterways. |
| `logo-primary-dark.svg` | The same mark with light lines, on Ink. |
| `logo-small.svg`, `logo-small-dark.svg` | Small sizes. Creek and river only, no contours. |
| `logo-quiet.svg` | A calmer seal with 100-foot contours only, for when the primary reads as busy. Light backgrounds. |
| `seal-full-survey.svg` | The full-density survey seal. Large sizes only, as a feature. Light backgrounds. |
| `avatar.svg`, `avatar.png` | The small mark on a Bone square, for profile pictures. |

Use the files unchanged. Do not recolor, crop, rotate or redraw them.

`logo-primary-dark.svg` draws its contour lines in `#6FA89A`. That color is in the file but is
not part of the palette.

### Wordmark

The seal sits above or beside the name, set in live type. There are no lockup files yet.

- "Wissahickon" is Spectral 600 in Ink, letter-spaced -0.01em.
- "ANALYTICS" is Libre Franklin 600 in Pine, in capitals, letter-spaced 0.36em.
- Beside a 76 px seal, the reference sheet sets the first line at 30 px and the second at 11 px,
  with a 22 px gap between seal and type.

### Sizes and clear space

These values are proposed and not yet approved. They come from rendering each file in Chromium
at a range of sizes. The original brief set one rule only: use the small mark at 48 px and under.

| Mark | Smallest on screen | Smallest in print |
| --- | --- | --- |
| Primary and quiet seals, light and dark | 64 px | 0.75 in (19 mm) |
| Small mark, light and dark | 16 px | 0.25 in (6 mm) |
| Full survey seal | 160 px | 1.75 in (44 mm) |

A size is the width of the SVG, which includes its own margin. Below 64 px, use the small mark.

Keep at least a quarter of the ring's diameter clear between the ring and anything else. The
files carry part of that margin themselves, so in practice leave one eighth of the file's width
clear beyond its edge on every side.

## Color

| Name | Hex | Use |
| --- | --- | --- |
| Ink | `#14211E` | Primary dark. Headings on light surfaces and the background of covers. |
| Pine | `#1F4D3F` | Primary brand green. Links, accents and the wordmark's second line. |
| Teal | `#2A7D6F` | Secondary accent. The mark and large text only. |
| Sage | `#7FB5A8` | Light accent. On Ink only. |
| Sand | `#E5DCCB` | Warm neutral fill. |
| Bone | `#F6F2E9` | Paper. The default background. |

The tokens file adds roles on top of the palette. A role either points at a palette color or
holds a text color that was checked for contrast. The ratios below are WCAG 2 contrast ratios,
printed by the check script. Body text needs 4.5:1 for AA; large text needs 3:1.

| Role | Value | On Bone | On Sand | On Ink |
| --- | --- | --- | --- | --- |
| `color.text.heading` | Ink | 14.85 | 12.19 | |
| `color.text.body` | `#33403B` | 9.70 | 7.97 | |
| `color.link.default` | Pine | 8.58 | 7.04 | |
| `color.text.accent` | `#256F63` | 5.32 | | |
| `color.text.muted` | `#586962` | 5.20 | | |
| `color.text.faint` | `#6B665B` | 5.11 | | |
| `color.text.inverse` | Bone | | | 14.85 |
| `color.text.inverse-accent` | Sage | | | 7.17 |
| `color.rule.default` | `#CFCABF` | | | |
| `color.rule.soft` | `#EFE7D8` | | | |

Rules that follow from the numbers:

- Teal is 4.41:1 on Bone, so it passes for large text and the mark but not for body text. For
  teal text at body size, use `color.text.accent`.
- Sage is 2.07:1 on Bone. Use it on Ink only.
- On Sand, use the heading, body and link colors only. Accent, muted and faint fall to between
  4.20:1 and 4.37:1 there.
- Muted and faint replace the grays on the original reference sheet (`#6B7D76` at 3.90:1 and
  `#928C7F` at 2.99:1 on Bone).

The tokens follow the
[Design Tokens Format Module 2025.10](https://www.designtokens.org/tr/2025.10/format/). Colors
use that version's object form with a `hex` fallback. A tool that predates 2025.10 and expects a
hex string can read `$value.hex`.

## Type

| Family | Role | Weights |
| --- | --- | --- |
| Spectral | Display and headings | 400 to 700 |
| Libre Franklin | Running text and interface | 400 to 800 |
| Space Mono | Small labels, dates and figures, used sparingly | 400, 700 |

All three are published under the SIL Open Font License and are available from Google Fonts. The
font files are not in this repo yet.

## Check

```sh
python3 scripts/check_tokens.py
```

The script needs Python 3.9 or later and nothing else. It checks that each color's components
match its hex value and that every text and surface pair in its list meets its minimum. It exits
with status 1 on any fault.

## Not here yet

Lockup files, favicons, font files, and builds of the tokens for CSS, TypeScript and Python. Each
is added when a second repo needs it.

## License

The code and the tokens are under the [MIT license](LICENSE). The logo files are not: see
[`logos/LICENSE.md`](logos/LICENSE.md). The reference sheet is kept as received apart from the
path to the logo files. Where its colors differ from the tokens, the tokens are right.
