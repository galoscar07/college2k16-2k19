package ro.ubb.xml;


import org.w3c.dom.Document;
import org.w3c.dom.Element;
import org.w3c.dom.Node;
import org.w3c.dom.NodeList;

import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.transform.Transformer;
import javax.xml.transform.TransformerFactory;
import javax.xml.transform.dom.DOMSource;
import javax.xml.transform.stream.StreamResult;
import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) throws Exception {

        System.out.println("hello");
        List<Book> books = loadData();
        books.forEach(System.out::println);
        Book myBook = new Book(
                "Light reading",
                "Zile Birmaneze",
                "George Orwell",
                1948,
                17.99F
        );
        saveBook(myBook);
    }

    private static void appendChildToElement(Document doc, Element parent, String tag, String value){
        Element element = doc.createElement(tag);
        element.setTextContent(value);
        parent.appendChild(element);
    }

    private static void saveBook(Book myBook) throws Exception {
        DocumentBuilderFactory dbFactory =  DocumentBuilderFactory.newInstance();
        DocumentBuilder dbBuilder = dbFactory.newDocumentBuilder();
        Document xmlDoc = dbBuilder.parse("./data/bookstore.xml");
        Element root = xmlDoc.getDocumentElement();

        Element ourBook = xmlDoc.createElement("book");
        ourBook.setAttribute("category", myBook.getCategory());
        appendChildToElement(xmlDoc, ourBook, "title", myBook.getTitle());
        appendChildToElement(xmlDoc, ourBook, "author", myBook.getAuthor());
        appendChildToElement(xmlDoc, ourBook, "year", String.valueOf(myBook.getYear()));
        appendChildToElement(xmlDoc, ourBook, "price", String.valueOf(myBook.getPrice()));

        root.appendChild(ourBook);

        Transformer transformer= TransformerFactory.newInstance().newTransformer();
        transformer.transform(new DOMSource(root),new StreamResult("./data/ourbooks.xml"));

    }


    private static String getTextByTagName(Element element, String tag){
        return element.getElementsByTagName(tag).item(0).getTextContent();
    }

    private static List<Book> loadData() throws Exception {

        List<Book> books = new ArrayList<>();

        DocumentBuilderFactory dbFactory =  DocumentBuilderFactory.newInstance();
        DocumentBuilder dbBuilder = dbFactory.newDocumentBuilder();
        Document xmlDoc = dbBuilder.parse("./data/bookstore.xml");
        Element root = xmlDoc.getDocumentElement();
        NodeList childNodes = root.getChildNodes();

        for (int index = 0; index < childNodes.getLength(); index++){
            Node child = childNodes.item(index);
            if(child instanceof Element) {
                Element bookElement = (Element) child;
                String category = bookElement.getAttribute("category");
                System.out.println(category);

                String author = getTextByTagName(bookElement, "author");
                String title = getTextByTagName(bookElement, "title");
                String year = getTextByTagName(bookElement, "year");
                String price = getTextByTagName(bookElement, "price");

                Book book = new Book(category, title, author, Integer.parseInt(year), Float.parseFloat(price));
                books.add(book); // pont ctrl + p
            }
        }

        return books;
    }
}
