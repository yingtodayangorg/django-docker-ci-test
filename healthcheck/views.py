from django.http import JsonResponse


def healthcheck(request):  # pragma: no cover
    return JsonResponse({"status": "ok"})
