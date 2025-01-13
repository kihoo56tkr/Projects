import java.util.Optional;

class DoneEvent extends Event {

    private final int identServer;
    
    DoneEvent(Customer customer, int identServer, double eventTime) {
        super(customer, eventTime, 0);
        this.identServer = identServer;
    }
    
    Pair<Event, Shop> next(Shop shop) {
        Server updatedServer = shop.getListServer().stream()
            .filter(x -> x.identOfServer() == this.identServer)
            .findFirst().map(x -> x.serveAfterWait(super.customer))
             .orElse(new Server(0));
        return new Pair<Event, Shop>(new TerminateEvent(super.customer),
            shop.update(updatedServer));
    }

    public String toString() {
        return super.toString() + " done";
    }
}
