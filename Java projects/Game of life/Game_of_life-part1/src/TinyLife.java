public class TinyLife {
    public static void main (String[] args) throws Exception{
        long newworld = setCell(0x00000000000000000,1,1,true);
        print(newworld);
        System.out.println(countNeighbours(newworld,2,1));
    }

    public static boolean getCell(long world, int col, int row) {
        boolean truthstate = ((7 >= col) & (0 <= col) & (7 >= row) & (0 <= row));
        if (truthstate) {
            return (PackedLong.get(world, (col + (row * 8))));
        }
        else{
            return truthstate;
        }
    }

    public static long setCell(long world, int col, int row, boolean value){
        boolean truthstate = ((7 >= col) & (0 <= col) & (7 >= row) & (0 <= row));
        if (truthstate){
            return (PackedLong.set(world, (col + 8*row),value));
        }
        else{
            return world;
        }
    }

    public static void print(long world){
        System.out.println("-");
        for (int row=0; row<8; row++){
            for (int col=0; col<8; col++){
                System.out.print(getCell(world,col,row)?"#":"_");
            }
            System.out.println();
        }
    }

    public static boolean computeCell(long world, int col, int row){
        boolean liveCell = getCell(world, col, row);
        int neighbours = countNeighbours(world, col, row);
        boolean nextCell = false;
        if (neighbours < 2) {
            nextCell = false;
        }
        if (liveCell && neighbours == 2 || liveCell && neighbours == 3){
            nextCell = true;
        }

        if (neighbours > 3){
            nextCell = false;
        }
        if (!liveCell && neighbours == 3) {
            nextCell = true;
        }
        return nextCell;
    }

    public static int countNeighbours(long world, int col, int row){
        int neighbours = 0;
        neighbours += (getCell(world, col-1, row-1)) ? 1 : 0;
        neighbours += (getCell(world, col, row-1)) ? 1 : 0;
        neighbours += (getCell(world, col+1, row-1)) ? 1 : 0;
        neighbours += (getCell(world, col-1, row)) ? 1 : 0;
        neighbours += (getCell(world, col+1, row)) ? 1 : 0;
        neighbours += (getCell(world, col-1, row+1)) ? 1 : 0;
        neighbours += (getCell(world, col, row+1)) ? 1 : 0;
        neighbours += (getCell(world, col+1, row+1)) ? 1 : 0;

        return neighbours;
    }

    public static long nextGeneration(long world){
        //to complete; compare this with sir's code!
    }


}
