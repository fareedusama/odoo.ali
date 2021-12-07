
from odoo import models, fields, api


class Department(models.Model):
    _name = 'university.department'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'department'

    name = fields.Char(
        string='Department Name', tracking=True,
        required=True)
    code = fields.Integer(
        string='Department Code',
        required=True)
    domain = fields.Char(
        string='Domain',
        required=True)
    sequance = fields.Integer(
        string='Sequance', 
        required=False)
    teacher_ids = fields.One2many(
        comodel_name='university.teacher',
        inverse_name='department_id',
        string='Teacher_ids',
        required=False)
    