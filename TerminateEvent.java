class TerminateEvent extends Event {

    TerminateEvent(Customer customer) {
        super(customer, -1.0);
    }

    Pair<Event, Shop> next(Shop shop) {
        return new Pair<Event, Shop>(new TerminateEvent(super.customer), shop);
    }

    public String toString() {
        return "";
    }
}
