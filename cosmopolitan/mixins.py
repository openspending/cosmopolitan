class ListDetailSerializerMixin(object):
    def get_serializer_class(self):
        if self.get_view_name().endswith('List'):
            return self.list_serializer
        return self.detail_serializer
