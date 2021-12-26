def get_status(is_busy):
    status = "busy" if is_busy else "available"
    return {"status" : status}
