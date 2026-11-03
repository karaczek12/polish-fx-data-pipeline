from decimal import Decimal

import requests

NBP_API_URL = "https://api.nbp.pl/api/exchangerates/rates/a"
SUPPORTED_CURRENCIES = {"EUR", "USD", "GBP"}

def parse_rate(payload: dict) -> dict:
    """Convert an NBP response into a simple record."""
    first_rate = payload["rates"][0]
    
    return {
        "currency": payload["code"],
        "effective_date": first_rate["effectiveDate"],
        "pln_per_unit": Decimal(str(first_rate["mid"])),
    }
    
def fetch_latest_rate(currency: str) -> dict:
    """Fetch the latest published average exchange rate."""
    currency = currency.upper()
    
    if currency not in SUPPORTED_CURRENCIES:
        raise ValueError(
            "Supported currencies are EUR, USD and GBP"
        )
    
    response = requests.get(
        f"{NBP_API_URL}/{currency}/",
        params={"format": "json"},
        timeout=10,
    )
    
    response.raise_for_status()
    return parse_rate(response.json())