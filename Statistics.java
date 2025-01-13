import java.util.List;
import java.util.stream.IntStream;

class Statistics {
    private final double leaveCount;
    private final double serveCount;
    private final double waitingTime;
    private final List<Customer> listOfCustomer;

    Statistics() {
        this.leaveCount = 0.0;
        this.serveCount = 0.0;
        this.waitingTime = 0.0;
        this.listOfCustomer = List.<Customer>of();
    }

    private Statistics(Event event, double leaveCount, double serveCount, double waitingTime,
        List<Customer> listOfCustomer) {
        if (event.toString().contains("leaves")) {
            this.leaveCount = leaveCount + 1.0;
            this.serveCount = serveCount;
            this.waitingTime = waitingTime;
            this.listOfCustomer = listOfCustomer;
        } else if (event.toString().contains("waits")) {
            this.leaveCount = leaveCount;
            this.serveCount = serveCount;
            this.waitingTime = waitingTime;
            this.listOfCustomer = IntStream.range(0, listOfCustomer.size() + 1)
                .mapToObj(x -> x < listOfCustomer.size() ? listOfCustomer.get(x) :
                new Customer(event.getCustomerID(), event.getEventTime())).toList();
        } else if (event.toString().contains("serves")) {
            this.leaveCount = leaveCount;
            this.serveCount = serveCount + 1.0;
            this.waitingTime = IntStream.range(0, listOfCustomer.size()).filter(x ->
                listOfCustomer.get(x).getIdentifier() == event.getCustomerID())
                .mapToObj(x -> event.getEventTime() - listOfCustomer.get(x)
                .serviceTimeTill() + waitingTime)
                .findFirst().orElse(waitingTime);
            this.listOfCustomer = listOfCustomer; 
        } else {
            this.leaveCount = leaveCount;
            this.serveCount = serveCount;
            this.waitingTime = waitingTime;
            this.listOfCustomer = listOfCustomer; 
        }
    }
    
    Statistics update(Event event) {
        return new Statistics(event, this.leaveCount, this.serveCount, this.waitingTime,
            this.listOfCustomer);
    }

    String compute() {
        if (this.waitingTime <= 0.0 || this.serveCount <= 0.0) {
            return "[0.000 " + String.format("%.0f", this.serveCount) + " "
                + String.format("%.0f", this.leaveCount) + "]";            
        }
        return "[" + String.format("%.3f", (this.waitingTime / this.serveCount))
            + " " + String.format("%.0f", this.serveCount) + " "
            + String.format("%.0f", this.leaveCount) + "]";
    }
}
