

public class Employee
{
    String name, phone_no, address;
    int age;
    double salary;
    public void printSalary()
    {
        System.out.println("Name: "+name);
        System.out.println("Age: "+age);
        System.out.println("Phone number: "+phone_no);
        System.out.println("Address "+address);
        System.out.println("Salary: "+salary);
    }
    public static void main(String[] args)
    {
        Employee emp = new Employee();
        emp.name = "Shiv";
        emp.age = 22;
        emp.phone_no = "9819980";
        emp.address = "Siraha";
        emp.salary = 30000.56;
        emp.printSalary();
    }
}
