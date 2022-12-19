

public class Savings
{
    double simpleInterest;
    
    public void interest(int p, int t, int r)
    {
        simpleInterest = (p*t*r)/100;
        System.out.println("The simple interest is "+simpleInterest);
    }
    public static void main(String[] args)
    {
        Savings se = new Savings();
        se.interest(2000,5,8);
        
    }

}
