import json
import sys
from collections.abc import Iterator
from pathlib import Path
from typing import Any

DEFAULT_TOKENS = Path(__file__).resolve().parent.parent / "tokens" / "wissahickon.tokens.json"
BODY_TEXT = 4.5
LARGE_TEXT = 3.0

PAIRS: tuple[tuple[str, str, float], ...] = (
    ("color.text.heading", "color.surface.page", BODY_TEXT),
    ("color.text.body", "color.surface.page", BODY_TEXT),
    ("color.text.accent", "color.surface.page", BODY_TEXT),
    ("color.text.muted", "color.surface.page", BODY_TEXT),
    ("color.text.faint", "color.surface.page", BODY_TEXT),
    ("color.link.default", "color.surface.page", BODY_TEXT),
    ("color.palette.teal", "color.surface.page", LARGE_TEXT),
    ("color.text.heading", "color.surface.fill", BODY_TEXT),
    ("color.text.body", "color.surface.fill", BODY_TEXT),
    ("color.link.default", "color.surface.fill", BODY_TEXT),
    ("color.text.inverse", "color.surface.inverse", BODY_TEXT),
    ("color.text.inverse-accent", "color.surface.inverse", BODY_TEXT),
)

Tree = dict[str, Any]


def tokens(tree: Tree, prefix: str) -> Iterator[tuple[str, Tree]]:
    for name, node in tree.items():
        if name.startswith("$") or not isinstance(node, dict):
            continue
        path = f"{prefix}{name}"
        if "$value" in node:
            yield path, node
        else:
            yield from tokens(node, f"{path}.")


def is_alias(value: Any) -> bool:
    return isinstance(value, str) and value.startswith("{") and value.endswith("}")


def resolve(tree: Tree, path: str) -> Any:
    node = tree
    for key in path.split("."):
        node = node[key]
    value = node["$value"]
    return resolve(tree, value[1:-1]) if is_alias(value) else value


def channels(hex_color: str) -> tuple[int, int, int]:
    digits = hex_color.removeprefix("#")
    return int(digits[0:2], 16), int(digits[2:4], 16), int(digits[4:6], 16)


def luminance(hex_color: str) -> float:
    def linear(channel: int) -> float:
        share = channel / 255
        return share / 12.92 if share <= 0.04045 else ((share + 0.055) / 1.055) ** 2.4

    red, green, blue = (linear(channel) for channel in channels(hex_color))
    return 0.2126 * red + 0.7152 * green + 0.0722 * blue


def contrast(first: str, second: str) -> float:
    lighter, darker = sorted((luminance(first), luminance(second)), reverse=True)
    return (lighter + 0.05) / (darker + 0.05)


def color_faults(tree: Tree) -> list[str]:
    faults = []
    for path, node in tokens(tree["color"], "color."):
        value = node["$value"]
        if is_alias(value):
            try:
                resolve(tree, path)
            except KeyError:
                faults.append(f"{path}: {value} points at no token")
        elif value["colorSpace"] != "srgb":
            faults.append(f"{path}: color space is {value['colorSpace']}, expected srgb")
        elif tuple(round(part * 255) for part in value["components"]) != channels(value["hex"]):
            faults.append(f"{path}: components do not match {value['hex']}")
    return faults


def contrast_faults(tree: Tree) -> list[str]:
    faults = []
    for text, surface, minimum in PAIRS:
        ratio = contrast(resolve(tree, text)["hex"], resolve(tree, surface)["hex"])
        verdict = "ok" if ratio >= minimum else "FAIL"
        print(f"{ratio:5.2f}  min {minimum:.1f}  {verdict:4}  {text} on {surface}")
        if ratio < minimum:
            faults.append(f"{text} on {surface}: {ratio:.2f} is under {minimum:.1f}")
    return faults


def main(argv: list[str]) -> int:
    path = Path(argv[1]) if len(argv) > 1 else DEFAULT_TOKENS
    tree = json.loads(path.read_text())
    faults = color_faults(tree) or contrast_faults(tree)
    for fault in faults:
        print(f"fault: {fault}", file=sys.stderr)
    return 1 if faults else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
