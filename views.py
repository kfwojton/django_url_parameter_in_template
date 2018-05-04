from django.views.generic.base import TemplateView



class CustomURLPath(TemplateView):
    template_name = "index.html"

    def get_context_data(self,  **kwargs):
        context = super(CustomURLPath, self).get_context_data(**kwargs)
        context['info'] = kwargs['info']
        return kwargs
