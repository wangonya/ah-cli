from click.testing import CliRunner
from app import main


def test_app():
    runner = CliRunner()
    res = runner.invoke(main)
    assert res.exit_code == 0
    assert res.output == "Hello World!\n"
