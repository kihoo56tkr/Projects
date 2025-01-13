import java.util.Comparator;
import java.util.Collection;
import java.util.PriorityQueue;
import java.util.Optional;

public class PQ<E extends Comparable<? super E>> {
    private final PriorityQueue<E> pq;

    public PQ() {
        this.pq = new PriorityQueue<E>();
    }

    public PQ(Collection<? extends E> source) {
        this.pq = new PriorityQueue<E>(source);
    }

    public PQ(Comparator<? super E> cmp) {
        this.pq = new PriorityQueue<E>(cmp);
    }

    public PQ(Collection<? extends E> source, Comparator<? super E> cmp) {
        this.pq = new PriorityQueue<E>(cmp);
        this.pq.addAll(source);
    }

    public boolean isEmpty() {
        return this.pq.isEmpty();
    }

    public PQ<E> add(E element) {
        PQ<E> copy = new PQ<E>(this.pq);
        copy.pq.add(element);
        return copy;
    }

    public Pair<Optional<E>, PQ<E>> poll() {
        PQ<E> copy = new PQ<E>(this.pq);
        Optional<E> t = Optional.ofNullable(copy.pq.poll());
        return new Pair<Optional<E>,PQ<E>>(t, copy);
    }

    @Override
    public String toString() {
        return this.pq.toString();
    }
}
