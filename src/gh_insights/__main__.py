import argparse
from rich.console import Console
from rich.table import Table

from gh_insights.api import get_top_repos, get_repo_languages

console = Console()


def cmd_top_repos(user: str, limit: int) -> None:
    repos = get_top_repos(user, limit=limit)
    table = Table(title=f"Top {limit} repos de {user}")
    table.add_column("Nombre", style="cyan", no_wrap=True)
    table.add_column("⭐ Stars", justify="right", style="yellow")
    table.add_column("Lenguajes", style="green")

    for repo in repos:
        languages = get_repo_languages(user, repo["name"])
        langs_str = ", ".join(languages.keys()) if languages else "N/A"
        table.add_row(repo["name"], str(repo["stargazers_count"]), langs_str)

    console.print(table)


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="gh-insights", description="CLI para ver estadísticas de GitHub"
    )
    subparsers = parser.add_subparsers(dest="command")

    # Subcomando: top-repos
    top_repos_parser = subparsers.add_parser(
        "top-repos", help="Muestra los repos más populares de un usuario"
    )
    top_repos_parser.add_argument("user", help="Nombre de usuario de GitHub")
    top_repos_parser.add_argument("--limit", type=int, default=5, help="Número de repos a mostrar")

    args = parser.parse_args()

    if args.command == "top-repos":
        cmd_top_repos(args.user, args.limit)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
