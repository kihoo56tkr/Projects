import java.util.Optional;

class ArriveEvent extends Event {

    ArriveEvent(Customer customer, double eventTime) {
        super(customer, eventTime, 1);
    }

    Pair<Event, Shop> next(Shop shop) {
        Optional<Server> optionalServer = shop.findServer(super.customer);
        return optionalServer.map(server -> new Pair<Event, Shop>(
            new ServeEvent(server.identOfServer(), super.eventTime, super.customer),
            shop.update(server.updateWaitList(super.customer))))
            .orElse(nextIsItWaitAEvent(shop));
    }

    private Pair<Event, Shop> nextIsItWaitAEvent(Shop shop) {
        Optional<Server> optionalServer = shop.findServerWaitEvent();
        return optionalServer.map(server -> new Pair<Event, Shop>(
            new WaitEvent(server.identOfServer(), super.customer, super.eventTime),
            shop.update(server.updateWaitList(super.customer))))
            .orElse(new Pair<Event, Shop>(new LeaveEvent(super.customer,
            super.eventTime), shop));
    }

    public String toString() {
        return super.toString() + " arrives";
    }
}
