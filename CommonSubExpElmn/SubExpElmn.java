import java.io.*;
import java.util.*;

class SubExpElmn {
    public static void main(String args[]) throws IOException {
        String s;

        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the size");
        int size = sc.nextInt();
        String arr[][] = new String[size][2];
        int index = 0;
        BufferedReader br = new BufferedReader(new InputStreamReader(new FileInputStream("input.txt")));
        while ((s = br.readLine()) != null) {
            arr[index][0] = s.substring(0, s.indexOf("="));
            arr[index][1] = s.substring(s.indexOf("=") + 1);
            index++;
        }
        for (int i = 1; i < arr.length; i++) {
            for (int j = i - 1; j >= 0; j--) {
                if (arr[i][1].equals(arr[j][1])) {
                    arr[i][1] = arr[j][0];
                    break;
                }
            }
        }
        for (int i = 0; i < arr.length; i++) {
            System.out.println(arr[i][0] + "=" + arr[i][1]);
        }
        sc.close();
        br.close();
    }
}
