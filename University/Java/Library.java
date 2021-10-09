import java.util.ArrayList;
import java.util.Hashtable;
import java.util.HashMap;
import java.util.Collections;

/**
 * Create an object representing a library, dependent on the Book class
 *
 * @author Courtney Evans
 * @version 08-10-2021
 */
public class Library
{
    private ArrayList<Book> books;
    private String name;
    /**
     * Constructor method for Library class
     * Uses its parameter to set the library's name.
     * Also initializes the library's field books to an empty collection of the appropriate type.
     */
    public Library(String aName)
    {
        this.name = aName;
        this.books = new ArrayList<>();
    }

    /**
     * adds a new Book to the library books collection using the supplied parameters.
     */
    public void addBook(String author, String title, String id)
    {
        Book newBook = new Book(author, title, id);
        this.books.add(newBook);
    }
    
    /**
     * will calculate a fine for a late book that a library user is returning
     */
    public double calculateFine(double price, int numDaysLate)
    {
        return (price * 1/50) * numDaysLate;
    }
 
    /**
     * receives the title of a Book as a parameter
     * returns an ArrayList of books the library owns whose titles match the parameter string
     */
    public ArrayList<Book> getMatchingBooks(String title)
    {
        ArrayList<Book> matches = new ArrayList<>();
        // trying my hand at the filter method
        this.books.stream().filter(b -> title == b.getTitle()).forEach(b -> matches.add(b));
        return matches;
    }
    
    /**
     * returns true if the parameter’s title matches that of any book in the collection and the book is not on loan
     */
    public boolean isAvailable(Book b) 
    {
        ArrayList<Book> matches = new ArrayList<>();
        for (Book book : this.books) if ((b.getTitle() == book.getTitle()) && (!(book.isOnLoan()))) return true;
        return false;  
    }
    /**
     * takes no arguments and prints all the books in the library in the order they appear in the books collection
     */
    public void listAllBooks()
    {
        // listing all books via use of collection method forEach
        this.books.forEach(book -> System.out.println("Title: "+book.getTitle()+", Author: "+book.getAuthor()+((book.isOnLoan()) ? " (on loan)" : " (available)")));
    }
    
    /**
     * takes a Book as an argument and sets the first book in the books list with a matching id to be on loan
     */
    public void loanBook(Book book)
    {
        for (Book b : this.books) 
        {
            if (b.getId() == book.getId()) 
            {
                b.setOnLoan(true);
                break;
            }   
        }
    }
    
    /**
     * takes a Book as an argument and removes from the books collection the first book with a matching id
     */
    public void removeBook(Book book)
    {
        for (Book b : this.books)
        {
            if (b.getId() == book.getId()) 
            {
                this.books.remove(b);
                return;
            }   
        }
        System.out.println("Book not found");
    }
}
