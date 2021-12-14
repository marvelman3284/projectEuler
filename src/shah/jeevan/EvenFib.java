package shah.jeevan;

public class EvenFib {
    public static int n1=0,n2=1,n3=0;
    public static int sum = 0;

    public static void main() {
       int count = 34;
       sumFibonacci(count);
       System.out.println(sum + " ");
    }

    public static void sumFibonacci(int count){
        if(count>0) {
            n3 = n1 + n2;
            n1 = n2;
            n2 = n3;

            if (n3 % 2 == 0) {
                sum += n3;
            }

            sumFibonacci(count-1);
        }
    }
}
