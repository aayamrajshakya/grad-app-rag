Talk title
Block Transactional Execution: Concurrency Models and Algorithms
Abstract
In the smart contract ecosystem each transaction contains code to be executed, and all nodes that execute the block of transactions must arrive at the same final state. Consequently, it becomes necessary to maximize the parallel execution of transactions within a node in settings where execution time is a bottleneck (e.g., under heavier workloads, larger blocks, or in future scaling designs) while still allowing all nodes to reach a consistent final state resulting from the execution of a set of transactions.  
  
The main challenge for maximizing the throughput of a node through parallel execution is transaction conflict resolution: when two transactions interact with the same data, like an account balance, their order matters. Imagine one transaction sends tokens from account A to account B, and another tries to send tokens from account B to account C. If the second transaction happens before the first one, the token  
balance in account B might be wrong, causing the entire system to break. Conflicts like these must be managed carefully, or you end up with an inconsistent, unusable blockchain state.  
This talk presents an overview and taxonomy of parallel execution methodologies for block transactional execution. We present lower bounds, algorithmic constructions and practical implementations for both EVM and MoveVM.
Bio
Srivatsan Ravi's research interests are centered around the theory and practice of distributed computing. His primarily work on algorithms and lower bounds for fault-tolerant distributed systems with a focus on building provably safe and secure concurrent/distributed systems and applications. 

Website
    [Srivatsan Ravi](https://sites.usc.edu/srivatsr/)
