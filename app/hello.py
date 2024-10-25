def get_greeting() -> str:
    """Return the greeting message"""
    return "Hello from rest-api-django!"


def main() -> None:
    """Print the greeting message"""
    print(get_greeting())


if __name__ == "__main__":  # pragma: no cover
    main()
