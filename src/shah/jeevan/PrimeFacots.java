// Failed Problem 3 attemp

package shah.jeevan;

import java.util.ArrayList;
import java.util.Arrays;

public class PrimeFacots {
    public static void main() {
        ArrayList<Long> arr = primes(600851475143);
        System.out.println(Arrays.toString(arr));
    }

    public static ArrayList<Long> primes(long num) {
        ArrayList<Long> arr = new ArrayList<>();
        for (long i = num; i > 0; i--) {
            if (i % 2 == 1 || i % 3 == 1) {
                if (i % num == 0) {
                    arr.add(i);
                }
            }
        }
        return arr;
    }
}
