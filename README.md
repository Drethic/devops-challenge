# Skyward DevOps Challenge

This repository is meant to be used as a challenge for DevOps candidates at Skyward.
You should fork/clone this repository to use as a basis for the challenge and provide the final solution in your own github account.

Make sure to add `SOLUTION.md` file to add extra comments if you feel those are necessary.

## Pre-requisites

- GitHub account: <https://github.com/signup>
- IaC Test account (choose one):
  - AWS Free Tier account: <https://aws.amazon.com/free/>
  - Localstack API: <https://localstack.cloud>
- Docker Hub account: <https://hub.docker.com>
- `Docker`: <https://www.docker.com>
- `Terraform`: <https://www.terraform.io>
- Kubernetes (choose one):
  - `KinD`: <https://kind.sigs.k8s.io>
  - `Minikube`: <https://minikube.sigs.k8s.io/docs/start/>
  - `k3s`: <https://k3s.io>

## First step!

Clone repository

```bash
git clone https://github.com/skywarditsolutions/devops-challenge.git
```

## Challenge 1. Docker and CI/CD

> Estimated time: 30 minutes

Now, show us your skills with Python (or whatever language you are most comfortable with) to develop a webserver (using `HTTPServer` python library) which listens on port `8000`. When you make a request to the server, it will return the following information:

![webserver-example.png](images/ch1-webserver-example.png "Example output Challenge-1")

Once you have it finished, can you create a Dockerfile and build an image with your application?

Helpers:

- [HTTPServer library](https://docs.python.org/3/library/http.server.html)
- [Dockerfile instructions](https://docs.docker.com/develop/develop-images/instructions/)

Optional:

- Application accepts arguments. Example: `--host`, `--port`
- Securize your Dockerfile
- Allow pass arguments when executing `docker run`. For example: `docker run <your-image-tag> --port 8081`
- Pass coverage with `dive` ([wagoodman/dive](https://github.com/wagoodman/dive)). Use `.dive-ci` that is provided in the repository

```bash
# command
CI=true dive <your-image-tag>

# result
Result:PASS [Total:3] [Passed:3] [Failed:0] [Warn:0] [Skipped:0]
```

- Upload your image to Docker Hub account with Github Actions ([docker/build-push-action](https://github.com/docker/build-push-action))

## Challenge 2. Kubernetes

> Estimated time: 45 minutes

Finally, deploy your Challenge 1 application on Kubernetes. Can you develop a Helm chart and deploy your image? The application will be exposed with an Ingress (choose the one you want: Nginx, Traefik…).

> Note: if you couldn’t complete Challenge 1, you can use the latest version of the `httpd` image on Helm chart.

Helpers:

- Helm best practices: <https://helm.sh/docs/chart_best_practices>
- NIP.io: <https://nip.io>
- Kubernetes:
  - `KinD`: <https://kind.sigs.k8s.io>
  - `Minikube`: <https://minikube.sigs.k8s.io/docs/start/>
  - `k3s`: <https://k3s.io>
- Ingress Controller: [services-networking/ingress-controllers/](https://kubernetes.io/docs/concepts/services-networking/ingress-controllers/)

Optional:

- Generate documentation for Helm chart ([norwoodj/helm-docs](https://github.com/norwoodj/helm-docs))
- Test end-to-end Helm chart with Github Action: [helm/chart-testing-action](https://github.com/helm/chart-testing-action)
- Validate `values.yaml` with `values.schema.json`

## Challenge 3. Infrastructure as a Code

> Estimated time: 2 hours

We’ve a infrastructure diagram, can you develop Terraform manifests? To check everything works properly, add `user_data` to install `httpd` (default config) and start service.

Maybe read helpers section can you give you how-to start the challenge and organize files. Create `challenge-3` folder to store all files.

![ch3-diagram-infrastructure.png](images/ch3-diagram-infrastructure.png "Diagram Challenge-3")

When you finish, you can reach Load Balancer a get the following output:

![ch3-output-load-balancer.png](images/ch3-output-load-balancer.png "Example output Challenge-3")

Helpers:

- IaC Test account:
  - AWS Free Tier account: <https://aws.amazon.com/free/>
  - Localstack API: <https://localstack.cloud>
- Terraform best practices: <https://cloud.google.com/docs/terraform/best-practices-for-terraform>
- Terraform AWS provider: <https://registry.terraform.io/providers/hashicorp/aws/latest>
- Terraform AWS modules:
  - Load Balancer: <https://registry.terraform.io/modules/terraform-aws-modules/alb/aws/latest>
  - S3: <https://registry.terraform.io/modules/terraform-aws-modules/s3-bucket/aws/latest>
  - RDS cluster: <https://registry.terraform.io/modules/terraform-aws-modules/rds-aurora/aws/latest>
  - VPC: <https://registry.terraform.io/modules/terraform-aws-modules/vpc/aws/latest>
  - Auto Scaling groups: <https://registry.terraform.io/modules/terraform-aws-modules/autoscaling/aws/latest>

Optional:

- Generate documentation for Terraform code (we provide `.terraform-docs.yaml` file): <https://github.com/terraform-docs/terraform-docs>
- Pass Terraform syntax checker and linters (we provide `.tflint.hcl` and `.tfsec.yaml` files):
  - `validate`: <https://developer.hashicorp.com/terraform/cli/commands/validate>
  - `fmt`: <https://developer.hashicorp.com/terraform/cli/commands/fmt>
  - `tflint`: <https://github.com/terraform-linters/tflint>
  - `tfsec`: <https://github.com/aquasecurity/tfsec> (save output, don't fix it!!)
- Create Terraform syntax checker and linters with GitHub Actions
