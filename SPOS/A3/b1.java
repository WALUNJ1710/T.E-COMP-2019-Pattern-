import java.util.*;
import java.util.scanner;

public class b1{
  static{
    system.loadlibrary("b1");
  }
  
  private native void add(int a, int b);
  private native void sub(int a, int b);
  private native void mult(int a, int b);
  private native void div(int a, int b);
  
  public static void main(String[] args){
    Scanner sc = new Scanner(System.in);
    System.out.println("Enter value of a: ");
    int a = sc.nextInt();
    System.out.println("Enter value of b: ");
    int b = sc.nextInt();
    
    new b1().add(a,b);
    new b1().sub(a,b);
    new b1().mult(a,b);
    new b1().div(a,b);
  }                     
}  
