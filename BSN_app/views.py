from django.views.generic import TemplateView


class MainView(TemplateView):
  template_name = "base_vue.html"