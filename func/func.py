import webbrowser

def prompt_open_url(url: str) -> None:
    """Спрашивает пользователя, стоит ли открыть URL в браузере."""
    ans = input(f"Открыть {url} ? (y/N): ").strip().lower()
    if ans == 'y':
        webbrowser.open(url)
        print("Открыл в браузере.")
    else:
        print("Пропущено.")