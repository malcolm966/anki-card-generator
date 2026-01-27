# Optimized Interview Questions for Yuan Fang (v2)
## Senior Backend Engineer - Japan Tech Companies (2025)

**Profile:** 7 years Java/Spring Boot | E-commerce & High-traffic Systems | Currently in Japan

---

## Part 1: Self-Introduction & Motivation

### 🔴 Must Prepare (100% will be asked)

| # | Question | Answer Strategy |
|---|----------|-----------------|
| 1 | **Tell me about yourself.** | 2-3 min: 7 years backend → Spring Boot/microservices expert → highlight Manka (current) + key achievement (100K concurrent users) |
| 2 | **Why do you want to join [Company]?** | Research company products + connect to your e-commerce/high-traffic experience |
| 3 | **Why did you choose to work in Japan?** | Personal motivation + professional growth + long-term commitment |
| 4 | **Why do you want to leave your current company?** | Positive framing: seeking larger scale challenges, not escaping problems |
| 5 | **What do you know about our company/products?** | Research: Rakuten Ichiba, LINE services, Mercari marketplace, etc. |

### 🟡 Likely to be Asked

| # | Question | Answer Strategy |
|---|----------|-----------------|
| 6 | What are your career goals for the next 3-5 years? | Technical depth → architect path OR team lead path |
| 7 | How do you adapt to Japanese work culture? | JLPT N2 + 2 years in Japan + respect for process |
| 8 | How do you communicate with Japanese team members? | Japanese for daily work + English for technical docs |
| 9 | What are your salary expectations? | Research market rate for senior backend in Osaka/Tokyo |
| 10 | Do you have any questions for us? | Prepare 3-5 thoughtful questions about team/tech/growth |

---

## Part 2: Behavioral Questions (STAR Method)

### 🔴 High Priority - Prepare with Specific Stories

| # | Question | Map to Project | STAR Key Points |
|---|----------|----------------|-----------------|
| 1 | **Describe your most challenging technical project.** | Order Service Optimization | S: Flash sale latency issues T: Replace caching layer A: Hazelcast migration R: 35% latency reduction |
| 2 | **Tell me about a time you led a development team.** | PLM System (Huayue) | S: Replace Windchill T: Lead 5 engineers A: Architecture design + task allocation R: Eliminated licensing costs, 95% satisfaction |
| 3 | **Tell me about a time you optimized system performance significantly.** | Multiple options | Option 1: Hazelcast (35% latency) Option 2: Elasticsearch (<50ms) Option 3: MongoDB+NAS (80% cost) |
| 4 | **Describe a time when you had to debug a difficult production issue.** | SkyWalking APM implementation | S: Slow incident response T: Implement APM A: SkyWalking across 3 teams R: 40% MTTR reduction |
| 5 | **How do you handle disagreements with team members?** | Any collaboration story | Focus: Listen → understand → propose data-driven solution → compromise |
| 6 | **Tell me about a time you delivered ahead of schedule.** | BOM Module (Huayue) | S: Tight deadline T: Activiti BPM workflow A: Parallel development R: 2 weeks early |
| 7 | **Describe a situation where requirements changed mid-project.** | Choose a real example | Show flexibility + communication + re-prioritization |

### 🟡 Medium Priority

| # | Question | Suggested Project |
|---|----------|-------------------|
| 8 | Tell me about a time you learned a new technology quickly. | Hazelcast or SkyWalking adoption |
| 9 | How do you handle tight deadlines and pressure? | Flash sale preparation at Manka |
| 10 | Describe your experience working in cross-functional teams. | Sinopec HR platform (17,000 departments) |
| 11 | Tell me about a time you took initiative without being asked. | APM implementation proposal |
| 12 | Tell me about a time you failed and how you recovered. | Prepare an honest example with lessons learned |
| 13 | How do you communicate technical issues to non-technical stakeholders? | Client presentations at Huayue/Beiming |

---

## Part 3: Technical - Java Core

### 🔴 High Priority (Senior Level Focus)

