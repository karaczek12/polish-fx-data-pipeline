from nbp import fetch_latest_rate


def main() -> None:
    quote = fetch_latest_rate("EUR")

    print(
        f"1 {quote['currency']} = "
        f"{quote['pln_per_unit']} PLN "
        f"(published {quote['effective_date']})"
    )


if __name__ == "__main__":
    main()