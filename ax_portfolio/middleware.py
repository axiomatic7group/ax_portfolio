class AgentDiscoveryMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        
        content_type = response.get('Content-Type', '')
        if 'text/html' in content_type:
            links = [
                '</sitemap.xml>; rel="service-doc"',
            ]
            
            if 'Link' in response:
                response['Link'] += ', ' + ', '.join(links)
            else:
                response['Link'] = ', '.join(links)
            
        return response
