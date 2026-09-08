---
name: lecture-notes
description: "Turn a raw lecture transcript (pasted text or an uploaded file) into a clean, chronological Word document (.docx) of notes, highlighting key topics and pulling out a to-do list of anything the lecturer assigned (readings, homework, deadlines). Reconstructs garbled transcript text from context instead of reproducing errors, and cross-checks names, terms, and structure against any other course material provided alongside it — slides, handouts, PDFs, a syllabus, even a photo of a whiteboard. Use whenever the user pastes or uploads lecture, class, seminar, or webinar transcript text and wants notes, a summary, a study guide, or a to-do list out of it — even without saying \"skill\" or naming the output format, and even if only a transcript is given. Also use for meeting-style recordings where \"lecture\" doesn't quite fit but the ask is the same: messy transcript in, structured notes + todos out."
---

# Lecture Notes

## What this skill is for

Lecture transcripts — especially auto-generated ones — are long, repetitive, and often garbled (dropped words, misheard homophones, run-on sentences with no punctuation). Nobody wants to study from that. This skill turns that raw text into something a student would actually want to open before an exam: notes that follow the lecture in order, a short list of the key topics that came up, and a to-do list of anything the lecturer told students to do.

The reason chronological order matters here (rather than reshuffling everything by theme) is that it keeps the notes anchored to how the lecture actually unfolded — easier to cross-reference against slides or a recording timestamp, and it avoids accidentally merging two similar-sounding topics that were actually discussed at different points for different reasons.

## Workflow

