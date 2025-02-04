# Istio Microservices Demo

This project demonstrates a microservices architecture using Istio service mesh, organized by different scenarios and features.

## Directory Structure

```
.
├── k8s/
│   ├── 1-basic-deployment/    # Core service deployments
│   │   ├── namespace.yaml
│   │   ├── product-service.yaml
│   │   ├── order-service.yaml
│   │   ├── redis.yaml
│   │   └── istio-gateway.yaml
│   │
│   ├── 2-traffic-management/  # Traffic routing and splitting
│   │   ├── traffic-splitting.yaml
│   │   └── order-service-v2-deployment.yaml
│   │
│   ├── 3-resilience/         # Circuit breaking and fault tolerance
│   │   ├── circuit-breaker.yaml
│   │   ├── retry-policy.yaml
│   │   └── fault-injection.yaml
│   │
│   └── test-utils/           # Testing and load generation
│       ├── fortio-client.yaml
│       ├── test-client.yaml
│       └── traffic-generator.yaml
│
└── services/                  # Microservices source code
    ├── order-service/
    └── product-service/
```

## Scenarios

### 1. Basic Deployment
Basic setup of microservices with Istio integration:
```bash
kubectl apply -f k8s/1-basic-deployment/
```

### 2. Traffic Management
Demonstrates traffic routing and canary deployments:
```bash
# Deploy v2 of order service
kubectl apply -f k8s/2-traffic-management/
```

### 3. Resilience
Showcases service mesh resilience features:
```bash
# Apply circuit breaker
kubectl apply -f k8s/3-resilience/circuit-breaker.yaml

# Apply retry policy
kubectl apply -f k8s/3-resilience/retry-policy.yaml

# Apply fault injection
kubectl apply -f k8s/3-resilience/fault-injection.yaml
```

### 4. Testing
Utilities for testing and load generation:
```bash
# Deploy test client
kubectl apply -f k8s/test-utils/test-client.yaml

# Generate test traffic
kubectl apply -f k8s/test-utils/traffic-generator.yaml
```

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

3. Deploy basic services:
```bash
kubectl apply -f k8s/1-basic-deployment/
```

4. Install Istio addons:
```bash
kubectl apply -f https://raw.githubusercontent.com/istio/istio/release-1.24/samples/addons/prometheus.yaml
kubectl apply -f https://raw.githubusercontent.com/istio/istio/release-1.24/samples/addons/grafana.yaml
kubectl apply -f https://raw.githubusercontent.com/istio/istio/release-1.24/samples/addons/kiali.yaml
kubectl apply -f https://raw.githubusercontent.com/istio/istio/release-1.24/samples/addons/jaeger.yaml
```

## Scenario Walkthroughs

### Traffic Management
1. Deploy v1 of services
2. Deploy v2 of order service
3. Apply traffic splitting
4. Monitor in Kiali dashboard

### Resilience Testing
1. Apply circuit breaker
2. Generate load with test client
3. Observe circuit breaker behavior
4. Apply fault injection
5. Monitor service behavior

## Monitoring

Access dashboards:
```bash
istioctl dashboard kiali     # Service mesh topology
istioctl dashboard grafana   # Metrics and monitoring
istioctl dashboard jaeger    # Distributed tracing
```

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.