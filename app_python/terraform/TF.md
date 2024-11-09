# Terraform Docker Infrastructure
This document captures the output of Terraform commands and key configurations for the Docker infrastructure.

## Terraform State Show

<details>
<summary>Click to expand Terraform State Show output</summary>

resource "docker_container" "nginx_container" {
    attach                                      = false
    bridge                                      = null
    command                                     = [
        "nginx",
        "-g",
        "daemon off;",
    ]
    container_read_refresh_timeout_milliseconds = 15000
    cpu_set                                     = null
    cpu_shares                                  = 0
    domainname                                  = null
    entrypoint                                  = [
        "/docker-entrypoint.sh",
    ]
    env                                         = []
    gateway                                     = "172.17.0.1"
    hostname                                    = "fc55240b4b8e"
    id                                          = "fc55240b4b8e2431f5a6ebf162dc33f79f4fc18a0efbd55ed8dc6e0d8241a10a"
    image                                       = "sha256:3b25b682ea82b2db3cc4fd48db818be788ee3f902ac7378090cf2624ec2442df"
    init                                        = false
    ip_address                                  = "172.17.0.2"
    ip_prefix_length                            = 16
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
    logs                                        = false
    max_retry_count                             = 0
    memory                                      = 0
    memory_swap                                 = 0
    must_run                                    = true
    name                                        = "nginx_container_name_"
    network_data                                = [
        {
            gateway                   = "172.17.0.1"
            global_ipv6_address       = null
            global_ipv6_prefix_length = 0
            ip_address                = "172.17.0.2"
            ip_prefix_length          = 16
            ipv6_gateway              = null
            network_name              = "bridge"
        },
    ]
    network_mode                                = "bridge"
    pid_mode                                    = null
    privileged                                  = false
    publish_all_ports                           = false
    read_only                                   = false
    remove_volumes                              = true
    restart                                     = "no"
    rm                                          = false
    runtime                                     = "runc"
    security_opts                               = []
    shm_size                                    = 64
    start                                       = true
    stdin_open                                  = false
    stop_signal                                 = "SIGQUIT"
    stop_timeout                                = 0
    tty                                         = false
    user                                        = null
    userns_mode                                 = null
    wait                                        = false
    wait_timeout                                = 60
    working_dir                                 = null

    ports {
        external = 8080
        internal = 80
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}

</details>

---

## Terraform State List

<details>
<summary>Click to expand Terraform State List output</summary>

docker_container.nginx_container
docker_image.nginx_image

</details>

---

## Applied Changes

<details>
<summary>Click to expand Terraform Apply Log</summary>

Terraform will perform the following actions:

  docker_container.nginx_container must be replaced
-/+ resource "docker_container" "nginx_container" {
      + bridge                                      = (known after apply)
      ~ command                                     = [
          - "nginx",
          - "-g",
          - "daemon off;",
        ] -> (known after apply)
      + container_logs                              = (known after apply)
      - cpu_shares                                  = 0 -> null
      - dns                                         = [] -> null
      - dns_opts                                    = [] -> null
      - dns_search                                  = [] -> null
      ~ entrypoint                                  = [
          - "/docker-entrypoint.sh",
        ] -> (known after apply)
      ~ env                                         = [] -> (known after apply)
      + exit_code                                   = (known after apply)
      ~ gateway                                     = "172.17.0.1" -> (known after apply)
      - group_add                                   = [] -> null
      ~ hostname                                    = "0700fda2cf8a" -> (known after apply)
      ~ id                                          = "0700fda2cf8abb142883f7957faa4edbe385cde74722c6d6f67a57ddd3557c5a" -> (known after apply)
      ~ init                                        = false -> (known after apply)
      ~ ip_address                                  = "172.17.0.2" -> (known after apply)
      ~ ip_prefix_length                            = 16 -> (known after apply)
      ~ ipc_mode                                    = "private" -> (known after apply)
      - links                                       = [] -> null
      ~ log_driver                                  = "json-file" -> (known after apply)
      - log_opts                                    = {} -> null
      - max_retry_count                             = 0 -> null
      - memory                                      = 0 -> null
      - memory_swap                                 = 0 -> null
        name                                        = "nginx_container_name_"
      ~ network_data                                = [
          - {
              - gateway                   = "172.17.0.1"
              - global_ipv6_prefix_length = 0
              - ip_address                = "172.17.0.2"
              - ip_prefix_length          = 16
              - network_name              = "bridge"
                # (2 unchanged attributes hidden)
            },
        ] -> (known after apply)
      - network_mode                                = "bridge" -> null # forces replacement
      - privileged                                  = false -> null
      - publish_all_ports                           = false -> null
      ~ runtime                                     = "runc" -> (known after apply)
      ~ security_opts                               = [] -> (known after apply)
      ~ shm_size                                    = 64 -> (known after apply)
      ~ stop_signal                                 = "SIGQUIT" -> (known after apply)
      ~ stop_timeout                                = 0 -> (known after apply)
      - storage_opts                                = {} -> null
      - sysctls                                     = {} -> null
      - tmpfs                                       = {} -> null
        # (20 unchanged attributes hidden)

      ~ healthcheck (known after apply)

      ~ labels (known after apply)

        # (1 unchanged block hidden)
    }

Plan: 1 to add, 0 to change, 1 to destroy.

Changes to Outputs:
  + container_info = {
      + id   = (known after apply)
      + ip   = (known after apply)
      + name = "nginx_container_name_"
    }

</details>

---

## Terraform Output

<details>
<summary>Click to expand Terraform Output details</summary>

container_info = {
  "id" = "fc55240b4b8e2431f5a6ebf162dc33f79f4fc18a0efbd55ed8dc6e0d8241a10a"
  "ip" = "172.17.0.2"
  "name" = "nginx_container_name_"
}

</details>

---

## AFTER Applying Terraform to this repository
Terraform succesfully applied. See `terraform/github` for more info
<details>
<summary>Click to expand Terraform Output details</summary>

repository_url = "https://github.com/eeetaF/S24-devops-labs"

</details>

## Best Practices applied
By following these best practices, we ensure a secure, manageable, and reliable Terraform setup for managing GitHub repository infrastructure.

### 1. Secure Storage of Sensitive Data
Using Environment Variables for Sensitive Tokens

- **Description**: We used an environment variable (`GITHUB_TOKEN`) to store and access the GitHub personal access token securely.
- **Reason**: Storing sensitive information such as API tokens in environment variables prevents exposing these credentials directly in configuration files, reducing the risk of accidental leaks.
- **Implementation**: The `github_token` variable in Terraform references this environment variable, ensuring it remains secure.

### 2. Resource Importation for Existing Infrastructure
Importing Existing GitHub Repository

- **Description**: Instead of creating a new GitHub repository, we used the `terraform import` command to import an existing repository into Terraform’s state.
- **Reason**: This approach allows Terraform to manage existing infrastructure without recreating resources, preserving existing data and settings.
- **Implementation**: We ensured the correct repository name in the `terraform import` command and verified the resource with `terraform state list` to avoid duplication.

### 3. Use of Resource Blocks Following Provider Requirements
Following Provider-Specific Naming and Attribute Requirements

- **Description**: We adhered to GitHub provider constraints by avoiding special characters (e.g., slashes) in the `name` field of the `github_repository` resource and removed creation-only attributes (e.g., `auto_init`) when managing existing resources.
- **Reason**: Ensuring compliance with provider-specific rules and limitations helps prevent errors during resource creation or import.
- **Implementation**: We formatted the repository name and attributes according to Terraform and GitHub provider requirements, allowing Terraform to interact smoothly with GitHub's API.

### 4. Configuration Modularity and Reusability

Separating Configuration into Modular Blocks
- **Description**: We organized the GitHub repository and branch protection configurations into separate resource blocks.
- **Reason**: Separating different parts of the configuration (e.g., repository setup and branch protection rules) improves readability, makes it easier to update, and supports modularity.
- **Implementation**: We defined `github_repository` and `github_branch_protection` as distinct blocks, making each part of the setup clear and manageable.

### 5. Documentation of Outputs
Providing Resource Outputs

- **Description**: The configuration includes an output block that displays the repository URL after it has been imported or created.
- **Reason**: Outputs are useful for capturing essential information, making it easy for users and downstream processes to access relevant details without checking individual resource configurations.
- **Implementation**: We added an output for `repository_url`, which provides easy access to the URL of the managed repository after each `terraform apply`.
