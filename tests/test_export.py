#  TODO: Mock test file read/write
from app import view, list


def test_export_view_json(runner):
    """
    Tests exporting single article to json
    """
    res = runner.invoke(view, ["new_wangonya", "-e", "json"])
    assert res.exit_code == 0


def test_export_list_json(runner):
    """
    Tests exporting articles list to json
    """
    res = runner.invoke(list, ["-e", "json"])
    assert res.exit_code == 0


def test_export_list_csv(runner):
    """
    Tests exporting articles list to csv
    """
    res = runner.invoke(list, ["-e", "csv"])
    assert res.exit_code == 0


def test_export_list_sqlite(runner):
    """
    Tests exporting articles list to sqlite
    """
    res = runner.invoke(list, ["-e", "sqlite"])
    assert res.exit_code == 0
