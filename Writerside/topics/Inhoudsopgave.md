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
  * Decision making
  * Start with the end in mind
  * Using whiteboards and brainstorming
  * Using mind maps
  * Using schemas like flowcharts, UML, ERD, C4, ...
    * Using mermaidjs, plantuml, miro, ...  

## General IT concepts:
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
    * /dev/null
    * /etc
    * /proc
    * /opt
    * /usr
    * /tmp 
    * /boot 
    * /home
  * Environment variables
  * The basics of applications
    * Installing and removing applications
    * Updating applications
    * Finding applications (whereis, which, find, locate, ...)
    * Reading application documentation (man pages, help, --help, -h, ...)
    * Reading application configuration (config files, environment variables, ...)
    * Reading application logs (log files, journalctl, ...)
    * 
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
    * 
  * 
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
    * 
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
  * Keep it simple, stupid (KISS)
  * You aren't gonna need it (YAGNI)

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
    * PyCharm
    * VS Code
    * Vim
    * JupyterLab
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
  * 
## Protocols and Standards:
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

## Hardware components and concepts:
  * CPU
  * RAM
  * Storage
  * Network
  * Motherboard
  * Power supply
  * Graphics card
  * Sound card
  * Input devices (mouse, keyboard, touchpad, touchscreen, etc.)
  * Output devices (monitor, printer, speakers, etc.)
  * BIOS and UEFI
  * Boot process
  * Physical aspects of Virtualization and containerization

## Operating Systems:
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
* Python CLI applications
* Python web applications
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
  * Aiohttp
  * Asyncpg
  * Async SQLAlchemy
* Python data science
* NumPy
* Pandas


## Server Management:
* Different linux flavors:
  * Ubuntu
  * Debian
  * CentOS
  * Fedora
  * Arch

* Linux server management
  * File transfer
  * Process management
  * Cron jobs, services and schedulers:
    * systemd 
    * cron
    * Celery
    * Airflow
    * 
  * Working with services under Systemd
  
* Security and authentication
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
* Cloud computing

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

## Projects:
* A basic web application with a database and API
* A web application with a database, API, and front-end
* A web application with a database, API, front-end, and authentication
* A web application with a database, API, front-end, authentication, and CI/CD
