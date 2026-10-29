def budget_status(total, budget):
    if total < budget:
        return "Within budget"
    else:
        return "Over budget"


status = budget_status(5000, 5000)
print(status)
