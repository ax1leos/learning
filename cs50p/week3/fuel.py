def get_fraction(request):
    while True:
        try:
            req_str = input(request)
            x, y = req_str.split("/")
            num_x = float(x)
            num_y = float(y)
            
            if num_x < 0 or num_y <= 0 or num_x > num_y:
                continue
            return num_x / num_y
        except (ValueError, ZeroDivisionError):
            pass

        
def main():
    x = get_fraction("Fraction: ")
    
    percentage = round(x * 100)
    
    match percentage:
        case p if p <= 1:
            print("E")
        case p if p >= 99:
            print("F")
        case _:
            print(f"{percentage}%")
    
main()
    