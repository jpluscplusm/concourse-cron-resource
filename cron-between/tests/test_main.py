from textwrap import dedent

from between import main as between


def test_main_output(capsys):
    between()
    captured = capsys.readouterr()
    assert captured.out == dedent("""\
        2021-01-14 12:00:00
        2021-02-14 12:00:00
        2021-03-14 12:00:00
        2021-04-14 12:00:00
        2021-05-14 12:00:00
        2021-06-14 12:00:00
        2021-07-14 12:00:00
        2021-08-14 12:00:00
        2021-09-14 12:00:00
        2021-10-14 12:00:00
        2021-11-14 12:00:00
        2021-12-14 12:00:00
    """)
