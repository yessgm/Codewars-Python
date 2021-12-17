def update_light(current):
    if current == "green":
        return "yellow"
    if current == "yellow":
        return "red"
    return "green"

# faster
# def update_light(current):
#     return {"green": "yellow", "yellow": "red", "red": "green"}[current]
