import java.util.Scanner;
public class Main
{
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        String word = sc.nextLine();
        int maxCnt = 0;
        int result = 987654321;
        int[] alpaCnt = new int[26];
        for (int i = 0; i<26; i++){
            alpaCnt[i] = 0;
        }
        for (char c : word.toCharArray()){
            int ascii = (int)c;
            int idx = 0;
          
            // 소문자
            if (ascii >= 97 && ascii <= 122){
              idx = ascii-97;
            }
            // 대문자
            else if (ascii >= 65 && ascii <= 90){
              idx = ascii-65;
            }
            alpaCnt[idx]++;
      
            if (alpaCnt[idx] > maxCnt){
                maxCnt = alpaCnt[idx];
                result = idx;
            }
        }

      int cnt = 0;
      for (int i=0; i<26; i++){
        if(alpaCnt[i] == maxCnt){
          cnt++;
        }
        if (cnt > 1){
          break;
        }
      }
      
      if (cnt>1){
        System.out.println("?");
      } else {
        System.out.println((char)(result+65));
      }
      sc.close();
    }
}
