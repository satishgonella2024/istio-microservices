# Istio Microservices Demo

This project demonstrates a microservices architecture using Istio service mesh, showcasing various Istio features including traffic management, resilience, and observability.

## Architecture

The application consists of two microservices:
- Product Service: Manages product information
- Order Service: Handles order creation and interacts with Product Service

## Prerequisites

- Docker
- Kubernetes cluster
- Istio (v1.24 or later)
- kubectl
- istioctl

## Installation

1. Clone the repository:
```bash
git clone https://github.com/satishgonella2024/istio-microservices.git
cd istio-microservices
```

2. Install Istio:
```bash
istioctl install --set profile=default -y
```

3. Install Istio addons:
```bash
kubectl apply -f https://raw.githubusercontent.com/istio/istio/release-1.24/samples/addons/prometheus.yaml
kubectl apply -f https://raw.githubusercontent.com/istio/istio/release-1.24/samples/addons/grafana.yaml
kubectl apply -f https://raw.githubusercontent.com/istio/istio/release-1.24/samples/addons/kiali.yaml
kubectl apply -f https://raw.githubusercontent.com/istio/istio/release-1.24/samples/addons/jaeger.yaml
```

4. Build and push Docker images:
```bash
# Build Product Service
cd services/product-service
docker buildx build --platform linux/amd64 -t satish2024/product-service:v1 --push .

# Build Order Service
cd ../order-service
docker buildx build --platform linux/amd64 -t satish2024/order-service:v1 --push .
```

5. Deploy the applications:
```bash
cd ../../k8s
kubectl apply -f namespace.yaml
kubectl apply -f redis.yaml
kubectl apply -f product-service.yaml
kubectl apply -f order-service.yaml
kubectl apply -f istio-gateway.yaml
```

## Features Demonstrated

### Traffic Management
- Circuit Breaking (`circuit-breaker.yaml`)
- Traffic Splitting (`traffic-splitting.yaml`)
- Fault Injection (`fault-injection.yaml`)
- Retry Policies (`retry-policy.yaml`)

### Resilience
- Health Checks
- Circuit Breakers
- Fault Tolerance

### Observability
- Kiali Dashboard
- Grafana Metrics
- Jaeger Tracing

## Directory Structure
```
.
├── k8s/                    # Kubernetes and Istio configurations
├── services/               # Microservices source code
│   ├── order-service/     # Order service
│   └── product-service/   # Product service
```

## Testing

1. Access the services:
```bash
export INGRESS_HOST=$(kubectl get svc istio-ingressgateway -n istio-system -o jsonpath='{.status.loadBalancer.ingress[0].ip}')

# Test product service
curl http://$INGRESS_HOST/products

# Test order service
curl -X POST http://$INGRESS_HOST/orders \
  -H "Content-Type: application/json" \
  -d '{"product_id": 1, "quantity": 2}'
```

2. Access dashboards:
```bash
istioctl dashboard kiali
istioctl dashboard grafana
istioctl dashboard jaeger
```

## Monitoring

1. Kiali Dashboard:
   - Service mesh topology
   - Traffic flow visualization
   - Health monitoring

2. Grafana:
   - Request rates
   - Error rates
   - Response times

3. Jaeger:
   - Distributed tracing
   - Request flows
   - Latency analysis

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.