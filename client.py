import requests, json

BASE_URL = 'http://127.0.0.1:5000'

def get_page():
    r = requests.get(BASE_URL)
    response = r.json()
    print(response)
    return response

def get_all_products():
    url = BASE_URL + '/product'
    r = requests.get(url)
    response = r.json()
    print(response)
    return response

def add_new_product(name, description, price, qty):  
    url = BASE_URL + '/product'
    headers = {'Content-Type': 'application/json'}
    new_product = {
	    "name": name,
	    "description": description,
	    "price": price,
	    "qty": qty
    }
    p = requests.post(url, json=new_product)
    print(p)
    p_converted = p.json()
    return p_converted

# Get single product
def get_product(id):
    url = BASE_URL + '/product/' + str(id)
    r = requests.get(url)
    response = r.json()
    print(response)
    return response

def update_product(id, name, description, price, qty):  
    url = BASE_URL + '/product/' + str(id)
    new_product = {
	"name": name,
	"description": description,
	"price": price,
	"qty": qty
    }
    
    p = requests.put(url, json=new_product)
    print(p)
    p_converted = p.json()
    return p_converted

def delete_product(id):  
    url = BASE_URL + '/product/' + str(id)
    p = requests.delete(url)
    print(p)
    p_converted = p.json()
    return p_converted

def add_new_user(name, age):  
    url = BASE_URL + '/user'
    new_user = {
	    "name": name,
	    "age": age,
    }
    p = requests.post(url, json=new_user)
    print(p)
    p_converted = p.json()
    return p_converted

def get_all_users():
    url = BASE_URL + '/user'
    r = requests.get(url)
    response = r.json()
    print(response)
    return response


if __name__ == "__main__":
    # get_all_products()
    # get_page()
    # num_Product = 9
    # add_new_product("Product "+str(num_Product), "add new product", 100.0, 30)
    # num_Product += 1
    # update_product(9, "Product New", "Updated Product newnew", 200.0, 40)
    # delete_product(2)
    # add_new_user("user name 2", 25)
    get_all_users()