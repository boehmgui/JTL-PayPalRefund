"""Class definition for PayPal API"""

__author__ = "Guido Boehm"
__filename__ = "PayPalClasses.py"
__credits__ = [""]
__license__ = ""
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

import json
import requests
import yaml

from src.Validator_Classes import CharField, CurrencyField

from datetime import datetime


class RefundFailed(Exception):
    pass


class Amount:
    """
    class definition for amount object according to PAYPal's API
    Note: a value '1,11' would be a bad one as it does not represent a propper float. However, this is not
        covererd by the Amount class.
        PayPal's API will raise an HTTP 400 error if value does not conform to expected format

    Raises
        ValueError: if either paremeter is None
    """
    value = CharField(4, 32)
    currency_code = CurrencyField()

    def __init__(self, value, currency_code):
        if value is None or currency_code is None:
            raise ValueError('value or currency code cannot be None')
        self.value = value
        self.currency_code = currency_code

    def __str__(self):
        return f'value: {self.value} - currency_code: {self.currency_code}'

    def __repr__(self):
        return f'value:({self.value}) - currency_code:({self.currency_code})'

    @property
    def amount(self):
        return {"value":  self.value, "currency_code": self.currency_code}


class PayPalAPI:
    """PayPalAPI

    implments some methods of PayPal's Tackers batch resource group described at https://developer.paypal.com/api/tracking/v1/#trackers-batch_post
    """
    baseurl: str = 'https://api-m.sandbox.paypal.com'
    debug: bool = False
    client_id = CharField(1)
    secret = CharField(1)

    def __init__(
            self, client_id: str, secret: str
    ):
        """ __init__

        initializes an instance of the PayPal class; sets client id and secret, which are required by some methods
        Generation of the credentials is described here: https://developer.paypal.com/api/rest/#link-getcredentials

        Args:
            client_id (str): client ID
            secret (str): client secret
        """
        self.client_id = client_id
        self.secret = secret
        self._token = None
        self._debug_message = ''

    @property
    def token(self):
        """
        returns the token that is required for API authentication

        Returns:
            _token (str): currebtly active token

        """
        return self._token

    def get_token(
            self, endpoint
    ):
        """get_token

        obtains the authentication token from PayPal API
        Args:
            endpoint (str): API endpoint for authentication

        Raises:
            raise_for_status: if http response code is not 200

        """
        url = PayPalAPI.baseurl + endpoint
        payload = 'grant_type=client_credentials'
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        response = requests.request(method='POST', url=url, auth=(self.client_id, self.secret), headers=headers,
                                    data=payload)
        if PayPalAPI.debug:
            self.debug_message = f"Method: {self.get_token.__name__}\n"
            self.debug_message = f"url={url}\n"
            # self.debug_message = f"headers={headers}\n"
            self.debug_message = f"payload={payload}\n"
            self.debug_message = f"http status code: {response.status_code} - {response.reason}\n\n"

        if response.ok:
            self._token = response.json()['access_token']
        else:
            response.raise_for_status()

    @property
    def debug_message(self):
        return self._debug_message

    @debug_message.setter
    def debug_message(
            self, value
    ):
        self._debug_message += str(value)

    def refund_transaction(
            self, endpoint: str, transaction_id: str, body=None
    ):
        """
        initiates the refund based on PAyPal's API decsribed here:
        https://developer.paypal.com/api/payments/v2/#captures_refund
        Args:
            endpoint (str): API endpoint for refund
            transaction_id (str): ID that references the capture ID - aka transaction ID
            body (dict): Optional - dictionary that contains:
                                    - dict with amount and currency_code
                                    - invoice_id (str): Optional - external invoice number for this order.
                                    Appears in both the payer's transaction history and the emails that the payer
                                    receives.
                                    - note_to_payer (str): Optional The reason for the refund

        """
        # construct url based on capture id and endpoint url
        endpoint = endpoint.replace('{capture_id}', transaction_id)
        url = PayPalAPI.baseurl + endpoint
        # construct headers
        headers =  {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer {}'.format(self.token)
        }
        payload = json.dumps(body)

        # post request
        response = requests.request(method='POST', url=url, headers=headers, data=payload)

        if PayPalAPI.debug:
            self.debug_message = f"Method: {self.refund_transaction.__name__}\n"
            self.debug_message = f"capture_id: {transaction_id}\n"
            self.debug_message = f"url={url}\n"
            # self.debug_message = f"headers={headers}\n"
            self.debug_message = f"payload={payload}\n"
            self.debug_message = f"http status code: {response.status_code} - {response.reason}\n\n"

        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError as ex:
            self.debug_message = 'full debug data\n\n'
            self.debug_message = "refund request failed\n"
            self.debug_message = yaml.dump(response.json())
            raise RefundFailed(*ex.args)


def main(args=None):
    pass


if __name__ == "__main__":

    main()
