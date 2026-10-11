from odoo import fields, models

class MealShoppingList(models.Model):
  _name = "meal.shopping.list"
  _description = "Shopping list for the future"

  week = fields.Integer(help="Week within this year in which this product will be used, for example in recipes.")
  produce_id = fields.Many2one("meal.produce", string="Product", required=True)
  quantity = fields.Float(help="Quantity you need for the week.")
  unit = fields.Char(help="Unit of the product's quantity.")
  recipe_ids = fields.Many2many("meal.recipe", string="For (Recipe)", help="Recipe in which this product is used.")
