def get_size(w,h,d):
    area = (w*h*2) + (w*d*2) + (h*d*2)
    volume = w*h*d
    return [area, volume]
