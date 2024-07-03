weight = 41.5

#Ground shipping
groundcost = ""
if weight <= 2:
  groundcost = (1.5 * weight) + 20
elif weight <= 6:
  groundcost = (3 * weight) + 20
elif weight <= 10:
  groundcost = 20 + 4 * weight
else:
  groundcost = (4.75 * weight) + 20

print(groundcost)

# ground shipping premium
ground_ship_prem = 125
print(ground_ship_prem)

# drone shipping
drone_shipping = ""

if weight <= 2:
  drone_shipping = weight * 4.5
elif weight <= 6:
  drone_shipping = weight * 9
elif weight <= 10:
  drone_shipping = weight * 12
else:
  drone_shipping = weight * 14.25

print(drone_shipping)