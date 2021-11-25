from pytest import mark

from asciidump import main


@mark.parametrize("options", [[], ["--style", "files/css/partial.scss"]])
def test_pass(options):
    main(["mock", "files/artdir"] + options)