| # | Question | Key Points to Cover |
|---|----------|---------------------|
| 1 | **Explain HashMap vs ConcurrentHashMap. When to use each?** | Segment locking (Java 7) → CAS + synchronized (Java 8), use ConcurrentHashMap for multi-threaded scenarios |
| 2 | **Difference between synchronized and ReentrantLock?** | ReentrantLock: tryLock, fairness, interruptible; synchronized: simpler, auto-release |
| 3 | **What is a deadlock? How do you prevent it?** | Lock ordering, timeout, tryLock, avoid nested locks |
| 4 | **Explain Java 8 Stream API with your project examples.** | filter/map/reduce, parallel streams, when NOT to use |
| 5 | **How does volatile work? When to use it?** | Visibility guarantee, no atomicity, use for flags |
| 6 | **Explain ThreadLocal and potential memory leaks.** | Thread-local storage, must remove() in thread pools |

### 🟡 Medium Priority

| # | Question |
|---|----------|
| 7 | Explain Java Collections Framework - List vs Set vs Map |
| 8 | What is the difference between `==` and `equals()`? |
| 9 | When to use Callable vs Runnable? |
| 10 | Explain Java memory model - heap vs stack |
| 11 | How does garbage collection work? G1 vs ZGC? |

---

## Part 4: Technical - Spring Boot & Spring Cloud

### 🔴 High Priority

| # | Question | Key Points |
|---|----------|------------|
| 1 | **Explain Spring Boot auto-configuration mechanism.** | @EnableAutoConfiguration → spring.factories → @Conditional annotations |
| 2 | **Explain @Transactional - propagation and isolation levels.** | REQUIRED/REQUIRES_NEW/NESTED, READ_COMMITTED default, proxy-based AOP |
| 3 | **Difference between @Component, @Service, @Repository, @Controller?** | Semantic difference, @Repository adds exception translation |
| 4 | **How to handle circular dependencies?** | Avoid via design, @Lazy, setter injection as last resort |
| 5 | **How does Spring Security authentication work?** | Filter chain, AuthenticationManager, UserDetailsService |
| 6 | **Explain Spring Bean lifecycle.** | Instantiation → populate properties → BeanNameAware → init → ready → destroy |
| 7 | **What is Spring Boot Actuator? How do you use it?** | /health, /metrics, /info, custom endpoints, integrate with SkyWalking |

### 🟡 Medium Priority

| # | Question |
|---|----------|
| 8 | Explain Spring Profiles for environment management |
| 9 | How to implement global exception handling? (@ControllerAdvice) |
| 10 | Difference between @RestController and @Controller? |
| 11 | Explain Spring Data JPA repository interfaces |
| 12 | How to optimize Spring Boot startup time? |
| 13 | Explain @ConfigurationProperties and validation |

---

## Part 5: Technical - Microservices & Distributed Systems

### 🔴 High Priority (Core to Your Experience)

| # | Question | Your Experience to Reference |
|---|----------|------------------------------|
| 1 | **What are microservices? Advantages and disadvantages?** | Manka: 3+ microservices teams |
| 2 | **Explain service discovery. How does Nacos work?** | Your tech stack includes Nacos |
| 3 | **What is Circuit Breaker pattern?** | Resilience4j, fallback, half-open state |
| 4 | **How do you handle distributed transactions?** | Saga pattern, eventual consistency, compensation |
| 5 | **Explain Event-Driven Architecture.** | Kafka experience at Manka |
| 6 | **How do you ensure idempotency in distributed systems?** | Idempotency key, deduplication, database constraints |
| 7 | **What is API Gateway? Why is it important?** | Routing, auth, rate limiting, aggregation |

### 🟡 Medium Priority

| # | Question |
|---|----------|
| 8 | How do you implement inter-service communication? (REST vs gRPC vs Kafka) |
| 9 | What is the difference between synchronous and asynchronous calls? |
| 10 | How do you handle API versioning in microservices? |
| 11 | Explain database-per-service pattern and its challenges |

---

## Part 6: Technical - Database & Caching

### 🔴 High Priority (Directly Related to Your Projects)

