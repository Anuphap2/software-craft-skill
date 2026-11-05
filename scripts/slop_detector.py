#!/usr/bin/env python3
"""
UI/UX Slop & Accessibility Scanner (Zero AI-Slop & WCAG Gate)
Part of software-craft-skill.
Detects unstyled emojis, generic purple/blue gradients, arbitrary non-token CSS, and accessibility flaws.
"""

import os
import re
import sys
import json
from typing import List, Dict, Any

# Common emoji regex pattern (excluding basic ascii)
EMOJI_PATTERN = re.compile(
    r'[\U0001F300-\U0001F6FF\U0001F900-\U0001F9FF\U0001FA70-\U0001FAFF\U00002702-\U000027B0\U0001F680-\U0001F6C0]'
)

# AI Slop Gradients: generic purple-to-blue / indigo-to-purple without semantic meaning
SLOP_GRADIENT_PATTERN = re.compile(
    r'(from-purple-\d+\s+to-blue-\d+|from-blue-\d+\s+to-purple-\d+|from-indigo-\d+\s+to-purple-\d+|from-violet-\d+\s+to-pink-\d+)'
)

# Arbitrary hardcoded Tailwind utility values (e.g. p-[17px], text-[#123456])
ARBITRARY_TAILWIND_PATTERN = re.compile(
    r'\b(p|m|px|py|pt|pb|pl|pr|w|h|text|bg|border)-\[([^\]]+)\]'
)

# Meaningless uppercase tracked-out eyebrow labels
TRACKED_EYEBROW_PATTERN = re.compile(
    r'\b(tracking-(?:widest|\[0\.\d+em\])\s+uppercase\s+text-(?:xs|\[10px\])|uppercase\s+tracking-(?:widest|\[0\.\d+em\])\s+text-(?:xs|\[10px\]))'
)

# Inline style attribute in JSX/HTML
INLINE_STYLE_PATTERN = re.compile(r'style=\{\{[^}]+\}\}')

# Dangerous outline-none without focus-visible
OUTLINE_NONE_PATTERN = re.compile(r'\boutline-none\b(?!.*focus-visible:)')


def scan_content(filepath: str, content: str) -> List[Dict[str, Any]]:
    issues = []
    lines = content.splitlines()

    for idx, line in enumerate(lines, 1):
        stripped = line.strip()
        if not stripped or stripped.startswith("//") or stripped.startswith("/*"):
            continue

        # 1. Check for Raw Emojis in JSX/HTML tags
        if any(tag in stripped for tag in ["<button", "<span", "<h1", "<h2", "<h3", "<p", "<a", "<div"]):
            emoji_matches = EMOJI_PATTERN.findall(stripped)
            if emoji_matches:
                issues.append({
                    "file": filepath,
                    "line": idx,
                    "category": "UIUX_AI_SLOP",
                    "severity": "HIGH",
                    "type": "UNSTYLED_EMOJI",
                    "found": ", ".join(set(emoji_matches)),
                    "message": f"Unstyled emoji '{emoji_matches[0]}' used directly in UI component. Use professional SVG icons (e.g., Lucide React) instead of raw emojis."
                })

        # 2. Check for Generic AI Slop Gradients
        gradient_match = SLOP_GRADIENT_PATTERN.search(stripped)
        if gradient_match:
            issues.append({
                "file": filepath,
                "line": idx,
                "category": "UIUX_AI_SLOP",
                "severity": "MEDIUM",
                "type": "GENERIC_PURPLE_GRADIENT",
                "found": gradient_match.group(0),
                "message": f"Generic AI-slop gradient '{gradient_match.group(0)}' detected. Use purposeful semantic background tokens or solid contrasting surfaces."
            })

        # 3. Check for Meaningless Tracked-Out Eyebrows
        eyebrow_match = TRACKED_EYEBROW_PATTERN.search(stripped)
        if eyebrow_match:
            issues.append({
                "file": filepath,
                "line": idx,
                "category": "UIUX_AI_SLOP",
                "severity": "LOW",
                "type": "TRACKED_EYEBROW_LABEL",
                "found": eyebrow_match.group(0),
                "message": "Meaningless tracked-out uppercase eyebrow label detected. Simplify hierarchy with strong, clean heading typography."
            })

        # 4. Check for Arbitrary Tailwind Values
        arbitrary_matches = ARBITRARY_TAILWIND_PATTERN.findall(stripped)
        if arbitrary_matches:
            for prefix, val in arbitrary_matches:
                # Allow standard css vars like bg-[var(--...)]
                if not val.startswith("var("):
                    issues.append({
                        "file": filepath,
                        "line": idx,
                        "category": "UIUX_TOKEN_HYGIENE",
                        "severity": "MEDIUM",
                        "type": "ARBITRARY_CSS_VALUE",
                        "found": f"{prefix}-[{val}]",
                        "message": f"Arbitrary hardcoded CSS '{prefix}-[{val}]' bypasses design tokens. Use standard theme spacing/color tokens."
                    })

        # 5. Check for Removed Outline without focus-visible (Accessibility risk)
        if OUTLINE_NONE_PATTERN.search(stripped) and "<button" in stripped:
            issues.append({
                "file": filepath,
                "line": idx,
                "category": "UIUX_ACCESSIBILITY",
                "severity": "HIGH",
                "type": "REMOVED_OUTLINE_WITHOUT_FOCUS_VISIBLE",
                "found": "outline-none",
                "message": "Button removes focus outline (`outline-none`) without `focus-visible:` ring. This violates WCAG 2.2 keyboard navigation."
            })

        # 6. Check for Inline Styles
        if INLINE_STYLE_PATTERN.search(stripped):
            issues.append({
                "file": filepath,
                "line": idx,
                "category": "UIUX_TOKEN_HYGIENE",
                "severity": "LOW",
                "type": "INLINE_STYLE_PROP",
                "found": "style={{...}}",
                "message": "Inline style detected. Migrate to semantic Tailwind classes or CSS variables for maintainability."
            })

    return issues


def scan_directory(target_dir: str) -> Dict[str, Any]:
    all_issues = []
    scanned_files = 0
    ignored_dirs = {".git", "node_modules", ".next", "dist", "build", "__pycache__", ".venv", "venv"}
    target_exts = {".jsx", ".tsx", ".html", ".vue", ".svelte", ".astro"}

    for root, dirs, files in os.walk(target_dir):
        dirs[:] = [d for d in dirs if d not in ignored_dirs]
        for file in files:
            ext = os.path.splitext(file)[1].lower()
            if ext in target_exts:
                filepath = os.path.join(root, file)
                try:
                    with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
                        content = f.read()
                    issues = scan_content(filepath, content)
                    all_issues.extend(issues)
                    scanned_files += 1
                except Exception as e:
                    sys.stderr.write(f"Error scanning {filepath}: {e}\n")

    return {
        "target_directory": os.path.abspath(target_dir),
        "files_scanned": scanned_files,
        "total_issues": len(all_issues),
        "issues": all_issues
    }


if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "."
    result = scan_directory(target)
    print(json.dumps(result, indent=2))
