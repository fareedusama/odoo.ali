
from odoo import models, fields, api
import datetime


class Teacher(models.Model):
    _name = 'university.teacher'
    _description = 'teacher'

    name = fields.Char(
        string='Teacher Name',
        required=True)
    code = fields.Integer(
        string='Teacher Code',
        required=True)
    domain = fields.Char(
        string='Domain',
        required=True)
    department_id = fields.Many2one(
        comodel_name='university.department',
        string='department',
        required=False)
    category_id = fields.Many2one(
        comodel_name='product.category',
        string='category',
        required=False)
    product_id = fields.Many2one(
        comodel_name='product.template',
        string='product',
        required=False)


    sequance = fields.Integer(
        string='Sequance',
        required=False)
    department_ids = fields.Many2many(
        comodel_name='university.department',
        string='Department_ids')
    in_active = fields.Boolean(
        string='In_active', 
        required=False)
    state = fields.Selection(
        string='Number',
        selection=[('active', 'Active'),
                   ('unactive', 'Unactive'), ],
        required=False, default='unactive' )
    department_code = fields.Integer(
        string='Department Code', related='department_id.code',
        required=False)
    unique_id = fields.Char(
        string='Unique_id',compute = 'compute_unique_id',
        required=False)
    def student(self):
        self.state = 'active'

    def sale(self):
        print('..')

    def compute_unique_id(self):
        for rec in self:
            rec.unique_id = ''
            if rec.department_id:
                rec.unique_id = str(datetime.date.today()) +'-'+ str(rec.id)

    @api.model
    def create(self, vals):
        program = super(Teacher, self).create(vals)
        if vals['name']:
            contact = self.env['res.partner'].create({
                'name' : vals['name'],
            })
        return program

    





        


    

