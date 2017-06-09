from odoo import models, fields, api


class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    @api.multi
    def finalize_invoice_move_lines(self, move_lines):
        self.ensure_one()
        for line in filter(lambda l: l[2]['tax_line_id'], move_lines):
            line[2]['tax_date'] = self.date_invoice
        return move_lines
