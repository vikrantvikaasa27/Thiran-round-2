inventory = {
    "P101": 10,
    "P102": 5,
    "P103": 20,
    "P104": 0
}

sales_orders = [
    {"order_id": "S1", "product_id": "P101", "quantity": 3},
    {"order_id": "S2", "product_id": "P102", "quantity": 2},
    {"order_id": "S3", "product_id": "P103", "quantity": 7},
    {"order_id": "S4", "product_id": "P104", "quantity": 4}
]

failed_orders = []
for order in sales_orders:
    pid = order["product_id"]
    qty = order["quantity"]
    oid = order["order_id"]
    
    if pid in inventory and inventory[pid] >= qty:
        inventory[pid] -= qty
        print(f"Order Processed: {oid}")
    else:
        reason = "Product not found" if pid not in inventory else "Insufficient stock"
        failed_orders.append({"order_id": oid, "product_id": pid, "quantity": qty, "reason": reason})
        print(f"Order Failed: {oid}")


print("\nUpdated Inventory:")
for pid, stock in inventory.items():
    print(f"Product ID: {pid}, Stock: {stock}")

print("\nFailed Orders:")
for failed in failed_orders:
    print(failed)
