class Customer {
    private final int identifier;
    private final double arrivalTime;
    
    Customer(int identifier, double arrivalTime) {
        this.identifier = identifier;
        this.arrivalTime = arrivalTime;
    }

    int getIdentifier() {
        return this.identifier;
    }

    double serviceTimeTill() {
        return arrivalTime;
    }

    Boolean canBeServed(double time) {
        return this.arrivalTime >= time;
    }
}
