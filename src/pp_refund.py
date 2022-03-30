#!/usr/bin/env python

"""
Project: PayPal TRefund

Description: updates the shipping information for a particular PayPal transaction

"""
__author__ = "Guido Boehm"
__projectname__ = "PayPalRefunf"
__filename__ = "pp_refund.py"
__credits__ = [""]
__license__ = "see LICENSE file"
__version__ = "0.0.1"
__maintainer__ = "Guido Boehm"
__email__ = "olb@family-boehm.de"
__status__ = "Prototype"
__copyright__ = """
Copyright 2022, Guido Boehm
All Rights Reserved. 
 
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, 
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES 
OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND 
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT 
HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, 
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING 
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR 
OTHER DEALINGS IN THE SOFTWARE. 
"""

from src.PayPalClasses import PayPalAPI, Amount
from src.utils.ParseKwargs import ParseKwargs

import argparse

import sys
import yaml

from dotenv import dotenv_values
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent.absolute()


def write_log(directory, filename, message):
    """write_log

    this function writes an error log to local disk

    :param directory: string: direactory name
    :param filename: string: filename
    :param message: str: message that is written to the file
    :return:
    """
    Path(directory).mkdir(parents=True, exist_ok=True)
    filename = Path(directory, filename + '.txt')
    with filename.open('a', encoding='utf-8') as file:
        file.write(message)


def main(args=None):
    """
    main function fo the script
    Args:
        args (dict): imput parameters

    Returns:

    """
    ###########################################################################
    # read parameters from yaml file
    ###########################################################################
    config_file = Path(SCRIPT_DIR, 'config.yaml')
    with config_file.open('r') as file:
        # The FullLoader parameter handles the conversion from YAML
        # scalar values to Python the dictionary format
        config = yaml.full_load(file)

    api = 'LiveAPI' if config['LiveModus'] else 'SandBoxAPI'
    if config['LiveModus']:
        credentials = {**dotenv_values(Path(SCRIPT_DIR, ".env.production").as_posix())}
    else:
        credentials = {**dotenv_values(Path(SCRIPT_DIR, ".env.sandbox").as_posix())}

    if not credentials:
        print('.env file with credentials not found - please refer to README.md for further information')
        write_log(Path(SCRIPT_DIR, './failed-refunds').as_posix(), args['refund_details']['capture_id'],
                  "Datei (.env.production oder .env.sandbox) nicht gefunden")
        sys.exit(1)

    PayPalAPI.baseurl = config[api]['BaseUrl']
    PayPalAPI.debug = config['Debug']

    # verify that capture id / transaction id is not None or an empty string
    capture_id = args['refund_details'].get('capture_id', None)
    if capture_id is None or not isinstance(capture_id, str) or len(capture_id.strip()) == 0:
        write_log(Path(SCRIPT_DIR, './failed-refunds').as_posix(), args['refund_details']['capture_id'],
                  str('capture-/transaction-id must be of str and must not be empty or None'))
        sys.exit(2)

    value = args['refund_details'].get('amount', None)
    currency_code = args['refund_details'].get('currency_code', None)
    # if both are not none we can try to instantiate Amount class - further validity checks will be done within that
    # class
    if value is not None and currency_code is not None:
        # instantiate amount to hold refund value and currency
        try:
            amount = Amount(value, currency_code)
        except (ValueError, KeyError) as err:
            write_log(Path(SCRIPT_DIR, './failed-refunds').as_posix(), args['refund_details']['capture_id'], str(err))
            sys.exit(2)

    # build request body
    # first check whether amount was instantiated
    if 'amount' in locals():
        body = {"amount": amount.amount}
    else:
        # if amaoun was not instantiated, create an empty body
        body: dict = {}

    if args['refund_details'].get('invoice_id', None) is not None:
        body["invoice_id"] = args['refund_details']['invoice_id']
    if args['refund_details'].get('note_to_payer', None) is not None:
        body["note_to_payer"] = args['refund_details']['note_to_payer']

    endpoint = config['LiveAPI']['EndPoint_Payments'] if config['LiveModus'] else config['SandBoxAPI']['EndPoint_Payments']

    paypal = PayPalAPI(client_id=credentials['Client_ID'], secret=credentials['Secret'])
    try:
        paypal.get_token(config[api]['EndPoint_Token'])
    except Exception as err:
        write_log(Path(SCRIPT_DIR, './failed-refunds').as_posix(), args['refund_details']['capture_id'], str(err))

    try:
        paypal.refund_transaction(endpoint, args['refund_details']['capture_id'], body)
    except Exception as err:
        # if refund failed we always have some debug data irrespective of settings inyaml file
        message = str(err) + '\n\n' + paypal.debug_message
        write_log(Path(SCRIPT_DIR, './failed-refunds').as_posix(), args['refund_details']['capture_id'], 'Errormessage: ' +
                  message + '\n')
        sys.exit(2)

    if paypal.debug_message:
        write_log(Path(SCRIPT_DIR, './logs').as_posix(), args['refund_details']['capture_id'], paypal.debug_message)
        sys.exit(0)


if __name__ == "__main__":
    arg_parser = argparse.ArgumentParser(
            description="Diese Skript erstattet den Betrag einer PayPal Transaktion"
    )
    req_args = arg_parser.add_argument_group(title='required arguments')
    req_args.add_argument(
            "--parameter", "-p", nargs='*',
            action=ParseKwargs,
            dest="parameters",
            help="bitte Transaktionsparameter angeben"
    )

    input_args = {}
    if len(sys.argv) > 1:
        usr_input = arg_parser.parse_args()

    else:
        arg_parser.print_help()
        sys.exit(2)
    input_args['refund_details'] = usr_input.parameters

    main(input_args)
