terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 2.13"
    }
  }
}

provider "docker" {
  host = "npipe:////./pipe/docker_engine"
}

# Create a Docker image resource
resource "docker_image" "nginx_image" {
  name         = "nginx:latest"
  keep_locally = false
}

# Create a Docker container using the nginx image
resource "docker_container" "nginx_container" {
  image = docker_image.nginx_image.latest
  name  = var.container_name
  ports {
    internal = 80
    external = 8080
  }
}

# Define a variable for the container name
variable "container_name" {
  description = "The name of the Docker container"
  type        = string
  default     = "container_name" # Default name if not specified
}

output "container_info" {
  value = {
    id   = docker_container.nginx_container.id
    name = docker_container.nginx_container.name
    ip   = docker_container.nginx_container.ip_address
  }
  description = "Details of the Docker container"
}

