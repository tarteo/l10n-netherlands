from odoo import models, fields, api


class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    tax_date = fields.Date(
        string='Tax Date'
    )

    date = fields.Date(
        string='Date',
        compute='_compute_date',
        index=True,
        copy=False,
        store=True
    )

    @api.depends('move_id', 'move_id.date', 'tax_date')
    @api.multi
    def _compute_date(self):
        for line in self:
            line.date = line.tax_date or self.move_id.date
