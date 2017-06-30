from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import ImageUploadSerializer


class ImageUploadRequest(APIView):
    serializer_class = ImageUploadSerializer

    EXPIRY_TIME = 60

    @staticmethod
    def get_upload_url(listing_id, doc_name):
        return "http://demo.com/storage/{}/{}".format(listing_id, doc_name)

    def post(self, request, listing_id):
        self.serializer_class(data=request.data).is_valid(raise_exception=True)
        doc_name = request.data['doc_name']

        upload_url = self.get_upload_url(listing_id, doc_name)

        results = {
            'successful': 'T',
            'result': {
                'upload_url': upload_url,
                'expiry_time': self.EXPIRY_TIME
            },
            'errors': []
        }

        return Response(results)
