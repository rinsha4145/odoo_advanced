from odoo import fields, models, api
from odoo.addons.payment_payu2 import const
from odoo.tools import urls
from odoo.tools.urls import urljoin
from urllib.parse import urlencode
from odoo.exceptions import RedirectWarning, ValidationError
from odoo.http import request

from odoo.exceptions import ValidationError
import hashlib


class PaymentProvider(models.Model):
    _inherit = 'payment.provider'

    code = fields.Selection(
        selection_add=[('payu2', 'PayU2')], ondelete={'payu2': 'set default'}
    )

    payu2_api_key = fields.Char(
        string="PayU API Key",
        help="The Test or Live API Key depending on the configuration of the provider",
        copy=False,

    )
    payu2_salt_key = fields.Char(
        string="PayU Merchant Salt", copy=False,
        help="Help to generate a secure hash (signature) for authenticating and verifying transactions",
    )

    def _get_payu_url(self, state):
        """get the url"""
        if state == 'enabled':
            return 'https://secure.payu.in'
        else:
            return 'https://test.payu.in'

    def _build_request_url(self, endpoint, **kwargs):
        """Override of `payment` to build the request URL."""
        if self.code != 'payu2':
            return super()._build_request_url(endpoint, **kwargs)
        base_url = self._get_payu_url(self.state)

        return urls.urljoin(base_url, endpoint)

    def _build_request_headers(self, *args, payu_access_token=None, **kwargs):
        """Override of `payment` to build the request headers."""
        print(90909)
        if self.code != "payu2":
            print(1234321,payu_access_token)
            print(11111,**kwargs)
            return super()._build_request_headers(
                *args, payu_access_token=payu_access_token, **kwargs
            )

        return {"Authorization": f"Bearer {payu_access_token}"}

    def _payu2_generate_signature(self, payment_data, incoming=False):
        """Generate the signature for the provided payment data. from salt"""
        signature_data = {**payment_data, "salt": self.payu2_salt_key}
        signature_keys = const.SIGNATURE_KEYS["incoming" if incoming else "outgoing"]
        signature_string = "|".join(str(signature_data.get(field, "")) for field in signature_keys)
        return hashlib.sha512(signature_string.encode()).hexdigest().lower()


