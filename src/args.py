import argparse

from src.config.available_banks import AVAILABLE_BANKS
from datetime import datetime


def get_args():
    parser = argparse.ArgumentParser(description="generating fakes payment receipts")
    now = datetime.now()
    parser.add_argument(
        "-b",
        "--bank",
        required=False,
        choices=AVAILABLE_BANKS,
        default="nu",
        help=f"bank (choices: {', '.join(AVAILABLE_BANKS)}; default: nu)",
    )
    parser.add_argument(
        "-d",
        "--date",
        required=False,
        default=str(now),
        help=f"date of the payment (default: {str(now).upper()})",
    )
    parser.add_argument(
        "-s",
        "--sender",
        required=False,
        default="Fake Name",
        help="name of the sender (who sends the payment; default: Fake Name)",
    )
    parser.add_argument(
        "-r",
        "--recipient",
        required=False,
        default="Fake Recipient",
        help="name of the recipient (who receives the payment; default: Fake Recipient)",
    )
    parser.add_argument(
        "-br",
        "--bank-recipient",
        required=False,
        default="Nu Pagamentos S.A",
        help="name of the bank recipient (who receives the payment; default: Nu Pagamentos S.A)",
    )
    parser.add_argument(
        "-a",
        "--account-agency",
        required=False,
        default="0001",
        help="agency number (default: 0001)",
    )
    parser.add_argument(
        "-n",
        "--account-number",
        required=False,
        default="999999999-9",
        help="account number (default: 999999999-9)",
    )
    parser.add_argument(
        "-v",
        "--value",
        required=False,
        default="123,50",
        help="value to be used in the receipt (default: 123,50)",
    )

    parser.add_argument(
        "-o",
        "--output",
        required=False,
        default="output.png",
        help="path to the output file (default: output.png)",
    )
    args = parser.parse_args()
    return args
