import java.util.Optional;
import java.util.List;
import java.util.stream.IntStream;
import java.util.stream.Stream;
import java.util.function.Supplier;

class Shop {
    private final List<Server> list;
    private final Supplier<Double> serviceTime;
    private final int maxQueue;

    Shop(int numberOfServers, Supplier<Double> serviceTime, int maxQueue) {
        this.list = IntStream.range(1, numberOfServers + 1).mapToObj(x -> new Server(x)).toList();
        this.serviceTime = serviceTime;
        this.maxQueue = maxQueue;
    }

    private Shop(List<Server> list, Supplier<Double> serviceTime, int maxQueue) {
        this.list = list;
        this.serviceTime = serviceTime;
        this.maxQueue = maxQueue;
    }

    Double getServiceTime() {
        return this.serviceTime.get();
    }
    
    Optional<Server> findServer(Customer c) {
        return this.list.stream().filter(x -> x.canServe(c)).findFirst();
    }

    Optional<Server> findServerWaitEvent() {
        return this.list.stream().filter(x -> x.isItWaitEvent(this.maxQueue)).findFirst();
    }
    
    Shop update(Server s) {
        return new Shop(this.list.stream()
        .map(x -> x.identOfServer() == s.identOfServer() ? s : x).toList(),
        this.serviceTime, this.maxQueue);
    }

    List<Server> getListServer() {
        return this.list;
    }
    
    public String toString() {
        return this.list.toString();
    }
}
