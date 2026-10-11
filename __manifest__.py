{
  "name": "meal", 
  "author": "Zach Joe", 
  "license": "LGPL-3", 
  "depends": ["base"], 
  "application": True, 
  "data": [
    "security/ir.model.access.csv", 

    "views/meal_recipe_views.xml",
    "views/meal_produce_views.xml", 
    "views/meal_plan_views.xml",
    "views/meal_shopping_list_views.xml", 
    "views/meal_menus.xml"
  ]
}