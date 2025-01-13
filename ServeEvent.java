import java.util.Optional;
import java.util.stream.Stream;

class ServeEvent extends Event {

    private final int identServer;
    
    ServeEvent(int identServer, double eventTime, Customer customer) {
        super(customer, eventTime, 0);
        this.identServer = identServer;
    }
    
    Pair<Event, Shop> next(Shop shop) {
        Server updatedServer = shop.getListServer().stream()
            .filter(x -> x.identOfServer() == this.identServer)
            .findFirst().map(x -> x.serve(shop.getServiceTime(), super.customer))
            .orElse(new Server(0));
        return new Pair<Event, Shop>(new DoneEvent(
            super.customer, this.identServer, updatedServer.getTimeAvailable()),
            shop.update(updatedServer));
    }

    public String toString() {
        return super.toString() + " serves by server " + this.identServer;
    }
}
