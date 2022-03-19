import java.util.*;

class Main {
  // even 1이면 길이 짝수, 0이면 홀수
  private static String pal(String str, int even, int[] charCnt) {
    int N = str.length();
    StringBuilder answer = new StringBuilder();
    StringBuilder sb = new StringBuilder();
    String sa = new String();
    char so = '0';
    // 알파벳 순서대로 몇 개씩 있는지 확인
    if (even == 1) {
      for (int i = 0; i < 26; i++) {
        if (charCnt[i] > 0) {
          for (int j = 0; j < charCnt[i] / 2; j++) {
            sb.append((char) (i + 65));
          }
        }
      }
      sa = sb.toString();
      answer.append(sa);
      answer.append(sb.reverse().toString());
    } else {
      for (int i = 0; i < 26; i++) {
        if (charCnt[i] % 2 == 0) { // 짝수개 존재
          for (int j = 0; j < charCnt[i] / 2; j++) {
            sb.append((char) (i + 65));
          }
        } else { // 홀수개 존재
          for (int j = 0; j < charCnt[i] / 2; j++) {
            sb.append((char) (i + 65));
          }
          so = (char) (i + 65);
        }
      }
      sa = sb.toString();
      answer.append(sa);
      answer.append(so);
      answer.append(sb.reverse().toString());
    }
    return answer.toString();
  }

  public static void main(String[] args) {

    // 입력
    String name;
    Scanner sc = new Scanner(System.in);
    name = sc.next();

    int[] charCnt = new int[26];
    int N = name.length();
    int cnt = 0;

    // 65 ~ 90
    // 알파벳 별로 등장한 문자 갯수 세기
    for (char c : name.toCharArray()) {
      int i = (int) c - 65;
      charCnt[i]++;
    }

    // 알파벳 별로 등장한 문자 갯수 세기
    if (N % 2 == 0) {
      for (int i = 0; i < charCnt.length; i++) {
        if (charCnt[i] % 2 != 0) {
          cnt++;
          System.out.println("I'm Sorry Hansoo");
          break;
        }
      }
      if (cnt == 0) {
        System.out.println(pal(name, 1, charCnt));
      }

    } else {
      for (int i = 0; i < charCnt.length; i++) {
        if (charCnt[i] % 2 != 0) {
          cnt++;
          if (cnt > 1) {
            System.out.println("I'm Sorry Hansoo");
            break;
          }
        }
      }
      if (cnt == 1) {
        System.out.println(pal(name, 0, charCnt));
      }
    }
    sc.close();
  }
}
