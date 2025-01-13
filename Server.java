import java.util.Optional;
import java.util.stream.IntStream;
import java.util.List;

class Server {
    private final int identifier;
    private final Optional<Double> timeAvailable;
    private final List<Customer> waitingQueue;
    
    Server(int identifier, double timeAvailable) {
        this.identifier = identifier;
        this.timeAvailable = Optional.of(timeAvailable);
        this.waitingQueue = List.<Customer>of();
    }
    
    Server(int identifier) {
        this.identifier = identifier;
        this.timeAvailable = Optional.empty();
        this.waitingQueue = List.<Customer>of();
    }

    private Server(int identifier, double timeAvailable, List<Customer> waitingQueue) {
        this.identifier = identifier;
        this.timeAvailable = Optional.of(timeAvailable);
        this.waitingQueue = waitingQueue;
    }
    
    public String toString() {
        return "server " + this.identifier;
    }

    Server serve(double serviceTime, Customer c) {
        if ((this.timeAvailable.map(x -> x).orElse(-1.0) <= 0.0) &&
            (this.waitingQueue.size() <= 0)) {
            return new Server(this.identifier, serviceTime + c.serviceTimeTill());
        } else if ((this.timeAvailable.map(x -> x).orElse(-1.0) <= 0.0) ||
            (c.serviceTimeTill() >= this.timeAvailable.map(x -> x).orElse(-1.0))) {
            return new Server(this.identifier, serviceTime + c.serviceTimeTill(),
                this.waitingQueue);
        } else if (this.waitingQueue.size() <= 0) {
            return new Server(this.identifier, this.timeAvailable.map(x -> x + serviceTime)
                .orElse(0.0));
        } else {
            return new Server(this.identifier, this.timeAvailable.map(x -> x + serviceTime)
                .orElse(0.0), this.waitingQueue);
        }
    }

    Boolean isItWaitEvent(int maxQueue) {
        return this.waitingQueue.size() <= maxQueue;
    }
    
    Boolean canServe(Customer c) {
        return this.timeAvailable.map(x -> c.canBeServed(x)).orElse(true);
    }

    Server updateWaitList(Customer c) {
        if (this.waitingQueue.size() != 0) {
            return new Server(this.identifier, this.timeAvailable.map(x -> x).orElse(0.0),
                IntStream.range(0, this.waitingQueue.size() + 1)
                .mapToObj(x -> x < this.waitingQueue.size() ? this.waitingQueue.get(x) : c)
                .toList());
        } else {
            return new Server(this.identifier, this.timeAvailable.map(x -> x).orElse(0.0),
                List.<Customer>of(c));
        }
    }

    Server serveAfterWait(Customer c) {
        return new Server(this.identifier, this.timeAvailable.map(x -> x).orElse(0.0),
            IntStream.range(1, this.waitingQueue.size())
            .mapToObj(x -> this.waitingQueue.get(x)).toList());
    }
    
    List<Customer> getWaitingQueue() {
        return this.waitingQueue;
    }

    double getTimeAvailable() {
        return this.timeAvailable.map(x -> x).orElse(0.0);
    }
    
    int identOfServer() {
        return this.identifier;
    }
}
