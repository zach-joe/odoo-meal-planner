from odoo import fields, models

class MealProduce(models.Model):
  _name = "meal.produce"
  _description = "Produce used within recipes as ingredients by assigning each with a quantity and unit. Used to ensure identity."

  name = fields.Char(required=True)
  form = fields.Char(help="The form of the produce. For example, you can get fresh or canned tomatoes.")
  is_staple = fields.Boolean(help="Staple means that it is assumed that you always have this product in your pantry - for example, salt. Staples will not be added to your shopping list (since you already have it!) Uncheck if this produce is perishable, for example chicken.")
  default_unit = fields.Char(help="The canonical unit that you would like to measure this produce throughout the system - from recipes to shopping lists. This will be useful for aggregating the amount you will use throughout your weekly recipes to form your shopping list.")
  note = fields.Text()