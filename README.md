# Mini Project: gRPC-based Recommender System

This project demonstrates a microservice architecture using gRPC and Protocol Buffers (protobuf). The system consists of two services: a `marketplace` service and a `recommendations` service, which communicate with each other using gRPC.

The project implements a book recommendation service where the `marketplace` service interacts with the `recommendations` service to fetch book recommendations based on user preferences.

## Table of Contents

1. [Technologies Used](#technologies-used)
2. [Project Setup](#project-setup)
3. [File Structure](#file-structure)
4. [Services Overview](#services-overview)
5. [Running the Project](#running-the-project)
6. [Testing](#testing)
7. [Docker Setup](#docker-setup)
8. [Contributing](#contributing)
9. [License](#license)

## Technologies Used

- **gRPC**: For remote procedure calls between services.
- **Protocol Buffers (protobuf)**: For defining message types and services.
- **Flask**: A Python-based web framework for the marketplace service.
- **Docker**: For containerization of the services.
- **Python**: The programming language used for both services.
- **pytest**: For testing the services.
  
## Project Setup

To get started with the project, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/Iman-Ahmad/gRPC-based-Recommender-System.git
   cd gRPC-based-Recommender-System
