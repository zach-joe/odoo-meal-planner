# Meal

A small Odoo 19 (Community) module for planning meals and turning the plan into a shopping list.

You keep a cookbook of recipes built from reusable produce, schedule recipes on a calendar, and generate a shopping list from the plan. Pantry staples (salt, soy sauce, oil) are left off the list because you already have them.

## Features

- **Produce** – ingredients with a name, form (e.g. fresh or canned tomatoes), default unit, and a _staple_ flag.
- **Recipes** – a name, a description, and ingredient lines (produce, quantity, unit).
- **Meal plan** – assign one or more recipes to a date and a meal period (breakfast, lunch, dinner).
- **Shopping list generation** – select plans and click _Generate Shopping List_. Ingredient quantities are summed per produce, staples are skipped, and the lines are tagged with the plan's week in this year.

### Staples and units

- Non-staple produce always uses the produce's default unit, so quantities can be summed reliably on the shopping list.
- Staple produce can use a different unit on a recipe line. For example, soy sauce may default to ml, but a recipe can say 2 tablespoons. Staples never reach the shopping list, so mixed units don't matter.

## Installation

1. Place this folder (named `meal`) in an Odoo 19 addons path.
2. Restart the Odoo server and update the apps list (with developer mode on).
3. Search for **Meal** in Apps and install it.

Or from the command line:

```bash
./odoo-bin -d <database> -i meal
```

The module only depends on `base`.

## Usage

1. **Meal → Cookbook → Produces**: add your produce. Tick _Staple_ for things you always have, and set a default unit.
2. **Meal → Cookbook → Recipes**: create a recipe and add ingredient lines.
3. **Meal → Planning**: add a plan with a date and one or more recipes.
4. Select one or more plans in the list view and click **Generate Shopping List**.
5. **Meal → Shopping**: see your aggregated shopping list for the meals you have planned.

## Structure

| Model                    | Purpose                                                       |
| ------------------------ | ------------------------------------------------------------- |
| `meal.produce`           | Reusable ingredient with default unit and staple flag         |
| `meal.recipe`            | Recipe with ingredient lines                                  |
| `meal.recipe.ingredient` | Produce, quantity and unit for a recipe                       |
| `meal.plan`              | Recipes scheduled on a date and meal period                   |
| `meal.shopping.list`     | Generated shopping list lines (week, produce, quantity, unit) |

The logic for generating shopping list from selected meal plans is in `action_generate_shopping_list` in `models/meal_plan.py`.

## Known limitations

This is a first version and deliberately basic:

- Clicking _Generate Shopping List_ more than once for the same plans creates duplicate lines.
- Plans are grouped by produce only. If you select plans from different weeks at once, quantities are merged under the first plan's week, so generate one week at a time.
- No automated tests, demo data, or search views yet.

## Possible next steps

- Group by week and produce, and avoid duplicates on regeneration.
- Add tests for the aggregation logic.
- Search and filter views, and a form view for plans.
- Unit conversion between compatible units.

## License

LGPL-3
