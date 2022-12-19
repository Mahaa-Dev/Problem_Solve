public class Interest {
  public static void main(String[] args) {
    double principle = 1000;
    double time = 5;
    double rate = 0.05;

    double interest = Interest(principle, time, rate);
    System.out.println("Simple interest: " + interest);
  }

  public static double Interest(double principle, double time, double rate) {
    return principle * time * rate;
  }
}
