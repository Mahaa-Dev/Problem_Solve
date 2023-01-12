import java.util.*;

public class MergeSort_2330772 {
    // Function to get input from user
    ArrayList<Integer> getInput(ArrayList<Integer> al) {
        System.out.println("      Merge Sort Algorithm using Java     ");
        Scanner anshu = new Scanner(System.in);
        // Getting input from user for array size
        System.out.println("Total number of elements you want in array: ");
        int userNumber = anshu.nextInt();

        System.out.println("Enter the  " + userNumber + " numbers you want to store in array : ");
        while (userNumber-- > 0) {
            al.add(anshu.nextInt());
        }
        return al;

    }

    // Function to print the sorted array
    void getOutput(ArrayList<Integer> al) {
        System.out.println(" Unsorted array : " + al);
        // Calls sort function
        sort(al, 0, al.size() - 1);

        System.out.println(" Sorted array :" + al);
    }

    // function for checking the elements and storing the elements in sorted order
    void merge(ArrayList<Integer> al, int beg, int mid, int end) {
        ArrayList<Integer> sortedElementsArray = new ArrayList<Integer>();
        // j is the first index of 1st array
        int j = mid + 1;
        // i is the first index of 2nd array
        int i = beg;

        while (i <= mid && j <= end) {
            if (al.get(i) < al.get(j)) {
                // Adds the element to the middle of the arraylist
                sortedElementsArray.add(al.get(i));
                i++;
            } else {
                // Adds the element to the end of the arraylist
                sortedElementsArray.add(al.get(j));
                j++;
            }
        }

        for (int k = i; k <= mid; k++)
            sortedElementsArray.add(al.get(k));

        for (int k = 0; k < sortedElementsArray.size(); k++) {
            al.set(beg + k, sortedElementsArray.get(k));
        }
    }

    // Divide array into two halves
    void sort(ArrayList<Integer> al, int beg, int end) {
        if (beg >= end)
            return;

        // SPlitting the array list into two each halves
        int mid = (beg + end) / 2;

        sort(al, beg, mid);
        sort(al, mid + 1, end);
        // Calling merge function to merge the sorted array
        merge(al, beg, mid, end);
    }

    // main function to get sorted array
    public static void main(String[] args) {
        MergeSort_2330772 value = new MergeSort_2330772();
        ArrayList<Integer> al = new ArrayList<Integer>();
        value.getInput(al);
        value.getOutput(al);

    }

}