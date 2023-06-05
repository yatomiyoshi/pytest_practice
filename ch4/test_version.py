import cards
from typer.testing import CliRunner

def test_version_v2(capsys):
    cards.cli.version()
    output = capsys.readouterr().out.rstrip()
    assert output == cards.__version__

def test_version_v3():
    runner = CliRunner()
    result = runner.invoke(cards.app, ["version"])
    output = result.output.rstrip()
    assert output == cards.__version__

def run_cards(*params):
    runner = CliRunner()
    result = runner.invoke(cards.app, params)
    return result.output.rstrip()

def test_run_cards():
    assert run_cards("version") == cards.__version__

def test_patch_get_path(monkeypatch, tmp_path):
    def fake_get_patch():
        return tmp_path
    
    monkeypatch.setattr(cards.cli, "get_path", fake_get_patch)
    assert run_cards("config") == str(tmp_path)