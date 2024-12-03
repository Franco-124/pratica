def calculate_total(products,descuento):
    total = 0
    for product in products:
        total += product['price']
    descuento = total *(descuento/100)
    total = total - descuento
    return total



def test_calculate_total_with_empty_list():
    print("Prueba")
    assert calculate_total([],10)==0

def test_calculate_total_with_single_product():
    products  = [{
        'nombre':'notebook',
        'price':100
    }]
    print(calculate_total(products,100))
    assert calculate_total(products,100)==0
    print("Prueba exitosa")

def test_calculate_total_with_multiple_products():
    products = [
        {
            'nombre':'notebook',
            'price': 50
        },
        {
            'nombre':'mouse',
            'price': 60
        }
    ]
    print(calculate_total(products,20))
    assert calculate_total(products,20)==88
    print("Prueba exitosa")


if __name__=="__main__":
    test_calculate_total_with_empty_list()
    print("Prueba exitosa")
    test_calculate_total_with_single_product()
    test_calculate_total_with_multiple_products()