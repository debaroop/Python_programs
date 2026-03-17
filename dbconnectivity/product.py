from db import get_connection


#create a new product
def add_product(name, price, stock):
    
    conn=None
    cursor=None
    
    try:
        print("starting add_product function")
        conn = get_connection()
        cursor = conn.cursor()
        query = "INSERT INTO products(name,price,stock) VALUES (%s,%s,%s)"
        cursor.execute(query,(name,price,stock))
        conn.commit()
        print(f"Product '{name}' is added successfully !!")
        
    except Exception as e:
        print(" error inserting product -->", e)
        
        
    finally:
        if cursor:
            cursor.close()
            
        if conn:
            conn.close()

def list_products():
    try:
       # print("starting add_product function")
        conn = get_connection()
        cursor = conn.cursor()
        
        query = "SELECT * FROM products"
        cursor.execute(query)
        
        rows= cursor.fetchall()
        print("Products below:")
        
        for row in rows:
            print(f"ID: {row[0]}, NAME: {row[1]}, PRICE: {row[2]}, Stock: {row[3]}")
       
    except Exception as e:
        print(" error inserting product -->", e)
        
        
    finally:
        if cursor:
            cursor.close()
            
        if conn:
            conn.close()
            
def update_product(product_id,price=None,stock=None):
 
    try:
        conn=get_connection()
        cursor=conn.cursor()  
        
        if price is not None:
            cursor.execute("UPDATE products SET price=%s WHERE ID=%s", (price, product_id))
            
        if stock is not None:
            cursor.execute("UPDATE products SET stock=%s WHERE ID=%s", (stock, product_id))
        conn.commit()
            
    except Exception as e:
          print(" error updating product -->", e)
        
    finally:
        if cursor:
            cursor.close()
            
        if conn:
            conn.close()
            
def delete_product(product_id):
    try:
        conn=get_connection()
        cursor=conn.cursor()  
        
        query="DELETE FROM products WHERE ID=%s" 
        cursor.execute(query, (product_id,))
            
        conn.commit()
            
    except Exception as e:
          print(" error deleting product -->", e)
        
    finally:
        if cursor:
            cursor.close()
            
        if conn:
            conn.close()
            