| # | Question | Your Experience |
|---|----------|-----------------|
| 1 | **How do you ensure data consistency between Redis and MySQL?** | Cache-aside, write-through, cache invalidation strategies |
| 2 | **Explain your Elasticsearch architecture for 13M documents.** | Manuscript Archive System: sharding, replicas, index optimization |
| 3 | **How did you achieve <50ms search latency?** | Index design, query optimization, caching |
| 4 | **Explain your MongoDB + NAS hybrid storage strategy.** | Beiming: hot/cold data separation, 80% cost reduction |
| 5 | **What is database sharding? When to use it?** | Horizontal partitioning, shard key selection |
| 6 | **Explain distributed caching with Hazelcast.** | Your Order Service project: near-cache, partition |

### 🟡 Medium Priority

| # | Question |
|---|----------|
| 7 | Explain ACID properties with examples |
| 8 | What is database indexing? B-tree vs Hash index? |
| 9 | Explain N+1 query problem and solutions |
| 10 | What is connection pooling? HikariCP best practices? |
| 11 | Explain optimistic vs pessimistic locking |
| 12 | What is CAP theorem? |

---

## Part 7: Technical - Message Queue & Kafka

### 🔴 High Priority (Core to Your Stack)

| # | Question | Key Points |
|---|----------|------------|
| 1 | **Explain Apache Kafka architecture.** | Broker, partition, consumer group, offset |
| 2 | **How do you ensure message ordering in Kafka?** | Partition key, single partition per order |
| 3 | **How do you handle message consumption failures?** | Retry, DLQ, idempotent consumer |
| 4 | **Kafka vs RabbitMQ - when to use each?** | Kafka: high throughput, log; RabbitMQ: complex routing |
| 5 | **Why did you replace Kafka+Caffeine with Hazelcast?** | Your project: local cache limitations, distributed consistency |

---

## Part 8: System Design Questions

### 🔴 High Priority (Tailored to Your Experience)

| # | Question | How to Answer |
|---|----------|---------------|
| 1 | **Design an e-commerce order system for flash sales (100K+ concurrent).** | Draw from Manka experience: rate limiting, inventory deduction, distributed lock, Hazelcast caching |
| 2 | **Design a distributed caching system.** | Hazelcast architecture, cache coherence, eviction policies |
| 3 | **Design a payment escrow system.** | Prepaid Funds Platform: state machine, distributed transaction, reconciliation |
| 4 | **Design a document search system for 13M+ articles.** | Elasticsearch: index strategy, sharding, relevance scoring |
| 5 | **Design an APM system for microservices.** | SkyWalking experience: distributed tracing, metrics, alerts |

### 🟡 Medium Priority

| # | Question |
|---|----------|
| 6 | Design a rate limiter (token bucket, sliding window) |
| 7 | Design a notification system |
| 8 | How do you handle high-traffic scenarios? |
| 9 | Design database schema for e-commerce (products, orders, inventory) |

---

## Part 9: Project Deep Dive Questions

### 🔴 Must Prepare in Detail

| # | Question | Preparation Notes |
|---|----------|-------------------|
| 1 | **Why did you choose Hazelcast over Kafka+Caffeine?** | Caffeine = local cache (inconsistent across nodes), Hazelcast = distributed (consistent), better for flash sale |
| 2 | **How did you design the PLM system to replace Windchill?** | Modular architecture, Activiti for workflow, phased migration |
| 3 | **How did you achieve <50ms latency for 13M document search?** | Index optimization, query DSL tuning, SSD storage, replica distribution |
| 4 | **How did you design the Prepaid Funds escrow flow?** | State machine, idempotency, distributed transaction (Saga), reconciliation job |
| 5 | **How did you reduce storage costs by 80%?** | MongoDB for metadata, NAS for files, tiered storage policy |
| 6 | **How did you implement SkyWalking across 3 teams?** | Agent deployment, custom plugins, dashboard setup, alerting rules |
| 7 | **How did the HR platform handle 1.9B monthly page views?** | CDN, database read replicas, caching layers, async processing |

---

## Part 10: Performance & Monitoring

### 🔴 High Priority

