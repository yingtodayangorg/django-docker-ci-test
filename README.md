# Despliegue de Aplicación Django en Kubernetes con GitHub Actions

Este proyecto demuestra cómo contenerizar, analizar, probar y desplegar una aplicación Django utilizando GitHub Actions y Kubernetes (usando Docker Desktop o Minikube como entorno local).

---

## 📁 Estructura del Proyecto

```
.
├── Dockerfile
├── docker-compose.yml
├── k8s/
│   ├── deployment.yaml
│   ├── service.yaml
│   ├── ingress.yaml
│   ├── configmap.yaml
│   ├── secret.yaml
│   └── volume.yaml
├── .github/workflows/
│   └── ci-cd.yml
├── manage.py
└── demo/
    └── ...
```

---

## ⚙️ Flujo del Pipeline (CI/CD)

El pipeline de GitHub Actions realiza las siguientes etapas:

1. **Checkout** del código
2. **Instalación de dependencias** (Python y herramientas de análisis)
3. **Análisis estático** (flake8)
4. **Escaneo de vulnerabilidades** con Trivy
5. **Ejecución de pruebas unitarias**
6. **Build y push del contenedor Docker a DockerHub**
7. **Escaneo de vulnerabilidades de imagen docker**
8. **Despliegue en Kubernetes**

---

## 📸 Diagrama del pipeline

![Pipeline](A_comprehensive_documentation_document_for_a_Djang.png)

---

## 🚀 Despliegue en Kubernetes

Se utiliza Ingress para enrutar el tráfico HTTP hacia el servicio de Django dentro del clúster.

- Acceso local a través de: `http://django-app.local` o `https://django-app.local`
- Puerto expuesto: `8080` en el host, redirigiendo al `8081` interno de Nginx para servir contenido estático, redirigido al `8000` interno de Gunicorn

**Componentes creados en Kubernetes:**
- `Deployment`: 2 réplicas de la app Django
- `Service`: ClusterIP con puerto 8080
- `Ingress`: Con host `django-app.local`
- `ConfigMap`: Variables como `DEBUG=0`, `SECURE_SSL_REDIRECT=False`
- `ConfigMapNginx`: Configuraciones internas de Nginx como reverse proxy
- `Secrets`: Variables sensibles como `DJANGO_SECRET_KEY`

---

## 🔐 Certificados SSL (opcional)

Se puede agregar Let’s Encrypt + cert-manager para generación automática de certificados TLS para entornos públicos.

```bash
kubectl create secret tls django-tls-secret --cert=./certs/cert.crt --key=./certs/cert.key
```
Los certificados se generaron con makecert para un ambiente local en el directorio `certs` con dominio `django-app.local`
---

## 🧪 Probar el servicio

- Verificar que `django-app.local` resuelva en `/etc/hosts` o `C:\Windows\System32\drivers\etc\hosts`
- Ejecuta: `kubectl port-forward svc/django-service 8080:8080`
- Accede a: [http://localhost:8080](http://localhost:8080)

---

## 📝 Notas

- El flag `SECURE_SSL_REDIRECT` debe estar desactivado si usas HTTP
- Se ejecuta `collectstatic` durante el build ya que se usa NGINX para servir archivos estáticos
