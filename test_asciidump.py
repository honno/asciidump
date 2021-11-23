from string import ascii_lowercase

from pytest import mark
from rich.console import Console
from rich.segment import Segment
from rich.style import Style

from asciidump import *

console = Console()


@mark.parametrize(
    "span, markup, segment",
    [
        (Span(Segment("text")), "text", Segment("text")),
        (
            Span(Segment("text", Style(color="blue"))),
            '<span class="blue">text</span>',
            Segment("text", Style(color="blue")),
        ),
    ],
)
def test_span(span, markup, segment):
    assert span.markup == markup
    assert next(console.render(span)) == segment


@mark.parametrize(
    "row, markup, segments",
    [
        (
            Row(Span(Segment(c)) for c in ascii_lowercase),
            ascii_lowercase,
            [Segment(c) for c in ascii_lowercase],
        ),
        (
            Row(
                [
                    Span(Segment("r", Style(color="red"))),
                    Span(Segment("b", Style(color="blue"))),
                    Span(Segment("g", Style(color="green"))),
                ]
            ),
            (
                '<span class="red">r</span>'
                '<span class="blue">b</span>'
                '<span class="green">g</span>'
            ),
            [
                Segment("r", Style(color="red")),
                Segment("b", Style(color="blue")),
                Segment("g", Style(color="green")),
            ],
        ),
    ],
)
def test_row(row, markup, segments):
    assert row.markup == markup
    assert list(console.render(row)) == segments
