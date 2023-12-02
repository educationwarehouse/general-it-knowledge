# Table of Contents
These are the core concepts and skills that a student in IT should learn to develop back-end services in Python with 
various front-end technologies and the specified workflow.

## Learning and communication skills:
  * Learn how to learn
    * ask questions
    * how to search
    * find answers
    * how to use different communities and platforms
    * know these sources: 
      * Social media platforms: 
        * Stack Overflow
        * GitHub
        * Reddit
        * Quora
        * Discord
        * X
        * Fora and dedicated communities
      * Google, duckduckgo, ...
      * Blogs
      * Documentation
      * Books
      * Videos
      * Podcasts
      * Courses
      * Conferences
      * Meetups
      * Mentors
      * Colleagues
      * Friends
  * Learn how to read documentation
    * README
    * Tutorials
    * How-to guides
    * Explanation
    * Reference
    * Discussion
  * Learn how to read source code
  * Learn to Query search engines and communities

## Thinking skills: 
  * Problem solving
  * Critical thinking
  * Analytical thinking
  * Logical thinking
  * Creative thinking
  * Systems thinking
  * Design thinking
  * Decision-making
  * Start with the end in mind
  * Using whiteboards and brainstorming
  * Using mind maps
  * Using schemas like flowcharts, UML, ERD, C4, ...
    * Using mermaidjs, plantuml, miro, ...  

## General IT concepts:
  * Filesystems (FAT, NTFS, ext4, BTRFS, ...)

### Linux and CLI
  * Multiuser systems 
  * Using the shell 
  * Navigating the file system
    * Absolute and relative paths
    * Hidden files and directories
    * File permissions
    * File ownership
    * File types
    * File attributes
    * File sizes
    * File timestamps
    * File contents
    * File compression
    * File encryption
    * File hashing
    * /dev (especially /dev/null and block devices)
    * /etc
    * /proc
    * /opt
    * /usr
    * /bin (and /usr/bin, /sbin/usr/sbin, /usr/local/bin, /usr/local/sbin, ...)
    * /tmp 
    * /boot
    * /home (and ~)
  * Environment variables
  * The basics of applications
    * Installing and removing applications
    * Updating applications
    * Finding applications (whereis, which, find, locate, ...)
    * Reading application documentation (man pages, help, --help, -h, ...)
    * Reading application configuration (config files, environment variables, ...)
    * Reading application logs (log files, journalctl, ...)
    * Memory requirements (RAM, swap, ...)
    * CPU requirements (cores, threads, ...)
    * Default streams (stdin, stdout, stderr)
        * Stdin
        * Stdout
        * Stderr

  * Starting and stopping applications (./, &, fg, bg, jobs, kill, $PATH, ...)
  * Common ways to send arguments and options
  * Aliases and functions
  * Using pipes and redirection
  * Using the shell interactively and non-interactively
  * Using the shell for automation: 
    * Bash scripting
    * Python scripting
    * Using other languages
  * Using the shell for local system administration
    * Filename Globbing (wildcards))  
    * Managing users and groups (adduser, usermod, userdel, groupadd, groupmod, groupdel, ...)
    * Managing permissions (chmod, chown, chgrp, umask, ...)
    * Managing services (systemctl, service, ...)
    * Managing processes (ps, top, kill, btop,htop, ...)
    * Managing files and directories (ls, cd, pwd, mkdir, touch, rm, rmdir, cp, mv, ...)
    * Managing storage (df, du, mount, umount, ...)
    * Managing networking (ip, ifconfig, ping, traceroute, ...)
    * Managing firewalls (ufw, iptables, ...)
    * Managing logs (journalctl, tail, grep, ...)
    * Managing backups (rsync, tar, ...)
    * Managing updates (apt, apt-get, aptitude, yum, dnf, ...)
    * Managing time (date, timedatectl, ...)
    * Managing history (history, histr, ...)
    * Managing remote systems (ssh, scp, sftp, rsync, ...)
    * stdin, stdout, stderr rediction (>, >>, 2>, 2>>, 2>&1, tee, ...)

### Virtual machines: 
  * Virtual machine software: 
    * VirtualBox
    * Vagrant
    * VMware
    * Hyper-V
    * QEMU
    * KVM
    * Xen
  * Working both locally and virtual 
    * connecting to your vm 
    * sharing files 
    * running services
    * connecting to services from your host 

### Containerization:
  * Docker and Docker Compose
  * Podman
  * Kubernetes

