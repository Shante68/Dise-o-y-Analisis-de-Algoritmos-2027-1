public class Tarea1 {

    static class Nodo {
        int valor;
        Nodo p1;
        Nodo p2;
        Nodo p3;

        public Nodo(int valor) {
            this.valor = valor;
            this.p1 = null;
            this.p2 = null;
            this.p3 = null;
        }
    }

    public static void main(String[] args) {

        Nodo nodo20 = new Nodo(20);
        Nodo nodo23 = new Nodo(23);
        Nodo nodo19 = new Nodo(19);
        Nodo nodo57 = new Nodo(57);
        Nodo nodo67 = new Nodo(67);
        Nodo nodo99 = new Nodo(99);

        Nodo head = nodo20;

        head.p1 = nodo23;
        head.p2 = nodo19;
        head.p3 = null;

        nodo23.p1 = null;
        nodo23.p2 = nodo57;
        nodo23.p3 = null;

        nodo19.p1 = null;
        nodo19.p2 = null;
        nodo19.p3 = nodo67;

        nodo57.p1 = null;
        nodo57.p2 = null;
        nodo57.p3 = null;

        nodo67.p1 = null;
        nodo67.p2 = nodo99;
        nodo67.p3 = null;

        nodo99.p1 = null;
        nodo99.p2 = null;
        nodo99.p3 = null;

        System.out.println("Valor del nodo 99 a partir de head: " + head.p2.p3.p2.valor);

        System.out.println("Valor del nodo 57 a partir de head: " + head.p1.p2.valor);
    }
}
