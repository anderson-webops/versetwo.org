"""Learner-defined relevance prompts and a checked account of returning to a draft."""

SIMZ_PROFILE = (
    'little-simz', '06', 'Little Simz', 'An earlier idea can have another use.',
    'Returning to a draft · artist interview · 2025',
    'In a 2025 Song Exploder interview, Little Simz said she wrote a poem in spring 2022 and returned to it two years later while making “Free.”',
    'This is her account of one song, not a schedule to follow or an explanation of fame. An earlier draft can give you material to keep, change or set aside.',
    'Keep a short original draft. If you want, return after a pause and notice one thing you would keep or change. You choose whether another version helps.',
    'Where would you want to practice that choice: on your own, with a willing collaborator, or with a teacher, librarian or music mentor?',
    'https://songexploder.net/little-simz',
    'Song Exploder · episode 294 · 2025; official transcript available',
)

GOAL_PROMPT = '''<section class="note" id="your-goal"><h2>Start with something you want to make.</h2><p>What would you like more control over: words, delivery, an arrangement, a reference, a budget, or something else? Keep your answer on paper, in your own notes or in your head. Pick one activity if it fits; trying them all is optional.</p></section>'''

def learner_connection(body):
    """Ask for the learner's connection before offering an adult-written example."""
    return body.replace(
        '<h3>One learning connection</h3>',
        '<h3>Does this help your goal?</h3><p>How might it help? “No connection” is fine. Adapt or skip this option:</p>',
    )

LEARNER_RESEARCH_NOTE = '''<section><h2>A connection you can choose</h2><p>These activities give you room to decide what, if anything, helps your music. The learning routes are suggestions. You can practice on your own, ask a willing collaborator, use a library or community program, or choose a class or tutor.</p><p>Research on <a href="https://files.eric.ed.gov/fulltext/ED565393.pdf">relevance in laboratory tasks</a> and <a href="https://journals.sagepub.com/doi/full/10.1177/1475725720965002">optional online training</a> comes from different settings and has mixed results. It has not tested this website or shown that it improves school outcomes. If an activity adds pressure or makes your goal feel harder, you can shorten it, choose another task or stop.</p></section>'''
