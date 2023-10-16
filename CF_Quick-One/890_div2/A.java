
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
      A[i] = scanner.nextInt();
    }
    int ans = 0;
    for (int i = 0; i < N - 1; i++) {
      if (A[i] > A[i + 1]) {
        ans = Math.max(ans, Math.max(A[i], A[i + 1]));
      }
    }
    System.out.println(ans);
  }
}
