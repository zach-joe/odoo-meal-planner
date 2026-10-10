from odoo import fields, models

class MealProduce(models.Model):
  _name = "meal.produce"
  _description = "Produce used within recipes as ingredients by assigning each with a quantity and unit. Used to ensure identity."

  name = fields.Char(required=True)
  type = fields.Char(help="(Optional) The form of the produce. For example, you can get fresh or canned tomatoes.")
  note = fields.Text()