## General Development concepts: 
  * Software development principles: 
    * SOLID
      * Single responsibility principle (SRP)
      * Open/closed principle (OCP)
      * Liskov substitution principle (LSP)
      * Interface segregation principle (ISP)
      * Dependency inversion principle (DIP)
    * General Responsibility Assignment Software Patterns (GRASP) 
      * Creator: The class responsible for creating an object should be the one that has the necessary information and resources to do so.
      * Information Expert: Assign a responsibility to the class that has the most information required to fulfill that responsibility.
      * High Cohesion: Classes should have a single, well-defined responsibility and should contain methods and attributes that are closely related to that responsibility.
      * Low Coupling: Classes should have minimal dependencies on other classes, promoting loose coupling and flexibility.
      * Controller: Assign the responsibility of handling system events and coordinating activities to a controller class.
      * Polymorphism: Use polymorphism to allow different classes to respond to the same message or interface in different ways. 
  * Composition over inheritance
  * Separation of concerns
  * Convention over configuration
  * Convention over code
  * Command–query separation (CQS)
  * Command–query responsibility segregation (CQRS)
  * Inversion of control (IoC)
  * Dependency injection (DI)
  * Don't repeat yourself (DRY)
  * Don't reinvent the wheel (DRW) / Don't repeat another (DRA)
  * Keep it simple, stupid (KISS)
  * You aren't gonna need it (YAGNI)
  * Technical debt
  * Code smells
 
### Choose your guiding principles 
  * ... 

#### Design patterns: 
In Python software development, several design patterns are commonly used to solve recurring design problems effectively. Here are some of the most commonly used design patterns:

  * **Singleton Pattern**: Ensures that a class has only one instance and provides a global point of access to that instance.
  * **Factory Method Pattern**: Defines an interface for creating an object but lets subclasses alter the type of objects that will be created.
  * **Abstract Factory Pattern**: Provides an interface for creating families of related or dependent objects without specifying their concrete classes.
  * **Builder Pattern**: Separates the construction of a complex object from its representation, allowing the same construction process to create various representations.
  * **Prototype Pattern**: Allows creating new objects by copying an existing object, known as the prototype, rather than creating them from scratch.
  * **Adapter Pattern**: Allows the interface of an existing class to be used as another interface, making it compatible with client code.
  * **Decorator Pattern**: Attaches additional responsibilities to an object dynamically, providing a flexible way to extend functionality.
  * **Proxy Pattern**: Provides a surrogate or placeholder for another object to control access to it.
  * **Observer Pattern**: Defines a one-to-many dependency between objects so that when one object changes state, all its dependents are notified and updated automatically.
  * **Strategy Pattern**: Defines a family of algorithms, encapsulates each one, and makes them interchangeable. It allows the algorithm to vary independently from clients that use it.
  * **Command Pattern**: Encapsulates a request as an object, thereby allowing for parameterization of clients with queues, requests, and operations.
  * **Chain of Responsibility Pattern**: Passes a request along a chain of handlers, where each handler decides whether to process the request or pass it to the next handler in the chain.
  * **State Pattern**: Allows an object to alter its behavior when its internal state changes. The object will appear to change its class.
  * **Template Method Pattern**: Defines the skeleton of an algorithm in the superclass but lets subclasses override specific steps of the algorithm without changing its structure.
  * **Composite Pattern**: Composes objects into tree structures to represent part-whole hierarchies. It allows clients to treat individual objects and compositions of objects uniformly.
  * **Iterator Pattern**: Provides a way to access the elements of an aggregate object sequentially without exposing its underlying representation.
  * **Visitor Pattern**: Represents an operation to be performed on elements of an object structure. It lets you define a new operation without changing the classes of the elements on which it operates.
  * **Memento Pattern**: Captures and externalizes an object's internal state so that the object can be restored to this state later.
  * **Bridge Pattern**: Separates an object’s abstraction from its implementation so that the two can vary independently.
  * **Composite Pattern**: Composes objects into tree structures to represent part-whole hierarchies. It allows clients to treat individual objects and compositions of objects uniformly.

#### Programming Paradigms:
  * Imperative
  * Declarative
  * Functional
  * Object-oriented
  * Procedural
  * Event-driven
  * Asynchronous
  * Concurrent
    * Parallel
    * Distributed
  * Reactive
  * Data-driven

#### Code best practices:
  * Code readability
  * Code reusability
  * Code maintainability
  * Code efficiency
  * Code smells 
  * Code refactoring
  * Code review

#### Reproducible development
  * Version control
  * Virtual environments
  * Containerization
  * Infrastructure as code
  * Configuration management
  * Continuous integration
  * Continuous delivery
  * Continuous deployment
  * DevOps 

