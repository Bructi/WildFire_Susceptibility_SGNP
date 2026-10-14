---
name: research-lab
description: >-
  Activate for academic writing, literature review, citation management, source
  verification, LaTeX document generation, or any task requiring traceable,
  integrity-checked research output. Enforces zero-fabrication for citations.
---

# Research Lab Skill

## When to Activate
- Writing a research paper, literature review, or report
- Verifying claims or sources before including them in a document
- Generating LaTeX documents with proper bibliography
- Conducting systematic literature searches
- Fact-checking or rebutting an argument with sourced evidence
- Summarising academic papers accurately

---

## Inputs Required
- Research question or topic
- Desired output format (LaTeX / Markdown / plain text)
- Citation style (APA / IEEE / Chicago / BibTeX — default: APA)
- Scope: breadth (survey) or depth (focused analysis)
- Any known sources or seed papers

---

## Phase 1 — Question Scoping

1. Restate the research question in one precise sentence.
2. Identify the key concepts and their boundaries.
3. Define what counts as a credible source for this topic:
   - Peer-reviewed journals (ACM, IEEE, Springer, Elsevier, etc.)
   - Preprints on arXiv / bioRxiv — acceptable with explicit labelling
   - Official documentation, RFCs, technical standards
   - News / blog posts — only as secondary contextual sources, never as primary evidence
4. Define the time horizon (e.g., "last 5 years" vs. "all time").

**Gate:** Confirmed question + source criteria before searching.

---

## Phase 2 — Source Discovery

Permitted search strategies:
1. `search_web` with precise academic queries (include `site:scholar.google.com`,
   `arxiv.org`, `semanticscholar.org` when appropriate).
2. `read_url_content` on specific paper abstracts or documentation pages.
3. Reference list chaining: read the references of a key paper and follow relevant ones.

Rules:
- Do NOT invent paper titles, authors, DOIs, or publication venues.
- If a source cannot be retrieved, record it as UNVERIFIED.
- For every source, record: Title, Authors, Venue, Year, URL or DOI, Access status.
- Distinguish between: VERIFIED (read and confirmed), PARAPHRASE (read but summarised),
  UNVERIFIED (not retrieved), CITED BY (mentioned in another source).

**Gate:** Minimum 3 VERIFIED sources before drafting for any factual claim.

---

## Phase 3 — Source Verification Checklist

For each source, verify:
- [ ] Title matches the actual document at the URL/DOI
- [ ] Authors match
- [ ] Year and venue are correct
- [ ] The claimed finding is actually present in the paper (not misattributed)
- [ ] No retraction notice exists (check Retraction Watch if in doubt)
- [ ] Quoted text is verbatim if presented as a direct quote

Mark each source with its verification status in the working notes.

---

## Phase 4 — Drafting

Rules:
- Every factual claim must cite at least one VERIFIED source.
- Paraphrased claims must not distort the original meaning.
- Direct quotes must be verbatim and enclosed in quotation marks.
- Speculation or inference must be labelled explicitly ("This suggests...", "One interpretation is...").
- Do NOT pad with fabricated statistics or vague references to "studies show".

Structure (default academic):
1. Abstract (150–250 words)
2. Introduction (problem + motivation + contributions)
3. Related Work (organised by theme, not chronology)
4. Main body (methodology / analysis / findings)
5. Discussion (implications, limitations)
6. Conclusion
7. References

---

## Phase 5 — LaTeX Generation (if requested)

1. Use standard document classes: `article`, `IEEEtran`, or `acmart` as appropriate.
2. Bibliography: use `bibtex` or `biblatex`. Never embed URLs directly as citations.
3. Generate `main.tex` and `references.bib` as separate files.
4. Compile check (if `pdflatex` / `latexmk` available):
   ```
   latexmk -pdf main.tex
   ```
5. Report compilation output verbatim. Fix errors before declaring success.
6. If LaTeX is not available, generate a well-formatted Markdown equivalent.

---

## Phase 6 — Integrity Audit

Before delivery, run this checklist:
- [ ] Every citation in the text has a corresponding reference entry
- [ ] Every reference entry is cited at least once
- [ ] No DOI or URL is a 404 (spot-check at least 30%)
- [ ] No direct quotes exceed fair-use length (typically 400 words for most journals)
- [ ] Findings not in VERIFIED sources are labelled as EXPECTED or INFERRED

---

## Phase 7 — Report

Deliver:
- Output file(s) with absolute path
- Source verification table (Title | Status | DOI/URL)
- Compilation result (for LaTeX: VERIFIED / FAILED)
- Known gaps or claims that need stronger sourcing
- Word / page count

---

## Failure Handling

| Situation | Action |
|---|---|
| Source URL returns 404 | Mark UNVERIFIED; find alternative or note gap |
| Fewer than 3 verified sources | State this explicitly; do not draft the claim |
| LaTeX compilation fails | Read full error log; fix before reporting success |
| Contradictory sources | Present both positions; do not silently pick one |
| Paywalled paper | Note access barrier; use abstract only; label clearly |

---

## Completion Criteria

- All factual claims have at least one VERIFIED source
- Citation style is consistent throughout
- Source verification table delivered
- LaTeX compiles without errors (if applicable)
- No fabricated citations, statistics, or author names
