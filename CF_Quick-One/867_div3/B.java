import java.util.Scanner;

public class soln2 {
    public static void main(String args[]) {
        Scanner scanner = new Scanner(System.in);
        int t = scanner.nextInt();

        while (t-- > 0) {
            int n = scanner.nextInt();
            int[] a = new int[n];
            for (int i = 0; i < n; i++) {
                a[i] = scanner.nextInt();
            }
            int max1 = Integer.MIN_VALUE;
            int max2 = Integer.MIN_VALUE;
            int min1 = Integer.MAX_VALUE;
            int min2 = Integer.MAX_VALUE;
            for (int i = 0; i < n; i++) {
                if (a[i] >= max1) {
                    max2 = max1;
                    max1 = a[i];
                }
                if (a[i] >= max2 && a[i] < max1) {
                    max2 = a[i];
                }
                if (a[i] <= min1) {
                    min2 = min1;
                    min1 = a[i];
                }
                if (a[i] <= min2 && a[i] > min1) {
                    min2 = a[i];
                }
            }
            // System.out.println(max1 + " " + max2 + " " + min1 + " " + min2); 
            long ans1 = (long) max1 * max2;
            long ans2 = (long) min1 * min2;
            if (ans1 > ans2) {
                System.out.println(ans1);

            } else {
                System.out.println(ans2);
            }

        }
        scanner.close();
    }
}