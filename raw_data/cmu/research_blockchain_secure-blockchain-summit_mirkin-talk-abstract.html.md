Talk title
Arbigraph: Verifiable Turing-Complete Execution Delegation
Abstract
Dependence on online infrastructure is rapidly growing as services like online payments and insurance replace traditional options, while others, like social networks, offer new capabilities.   
The centralized service operators wield unilateral authority over user conflicts, content moderation, and access to essential services. In the context of payments, blockchains provide a decentralized alternative.   
They also enable decentralized execution of stateful programs called smart contracts. But those are insufficient for other services as they lack contextual understanding and interpretative capabilities. Advancements in machine learning (ML) are raising interest in actually-smart contracts, but blockchain computation constraints prohibit direct ML inference execution. Various projects deploy computation delegation mechanisms, but they are inappropriate for ML workloads as they lack Turing-completeness, prohibit parallel computation, or suffer from high overhead.  
  
We present Arbigraph, a blockchain-based execution delegation protocol. Like previous optimistic solutions, the parties submit their computation results, allowing a smart contract to arbitrate in case of dispute. But Arbigraph employs a novel dual-graph data structure and takes advantage of the nature of the dispute process to achieve Turing completeness, constant-time memory access, and parallel execution. We formalize the problem and show that Arbigraph guarantees completeness, soundness, and progress. Experiments on LLM inference as well as matrix multiplication, which is at the core of ML inference, demonstrate that parallelization speedup grows linearly with matrix dimensions. We demonstrate Arbigraph's practical cost with a deployment on the Avalanche blockchain. Arbigraph thus enables decentralized, context-aware decision-making and paves the way for novel blockchain use cases.
Bio
Michael Mirkin is a Ph.D. student at Technion - Israel Institute of Technology. More details:  

Website

