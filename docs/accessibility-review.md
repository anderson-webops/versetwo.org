# Accessibility and offline review

This protocol is for an adult reviewer. It records the prototype's remaining
technical questions without collecting participant data or recruiting minors.
No accessibility certification is claimed.

## Checks performed here

Source checks cover page language/title, one main landmark and h1, unique IDs,
local links, a focusable skip destination and native disclosure summaries.
The representative keyboard route and narrow-screen checks are recorded in
validation.md. A doubled-root-font test copy is prepared by
`python3 scripts/prepare_text_check.py`; it changes the HTML root font from
16 px to 32 px without adding client JavaScript. This stress test is distinct
from a browser's actual text-size or zoom setting.

## Ordinary browser and device checks still needed

- Extract the offline ZIP and open index.html directly, disconnect, close and
  reopen the page. Visit all eight pages and expand all five activity answers.
  The external source pages are expected to need internet. No local security
  setting should need to be relaxed; use the PDF if HTML opening is restricted.
- Set actual browser text size or zoom to 200%. Read each page and use its
  links/disclosures. Check for clipped words, overlapping controls, content
  hidden behind other content and unexpected horizontal scrolling. Reset the
  setting afterward. Record the browser, device and setting used.
- Use only the keyboard: Tab to Skip to content, Enter, then Tab through main
  actions. Open and close each of the five disclosures with Enter and Space. Check visible
  focus and Shift+Tab in reverse order. Confirm that no control traps focus.
- With a screen reader, check the title, main/navigation landmarks, headings,
  meaningful link names and disclosure expanded/collapsed announcements.
  Listen to the original verse line breaks and each budget label/amount pair.
  Check that the decorative slash and numbered story badges are not confusing.
- With ordinary touch input, activate navigation, profile links, disclosures
  and the PDF link. Try portrait and landscape on an intended low-cost device.
- Print in another browser. Check all stories, activity answers and source
  URLs. The supplied PDF has been visually reviewed; this does not guarantee
  that every browser's print output has identical pagination.

A concise finding should name the page, device/browser or assistive tool,
steps, expected behavior and actual behavior. Do not include personal lyrics,
minor identity, school records or case history. Reviewers can describe an
accessibility problem without supplying sensitive information.

## Human and partner questions

Youth usefulness, language respect, artist recognition, reading preferences,
feasible support routes and safeguarding cannot be established by the code
checks. Those require the separately authorized qualified-partner process in
pilot-plan.md. A screen-reader reviewer does not need to be a youth participant
or program partner to review technical accessibility.
