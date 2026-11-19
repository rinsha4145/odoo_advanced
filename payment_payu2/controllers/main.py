from odoo import http
from odoo.http import request
import pprint
from odoo.tools import consteq
from odoo.addons.payment.logging import get_payment_logger
from werkzeug.exceptions import Forbidden

from odoo.exceptions import ValidationError

from odoo.addons.payment_payu2 import const


_logger = get_payment_logger(__name__)

class PayuController(http.Controller):

    @http.route(const.PAYMENT_RETURN_ROUTE,type='http',auth="public",methods=["POST"],csrf=False)
    def payu_return_from_checkout(self, **data):
        print(4567,_logger)
        _logger.info("Handling redirection from PayU with data:\n%s", pprint.pformat(data))
        tx_sudo = self.env["payment.transaction"].sudo()._search_by_reference("payu2", data)
        print(678,tx_sudo.read())
        print(88888,data)
        if tx_sudo:
            self._verify_signature(data, tx_sudo)
            tx_sudo._process("payu2", data)
            print(67890,data)
        return request.redirect("/payment/status")

    @staticmethod
    def _verify_signature(payment_data, tx_sudo):
        received_signature = payment_data.get("hash")
        expected_signature = tx_sudo.provider_id._payu2_generate_signature(
            payment_data, incoming=True
        )
        if not consteq(received_signature, expected_signature):
            _logger.warning("Received payment data with invalid signature.")
            raise Forbidden