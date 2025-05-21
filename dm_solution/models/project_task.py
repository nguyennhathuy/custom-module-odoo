# -*- coding: utf-8 -*-
from odoo import fields, models, _

class Task(models.Model):
    _inherit = 'project.task'

    manager_ids = fields.Many2many('res.users', relation='project_todo_user_rel', column1='task_id', column2='user_id',string='Manager', tracking=True)