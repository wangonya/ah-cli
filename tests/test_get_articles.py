from app import view, list


def test_view_not_found(runner):
    """
    Tests that fetching a non existent
    article returns 404
    """
    res = runner.invoke(view, ["1"])
    assert res.exit_code == 0
    assert "Status code: 404" in res.output


def test_view_found(runner):
    """
    Tests that fetching existent article
    returns 200
    """
    res = runner.invoke(view, ["new_wangonya"])
    assert res.exit_code == 0
    assert "Status code: 200" in res.output


def test_list(runner):
    """
    Tests fetching list of articles
    """
    res = runner.invoke(list)
    assert res.exit_code == 0
    assert "Status code: 200" in res.output

    res = runner.invoke(list, ["--limit", "2"])
    assert res.exit_code == 0
    assert "Limited to 2 articles" in res.output
