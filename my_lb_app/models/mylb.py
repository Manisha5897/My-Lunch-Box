from odoo import api, fields, models

# student model
class myLbApp(models.Model):
    _name = "lb.app.mylb"
    _description = "MyApp"

    name = fields.Char(string='Student Name', required=True)
    address = fields.Text(string='Address')
    cntc = fields.Text(string='Contact No', required=True)
    email = fields.Text(string='E-Mail', required=True,
                        help='E-mail should be must enter')
    innm = fields.Many2one("institute.app", string='Institute Name')
    course = fields.Many2one(comodel_name='lb.app.newmylb',
                          string='Course Name', required=True)

# course model
class newLbApp(models.Model):
    _name = "lb.app.newmylb"
    _description = "MyApp"

    name = fields.Text(string="Course Name")
    fees = fields.Integer(string='Fees')

# institute model
class institute(models.Model):
	_name = "institute.app"
	_description = "MyApp"

	instname = fields.One2many("lb.app.mylb",'address','email' string="Institute Name")
	addr = fields.Text(string="Address")