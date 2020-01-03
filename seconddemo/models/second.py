from odoo import fields, models, api

class city(models.Model):
    _name = "country.demo.city"
    _description = "city.demo"
    _rec_name= "city_name"

    city_name = fields.Char(string="city name", required=True)
    area_name = fields.Text(string="area name", required=True)
    pincode = fields.Integer(string="pincode no", default=12345)
    city_population = fields.Integer(string="no", required=True)
    # country_state_name = fields.Many2one(comodel_name="country.demo.state",string="state name")
    # country_city_name = fields.Many2one(comodel_name="country.demo.country",string="abc name")
    selection_test = fields.Selection([('test1', "Test1")])

    @api.onchange('selection_test')
    def onchange_test(self):
        city_name="vishal"
        print("\n\n\n\n\n")
        print("in  >>>>>>>>>>>>>>>>>>>>>>>>>. def onchange_test(self):")
        print("\n\n\n\n\n")

class state(models.Model):
    _name = "country.demo.state"
    _description="state.demo"
    _rec_name="state_name"

    state_name = fields.Char(string="state_name", required=True)
    state_population=fields.Integer(string="no",required=True)
    city_name_in_state = fields.Many2one(comodel_name="country.demo.city",string="citys name", required=True)

class country(models.Model):
    _name = "country.demo.country"
    _description="country demo"

    country_name = fields.Char(string="country name")
    country_state_name = fields.Many2one(comodel_name="country.demo.state",string="state name")
    country_city_name = fields.Many2one(comodel_name="country.demo.city",string="city name")

class chield(models.Model):
    _name = "chield.chield"
    _description = "chield.demo"
    _rec_name = "chield_name"

    chield_name = fields.Char(string="chield_name")
    parent_name=fields.Many2one("parent.parent")

class parent(models.Model):
    _name = "parent.parent"
    _description="parent.demo"

    parent_name= fields.Char(string="parent_name")
    chieldss=fields.One2many("chield.chield", "parent_name")

class country_state(models.Model):
    _name = "country.state"
    _description = "country.state.city"

    name = fields.Char(string="country_name")
    state_names = fields.Many2many(comodel_name = "country.demo.state",string="state name")
    country_city_name = fields.Many2many(comodel_name="country.demo.city",string="city name")