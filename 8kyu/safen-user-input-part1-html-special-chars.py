def html_special_chars(data):
    harmful = {"<":"&lt;", ">":"&gt;", '"': "&quot;", "&":"&amp;" }
    new_data= ""

    for i in data:
        if i in harmful:
            new_data = new_data + harmful[i]
        else:
            new_data = new_data + i
    return new_data

# Faster:
# def html_special_chars(data): 
#     return data.replace('&', "&amp;").replace('>', "&gt;").replace('<', "&lt;").replace('\"', "&quot;")
