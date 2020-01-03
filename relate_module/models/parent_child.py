from odoo import api, fields, models

class parent(models.Model):
    _name = "parent.app"
    _description = "MyApp"
    _rec_name = "pname"

    pname = fields.Char(string="Parent Name", required=True)
    childs = fields.One2many("child.app","panm")

class child(models.Model):
	_name = "child.app"
	_description = "MyApp"
	_rec_name="cname"

	cname = fields.Char(string="Child Name")
	panm = fields.Many2one("parent.app")

# //////////////module 2////////////////

class countrys(models.Model):
	_name = "countrys.app"
	_description = "MyApp"
	_rec_name="cntrynm"

	cntrynm = fields.Char(string="Country Name")
	states = fields.One2many("stats.app","statnm", string="State Name")

class stats(models.Model):
	_name = "stats.app"
	_description = "MyApp"
	_rec_name="statnm"

	statnm = fields.Char(string="Stat Name")
	cont = fields.Many2one("countrys.app", string="Country Name")
	cities = fields.One2many("citys.app","citynm", string="City Name")

class citys(models.Model):
	_name = "citys.app"
	_description = "MyApp"
	_rec_name="citynm"

	citynm = fields.Char(string="City Name")
	state = fields.Many2one("stats.app", string="State Name")
	cntry = fields.Many2one("countrys.app", string="Country Name")