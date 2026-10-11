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

  def action_generate_shopping_list(self):
    shopping_list = []

    # Iterate over each recipe meal within a plan
    for plan in self: 

      # Iterate over each ingredient within that recipe
      for ingredient in plan.recipe_ids.ingredient_ids: 

        # Find the produce that recipe ingredient corresponds to 
        produce = ingredient.produce_id

        # Only start adding this produce to the shopping list if the produce
        # is not a staple
        if not produce.is_staple: 

          # See if this produce is already in the shopping list and has its line
          shopping_list_item = next(
            (item for item in shopping_list if item["produce_id"].id == produce.id), 
            None
          )

          if shopping_list_item:
            # If line found, add the quantity the recipe calls for this ingredient to it
            shopping_list_item["quantity"] += ingredient.quantity

          else:
            # If not found, add a new line to the shopping list
            shopping_list.append({
              "week": plan.date.isocalendar()[1], 
              "produce_id": produce, 
              "quantity": ingredient.quantity, 
              "unit": produce.default_unit, 
            })

    # Populate the shopping list with needed ingredients
    for list_item in shopping_list:
      self.env["meal.shopping.list"].create({
        "week": list_item["week"], 
        "produce_id": list_item["produce_id"].id, 
        "quantity": list_item["quantity"], 
        "unit": list_item["unit"]
      })

    return True