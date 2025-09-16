import argparse

from src.config.available_banks import AVAILABLE_BANKS

def get_args():
    parser = argparse.ArgumentParser(description="generating fakes payment receipts")
    parser.add_argument(
        '-b', '--bank',
        required=False,
        choices=AVAILABLE_BANKS,
        default='nu',
        help=f"bank (choices: {', '.join(AVAILABLE_BANKS)}; default: nu)"
    )
    parser.add_argument('-o', '--output', required=False, default='output.png', help='path to the output file (default: output.png)')
    args = parser.parse_args()
    return args