1. **Get the transcript, and check for other course material.** The transcript may be pasted directly in the chat, or in an uploaded file (.txt, .docx, .pdf, .vtt/.srt, etc.). The user may also provide other material from the same session — slides (.pptx), a handout or reading (.pdf, .docx), a syllabus, a photo of a whiteboard, anything that documents the same lecture. Treat that as a bonus reference, not a second thing to summarize — its job is to ground the notes you're writing from the transcript, not to be written up itself. If nothing else was provided, proceed with the transcript alone; don't ask for supporting material unless the transcript is so garbled in a load-bearing spot (a name you'll reuse repeatedly, a formula, an acronym central to the lecture) that guessing would actively mislead the student. If a file isn't already visible in context, read it from disk first. Some environments ship helper skills for this under `/mnt/skills/public/` (`file-reading/SKILL.md` for formats generally, `pptx/SKILL.md` for slides, `pdf-reading/SKILL.md` for PDFs) — use them if that directory exists, and otherwise open the file with whatever tooling is available locally (`python-pptx` for slides, `pdftotext` or `pypdf` for PDFs, `python-docx` for Word files, a plain text read for .txt/.vtt/.srt).

   Before writing any output, work out how you'll build the Word document, since that's the final deliverable. If `/mnt/skills/public/docx/SKILL.md` exists, read it — it covers headings, bullet/checklist formatting, and styles for that environment. If it doesn't, use a docx library directly (`python-docx` is the usual choice) and apply real Word styles — `Heading 1`/`Heading 2`/`Heading 3`, `List Bullet` for bullets, and a checkbox character (`☐`) for to-do items — rather than writing literal `#` or `-` characters into paragraph text.

2. **Read everything before writing anything.** Skimming and writing notes in one pass tends to miss the point of things said early on that only make sense once you've seen where the lecture ends up. Get the full arc first: what's the course/topic, roughly how many distinct segments or subtopics does it move through, where do asides ("by the way, this will be on the exam") show up. If other course material was provided, read through it too at this stage — slides are usually the fastest way to see the intended shape of a lecture (titles, section breaks, emphasized terms), a syllabus gives you the course's overall structure and vocabulary, and a handout or reading tells you what the lecturer assumed students already had in front of them. Get this context before you dive into the messier transcript.

3. **Reconstruct garbled text from context, don't transcribe the garbling.** Auto-transcripts routinely mangle technical terms, names, and homophones ("EWA" becoming "you wah", a professor's name spelled three different ways, missing negations that flip a sentence's meaning). Use the surrounding sentence, the subject of the course, and ordinary domain knowledge to figure out what was actually said, and write the *corrected* version.

   If other course material is available, it's your best source of truth for exactly this problem — a garbled name, acronym, or term is often spelled out cleanly on a slide, in a handout, or in the syllabus. Check that material for anything you're unsure about before falling back on inference or a web search. It also helps confirm which things the lecturer considers the actual key topics (a bolded term on a slide, or a term that recurs in an assigned reading, is a stronger signal than your own read of the transcript), and can resolve which of two similar-sounding topics a confusing passage is actually about.

   This material is a reference for accuracy, not a template for structure, though — keep following the transcript's chronological order in the Notes section (see step 5) even when a slide deck or handout is organized differently; lecturers skip around, take questions, and go on tangents that reproducing another document's structure would flatten.

   If a passage is short enough or ambiguous enough that you're genuinely guessing rather than confidently reconstructing — including after checking any other course material — keep it but mark it inline with `[unclear: ...]` so the student knows to double check that spot against the recording. Don't silently invent specifics you're not confident about (numbers, dates, names), and don't pepper the whole document with these tags for ordinary filler words.

4. **If slides or other visual course material were provided, go through all of it page by page — for images worth embedding, and for content worth mining — by default, not just when the transcript hints at something visual.** This is a distinct pass, worth doing thoroughly every time: convert the material to page images (see the pptx or pdf skill for the render commands — typically `soffice --headless --convert-to pdf` followed by `pdftoppm`) and look at each one. The best finds tend to be things the transcript gave no reason to expect — a scanned document, a data chart the lecturer only described vaguely, a diagram whose value is genuinely visual, or a slide's clean wording of something the transcript garbled. Don't wait for a cue like "as you can see here"; a slide that resolves a garbled name, sharpens a citation, or corrects something the transcript got wrong is worth finding even if nothing in the audio flagged it as special.

   Watch for one gotcha: if a deck has hidden slides (common in decks reused across years), a slide's position in a straight PDF export won't match its real slide number. If you need to cite an accurate slide number in a caption, check the source file directly (e.g. `python-pptx`) rather than trusting the export's page order.

   Not everything is worth embedding as an image. A genuine diagram, chart, scanned document, or photo — something prose can't capture as well — is worth it. A slide that's just bullet-point text, a logo, or a generic decorative icon isn't worth embedding, but "not worth embedding" doesn't mean "not worth reading." Text-only slides are often where the sharpest version of a point lives — precise wording for a definition, a numbered framework the transcript only gestured at, an example given cleanly rather than garbled through speech. Read every slide for content, not just for embed-worthiness, and fold anything that sharpens or corrects the notes into the prose (this overlaps with step 3, but the point-by-point visual pass here tends to surface things a flat text extraction glosses over). And keep it tied to the lecture: an embedded image or a text-based correction should support or correct something the transcript actually touches on, even loosely — it's a reason to enrich a point already being made, not license to introduce a topic the lecture never got to (same principle as reconstructing text in step 3).

   When you do find something worth embedding, let it improve the surrounding prose too, not just decorate it — a resolved acronym, a corrected name, or a real citation found this way is worth rewriting the text for, the same as any other cross-check. In the docx itself, embed the image (`ImageRun` if you're using the docx skill's toolkit, `document.add_picture()` in `python-docx`), size it to fit the page width, center it, and caption it with a one-line description plus which slide it came from.

5. **Write the notes following the template below**, in the order topics actually came up in the lecture. Use sub-headers when the lecture clearly shifts to a new subtopic — you don't need to force a new header for every minor tangent.

6. **Pull out key topics separately.** These are the concepts, terms, frameworks, or names a student would want to know are "the point" of this lecture — not just anything that was mentioned. A good test: if a student only read this section, would they know what to go look up or study further? If other course material is available, let its emphasis weigh heavily here — a title slide or a "learning goals" bullet, a heading in a handout, a term that shows up repeatedly in an assigned reading.

7. **Pull out to-dos separately.** Anything the lecturer explicitly asked students to do: readings, assignments, deadlines, "review X before next class," "bring Y to the next session," office hours mentioned, exam/quiz dates. Keep these as their own checklist, not folded into the running notes — todos get missed when they're buried in prose. If the lecture had no explicit asks, say so rather than omitting the section or inventing one.

8. **Save as a Word document (.docx)** and present it to the user. Use a short, descriptive filename derived from the course/lecture topic if it's stated (e.g. `requirements-engineering-lecture3-notes.docx`); fall back to `lecture-notes.docx` if nothing identifiable is stated.

## Output template

Use this structure (shown here in Markdown shorthand for readability — build it as a properly formatted Word document per step 1's approach, with real Heading 1/2/3 styles, bullet lists, and checkboxes, not literal `#` characters or hyphens in the text). Omit the date/course line if the transcript doesn't indicate it — don't guess at a date or course name.

```markdown
# [Lecture/Course Title]
*[Date, if stated]*

## Overview
2-4 sentences: what this lecture covered and why it matters / how it fits the course.

## Key Topics
- **[Term/concept 1]** — one-line gloss of what it means or why it came up
- **[Term/concept 2]** — ...

## Notes
Chronological, following the lecture's actual flow. Use heading levels when the topic shifts. Write in clear prose/bullets — not a word-for-word cleanup of the transcript, but not so compressed that context is lost either. Embed images inline where relevant (see step 4), each with a one-line caption noting what it is and its source slide.

## To-Dos
- [ ] Item the lecturer assigned, with any stated deadline
- [ ] ...

(If nothing was assigned: "No action items mentioned in this lecture.")
```

A fuller worked example of the *content and level of detail* (not final docx formatting) lives in `assets/example-output.md`.

## Things to watch for

- **Don't just compress everything into terse bullet fragments.** The point is notes a person can actually study from later without the original transcript — full enough sentences to stand alone, but not a re-transcription.
- **Multiple speakers (Q&A, guest lecturers):** attribute clearly ("A student asked about X; the lecturer explained...") rather than blending viewpoints together.
- **Very long transcripts:** it's fine, and often better, to build the Notes section incrementally — draft it in chunks that follow the transcript's own natural breaks (e.g. per topic shift) rather than trying to hold the entire thing in view at once and losing detail.
- **If the transcript is a fragment** (clearly cuts off mid-lecture), don't invent a wrap-up or overview claiming to cover the whole session — describe only what's actually there.
- **If other course material and the transcript disagree** (a number, a name, a claim), trust whichever is more likely to be authoritative for that specific detail — a spelled-out name or defined term in a slide, handout, or syllabus beats a mangled transcript every time, but a document can also be an older draft than what was actually presented, so don't silently override something the speaker clearly and repeatedly said on tape just because a document differs. If it's a meaningful discrepancy rather than an obvious transcript error, it's fine to note it briefly rather than picking one silently.
- **Embedded images need a caption, not just a drop-in.** A figure with no label forces the reader to guess why it's there. One line is enough: what it shows, and which slide it came from — that's also what lets a correction (a resolved name, a real citation) be traced back to its source.
