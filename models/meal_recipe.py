from odoo import fields, models

class MealRecipe(models.Model):
  _name = "meal.recipe"
  _description = "Recipes to be managed by this meal-planning model"

  name = fields.Char(required=True)
  description = fields.Text()
  