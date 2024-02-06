
#  Django application for blog-posts

Django web application that is a simple social media platform where users can create, edit and delete posts, comment on posts and manage their profiles. It consists of several components, including templates for user profiles, posts, and comments, along with associated views, forms and administrative configurations.
## Required

- Docker
- Python 3.10
- K3d
- PostgreSQL
## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`POSTGRES_USER`

`POSTGRES_PASSWORD`


## Running (Docker)
To start the app using Dockerfile and docker-compose run

```bash
  docker-compose up
```


## Running (Kubernetes)

To start the app using Kubernetes manifests run

```bash
k3d cluster create myCluster -p "8081:80@loadbalancer"
```
```bash
cd kubernetes
```
```bash
kubectl apply -f namespace.yml -f db.yml -f db-migration-job.yml deployment.yml -f service.yml -f ingress.yml 
```
**The order of the manifests matters**
