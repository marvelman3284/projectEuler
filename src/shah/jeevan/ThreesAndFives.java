// Problem 1

package shah.jeevan;

public class ThreesAndFives {
    public static void main () {
        int[] arr = genArr();
        System.out.println(fizzbuzz(arr));
    }

    public static int[] genArr() {
        int[] arr = new int[1000];
        for (int i = 0; i < 1000; i++) {
            arr[i] = i;
        }
        return arr;
    }

    public static int fizzbuzz(int[] arr) {
        int sum = 0;
        for (int i : arr) {
            if ( i % 3 == 0 || i % 5 == 0 ) {
                sum += i;
            }
        }
        return sum;
    }
}
