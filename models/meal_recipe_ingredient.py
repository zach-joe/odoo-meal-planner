from odoo import fields, models

class MealRecipeIngredient(models.Model):
  _name = "meal.recipe.ingredient"
  _description = "Ingredients that are used in recipes with their respective quantity. "

  produce_ids = fields.Many2one("meal.produce", string="Produce being used")
  description = fields.Text()
  quantity = fields.Integer()
  unit = fields.Char()
  recipe_id = fields.Many2one("meal.recipe", string="Recipe used")