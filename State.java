import java.util.Optional;

class State {
    private final PQ<Event> pq;
    private final Shop shop;
    private final String toPrint;
    private final Boolean terminate;
    private final Statistics stats;

    State(PQ<Event> pq, Shop shop) {
        this.pq = pq;
        this.shop = shop;
        this.toPrint = "";
        this.terminate = false;
        this.stats = new Statistics();
    }

    private State(PQ<Event> pq, Shop shop, String toPrint, Boolean terminate, Statistics stats) {
        this.pq = pq;
        this.shop = shop;
        this.toPrint = toPrint;
        this.terminate = terminate;
        this.stats = stats;
    }

    Boolean isEmpty() {
        return this.pq.poll().t().map(x -> x.toString()).orElse("").isEmpty() && this.terminate;
    }

    State next() {
        Pair<Optional<Event>, PQ<Event>> polledPQ = this.pq.poll();
        Optional<Event> nextEvent = polledPQ.t();
        PQ<Event> updatedPQ = polledPQ.u();
        Optional<Event> nextNextEvent = updatedPQ.poll().t();
        
        Optional<Pair<Event, Shop>> updatedPair = nextEvent.map(x -> x.next(this.shop))
            .map(x -> Optional.of(x)).orElse(Optional.empty());

        Boolean terminate = nextEvent.map(event -> event.toString().isEmpty()).orElse(true);
        
        return new State(updatedPair.map(event -> updatedPQ.add(event.t())).orElse(updatedPQ),
            updatedPair.map(x -> x.u()).orElse(this.shop),
            this.toPrint + nextEvent.filter(event -> !event.toString().equals("1"))
            .map(event -> event.toString() + "\n").orElse(""),
            terminate, nextEvent.map(event -> this.stats.update(event)).orElse(this.stats));
    }

    public String toString() {
        if (this.terminate.equals(true)) {
            return toPrint.trim() + "\n" + this.stats.compute();
        }
        return toPrint.trim();
    }
}
