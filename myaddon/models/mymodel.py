from odoo import models, fields


class MyModel(models.Model):
    _name = "myaddon.mymodel"
    _description = "My Model"

    thename = fields.Char(string="Their surames", required=True)
