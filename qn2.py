packages = [
    {"package_id": "PKG1", "priority": 2, "weight": 5.2},
    {"package_id": "PKG2", "priority": 1, "weight": 7.5},
    {"package_id": "PKG3", "priority": 2, "weight": 4.0},
    {"package_id": "PKG4", "priority": 1, "weight": 2.3},
    {"package_id": "PKG5", "priority": 3, "weight": 5.2}
]

sorted_packages = sorted(packages, key=lambda x: (x['priority'], x['weight']))

print("Sorted Conveyor Belt:")
for pkg in sorted_packages:
    print(pkg)
