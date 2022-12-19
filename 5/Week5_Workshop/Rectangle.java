

public class Rectangle
{
   int length = 5;
   int breadth = 6;
   
   public void printArea()
   {
       int area = length * breadth;
       System.out.println("Area of rectangle is "+area);
   }
   public void printPerimeter()
   {
       int perimeter = 2*(length + breadth);
       System.out.println("Perimeter of rectangle is "+perimeter);
   }
   
   public static void main(String[] args)
   {
       Rectangle rec = new Rectangle();
       rec.printArea();
       rec.printPerimeter();
   }
}
