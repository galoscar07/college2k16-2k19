package main;

import java.util.ArrayList;
import java.util.Collection;
import java.util.List;
import java.util.Random;
import java.util.concurrent.Callable;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.locks.ReentrantLock;
import java.util.stream.Collectors;

public class Main {
    // how many types of products
    public static final int TYPES_OF_PRODUCTS = 4;
    // Min and max quantity of products in the market
    public static final int MIN_QUANTITY = 1000000;
    public static final int MAX_QUANTITY = 2000000;
    // Min and max price for products in the store
    public static final int MIN_PRICE = 1;
    public static final int MAX_PRICE = 10;
    // Min and max sale for products in each thread
    public static final int MIN_SALES = 1000;
    public static final int MAX_SALES = 5000;
    // Min and max numbers of products in wach sale
    public static final int MIN_ITEMS_PER_SALE = 0;
    public static final int MAX_ITEMS_PER_SALE = 50;
    // Number of threads
    public static final int THREADS = 4;
    // List of products
    public static List<Product> products;
    // List of bills
    public static List<List<Product>> bills;
    // Amount of money earned
    public static int money;
    public static ReentrantLock lock;
    public static Random random;

    public static Callable<Void> createTask(String name, int sales) {
        return () -> {
            // Start the execution of the thread
            System.out.println(name + " Start");
            // It will run as many times as given when created
            for (int i = 0; i < sales; i++) {
                boolean cancelled = false;
                List<Product> sale = new ArrayList<>();
                int total = 0;

                // Lock the thread here
                lock.lock();
                try {
                    // For each product we are going to try and create a transaction
                    for (Product p : products) {
                        // Generate a random number of bought items in this sale
                        int quantity = random.nextInt(MAX_ITEMS_PER_SALE) + MIN_ITEMS_PER_SALE;

                        // If the number generated is greater than the number of elements that we have left in the
                        // quantity then set the cancelled flag to true and break the execution
                        if (quantity > p.quantity) {
                            System.out.println(name + " Not enough products left in stock -> sale canceled");
                            cancelled = true;
                            break;
                        }

                        // If not then add the transaction
                        sale.add(new Product(p.name, p.price, quantity));
                        p.quantity -= quantity;

                    }
                } finally {
                    lock.unlock();
                }

                if (cancelled) {
                    // If it was a failed transaction just continue without doing anything
                    continue;
                }

                // If everything worked create the output message and print it out
                total = sale.stream().map(p -> p.quantity * p.price).mapToInt(Integer::intValue).sum();
                String message = "\n" + name + " Sale: \n";
                message += String.join("\n", sale.stream().map(Product::toString).collect(Collectors.toList()));
                message += "\nSale total " + total;

                System.out.println(message);

                // We lock the thread again so it doesn't change it's value
                lock.lock();
                try {
                    // We add the transaction into the transaction list
                    bills.add(sale);
                    // We add the money to the total
                    money += total;
                } finally {
                    // unlock
                    lock.unlock();
                }
            }

            // done, and repeat the process
            System.out.println('\n' + name + " End");
            return null;
        };
    }

    public static void main(String[] args) {
        // Initialize the product list as an empty list, bills also as an empty list and money as 0
        products = new ArrayList<>();
        bills = new ArrayList<>();
        money = 0;

        // Generate the list of products
        random = new Random();
        // We are going to have a list of 4 products
        for (int i = 0; i < TYPES_OF_PRODUCTS; i++) {
            // We are going to give as name the product type number between 1-4, price will be a random generated number
            //between 1 and 10 and quantity will be also a random generated number between 1000000 and 2000000
            products.add(new Product(String.valueOf(i), random.nextInt(MAX_PRICE) + MIN_PRICE,
                    random.nextInt(MAX_QUANTITY) + MIN_QUANTITY));
        }

        // Print the list of products that was just created
        System.out.println("Products: ");
        products.forEach(System.out::println);
        System.out.println();

        // We are creating a thread-pool of 4 tasks that will be called.
        ExecutorService executor = Executors.newFixedThreadPool(THREADS);
        lock = new ReentrantLock();
        // Creating the list of Callable objects
        List<Callable<Void>> tasks = new ArrayList<>();

        // Creates the list of threads giving them as function createTask fct and the number of execution with will be a
        // number between 1000 and 5000
        for (int i = 0; i < THREADS; i++) {
            tasks.add(createTask(String.valueOf(i), random.nextInt(MAX_SALES) + MIN_SALES));
        }

        // invoke all the threads created
        try {
            executor.invokeAll(tasks);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

        // compute the number of money and stop the execution.
        System.out.println("\nmain Money: " + money);
        int total = bills.stream().flatMap(Collection::stream).mapToInt(p -> p.price * p.quantity).sum();
        System.out.println("main Total: " + total);

        System.out.println("main End");
        executor.shutdown();
    }
}
