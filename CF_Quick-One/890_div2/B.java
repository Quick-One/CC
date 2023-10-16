
// import java.util.Arrays;
import java.util.Scanner;


public class soln {

  private static final Scanner scanner = new Scanner(System.in);

  public static void main(String[] args) {

    int t = scanner.nextInt();
    while (t-- > 0) {
      solve();
    }
    scanner.close();

  }

  public static void solve() {
    int N = scanner.nextInt();
    int A[] = new int[N];
    for (int i = 0; i < N; i++) {
      A[i] = scanner.nextInt() - 1;
    }
  
    if (N == 1){
      System.out.println("NO");
      return;
    }
    int c = 0;
    // count number of 0s
    for (int i = 0; i < N; i++) {
      if (A[i] == 0) {
        c++;
      }
    }

    int alpha = 0;
    for (int i : A) {
      alpha += i;
      if (alpha >= c){
        System.out.println("YES");
        return;
      }
    }
    System.out.println("NO");

  }
}
