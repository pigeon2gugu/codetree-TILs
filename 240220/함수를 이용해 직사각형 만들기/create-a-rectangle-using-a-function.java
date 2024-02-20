import java.io.*;
import java.util.*;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    public static void main(String[] args) throws IOException {
        String input = br.readLine();
        StringTokenizer st = new StringTokenizer(input);
        run(st);

        br.close();
    }

    private static void run(StringTokenizer st) {
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                System.out.print("1");
            }
            System.out.println();
        }
    }


}