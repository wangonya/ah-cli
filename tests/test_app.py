from app import cli


def test_app(runner):
    """
    Basic test to check that invoking 'ah'
    with no command returns welcome message
    """
    res = runner.invoke(cli)
    assert res.exit_code == 0
    assert "Welcome to the ah console app" in res.output
