package main;

// Class that will help us out with solving the problem, it will represents the product in our store
public class Product {
    // The product will have a name, price and quantity
    public String name;
    public int price;
    public int quantity;

    public Product(String name, int price, int quantity) {
        this.name = name;
        this.price = price;
        this.quantity = quantity;
    }

    // Override the toString method to print out the product how to we want
    @Override
    public String toString() {
        return "Name: " + name + " Price: " + price + " Quantity: " + quantity;
    }
}
