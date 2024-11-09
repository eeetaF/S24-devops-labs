terraform {
  required_providers {
    github = {
      source  = "integrations/github"
      version = "~> 5.0"
    }
  }
}

provider "github" {
  token = var.github_token
}

variable "github_token" {
  type        = string
  description = "GitHub personal access token"
  sensitive   = true
}

# Define the GitHub repository without slashes or unsupported characters
resource "github_repository" "s24_devops_labs" {
  name        = "S24-devops-labs"  # Just the repository name without additional characters
  description = "This is an existing repository managed by Terraform"
  visibility  = "public"
}

# Define branch protection rules for the default branch
resource "github_branch_protection" "main_branch_protection" {
  repository_id   = github_repository.s24_devops_labs.node_id
  pattern         = "main"
  enforce_admins  = true

  required_status_checks {
    strict   = true
    contexts = []
  }

  required_pull_request_reviews {
    dismiss_stale_reviews           = true
    require_code_owner_reviews      = true
    required_approving_review_count = 1
  }
}

# Output the repository URL
output "repository_url" {
  value       = github_repository.s24_devops_labs.html_url
  description = "URL of the GitHub repository"
}
