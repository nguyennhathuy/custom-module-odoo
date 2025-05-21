# -*- coding: utf-8 -*-

from odoo import models, fields, api

class PowerbiLink(models.Model):
    # Các thuộc tính và trường của model sẽ được định nghĩa ở đây
    _name = 'powerbi.link'
    
    name = fields.Char(string='Report Name', required=True, help="The user-friendly name of the Power BI report.")
    powerbi_url = fields.Char(string='Power BI URL', required=True, help="The public embed URL for the Power BI report.")
    description = fields.Text(string='Description', help="A detailed description or notes about the report.")
    sequence = fields.Integer(string='Sequence', default=10, help="Used to order the links in lists.")
    active = fields.Boolean(string='Active', default=True, help="Uncheck to hide this link without deleting it.")
    type_dashboard = fields.Selection([('garage', 'Garage'), ('attendance', 'Attendance')], required=True)
    # Thêm các trường khác nếu cần, ví dụ:
    # category_id = fields.Many2one('powerbi.link.category', string='Category')

    @api.depends('powerbi_url')
    def _compute_embed_url(self):
        for record in self:
            record.embed_url = record.powerbi_url or 'about:blank'