| # | Question | Your Experience |
|---|----------|-----------------|
| 1 | **How do you identify performance bottlenecks?** | SkyWalking traces, slow query logs, JVM profiling |
| 2 | **Explain your APM implementation experience.** | SkyWalking: 40% MTTR reduction, 3 teams |
| 3 | **How do you optimize database queries?** | EXPLAIN, index analysis, query rewriting |
| 4 | **How do you handle memory leaks in Java?** | Heap dump analysis, MAT tool, ThreadLocal cleanup |

---

## Part 11: Coding Questions

### 🔴 Practice These (Most Relevant)

| # | Problem | Why Important |
|---|---------|---------------|
| 1 | **LRU Cache (LeetCode 146)** | Directly related to caching experience |
| 2 | **Two Sum (LeetCode 1)** | HashMap pattern, warm-up question |
| 3 | **Implement Rate Limiter** | System design coding |
| 4 | **Thread-safe Singleton** | Concurrency basics |
| 5 | **Producer-Consumer with BlockingQueue** | Matches Kafka experience |

### 🟡 Medium Priority

| # | Problem |
|---|---------|
| 6 | Reverse Linked List (LeetCode 206) |
| 7 | Merge Intervals (LeetCode 56) |
| 8 | Longest Substring Without Repeating (LeetCode 3) |

---

## Key Metrics to Memorize

| Project | Metric | Number |
|---------|--------|--------|
| Order Service (Manka) | Latency reduction | **35%** |
| Order Service (Manka) | Concurrent users | **100K+** |
| APM Implementation | MTTR reduction | **40%** |
| APM Implementation | Teams covered | **3** |
| PLM System (Huayue) | SKUs managed | **100** |
| PLM System (Huayue) | Parts managed | **50,000+** |
| PLM System (Huayue) | Client satisfaction | **95%** |
| BOM Module | Delivery | **2 weeks early** |
| Product approval cycle | Reduction | **30%** |
| Manuscript Archive (Beiming) | Articles | **13M** |
| Manuscript Archive (Beiming) | Monthly active users | **10M+** |
| Manuscript Archive (Beiming) | Search latency | **<50ms** |
| Manuscript Archive (Beiming) | QPS | **100+** |
| Storage Strategy | Cost reduction | **80%** |
| HR Platform (Sinopec) | Employees | **280,000** |
| HR Platform (Sinopec) | Departments | **17,000** |
| HR Platform (Sinopec) | Monthly page views | **1.9B** |
| HR Platform (Sinopec) | Automated workflows | **90** |

---

## 4-Week Preparation Plan

### Week 1: Core Technical
- [ ] Java concurrency (synchronized, ReentrantLock, volatile, ThreadLocal)
- [ ] Spring Boot internals (auto-config, bean lifecycle, @Transactional)
- [ ] Review all your project architectures

### Week 2: Distributed Systems
- [ ] Microservices patterns (circuit breaker, saga, event-driven)
- [ ] Kafka deep dive
- [ ] Caching strategies (Redis, Hazelcast)
- [ ] Elasticsearch optimization

### Week 3: System Design + Behavioral
- [ ] Practice designing e-commerce order system
- [ ] Practice designing caching system
- [ ] Prepare STAR stories for all behavioral questions
- [ ] Practice "Tell me about yourself" (2 min version)

### Week 4: Mock Interview + Polish
- [ ] LeetCode: 2-3 problems daily (focus on listed problems)
- [ ] Mock interviews with friends
- [ ] Research target companies thoroughly
- [ ] Prepare questions to ask interviewers

---

## Questions to Ask Interviewers

1. What does the tech stack look like for the team I'd be joining?
2. How does the team handle on-call and incident response?
3. What are the biggest technical challenges the team is facing?
4. How do you approach technical debt?
5. What does career growth look like for senior engineers here?
6. How does the team collaborate with other teams?
7. What's the development process like? (Agile/Scrum specifics)

---

*Version 2.0 - Refined based on resume analysis and 2025 trends*
*Total Questions: 120+ (prioritized and mapped to your experience)*
