def print_header(title):
    print("\n" + "=" * 60)
    print(title.upper())
    print("=" * 60)


def print_success(message):
    print(f"✅ {message}")


def print_error(message):
    print(f"❌ {message}")


def print_separator():
    print("-" * 60)