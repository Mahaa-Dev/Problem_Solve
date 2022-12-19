

public class Sum
{
    public int findSum(int a, int b, int c)
    {
        int sum = a + b + c;
        return sum;
        
    }
    public static void main(String[] args)
    {
        Sum ss = new Sum();
        System.out.println(ss.findSum(20,5,4));
        System.out.println(ss.findSum(2,5,4));
        System.out.println(ss.findSum(8,5,4));
        
    }
    

    
}
