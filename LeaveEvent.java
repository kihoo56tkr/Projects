import java.util.Optional;

class LeaveEvent extends Event {

    LeaveEvent(Customer customer, double eventTime) {
        super(customer, eventTime, 2);
    }

    Pair<Event, Shop> next(Shop shop) {
        return new Pair<Event, Shop>(new TerminateEvent(super.customer), shop);
    }

    public String toString() {
        return super.toString() + " leaves";
    }
}
