---
name: editorial-presentation
description: >-
  Activate when generating or editing a PPTX presentation. Produces visually
  engaging, genuinely editable PowerPoint files using PptxGenJS via Node.js.
  Preserves native PPTX elements (text, shapes, charts, images). Does NOT
  produce PDF-only or image-only outputs.
---

# Editorial Presentation Skill

## When to Activate
- User requests a slide deck, presentation, or PPTX file
- Converting outline / research notes into a structured presentation
- Redesigning or editing an existing PPTX
- Creating a visual narrative for a report, proposal, or talk

---

## Inputs Required
- Topic, audience, and purpose
- Approximate slide count (default: 10–15)
- Content: outline, research notes, raw text, or URL
- Preferred visual style (corporate / academic / creative — default: clean corporate)
- Brand colors if provided (default: dark navy #1B2A4A + accent #F5A623)

---

## Toolchain Decision

**PptxGenJS** is the default tool (free, produces native editable PPTX, runs via Node.js).

Check availability before proceeding:
```
node -e "require('pptxgenjs')" 2>&1
```
- If available → proceed with PptxGenJS script approach (Phase 3a).
- If not available and Node.js is installed → install locally:
  `npm install pptxgenjs --prefix ./pptx-temp` (single-use temp folder).
- If Node.js is absent → fall back to python-pptx if Python is installed.
- If neither is available → generate a structured `.md` slide outline and inform the user
  of the tool prerequisite. Do NOT generate a fake PPTX path.

---

## Phase 1 — Content Architecture

1. Identify audience and goal (inform / persuade / instruct / entertain).
2. Define narrative arc:
   - **Opening**: Hook + problem statement (1–2 slides)
   - **Body**: 3–5 main points, one idea per slide
   - **Evidence**: Data, visuals, or examples per point
   - **Closing**: Summary + clear call to action (1–2 slides)
3. Draft a slide-by-slide outline:
   - Slide N: [Title] | [3–5 bullet points max] | [Visual suggestion] | [Speaker notes]
4. Confirm outline with user or proceed if content is unambiguous.

**Gate:** Outline complete before any file generation.

---

## Phase 2 — Visual Design Decisions

Apply these rules for every slide:
- **Typography**: Title ≥ 28pt, body ≥ 18pt. Prefer sans-serif (Calibri, Arial, Helvetica).
- **Text density**: Maximum 6 lines per slide; maximum 8 words per line.
- **Color contrast**: WCAG AA minimum (4.5:1 ratio for body text).
- **Visuals**: Use `generate_image` for custom diagrams/graphics when relevant.
- **Consistency**: Same font, palette, and layout grid throughout.
- **No clipart or decorative noise** — every element must serve a purpose.

---

## Phase 3a — PptxGenJS Generation Script

Generate a `build-deck.js` Node.js script that:
1. Imports `pptxgenjs`.
2. Sets presentation metadata (title, author, subject).
3. Defines a slide master with brand colors, fonts, and logo placeholder.
4. Adds each slide from the outline with:
   - Native text boxes (editable)
   - Proper font sizes and colors
   - Background color or image
   - Speaker notes as PPTX notes (not text boxes)
5. Saves to `output/<deck-name>.pptx`.

Run the script:
```
node build-deck.js
```
Verify the output file exists and has non-zero size.

---

## Phase 3b — python-pptx Fallback

If PptxGenJS is unavailable, generate a `build-deck.py` script using `python-pptx`.
Apply the same design rules. Run: `python build-deck.py`.

---

## Phase 4 — Verification

1. Confirm output file exists: `dir output\*.pptx` or `ls output/*.pptx`.
2. Check file size > 10 KB (empty PPTX = broken script).
3. Report slide count, file path, and file size.
4. State: VERIFIED (file exists and non-empty) or FAILED (with error).
5. Do NOT claim the file is "ready" without confirming it exists.

---

## Phase 5 — Report

Deliver:
- Output file path (absolute)
- Slide count and outline summary
- Toolchain used (PptxGenJS / python-pptx / outline-only)
- How to open and edit in PowerPoint or LibreOffice Impress
- Any manual steps required (e.g., replace image placeholders)

---

## Failure Handling

| Situation | Action |
|---|---|
| Node.js / Python absent | Generate `.md` outline; inform user of prerequisite |
| Script error | Read full stderr; fix the script; re-run |
| Font not found | Fall back to Arial; do not abort |
| Image generation fails | Insert placeholder text; note it in report |
| Output file is 0 bytes | Debug script; re-run; never report success |

---

## Completion Criteria

- PPTX file exists at the stated path with non-zero size
- Every slide matches the approved outline
- Text is editable (not rasterized)
- Speaker notes present for each slide
- Toolchain and file path reported accurately
