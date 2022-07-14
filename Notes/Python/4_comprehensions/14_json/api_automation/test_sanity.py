from requests import request

# Sanity test to check if few selected/important pages in the application are not broken
pages = [ 'login', 'register', 'cart', 'wishlist', 'books', 'computers', 'desktops', 'notebooks', 'accessories', 
        'electronics','camera-photo', 'cell-phones', 'apparel-shoes', 'digital-downloads', 'jewelry', 
        'gift-cards', 'iphone'
        ]

for page in pages:
    response = request("GET", f'http://demowebshop.tricentis.com/{page}')
    if response.status_code == 200:
        print("PASS")
    else:
        print(f"FAIL: Page {page} is not working")