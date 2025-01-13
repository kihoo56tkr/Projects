import java.util.List;
import java.util.stream.Stream;
import java.util.function.Supplier;

class Simulator {
    private final int numOfServers;
    private final int numOfCustomers;
    private final List<Pair<Integer, Double>> arrivals;
    private final int qmax;
    private final Supplier<Double> serviceTime;

    Simulator(int numOfServers, int qmax, Supplier<Double> serviceTime, int numOfCustomers,
        List<Pair<Integer, Double>> arrivals) {
        this.numOfServers = numOfServers;
        this.numOfCustomers = numOfCustomers;
        this.arrivals = arrivals;
        this.qmax = qmax;
        this.serviceTime = serviceTime;
    }

    State run() {
        PQ<Event> pq = new PQ<Event>();
        for (int i = 0; i < this.numOfCustomers; i++) {
            pq = pq.add(new ArriveEvent(new Customer(arrivals.get(i).t(),
                arrivals.get(i).u()), arrivals.get(i).u()));
        }
        
        State state = new State(pq,
            new Shop(this.numOfServers, this.serviceTime, this.qmax));

        while (!state.isEmpty()) {
            state = state.next();
        }
        return state;
    }
}
