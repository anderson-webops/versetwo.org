"""Original learner activities and a flexible plan; no participant data is stored."""

GZA_PROFILE = (
    'gza', '04', 'GZA', 'Let a question become an idea.',
    'Curiosity · first-person article · 2015',
    (('Long-time interest', 'Science, to understand what is around him'), ('Became', 'Material to write about')),
    'This is his account of an interest, not a science qualification or proof that one subject makes better music. You can choose a topic that matters to you; no artist gets to decide your taste.',
    'Check one fact about a topic you like. Try two original lines using it. Keep a note of what the source actually supports.',
    'Ask a librarian or subject teacher to help check a reference you want to use in a verse, paragraph or presentation.',
    'https://medium.com/cuepoint/gza-speaks-the-lost-art-of-lyricism-ee84510e7268',
    'Cuepoint / Medium · May 27, 2015',
)

ACTIVITY_ROUTES = {
    'black-thought': ('four-lines', 'Try the four-line activity'),
    'rapsody': ('emphasis', 'Try moving the emphasis'),
    'megan': ('week.html', 'Make room for two goals'),
    'gza': ('reference', 'Try checking a reference'),
}

ACTIVITY3 = '''<article class="activity" id="emphasis">
<p class="eyebrow">03 / Delivery &amp; meaning · about 3–5 minutes</p>
<h2>Same words. Different emphasis.</h2>
<p>Change what a listener notices without changing the words. Speak privately, mark the sentence on paper, or think through the meanings.</p>
<div class="example"><span>Original teaching sentence</span><p class="verse">We can start the track tomorrow.</p></div>
<ol class="steps"><li>Put the emphasis on <strong>we</strong>. What might that suggest about who will start?</li><li>Move it to <strong>start</strong>, then <strong>tomorrow</strong>. What changes?</li><li>Try a pause after “track.” Mark it with a slash if you prefer. Does that create a different expectation?</li><li>Choose an emphasis for an original line of your own. What do you want a listener to notice?</li></ol>
<details><summary>Compare three possible readings</summary><p><strong>WE</strong> might contrast this group with somebody else. <strong>START</strong> might distinguish beginning from finishing. <strong>TOMORROW</strong> might contrast tomorrow with today. Context can change the reading.</p></details>
<p class="source">In her <a href="https://blog.sonicbids.com/rapsody-interview">January 8, 2014 Sonicbids interview</a>, Rapsody discussed cadence and melody. <a href="stories.html#rapsody">Rapsody’s process story</a>.</p>
<h3>One learning connection</h3><p>Ask a teacher, tutor or drama/music mentor to compare two readings of a sentence from an assignment you choose. Your language variety is not an error; timing and emphasis are only part of delivery.</p>
<a class="button secondary" href="next-step.html#writing">Find support for writing or delivery</a></article>'''

ACTIVITY4 = '''<article class="activity" id="reference">
<p class="eyebrow">04 / Research &amp; word choice · about 5–8 minutes</p>
<h2>A reference that earns its place.</h2>
<div class="source-cards"><section><h3>Source A · NASA</h3><p><strong>Our paraphrase:</strong> The Moon reflects a small part of the sunlight that reaches it.</p><p class="source"><a href="https://science.nasa.gov/moon/moonlight/">Moonlight</a> · NASA Science · updated February 12, 2026 · explanation of reflected light.</p></section>
<section><h3>Source B · ESA</h3><p><strong>Our paraphrase:</strong> ESA compares planets reflecting starlight with our Moon reflecting sunlight.</p><p class="source"><a href="https://www.esa.int/Science_Exploration/Space_Science/Exoplanets/What_do_exoplanets_look_like">What do exoplanets look like?</a> · European Space Agency · “Clouds and surface” section · no publication date displayed; checked October 2, 2026.</p></section></div>
<ol class="steps"><li><strong>State the narrow fact.</strong> What do both cards support? What would go beyond them?</li><li><strong>Check where it came from.</strong> These are explanations from two agencies. Neither page attributes this explanation to the other. They are not two new experiments. Two headlines repeating one interview would still be one origin.</li><li><strong>Make two original lines.</strong> Use the idea and keep a source note. Rhyme is optional. A metaphor can be imagined; a factual claim needs support.</li><li><strong>Ask if it belongs.</strong> Does the detail help your scene or meaning, or is it there only to sound impressive?</li></ol>
<details><summary>Compare with one original example</summary><p class="verse">The Moon sends borrowed sunlight down.<br>I carry yesterday’s idea through town.</p><p>The first line uses reflected sunlight; “borrowed” is a metaphor. The second line is imagined.</p></details>
<p class="source"><a href="stories.html#gza">GZA's 2015 account</a>.</p>
<h3>One learning connection</h3><p>If useful, ask a librarian or subject teacher to check your claim. The source cards above work offline.</p>
<a class="button secondary" href="next-step.html#research">Find help checking a source</a></article>'''

