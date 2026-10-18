"""Command-line entry point for unit conversion."""

import argparse

from converter import (
    celsius_to_fahrenheit,
    fahrenheit_to_celsius,
    kilometers_to_miles,
    miles_to_kilometers,
)

CONVERSIONS = {
    "km-to-mi": kilometers_to_miles,
    "mi-to-km": miles_to_kilometers,
    "c-to-f": celsius_to_fahrenheit,
    "f-to-c": fahrenheit_to_celsius,
}


def main() -> None:
    parser = argparse.ArgumentParser(description="Convert length or temperature")
    parser.add_argument("conversion", choices=CONVERSIONS)
    parser.add_argument("value", type=float)
    args = parser.parse_args()
    result = CONVERSIONS[args.conversion](args.value)
    print(f"{result:.4f}")


if __name__ == "__main__":
    main()
