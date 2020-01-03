from odoo import api, fields, models

class comman(models.Model):
	_name = "comman.app"
	_description = "MyData"

	name = fields.Char(string='Name')
	add = fields.Char(string='Address')

class stud(models.Model):
    _name = 'student.app'
    _description = 'MyData'
    _inherit = 'comman.app'

    sid = fields.Integer(string='Student id')
    bdate = fields.Date(string='Birth Date')
    mno = fields.Integer(string='Mobile No')

class Teacher(models.Model):
    _name = 'teach.app'
    _description = 'MyData'
    _inherit = 'comman.app'

    tid = fields.Integer(string='Teacher id')
    mno = fields.Integer(string='Mobile No')

class stotal(models.Model):
    _description = 'Description'
    _inherit = 'student.app'

    total = fields.Integer(string='Total Student')