from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

class GenericPagination(PageNumberPagination):
    page_size = 12
    page_query_param = 'page'
    max_page_size = 1000

    def get_page_size(self, request):
        if request.query_params.get('all'):
            return None  # Retorna todos os itens
        return super().get_page_size(request)

    def get_paginated_response(self, data):
        return Response({
            'count': self.page.paginator.count, 
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'previous_page_number': self.page.previous_page_number() if self.page.has_previous() else None,
            'next_page_number': self.page.next_page_number() if self.page.has_next() else None,
            'current_page': self.page.number,
            'total_pages': self.page.paginator.num_pages,  # Número total de páginas
            
            'results': data
        })