class LowercaseMiddleware(object):
    def process_request(self, request):
        request.path_info = request.path_info.lower()
