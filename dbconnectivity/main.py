from product import add_product, list_products, update_product, delete_product

def menu():
    
    while True:
        print("1. Add Product")
        print("2. List all Products")
        print("3. Update Product")
        print("4. Delete Product")
        print("5. Exit")
        
        choice=input("Enter your choice (1-5):")
        
        if choice =="1":
             name= input("Enter product name:") 
             price= float(input("Enter product price:"))  
             stock= int(input("Enter product stock quantity:")) 
             add_product(name, price,stock)
             
        elif choice == "2":
            list_products()
            
        elif choice == "3":
            pid = int(input("Enter product id to update:"))
            price=input("Enter new price")
            stock=input("Enter new stock")
            
            update_product(pid,
               price=float(price) if price else None,
               stock=int(stock) if stock else None)
            
        elif choice == "4":
            pid =int(input("Enter the product id to delete"))
            delete_product(pid)
            
        else:
            print("Wrong option")
            exit()
            
if __name__ == "__main__":
    menu()
