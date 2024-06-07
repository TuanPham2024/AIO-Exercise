# Calculate sum a, b
def sum(a, b):
    return a + b

def substract(a, b):
    return a - b

def multiply(a, b):
    return a*b

def exponent(a, n):
    return a**n

#kiểm tra xem module hiện tại (__name__) == "__main__" hay không, 
# tức đang chạy như một script độc lập chứ không phải được import từ một module khác
# Kỹ thuật dùng để ngăn chặn code chạy khi file được import như một module
if __name__ == "_main__":
    print(f"Total : {sum(1, 2)}")