#### Different scales withing software architecture 
  * Monoliths
  * Services Oriented AArchitecture 
  * Microservices
  * Serverless computing
  * Event-driven architecture
  * Command Query Responsibility Segregation (CQRS)
  * Event Sourcing

#### Project management and collaboration
  * SCRUM and Agile vs Waterfall 
  * Epics, User stories, and Tasks
  * Issues vs Changes 
  * Using Project management software: 
    * Github 
    * Gitlab
    * Taiga

#### Learn your IDE 
  * IDEs
    * PyCharm (get the student license for the PRO version, highly recommended)
    * VS Code (free, construct your own flavor)
    * Vim (free. For the tough folks)
    * JupyterLab (free, webbased datascience oriented)
  * Plugins
  * Shortcuts/keybindings
  * Quick selections
  * Artificial intelligence
  * Refactoring tools
  * Debugging tools
  * Code completion
  * Code snippets
  * Code formatting
  * Integrating external tools
  * Database management
  * Data manipulation
  * Importing and exporting data
  * Version control
  * Regular expressions
  * Multicursor edits

#### Common memory structures:
  * Stack
  * Heap
  * Queue
  * Linked list
  * Tree
  * Graph
  * Hash table
  * Cache
  * Buffer
  * File
  * Database
  * Network
  * Cloud

#### Common data structures:
  * Array
  * List
  * Tuple
  * Set
  * Dictionary and Hash-table
  * String
  * Binary and String
  * Tree
  * Graph
  * Cache (LRU, MRU, LFU, MFU, RR, ...)
  * Streams (stdin, stdout, stderr)
  * File handles (file, socket, pipe, ...)

#### Data persistence:
  * Filesystem
  * Database
  * Cache
  * Network
    * Samba 
    * NFS
    * SSHFS
    * FTP
    * HTTP
    * WebDAV
    * IPFS
    * BitTorrent
  * Cloud: 
    * AWS
    * Azure
    * GCP
    * Digital Ocean
    * Linode
    * Heroku
    * Netlify

#### Common inter process communication (IPC) methods:
  * Sync and Async revisited
  * Files
  * The primitives: 
    * Shared memory
    * Semaphores
    * Message queues
    * Pipes
    * Sockets
    * Signals
    * File locks
    * RPC
  * REST
  * WebSockets
  * WebRTC
  * Message queues
  * MQTT
  * AMQP 
  * Databases: postgres  
  * Lib: Diskcache using sqlite

### Protocols and Standards:
  * UUID (RFC 4122)
  * URI, URL, and URN (RFC 3986)
  * IP (RFC 791)
  * TCP (RFC 793)
  * UDP (RFC 768)
  * HTTP and HTTPS (RFC 2616)
  * WebSockets (RFC 6455)
  * TOTP (RFC 6238)
  * WebAuthn 
  * OAuth 2.0 (RFC 6749)
  * OpenID Connect
  * JSON Web Tokens (JWT) (RFC 7519)
  * Encryption: 
    * Preshared key
    * Symmetric key
    * Asymmetric key
    * Public key infrastructure (PKI)
    * Digital signatures
    * Certificates
    * Hashing
    * Password hashing
    * Key derivation functions (KDF)
  * MQTT (RFC 9431)
  * Posix regular expressions

## Hardware components and concepts:
  * CPU (cores, threads, cache, clock speed, vendors, architectures, etc.)
  * Volatile RAM (types, clock speed, latency, etc.)
  * Motherboard (Bus, architecture)
  * Network (pre-boot execution environment (PXE), network boot, etc.)
  * Nonvolatile Storage
      * Hard disk drive (HDD)
      * Solid-state drive (SSD)
      * Memory mapped drives (RAM disk)
      * Network attached storage (NAS) & Storage area network (SAN)
      * RAID
      * Tapes for archival
      * Online storage as a service (cloud storage)
  * Power supply (requirements, green computing, etc.)
  * Graphics card (GPU, internal and auxiliary)
  * Input devices (mouse, keyboard, touchpad, touchscreen, network, etc.)
  * Output devices (monitor, printer, speakers, network, etc.)
  * BIOS and UEFI, bootloaders, bootorder
  * Boot process (POST, MBR, GRUB, etc.)
  * Physical aspects of Virtualization and containerization (hypervisor, host, guest, bios extensions, etc.)

## Operating Systems:
  * Kernel vs OS
    * Linux
      * Ubuntu
      * Debian
      * CentOS
      * Fedora
      * Arch
    * Windows
    * Mac OS
    * Mobile
      * Android
      * iOS
  * and tons of others

