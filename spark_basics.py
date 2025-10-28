Mechanism: Performs a "map-side combine" or "local aggregation" before shuffling. 
This means that within each partition, 
values for the same key are partially aggregated before being shuffled across the network.

rdd = sc.parallelize([("A", 1), ("B", 2), ("A", 3), ("B", 4)])
result = rdd.reduceByKey(lambda x, y: x + y)
# result will be [("A", 4), ("B", 6)]
#######################################################
Shuffles all values for a given key to a single partition,
 where they are then collected into an iterable. No pre-aggregation occurs before the shuffle.
rdd = sc.parallelize([("A", 1), ("B", 2), ("A", 3), ("B", 4)])
result = rdd.groupByKey()
# result will be [("A", <iterable containing 1, 3>), ("B", <iterable containing 2, 4>)]