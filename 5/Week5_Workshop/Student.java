
/**
 * Write a description of class Main here.
 *
 * @author (your name)
 * @version (a version number or a date)
 */
public class Student
{
    // instance variables - replace the example below with your own
    int roll_no;
    String name;

    /**
     *  class Main
     */
    public static void main(String[] args)
    {
        // initialise instance variables
        Student object = new Student();
        object.roll_no = 2;
        object.name = "John";
        System.out.println(object.roll_no);
        System.out.println(object.name);
        
    }

    
}
