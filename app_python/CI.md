# Continuous Integration (CI)

This document outlines the best practices and strategies implemented in project's GitHub Actions CI workflow to ensure efficient, reliable, and maintainable continuous integration.

## Workflow Overview

Our CI workflow is defined in `.github/workflows/ci.yml` and runs on each push or pull request to the `main` branch. It automates several essential steps:
1. **Dependencies Installation**
2. **Code Quality Linting**
3. **Unit Testing**
4. **Docker Login, Build, and Push**

Each of these steps is designed to maintain code quality, enforce standards, and streamline deployment processes.

## Best Practices Implemented

#### Dependency Management and Caching
 By caching dependencies and Docker layers, we prevent the reinstallation of packages or rebuilding of Docker images that haven’t changed, saving time and resources.

#### Implementation
- **Python Dependencies**: We install dependencies from `requirements.txt` and cache them using a checksum of this file. This way, if `requirements.txt` hasn’t changed, the cached dependencies are reused.
- **Docker Layer Caching**: Docker layers are cached to speed up image builds. The cache key is based on a hash of `app_python/requirements.txt`, ensuring that only changes to dependencies trigger a new cache.

#### Benefits
- **Efficiency**: Caching reduces redundant installations and build times, improving CI efficiency.
- **Consistency**: By caching dependencies based on `requirements.txt`, we ensure that the environment remains consistent across CI runs unless dependencies change.
