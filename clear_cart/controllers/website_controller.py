from odoo import http
from odoo.http import request
from odoo import fields
from datetime import datetime



class WebsiteCustomerForm(http.Controller):
    @http.route('/shop/clear_cart', type='http', auth='public', website=True)
    def clear_cart(self):
        print(345678,request.context)

        request.cart.order_line.unlink()
        request.session['website_sale_cart_quantity'] = 0
        return request.render('website_sale.cart')




