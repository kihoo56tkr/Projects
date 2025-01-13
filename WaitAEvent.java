import java.util.stream.IntStream;
import java.util.List;

class WaitAEvent extends Event {
    private final int identServer;

    WaitAEvent(int identServer, Customer customer, double eventTime) {
        super(customer, eventTime, 1);
        this.identServer = identServer;
    }

    Pair<Event, Shop> next(Shop shop) {
        Server updatedServer = shop.getListServer().stream()
            .filter(x -> (x.identOfServer() == this.identServer))
            .findFirst().orElse(new Server(0));
        if (updatedServer.getWaitingQueue().get(0).getIdentifier() ==
            super.customer.getIdentifier()) {
            return new Pair<Event, Shop>(new ServeEvent(this.identServer,
                updatedServer.getTimeAvailable(), super.customer), shop);
        }
        return new Pair<Event, Shop>(new WaitAEvent(this.identServer, super.customer,
            updatedServer.getTimeAvailable()), shop);
    }

    public String toString() {
        return "1";
    }
}
