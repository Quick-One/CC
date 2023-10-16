
// import java.util.Arrays;
import java.util.Scanner;


public class soln{

  private static final Scanner scanner = new Scanner(System.in);

  public static void main(String[] args) {

    int t = scanner.nextInt();
    while (t-- > 0) {
      solve();
    }
    scanner.close();

  }

  public static void solve() {
    long N = scanner.nextLong();
    long i = 1;
    long ans = 0;
    while (true) {
      if (N % i == 0) {
        ans += 1;
      }
      else {
        break;
      }
      i += 1;
    }
    System.out.println(ans);
  }
}
