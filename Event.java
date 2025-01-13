import java.util.Optional;

abstract class Event implements Comparable<Event> {
    protected final Customer customer;
    protected final double eventTime;
    protected final int typeOfEvent;

    Event(Customer customer, double eventTime) {
        this.customer = customer;
        this.eventTime = eventTime;
        this.typeOfEvent = -1;
    }

    protected Event(Customer customer, double eventTime, int typeOfEvent) {
        this.customer = customer;
        this.eventTime = eventTime;
        this.typeOfEvent = typeOfEvent;
    }

    int getCustomerID() {
        return this.customer.getIdentifier();
    }

    double getEventTime() {
        return this.eventTime;
    }

    public int compareTo(Event event) {
        if (this.eventTime < 0.0 && event.eventTime < 0.0) {
            return 0;
        } else if (event.eventTime < 0.0) {
            return -1;
        } else if (this.eventTime < 0.0) {
            return 1;
        }

        if (Double.compare(this.eventTime, event.eventTime) != 0) {
            return Double.compare(this.eventTime, event.eventTime);
        } 
        
        if (this.typeOfEvent - event.typeOfEvent != 0) {
            return this.typeOfEvent - event.typeOfEvent;
        } else {
            return this.customer.getIdentifier() - event.customer.getIdentifier();
        }
    }
    
    abstract Pair<Event, Shop> next(Shop shop);
    
    public String toString() {
        return String.format("%.3f", this.eventTime) +
            " customer " + this.customer.getIdentifier();
    }
}
