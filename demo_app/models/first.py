from odoo import api, fields, models

class firstDemo(models.Model):
	_name = "demo.app.firstdemo"
	_description = "First Demo Application"

	name = fields.Char(string='Provider Name', required=True)
	price = fields.Integer(string='Price', required=True, help='')