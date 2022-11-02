public class FibonacciCache {
    public static void main(String[] args) throws Exception{
        store();
        arrayprinter();
        reset();
        System.out.println("******************");
        arrayprinter();
        store();
        System.out.println("******************");
        System.out.println(get(5));
    }
    public static long[] fib = new long[20];

    public static void store() {
        if (fib.length>0){
            fib[0] = 1L;
            if (fib.length>1){
                fib[1] = 1L;
                for (int i = 2; i<fib.length;i++){
                    fib[i] = fib[i-1] + fib[i-2];
                }
            }
        }
    }

    public static void reset(){
        for (int i = 0; i<fib.length;i++){
            fib[i] = 0;
        }
    }

    public static long get(int i){
        if(i>=0 && i<fib.length){
            return fib[i];
        }
        return -1L;
    }

    public static void arrayprinter(){
        for (int i=0;i<fib.length;i++){
            System.out.println(fib[i]);
        }
    }

}
