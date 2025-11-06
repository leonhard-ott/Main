from django.http import JsonResponse


def health(request):
    """Simple health endpoint used by the frontend during development."""
    return JsonResponse({"status": "ok", "message": "OctoFit backend is up"})
