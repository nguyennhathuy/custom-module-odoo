from odoo import api, fields, models

class ResConfigSettings(models.TransientModel):
    group_powerbi_dashboard = fields.Boolean("PowerBI Dashboard", implied_group="project.group_project_stages")