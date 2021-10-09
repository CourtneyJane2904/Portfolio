
/**
 * Creates an object representing a book in a library
 *
 * @author Courtney Evans | L3401977
 * @version 08-10-2021
 */
public class Book
{
    // the author of the book, title of the book and id of the book 
    private String author,title,id;
    // bool value indicating whether a book is on loan
    private boolean onLoan;
    
    /**
    * Constructor for objects of class Book
    * Creates instances of author, title, id and onLoan, most of their values assigned by supplied parameters
    * The constructor uses its three parameters to set the values of the corresponding fields
    */
    public Book(String anAuthor, String aTitle, String anId)
    {
        // The constructor uses its three parameters to set the values of the corresponding fields.
        this.author = anAuthor;
        this.title = aTitle;
        this.id = anId;
        // The field onLoan should be set to false
        this.onLoan = false;
    }
    // getters
    public String getAuthor() 
    {
        return this.author;
    }
    
    public String getTitle() 
    {
        return this.title;
    }

    public String getId() 
    {
        return this.id;
    }
    
    public boolean isOnLoan() 
    {
        return this.onLoan;
    }
    // setter
    public void setOnLoan(boolean onLoan) 
    {
        this.onLoan = onLoan;
    }
    
    /**
    * This method should return a string describing the book, using the following format:
    * Title: title, Author: author (availability)
    */
    public String toString() 
    {
        return "Title: "+this.title+", Author: "+this.author+((this.onLoan) ? " (on loan)" : " (available)");
    }
    
    /**
    * Returns true if the book has a valid id, and otherwise returns false.
    */
    public boolean verifyId()
    {
        int idLen = this.id.length();
        // An id must be 7 characters in length, otherwise the method returns false
        if (idLen == 7)
        {
            // total starts at 0
            int total = 0;
            // For each character ch in the id- an alternate way to loop not involving charAt
            for (char ch : this.id.toCharArray())
            {
                // The expression ch % 10 is evaluated, and the resulting number is added to a total
                total += ch % 10;
            }
            total %= 7;
            // total % 7 is calculated. If the result is 0 then the id is valid
            return ((total == 0) ? true : false);
        }
        else
        {
            return false;
        }
    }
}
