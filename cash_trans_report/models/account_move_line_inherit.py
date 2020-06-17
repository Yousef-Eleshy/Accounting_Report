# -*- coding: utf-8 -*-
from odoo import fields, models, api, _


class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    journal_type = fields.Selection(related='journal_id.type', store=True)
