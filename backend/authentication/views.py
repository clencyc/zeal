import logging
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.request import Request
from .serializers import AuthSerializer

# Configure logging
logger = logging.getLogger(__name__)

@api_view(['POST'])
@permission_classes([AllowAny])
def register_or_login(request: Request):
    try:
        is_registration = 'confirm_password' in request.data
        serializer = AuthSerializer(data=request.data, context={'is_registration': is_registration})
        if serializer.is_valid():
            user = serializer.validated_data['user']
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        logger.error(f"Serializer errors: {serializer.errors}")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        logger.exception("An error occurred during registration or login")
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)