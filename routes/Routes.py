'''All the Endpoint we keep in the Routes.py '''

class Routes:
    BASE_URL = "https://fakestoreapi.com"

    #Product
    GET_ALL_PRODUCTS= '/products'
    GET_PRODUCT_BY_ID= '/products/{id}'
    GET_PRODUCT_WITH_LIMIT= '/products?limit={limit}'
    GET_PRODUCT_BY_CATEGORY= '/products/category/{category}'
    GET_PRODUCTS_SORTED= '/products?sort={order}'
    GET_ALL_CATEGORIES= '/products/categories'
    CREATE_PRODUCT= '/products'
    UPDATE_PRODUCT= '/products/{id}'
    DELETE_PRODUCT= '/products/{id}'

    #Users
    GET_ALL_USERS= '/users'
    GET_USER_BY_ID= '/users/{id}'
    GET_USER_WITH_LIMIT= '/users?limit={limit}'
    GET_USER_SORTED= '/users?sort={order}'
    CREATE_USER= '/users'
    UPDATE_USER= '/users/{id}'
    DELETE_USER= '/users/{id}'


    #Carts
    GET_ALL_CART= '/carts'
    GET_CART_BY_ID= '/carts/{id}'
    GET_CART_SORTED_BY_DATE= '/carts?startdate={start_date}&enddate={end_date}'
    GET_USER_CART= '/carts/user/{id}'
    GET_USER_CART_BY_DATE= '/carts/user/{id}?startdate={start_date}&enddate={end_date}'
    GET_CART_BY_LIMIT= '/carts?limit={limit}'
    GET_CART_SORTED_BY_ORDER= '/carts?sort={order}'
    CREATE_CART= '/carts'
    UPDATE_CART= '/carts/{id}'
    DELETE_CART= '/carts/{id}'
