from decimal import Decimal

import pytest

from fx_pipeline.nbp import (
    fetch_latest_rate,
    parse_rate,
)

def test_parse_rate_extracts_expected_values():
    # Invented test data, not an actual NBP quotation.
    sample_response = {
        "code": "EUR",
        "rates": [
            {
                "effectiveDate": "2026-01-15",
                "mid": 4.25,
            }
        ],
    }

    result = parse_rate(sample_response)

    assert result["currency"] == "EUR"
    assert result["effective_date"] == "2026-01-15"
    assert result["pln_per_unit"] == Decimal("4.25")


def test_unsupported_currency_is_rejected():
    with pytest.raises(ValueError):
        fetch_latest_rate("XYZ")