## Networking:
  * OSI model
  * TCP/IP
  * IPv4 and IPv6
  * DNS
  * DHCP
  * PAT/NAT
  * Routing
  * Subnetting
  * Firewalls
  * (SSH) Tunneling
  * VPN
  * Proxy
  * Reverse proxy
  * Load balancing
  * HTTP and HTTPS
  * WebSockets
  * WebRTC

## Security:
  * Authentication
  * Authorization
  * Access control
  * Encryption
  * Hashing
  * Digital signatures
  * Certificates
  * Public key infrastructure
  * Passwords
  * 2FA and MFA
  * Security best practices

## Version Control:
  * Git, Mercurial, and SVN
    * GitHub
    * GitLab
    * Bitbucket
    * GitFlow
  * Semantic versioning (SEMVER)
  * Conventional commits
    * Commit messages
    * Change logs and release notes
    * Automating versioning and changelogs using [Semantic release](https://github.com/semantic-release/semantic-release)

## Text Editors and IDEs:
  * Vim
  * VS Code
  * PyCharm
  * JupyterLab

## Python Programming:
  * Python (3) syntax
  * Zen of Python
  * Python data types
  * Python data structures
  * Python control flow
  * Python functions
  * Python classes and objects
  * Python modules
  * Python packages
  * Python iterators
  * Python generators
  * Python decorators
  * Python context managers
  * Python magic methods
  * Python standard library
  * Python built-in functions
  * Python built-in modules
  * Python built-in types
  * Python built-in exceptions
  * Python virtual environments
  * Python packaging
  * Python documentation
  * Python logging
  * Python testing
  * Distributing Python packages

  * Static Typing
    * Static type checking
    * Type hints
    * Mypy
  * Writing better code: 
    * PEP 8 & PEP 257
    * Python documentation
  * Python logging

## Python for application development:
  * Python CLI applications
  * Python web applications
  * Database connectivity and abstraction layers
    * SQLAlchemy
    * pydal 
  * Python web frameworks
    * WSGI
    * ASGI
    * Web2py
    * Py4web
    * Django
    * Flask
    * FastAPI
    * Starlette
    * Tornado
    * Sanic
  * Python web servers: 
    * Gunicorn
    * Uvicorn
    * Hypercorn
    * Bjoern
  * Python asynchronous programming
    * Asyncio
    * Asyncpg
    * Trio
    * Anyio 
  * Python data science
    * NumPy
    * Pandas

## Monitoring and Logging:
  * Logging
  * Log/error levels
  * Log rotation
  * Syslog
  * Searching logs
  * Monitoring
  * Metrics
  * Alerting
  * Dashboards


## Testing:
  * Test-driven development
  * Unit testing
  * Integration testing
  * End-to-end testing
  * Static code analysis
  * Test coverage
  * CI/CD
  
## DevOps:
  * Continuous integration
  * Continuous deployment
  * Combining development with operations
  * Infrastructure as code
  * Configuration management
  * Remote management using SSH, Fabric and EDWH

## Server Management:
* Different linux flavors:
  * Ubuntu
  * Debian
  * CentOS
  * Fedora
  * Arch

## Linux server management
  * File transfer
  * Process management
  * Cron jobs, services and schedulers:
    * systemd 
    * cron
    * Celery
    * Airflow
    * 
  * Working with services under Systemd

## Security and authentication
  * SSH access: 
    * SSH keys
    * SSH agent
    * SSH tunneling
    * SSH config

* DevOps and CI/CD
* Monitoring and logging

## Scalability and Architecture:
* Scalability concepts
* Software design and patterns
* HTTP and RESTful APIs
* Database management
* Microservices
  * invalidating distributed cached
  * OPS is way more important compared to monoliths
* Cloud computing
  * OPS is even more important than microservices 
  * Use best-of-breed providers for each service
  * Buy managed services
* Licensing and legal issues
  * Open source
  * Copyleft
  * Creative Commons
  * MIT
  * GPL
  * Apache
  * BSD
  * LGPL
  * AGPL
  * Proprietary
  * EULA
  * Terms of service
  * Privacy policy
* Security and privacy 
  * GDPR
  * HIPAA
* Vendor lock-in

## Back-End Development:
  * Static file hosting
  * Dynamic content
  * Creating applications 
  * URI revisited 
  * HTTP and the conversation between client and server
  * Using HTTP verbs, paths and headers: 
    * Cookies and sessions, authentication and authorization
    * CORS and CSRF
  * Web frameworks (web2py, py4web)
  * Database management (PostgreSQL, SQLite)
  * API development and REST
  * Version control (Git)
  * Secret management (.env, .gitignore, .dockerignore)
  * Using containers with SOA and microservices 
  * Reverse proxies and load balancers
  * Service discovery
  * Internal/virtual networking 
  * Docker compose vs docker swarm
  * Kubernetes and other headaches 


## Front-End Development:
  * HTML, CSS, and JavaScript
  * Frameworks:
    * React, Vue, Svelte, jQuery, Bootstrap
    * Webpack and bundlers
  * State management
  * Single-page applications
  * Progressive web apps
  * Web components
  * OWASP top 10
   * Cross-site scripting (XSS)
   * Cross-site request forgery (CSRF)
   * SQL injection
   * Broken authentication
   * Sensitive data exposure
   * XML external entities (XXE)
   * Security misconfigurations
   * Insecure deserialization
   * Using components with known vulnerabilities
   * Insufficient logging and monitoring

## Database Management:
  * SQL and NoSQL
  * Different database systems: 
    * PostgreSQL
    * SQLite
    * Redis
  * Database design
  * Database management, adminstration, and maintenance
  * Database security
  * Database optimization using indexes
  * Database migration and versioning
  * Database replication
  * Database backup and recovery

## Decentralization:
  * Content delivery network (CDN)
  * NOSTR (Notes and other stuff through relays)
  * ActivityPub
  * Peer-to-peer networks
  * Blockchain
  * Distributed ledger technology
  * Distributed file systems
  * Distributed databases
  * Distributed computing
  * Distributed consensus
    * Raft

## Devop patterns:

1. **Configuration Management:**
   - **Infrastructure as Code (IaC):** Representing infrastructure configurations as code to automate provisioning and configuration.
   - **Orchestration Patterns:** Designing and managing complex, multi-step processes for system provisioning and configuration.

2. **Monitoring and Logging:**
   - **Centralized Logging:** Aggregating logs from various sources into a central repository for analysis.
   - **Alerting Patterns:** Implementing strategies for timely notification of system issues.
   - **Metrics Collection:** Gathering performance data from systems and applications for analysis.

3. **Security and Access Control:**
   - **Least Privilege Principle:** Providing the minimum level of access needed for users or processes.
   - **Segregation of Duties:** Separating tasks and responsibilities to reduce security risks.
   - **Security Patch Management:** Applying patches and updates to mitigate security vulnerabilities.

4. **High Availability and Redundancy:**
   - **Failover and Load Balancing:** Ensuring system availability by redirecting traffic in case of failures.
   - **Clustering:** Combining multiple servers into a single logical unit to enhance reliability.
   - **Backup and Disaster Recovery:** Creating and maintaining backups to recover from data loss or system failures.

5. **Scaling and Performance Optimization:**
   - **Horizontal Scaling:** Adding more servers to handle increased loads.
   - **Vertical Scaling:** Increasing the resources (CPU, memory) of existing servers.
   - **Caching Strategies:** Implementing caching to reduce database and network load.

6. **Automation and Scripting:**
   - **Scripting Patterns:** Developing scripts for common administrative tasks.
   - **Job Scheduling:** Automating recurring tasks and processes.

7. **Networking and Security Patterns:**
   - **Firewall Rules and ACLs:** Defining rules and access control lists for network security.
   - **VLAN Segmentation:** Separating network traffic logically to enhance security.
   - **DMZ (Demilitarized Zone):** Creating a network segment isolated from the internal network for hosting public-facing services.

8. **Backup and Restore Patterns:**
   - **Incremental Backups:** Backing up only the changes made since the last backup to reduce storage requirements and backup times.
   - **Bare-Metal Restore:** Recovering an entire system from backup, including the operating system and data.

9. **User and Identity Management:**
   - **Single Sign-On (SSO):** Allowing users to access multiple systems with a single set of credentials.
   - **Role-Based Access Control (RBAC):** Assigning permissions to users based on their roles and responsibilities.

10. **Patch Management:**
    - **Scheduled Patching:** Applying system updates and patches during maintenance windows to minimize disruption.
    - **Rollback Procedures:** Having plans to revert changes in case of issues caused by patches.

11. **Disaster Recovery and Business Continuity Planning:**
    - **Disaster Recovery Plan (DRP):** Developing strategies and procedures for restoring operations after a disaster.
    - **Business Continuity Plan (BCP):** Ensuring the continuity of essential business functions during and after a disaster.
