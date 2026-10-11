from odoo import fields, models

class MealPlan(models.Model):
  _name = "meal.plan"
  _description = "Meal plans for which recipes will be cooked on which days at which meal period."

  date = fields.Date(required=True)
  period = fields.Selection(
    string="Time of Day", 
    selection=[
      ("breakfast", "Breakfast"),
      ("lunch", "Lunch"),
      ("dinner", "Dinner"),
    ], 
    help="When during the day would you like to cook your planned recipe."
  )
  recipe_ids = fields.Many2many("meal.recipe", string="Recipe", required=True)