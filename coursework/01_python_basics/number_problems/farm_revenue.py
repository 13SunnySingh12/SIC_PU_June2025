# Total land and divisions
total_land = 80
segments = 5
land_per_crop = total_land / segments  # 16 acres per crop

# Yield of crops (in tonnes)
tomato_yield = (0.3 * land_per_crop * 10) + (0.7 * land_per_crop * 12)
potato_yield = land_per_crop * 10
cabbage_yield = land_per_crop * 14
sunflower_yield = land_per_crop * 0.7
sugarcane_yield = land_per_crop * 45

# Prices
tomato_price_per_kg = 7
potato_price_per_kg = 20
cabbage_price_per_kg = 24
sunflower_price_per_kg = 200
sugarcane_price_per_tonne = 4000

# Convert tonnes to kg and calculate sales (1 tonnes -> 1000kg)
tomato_sales = tomato_yield * 1000 * tomato_price_per_kg
potato_sales = potato_yield * 1000 * potato_price_per_kg
cabbage_sales = cabbage_yield * 1000 * cabbage_price_per_kg
sunflower_sales = sunflower_yield * 1000 * sunflower_price_per_kg
sugarcane_sales = sugarcane_yield * sugarcane_price_per_tonne 


total_sales = tomato_sales + potato_sales + cabbage_sales + sunflower_sales + sugarcane_sales


chemical_free_sales = tomato_sales + potato_sales + cabbage_sales + sunflower_sales


print("Overall sales achieved by Mahesh from the 80 acres of land: Rs.",total_sales)
print("Sales realisation from chemical-free farming at the end of 11 months: Rs.",chemical_free_sales)
