
public class Average
{
    public double findAverage(int a, int b, int c)
    {
        double avg = (a + b + c)/3.0;
        return avg;
    }
    public static void main(String[] args)
    {
        Average ag = new Average();
        System.out.println(ag.findAverage(5,4,1));
        System.out.println(ag.findAverage(5,4,3));
        
    }
    
}
