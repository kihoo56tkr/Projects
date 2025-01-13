# Discrete Event Simulator
This project demonstrates the implementation of a Discrete Event Simulator designed to model systems with multiple servers, queues, and customer events. The simulator tracks state transitions over time and collects performance statistics, making it a valuable tool for studying real-world scenarios such as queueing systems in restaurants, banks, or other service-based environments.

Key Characteristics of the Simulator:
1. Event-Driven Simulation:
- Models events such as ARRIVE, SERVE, WAIT, LEAVE, and DONE.
- Events are processed sequentially using a priority queue.
- Time formatting is precise to three decimal places using String.format.

2. Multi-Server, Multi-Queue System:
- Each server has its own queue with a configurable maximum queue length.
- Customers are served in a first-come, first-served manner.
- Supports dynamic queuing or customer departure when queues are full.

3. On-Demand Service Time:
- Service time is generated using the Supplier<Double> interface.
- Only invoked when a customer is served, optimizing resource usage.

4. Performance Statistics:
- Calculates the average waiting time for served customers.
- Tracks the number of customers served and those who leave unserved.

