"""Shared activity copy and a checked account of returning to a draft."""

import re

SIMZ_PROFILE = (
    'little-simz', '06', 'Little Simz', 'An earlier idea can have another use.',
    'Returning to a draft · artist interview · 2025',
    (('Spring 2022', 'Wrote a poem'), ('Two years later', 'Came back to it while making “Free”')),
    'This is her account of one song, not a schedule to follow or an explanation of fame. An earlier draft can give you material to keep, change or set aside.',
    'Keep a short original draft. If you want, return after a pause and notice one thing you would keep or change. You choose whether another version helps.',
    'Where would you want to practice that choice: on your own, with a willing collaborator, or with a teacher, librarian or music mentor?',
    'https://songexploder.net/little-simz',
    'Song Exploder · episode 294 · 2025; official transcript available',
)

def learner_connection(body):
    """Remove the repeated transfer commentary, retaining the local support link."""
    result, count = re.subn(
        r'<h3>One learning connection</h3><p>.*?</p>', '', body, flags=re.S,
    )
    if count != 1:
        raise ValueError('Expected one activity connection block')
    return result

LEARNER_RESEARCH_NOTE = '''<section><h2>A connection you can choose</h2><p>The learning routes are suggestions: independent practice, a collaborator, a library or community program, a class or a tutor.</p><p>Research on <a href="https://files.eric.ed.gov/fulltext/ED565393.pdf">relevance in laboratory tasks</a> and <a href="https://journals.sagepub.com/doi/full/10.1177/1475725720965002">optional online training</a> comes from different settings and has mixed results. It has not tested this website or shown that it improves school outcomes.</p></section>'''
