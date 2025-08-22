import subprocess
import sys
from pathlib import Path


def run_cmd(args: list[str]) -> str:
    out = subprocess.check_output([sys.executable, "-m", "gh_insights", *args])
    return out.decode().strip()


def test_cli_top_repos_output(tmp_path: Path) -> None:
    # Test superficial: el comando se ejecuta y muestra cabecera esperada
    out = run_cmd(["top-repos", "torvalds", "--limit", "1"])
    assert "Top" in out or "repos" in out
