from odoo import api, fields, models

class MealRecipeIngredient(models.Model):
  _name = "meal.recipe.ingredient"
  _description = "Ingredients that are used in recipes with their respective quantity. "

  produce_id = fields.Many2one("meal.produce", required=True, string="Produce being used")
  description = fields.Text()
  recipe_id = fields.Many2one("meal.recipe", string="Recipe used")

  quantity = fields.Float()
  unit = fields.Char(
    compute="_compute_unit", 
    store=True, 
    readonly=False, 
  )

  @api.depends("produce_id")
  def _compute_unit(self):
    for ingredient in self: 
      ingredient.unit = ingredient.produce_id.default_unit

  is_staple = fields.Boolean(
    related="produce_id.is_staple"
  )