ACTIVITY5 = '''<article class="activity" id="viewpoints">
<p class="eyebrow">05 / Storytelling &amp; collaboration · about 5 minutes</p>
<h2>Same moment. Two viewpoints.</h2>
<div class="example"><span>Invented rehearsal scene</span><p>Alex thinks rehearsal begins at four. Jordan thinks it begins at five. They are reading different versions of a message. Neither has checked which version is current.</p></div>
<ol class="steps"><li>Write, speak privately or imagine two lines from Alex's view. What does Alex know? What is still an assumption?</li><li>Try two lines from Jordan's view. Let the difference come from information, not a stereotype about either person.</li><li>Choose what a listener should understand that the characters do not yet know.</li><li>Write one useful question the collaborators could ask to check the plan.</li></ol>
<details><summary>Compare one possible pair</summary><p class="verse">Alex: “The saved note says four; I’m ready by the door.”<br>Jordan: “My screen says five; I think I’m right on time.”</p><p>These original fictional lines show why each person might believe the schedule. A useful question is: “Which message is the latest, and can we confirm the time together?”</p></details>
<h3>One learning connection</h3><p>Compare point of view in a story or assignment with a teacher or tutor. For a group project, agree how changes will be confirmed. This is an original teaching exercise; storytelling is one musical choice, not a rule for every rap.</p>
<a class="button secondary" href="next-step.html#writing">Find support for a writing task</a></article>'''

ACTIVITY_LINKS = [
    ('four-lines', 'Four lines'), ('show', 'The $500 show'),
    ('emphasis', 'Move the emphasis'), ('reference', 'Check a reference'),
    ('viewpoints', 'Two viewpoints'),
]

WEEK = '''<h1>Your week</h1>
<ol class="week-steps">
<li><h2>1 · Pick a small target</h2><p><strong>Music:</strong> Choose clearer imagery, delivery, a reference or understanding a budget.</p><p><strong>Learning:</strong> Pick one question about an assignment, skill, credit or learning option. Name someone who could help.</p></li>
<li><h2>2 · Collect a detail</h2><p><strong>Music:</strong> Notice three details about an ordinary object or invented place.</p><p><strong>Learning:</strong> Read, listen to or discuss a short passage. Keep one question for a teacher or librarian.</p></li>
<li><h2>3 · Check a reference</h2><p><strong>Music:</strong> Try <a href="practice-reference.html">two lines with a checked fact</a>, or use the provided Moon example.</p><p><strong>Learning:</strong> Identify what a source supports. Ask for source help if you need it.</p></li>
<li><h2>4 · Keep two versions</h2><p><strong>Music:</strong> Try <a href="practice-four-lines.html">a second version of four lines</a>.</p><p><strong>Learning:</strong> Apply one revision to an assignment you choose, or ask a tutor to compare two versions with you.</p></li>
<li><h2>5 · Explain the money</h2><p><strong>Music:</strong> Explain the split in <a href="practice-show.html">the invented $500 show</a>.</p><p><strong>Learning:</strong> Practice the subtraction/division, or ask a math teacher or tutor where the calculation gets confusing.</p></li>
<li><h2>6 · Try a step if it fits</h2><p><strong>Music:</strong> Read, speak privately or silently review a short piece, or <a href="practice-choose-part.html">compare two arrangements</a>.</p><p><strong>Learning:</strong> If useful, try one action: practice a music skill independently, use a library resource, ask a collaborator or tutor for help, begin an assignment, or ask a counselor about credits/options.</p></li>
<li><h2>7 · Keep what helped</h2><p><strong>Music:</strong> Compare what changed and what you want to keep.</p><p><strong>Learning:</strong> Name one helpful thing and one difficulty. Choose a realistic next action, change the plan, or choose none.</p></li></ol>
<section><h2>Make the support request concrete</h2><p>“Could you help me with ____? I can try ____ at ____. The part that might get in the way is ____.”</p><p>If you are not enrolled, ask an education worker about locally appropriate options and eligibility. Safety, transport, work, money and learning access may need practical support beyond an activity.</p><a class="button secondary" href="next-step.html">Choose a support route</a></section>
'''
